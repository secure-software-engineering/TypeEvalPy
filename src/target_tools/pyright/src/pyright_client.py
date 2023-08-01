import logging
import pathlib
import subprocess
import sys
import requests
import threading
import json
import time
import re
import os
import pyright_langservers as pyright_lsp
import sansio_lsp_client as lsp
import uvicorn
from fastapi import FastAPI

logging.basicConfig(
    filename="pyright_server.log", encoding="utf-8", level=logging.DEBUG, filemode="w"
)
logging.debug("Testing")

langserver_dir = pathlib.Path("/usr/local/bin")

dummy_file_location = pathlib.Path("/app/pyright_client.py")

SERVER_COMMANDS = {
    "pyright": [
        langserver_dir
        / f"pyright-langserver{'.cmd' if sys.platform == 'win32' else ''}",
        "--verbose",
        "--stdio",
    ],
}
DATATYPE_MAP = {}
TYPE_ALIAS_MAP = {}
TYPE_CLASS_MAP = {}


class PyrightClient:
    def __init__(self) -> None:
        self.pyright_process = subprocess.Popen(
            SERVER_COMMANDS["pyright"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
        )

        self.tserver = pyright_lsp.ThreadedServer(
            self.pyright_process,
            dummy_file_location.parent.as_uri(),
            set_workspace_folders=False,
        )

        self.tserver.wait_for_message_of_type(lsp.Initialized, timeout=15)
        # self.tserver.wait_for_message_of_type(lsp.RegisterCapabilityRequest).reply()


app = FastAPI()
RETRY_SLEEP = 0.25

client = PyrightClient()


def doc_pos(file_uri, lineno, column):
    return lsp.TextDocumentPosition(
        textDocument=lsp.TextDocumentIdentifier(uri=file_uri),
        position=lsp.Position(line=lineno, character=column),
    )


current_open_file = ""


def open_file(file_path):
    global current_open_file
    if current_open_file == file_path:
        return

    file_path = pathlib.Path(file_path)
    client.tserver.lsp_client.did_open(
        lsp.TextDocumentItem(
            uri=file_path.as_uri(),
            languageId="python",
            text=open(file_path).read(),
            version=0,
        )
    )

    current_open_file = file_path


def get_type(str_type):
    res = []
    if str_type in DATATYPE_MAP:
        res.append(DATATYPE_MAP[str_type])
    elif str_type in ["None", "Unknown", "Any"]:
        pass
    elif "|" in str_type:
        types_t = str_type.split("|")
        for _i in types_t:
            res.extend(get_type(_i.replace("(", "").replace(")", "").strip()))
    elif str_type.startswith(("ndarray", "NDArray")):
        res.append(DATATYPE_MAP["ndarray"])
    elif str_type.startswith("NDFrame"):
        res.append(DATATYPE_MAP["DataFrame"])
    elif str_type.startswith("Tuple"):
        # types_t = (
        #     _t.split("Tuple")[1].replace("[", "").replace("]", "").split(",")
        # )
        res.append("tuple")
    else:
        logging.info("Not found in dict")
        logging.info(str_type)
        res = []

    return res


def get_data_type(value):
    if isinstance(value, str):
        return "str"
    elif isinstance(value, int):
        return "int"
    elif isinstance(value, float):
        return "float"
    else:
        return value


@app.get("/")
def get_hover(file_path, lineno, col_offset, func_name):
    print(file_path)
    open_file(file_path)
    file_path = pathlib.Path(file_path)

    _pos = doc_pos(file_path.as_uri(), lineno, col_offset)
    client.tserver.lsp_client.hover(_pos)
    hover_msg = client.tserver.wait_for_message_of_type(lsp.Hover, timeout=15)
    directory_name, file_path = os.path.split(file_path)
    res = None
    # TODO: do some parsing of the hover message here
    if hover_msg.contents:
        _type = hover_msg.contents.value
        print(_type)
        result = {
            "file": str(file_path),
            "line_number": int(lineno) + 1,
            "col_offset": int(col_offset) + 1,
        }
        if func_name:
            result["function"] = func_name
        try:
            if _type.startswith("```python\n(function)"):
                _type_name = _type.split("-> ")[0].split("python\n(function) ")[1]
                _type_value = _type.split("-> ")[-1].strip().strip("`\n")
                result["type"] = f"[{_type_value}]"
            elif _type.startswith("```python\n(variable)"):
                if "->" in _type:
                    _type_name = (
                        _type.split("-> ")[0]
                        .split("python\n(variable) def ")[1]
                        .strip()
                        .split("(")[0]
                    )
                    _type_value = _type.split("-> ")[-1].strip().strip("`\n")
                else:
                    _type_name = _type.split(":")[0].split("python\n(variable) ")[1]
                    _type_value = _type.split(":")[1].strip().strip("`\n")
                result["variable"] = _type_name
                result["type"] = f"[{_type_value}]"
            elif _type.startswith("```python\n(parameter)"):
                if "->" in _type:
                    _type_name = (
                        _type.split("-> ")[0]
                        .split("python\n(parameter) def ")[1]
                        .strip()
                        .split("(")[0]
                    )
                    _type_value = _type.split("-> ")[-1].strip().strip("`\n")
                else:
                    _type_name = _type.split(":")[0].split("python\n(parameter) ")[1]
                    _type_value = _type.split(":")[1].strip().strip("`\n")
                result["parameter"] = _type_name
                result["type"] = f"[{_type_value}]"
            else:
                _t = hover_msg.contents.value.split("-> ")[1].split("\n")[0]
                res = get_type(_t)
            if result["type"] and "Literal" in result["type"]:
                type_value = result["type"].split("Literal[")[1].split("]")[0]
                type_value = eval(type_value)
                result["type"] = get_data_type(type_value)
                # res = get_type(_t)
            print(result)
        except Exception as e:
            print(e)
            res = None
    else:
        res = None
    logging.info(
        f"\nReturning - {func_name} - lineno: {lineno} col_offset: {col_offset}"
    )
    logging.info({"data": res, "hover_msg": hover_msg})
    return result


# hover_msg
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8088)
