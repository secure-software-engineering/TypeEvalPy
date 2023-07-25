import contextlib
import functools
import os
import pathlib
import pprint
import queue
import re
import shutil
import subprocess
import sys
import textwrap
import threading
import time

import pytest
import sansio_lsp_client as lsp
from icecream import ic

METHOD_COMPLETION = "completion"
METHOD_HOVER = "hover"
METHOD_SIG_HELP = "signatureHelp"
METHOD_DEFINITION = "definition"
METHOD_REFERENCES = "references"
METHOD_IMPLEMENTATION = "implementation"
METHOD_DECLARATION = "declaration"
METHOD_TYPEDEF = "typeDefinition"
METHOD_DOC_SYMBOLS = "documentSymbol"
METHOD_FORMAT_DOC = "formatting"
METHOD_FORMAT_SEL = "rangeFormatting"

RESPONSE_TYPES = {
    METHOD_COMPLETION: lsp.Completion,
    METHOD_HOVER: lsp.Hover,
    METHOD_SIG_HELP: lsp.SignatureHelp,
    METHOD_DEFINITION: lsp.Definition,
    METHOD_REFERENCES: lsp.References,
    METHOD_IMPLEMENTATION: lsp.Implementation,
    METHOD_DECLARATION: lsp.Declaration,
    METHOD_TYPEDEF: lsp.TypeDefinition,
    METHOD_DOC_SYMBOLS: lsp.MDocumentSymbols,
    METHOD_FORMAT_DOC: lsp.DocumentFormatting,
    METHOD_FORMAT_SEL: lsp.DocumentFormatting,
}


def find_method_marker(text, method):
    """searches for line: `<code> #<method>-<shift>`
    - example: `sys.getdefaultencoding() #{METHOD_COMPLETION}-5`
      position returned will be 5 chars before `#...`: `sys.getdefaultencodi | ng()`
    """
    match = re.search(rf"\#{method}-(\d+)", text)
    before_match = text[: match.start()]
    lineno = before_match.count("\n")
    column = len(before_match.split("\n")[-1]) - int(match.group(1))
    return lsp.Position(line=lineno, character=column)


class ThreadedServer:
    """
    Gathers all messages received from server - to handle random-order-messages
    that are not a response to a request.
    """

    def __init__(self, process, root_uri, *, set_workspace_folders=True):
        self.process = process
        self.root_uri = root_uri
        self.lsp_client = lsp.Client(
            process_id=os.getpid(),
            root_uri=root_uri,
            workspace_folders=(
                [lsp.WorkspaceFolder(uri=self.root_uri, name="Root")]
                if set_workspace_folders
                else None
            ),
            trace="verbose",
        )
        self.msgs = []

        self._pout = process.stdout
        self._pin = process.stdin

        self._read_q = queue.Queue()
        self._send_q = queue.Queue()

        self.reader_thread = threading.Thread(
            target=self._read_loop, name="lsp-reader", daemon=True
        )
        self.writer_thread = threading.Thread(
            target=self._send_loop, name="lsp-writer", daemon=True
        )

        self.reader_thread.start()
        self.writer_thread.start()

        self.exception = None

    # threaded
    def _read_loop(self):
        try:
            while True:
                data = self.process.stdout.read(1)

                if data == b"":
                    break

                self._read_q.put(data)
        except Exception as ex:
            self.exception = ex
        self._send_q.put_nowait(None)  # stop send loop

    # threaded
    def _send_loop(self):
        try:
            while True:
                chunk = self._send_q.get()
                if chunk is None:
                    break

                self.process.stdin.write(chunk)
                self.process.stdin.flush()
        except Exception as ex:
            self.exception = ex

    def _queue_data_to_send(self):
        send_buf = self.lsp_client.send()
        if send_buf:
            self._send_q.put(send_buf)

    def _read_data_received(self):
        while not self._read_q.empty():
            data = self._read_q.get()
            events = self.lsp_client.recv(data)
            for ev in events:
                self.msgs.append(ev)
                self._try_default_reply(ev)

    def _try_default_reply(self, msg):
        if isinstance(
            msg,
            (
                lsp.ShowMessageRequest,
                lsp.WorkDoneProgressCreate,
                lsp.RegisterCapabilityRequest,
                lsp.ConfigurationRequest,
            ),
        ):
            msg.reply()

        elif isinstance(msg, lsp.WorkspaceFolders):
            msg.reply([lsp.WorkspaceFolder(uri=self.root_uri, name="Root")])

    #        else:
    #            print(f"Can't autoreply: {type(msg)}")

    def wait_for_message_of_type(self, type_, timeout=5):
        end_time = time.monotonic() + timeout
        while time.monotonic() < end_time:
            self._queue_data_to_send()
            self._read_data_received()

            # raise thread's exception if have any
            if self.exception:
                raise self.exception

            for msg in self.msgs:
                if isinstance(msg, type_):
                    self.msgs.remove(msg)
                    return msg

            time.sleep(0.2)

        raise Exception(
            f"Didn't receive {type_} in time; have: " + pprint.pformat(self.msgs)
        )

    def exit_cleanly(self):
        # Not necessarily error, gopls sends logging messages for example
        #        if self.msgs:
        #            print(
        #                "* unprocessed messages: " + pprint.pformat(self.msgs)
        #            )

        assert self.lsp_client.state == lsp.ClientState.NORMAL
        self.lsp_client.shutdown()
        self.wait_for_message_of_type(lsp.Shutdown)
        self.lsp_client.exit()
        self._queue_data_to_send()
        self._read_data_received()

    def do_method(self, text, file_uri, method, response_type=None):
        def doc_pos():
            return lsp.TextDocumentPosition(
                textDocument=lsp.TextDocumentIdentifier(uri=file_uri),
                position=find_method_marker(text, method),
            )

        if not response_type:
            response_type = RESPONSE_TYPES[method]

        if method == METHOD_COMPLETION:
            event_id = self.lsp_client.completion(
                text_document_position=doc_pos(),
                context=lsp.CompletionContext(
                    triggerKind=lsp.CompletionTriggerKind.INVOKED
                ),
            )
        elif method == METHOD_HOVER:
            event_id = self.lsp_client.hover(text_document_position=doc_pos())
        elif method == METHOD_SIG_HELP:
            event_id = self.lsp_client.signatureHelp(text_document_position=doc_pos())
        elif method == METHOD_DEFINITION:
            event_id = self.lsp_client.definition(text_document_position=doc_pos())
        elif method == METHOD_REFERENCES:
            event_id = self.lsp_client.references(text_document_position=doc_pos())
        elif method == METHOD_IMPLEMENTATION:
            event_id = self.lsp_client.implementation(text_document_position=doc_pos())
        elif method == METHOD_DECLARATION:
            event_id = self.lsp_client.declaration(text_document_position=doc_pos())
        elif method == METHOD_TYPEDEF:
            event_id = self.lsp_client.typeDefinition(text_document_position=doc_pos())
        elif method == METHOD_DOC_SYMBOLS:
            _docid = lsp.TextDocumentIdentifier(uri=file_uri)
            event_id = self.lsp_client.documentSymbol(text_document=_docid)
        else:
            raise NotImplementedError(method)

        resp = self.wait_for_message_of_type(response_type)
        assert not hasattr(resp, "message_id") or resp.message_id == event_id
        return resp


langserver_dir = pathlib.Path(__file__).absolute().parent / "langservers"


_clangd_10 = next(langserver_dir.glob("clangd_10.*/bin/clangd"), None)
_clangd_11 = next(langserver_dir.glob("clangd_11.*/bin/clangd"), None)
SERVER_COMMANDS = {
    "pyls": [sys.executable, "-m", "pyls"],
    "pyright": [
        langserver_dir
        / f"node_modules/.bin/pyright-langserver{'.cmd' if sys.platform == 'win32' else ''}",
        "--verbose",
        "--stdio",
    ],
    "js": [langserver_dir / "node_modules/.bin/javascript-typescript-stdio"],
    "clangd_10": [_clangd_10],
    "clangd_11": [_clangd_11],
    "gopls": [langserver_dir / "bin" / "gopls"],
}


@contextlib.contextmanager
def start_server(langserver_name, project_root, file_contents):
    command = SERVER_COMMANDS[langserver_name]

    # Create files before langserver starts
    for fn, text in file_contents.items():
        path = project_root / fn
        path.write_text(text)

    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    tserver = ThreadedServer(
        process,
        ic(project_root.as_uri()),
        set_workspace_folders=langserver_name != "pyright",
    )

    try:
        yield (tserver, project_root)
    except Exception as e:
        # Prevent freezing tests
        process.kill()
        raise e

    tserver.exit_cleanly()


def check_that_langserver_works(langserver_name, tmp_path):
    if langserver_name in {"pyls", "pyright"}:
        file_contents = {
            "foo.py": textwrap.dedent(
                f"""\
                import sys
                def do_foo(): #{METHOD_DEFINITION}-5
                    sys.getdefaultencoding() #{METHOD_HOVER}-5
                def do_bar(): #{METHOD_REFERENCES}-5
                    sys.intern("hey") #{METHOD_SIG_HELP}-2

                do_ #{METHOD_COMPLETION}-1"""
            )
        }
        filename = "foo.py"
        language_id = "python"

    elif langserver_name == "js":
        file_contents = {
            "foo.js": textwrap.dedent(
                f"""\
                function doSomethingWithFoo(x, y) {{
                    const blah = x + y;
                    return asdf asdf;
                }}

                doS //#{METHOD_COMPLETION}-3"""
            )
        }
        filename = "foo.js"
        language_id = "javascript"

    elif langserver_name in ("clangd_10", "clangd_11"):
        file_contents = {
            "foo.c": textwrap.dedent(
                f"""\
                #include <stdio.h>
                void do_foo(void);
                void do_foo(void) {{//#{METHOD_DECLARATION}-13
                }}
                int do_bar(char x, long y) {{
                    short z = x + y;
                }}

                int main(void) {{ do_ //#{METHOD_COMPLETION}-3"""
            )
        }
        filename = "foo.c"
        language_id = "c"

    elif langserver_name == "gopls":
        file_contents = {
            "foo.go": textwrap.dedent(
                f"""\
                package main

                import "fmt"

                type Creature struct {{
                    Name string
                }}
                func (c*Creature) Dump() {{
                    fmt.Printf("Name: '%s'", c.Name)
                }}

                func doSomethingWithFoo(x, y) string {{
                    blah := x + y
                    cat := &Creature{{"cat"}} //#{METHOD_TYPEDEF}-18
                    cat := &Creature{{"cat"}} //#{METHOD_IMPLEMENTATION}-14
                    cat.Dump() //#{METHOD_IMPLEMENTATION}-7
                    return asdf asdf
                }}
                var s1 = doS //#{METHOD_COMPLETION}-3"""
            ),
            "go.mod": textwrap.dedent(
                """\
                module example.com/hellp

                go 1.10
                """
            ),
        }
        filename = "foo.go"
        language_id = "go"
    else:
        raise ValueError(langserver_name)

    with start_server(langserver_name, tmp_path, file_contents) as (
        tserver,
        project_root,
    ):
        # Initialized #####
        tserver.wait_for_message_of_type(lsp.Initialized)

        if langserver_name == "pyright":
            tserver.wait_for_message_of_type(lsp.RegisterCapabilityRequest).reply()

        tserver.lsp_client.did_open(
            lsp.TextDocumentItem(
                uri=ic((project_root / filename).as_uri()),
                languageId=language_id,
                text=file_contents[filename],
                version=0,
            )
        )

        # Diagnostics #####
        diagnostics = tserver.wait_for_message_of_type(lsp.PublishDiagnostics)
        assert (
            diagnostics.uri.casefold() == (project_root / filename).as_uri().casefold()
        )
        diag_msgs = [diag.message for diag in diagnostics.diagnostics]

        if langserver_name == "pyls":
            assert "undefined name 'do_'" in diag_msgs
            assert "E302 expected 2 blank lines, found 0" in diag_msgs
            assert "W292 no newline at end of file" in diag_msgs
        elif langserver_name == "pyright":
            assert diag_msgs == ['"do_" is not defined', "Expression value is unused"]
        elif langserver_name == "js":
            assert diag_msgs == ["';' expected."]
        elif langserver_name in ("clangd_10", "clangd_11"):
            assert diag_msgs == [
                "Non-void function does not return a value",
                "Use of undeclared identifier 'do_'",
                "Expected '}'",
            ]
        elif langserver_name == "gopls":
            assert diag_msgs == ["expected ';', found asdf"]
        else:
            raise ValueError(f"{langserver_name}: {pprint.pformat(diag_msgs)}")

        do_method = functools.partial(
            tserver.do_method,
            file_contents[filename],
            (project_root / filename).as_uri(),
        )

        # Completions #####
        completions = do_method(METHOD_COMPLETION)
        completion_labels = [item.label for item in completions.completion_list.items]

        if langserver_name == "pyls":
            assert completion_labels == ["do_bar()", "do_foo()"]
        elif langserver_name == "pyright":
            assert completion_labels == [
                "__doc__",
                "do_foo",
                "do_bar",
                "dont_write_bytecode",
            ]
        elif langserver_name in ("js", "gopls"):
            assert "doSomethingWithFoo" in completion_labels
        elif langserver_name in ("clangd_10", "clangd_11"):
            assert " do_foo()" in completion_labels
            assert " do_bar(char x, long y)" in completion_labels
        else:
            raise ValueError(f"{langserver_name}: {pprint.pformat(completion_labels)}")

        if langserver_name == "pyls":
            # Hover #####
            hover = do_method(METHOD_HOVER)
            # NOTE: crude because response changes from one Python version to another
            assert "getdefaultencoding() -> str" in str(hover.contents)

            # signatureHelp #####
            sighelp = do_method(METHOD_SIG_HELP)

            assert len(sighelp.signatures) > 0
            active_sig = sighelp.signatures[sighelp.activeSignature]
            assert isinstance(active_sig, lsp.SignatureInformation)
            assert len(active_sig.parameters) > 0
            assert isinstance(active_sig.parameters[0], lsp.ParameterInformation)

            # definition #####
            definitions = do_method(METHOD_DEFINITION)

            assert (
                isinstance(definitions.result, lsp.Location)
                or len(definitions.result) == 1
            )
            item = (
                definitions.result[0]
                if isinstance(definitions.result, list)
                else definitions.result
            )
            assert isinstance(item, lsp.Location)  # TODO: could also be LocationLink
            assert item.uri.casefold() == (project_root / filename).as_uri().casefold()
            assert (
                METHOD_DEFINITION
                in file_contents["foo.py"].splitlines()[item.range.start.line]
            )

            # references #####
            [item] = do_method(METHOD_REFERENCES).result
            assert isinstance(item, lsp.Location)
            assert item.uri.casefold() == (project_root / filename).as_uri().casefold()
            assert (
                METHOD_REFERENCES
                in file_contents["foo.py"].splitlines()[item.range.start.line]
            )

            # documentSymbol #####
            doc_symbols = do_method(METHOD_DOC_SYMBOLS)
            assert len(doc_symbols.result) == 3
            assert {s.name for s in doc_symbols.result} == {"sys", "do_foo", "do_bar"}

            # formatting #####
            tserver.lsp_client.formatting(
                text_document=lsp.TextDocumentIdentifier(
                    uri=(project_root / filename).as_uri()
                ),
                options=lsp.FormattingOptions(tabSize=4, insertSpaces=True),
            )
            formatting = tserver.wait_for_message_of_type(
                RESPONSE_TYPES[METHOD_FORMAT_DOC]
            )
            assert formatting.result

            # Error -- method not supported by server #####
            # This creates a scary exception in pytest output. That's expected.
            tserver.lsp_client.workspace_symbol()
            err = tserver.wait_for_message_of_type(lsp.ResponseError)
            assert err.message == "Method Not Found: workspace/symbol"

        if langserver_name in ("clangd_10", "clangd_11"):
            # workspace/symbol #####
            # TODO - empty for some reason
            # tserver.lsp_client.workspace_symbol()
            # w_symb = tserver.wait_for_message_of_type(lsp.MWorkspaceSymbols)

            # declaration #####
            declaration = do_method(METHOD_DECLARATION)
            assert len(declaration.result) == 1
            assert (
                declaration.result[0].uri.casefold()
                == (project_root / filename).as_uri().casefold()
            )

        if langserver_name == "gopls":
            # implementation #####
            # TODO - null result for some reason
            # implementation = do_method(METHOD_IMPLEMENTATION)
            # print(f' implementation: {implementation}')

            # typeDefinition #####
            typedef = do_method(METHOD_TYPEDEF)
            assert len(typedef.result) == 1
            assert (
                typedef.result[0].uri.casefold()
                == (project_root / filename).as_uri().casefold()
            )


def test_pyls(tmp_path):
    check_that_langserver_works("pyls", tmp_path)


@pytest.mark.skipif(
    not (langserver_dir / "node_modules/.bin/pyright-langserver").exists(),
    reason="pyright-langserver not found in node_modules",
)
def test_pyright(tmp_path):
    check_that_langserver_works("pyright", tmp_path)


@pytest.mark.skipif(
    not (langserver_dir / "node_modules/.bin/javascript-typescript-stdio").exists(),
    reason="javascript-typescript-langserver not found",
)
@pytest.mark.skipif(shutil.which("node") is None, reason="node not found in $PATH")
def test_javascript_typescript_langserver(tmp_path):
    check_that_langserver_works("js", tmp_path)


@pytest.mark.skipif(
    sys.platform == "win32", reason="don't know how clangd works on windows"
)
@pytest.mark.skipif(_clangd_10 is None, reason="clangd 10 not found")
def test_clangd_10(tmp_path):
    check_that_langserver_works("clangd_10", tmp_path)


@pytest.mark.skipif(
    sys.platform == "win32", reason="don't know how clangd works on windows"
)
@pytest.mark.skipif(_clangd_11 is None, reason="clangd 11 not found")
def test_clangd_11(tmp_path):
    check_that_langserver_works("clangd_11", tmp_path)


@pytest.mark.skipif(
    sys.platform == "win32", reason="don't know how go works on windows"
)
@pytest.mark.skipif(
    not (langserver_dir / "bin" / "gopls").exists(),
    reason="gopls not installed in tests/langservers/bin/gopls",
)
def test_gopls(tmp_path):
    check_that_langserver_works("gopls", tmp_path)
