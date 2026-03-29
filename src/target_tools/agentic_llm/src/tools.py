import ast
import io
import json
import os
import re
import tokenize
from pathlib import Path

# Configurable via env var for local development; defaults to Docker path
ALLOWED_BASE = os.environ.get("TYPEEVALPY_BENCHMARK_PATH", "/tmp/micro-benchmark")


def _validate_path(path: str) -> str:
    resolved = str(Path(path).resolve())
    if not resolved.startswith(ALLOWED_BASE):
        raise PermissionError(f"Path outside benchmark directory: {path}")
    if not os.path.exists(resolved):
        raise FileNotFoundError(f"Path does not exist: {path}")
    return resolved


def _strip_comments(source: str) -> str:
    """Replace comment text with bare '#', preserving line numbers."""
    lines = source.splitlines(keepends=True)
    try:
        tokens = tokenize.generate_tokens(io.StringIO(source).readline)
        for tok_type, _, tok_start, _, _ in tokens:
            if tok_type == tokenize.COMMENT:
                row, col = tok_start
                line = lines[row - 1]
                stripped = line.rstrip("\r\n")
                ending = line[len(stripped):]
                lines[row - 1] = line[:col] + "#" + ending
    except tokenize.TokenError:
        pass
    return "".join(lines)


def read_file(path: str) -> str:
    """Read the contents of a Python source file with comments stripped."""
    resolved = _validate_path(path)
    with open(resolved, "r", encoding="utf-8") as f:
        source = f.read()
    if resolved.endswith(".py"):
        return _strip_comments(source)
    return source


def list_directory(path: str) -> str:
    """List files and subdirectories at the given path."""
    resolved = _validate_path(path)
    if not os.path.isdir(resolved):
        raise NotADirectoryError(f"Not a directory: {path}")
    entries = sorted(os.listdir(resolved))
    return "\n".join(entries) if entries else "(empty directory)"


def get_ast_summary(path: str) -> str:
    """
    Parse a Python file and return a JSON summary of its structure with
    exact line_number and col_offset for each element (1-indexed col_offset).
    """
    resolved = _validate_path(path)
    with open(resolved, "r", encoding="utf-8") as f:
        source = f.read()

    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        return json.dumps({"error": f"SyntaxError: {e}"})

    filename = Path(resolved).name

    summary = {
        "filename": filename,
        "functions": [],
        "classes": [],
        "module_variables": [],
    }

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _flatten_assign_targets(targets, stmt_lineno):
        """
        Yield (name, lineno, col_offset+1) for every Name/Attribute leaf in
        an assignment target list, recursively handling Tuple/List unpacking.
        Uses stmt_lineno as a fallback when a sub-target lacks its own lineno
        (e.g. elements inside a Tuple target share the statement's lineno).
        """
        for target in targets:
            yield from _flatten_target(target, stmt_lineno)

    def _flatten_target(target, stmt_lineno):
        if isinstance(target, ast.Name):
            yield (target.id, getattr(target, "lineno", stmt_lineno), target.col_offset + 1)
        elif isinstance(target, ast.Attribute):
            # e.g. self.x = ...
            if isinstance(target.value, ast.Name):
                attr_name = f"{target.value.id}.{target.attr}"
                yield (attr_name, getattr(target, "lineno", stmt_lineno), target.col_offset + 1)
        elif isinstance(target, (ast.Tuple, ast.List)):
            for elt in target.elts:
                yield from _flatten_target(elt, stmt_lineno)

    def collect_local_vars(func_node):
        """
        Collect variable names (with line/col) from a function body.
        Handles: simple assignments, tuple unpacking, for-loop targets,
        walrus operators, augmented assignments, and self.x attributes.
        Does NOT descend into nested functions or class definitions.
        """
        local_vars = []
        seen = set()  # deduplicate (name, line, col)

        def _add(name, lineno, col):
            key = (name, lineno, col)
            if key not in seen:
                seen.add(key)
                local_vars.append({"name": name, "line_number": lineno, "col_offset": col})

        def _walk_body(stmts):
            for stmt in stmts:
                # Don't descend into nested functions or classes
                if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                    continue

                # Simple / tuple-unpacking assignments
                if isinstance(stmt, ast.Assign):
                    for name, ln, col in _flatten_assign_targets(stmt.targets, stmt.lineno):
                        _add(name, ln, col)

                # Annotated assignment (x: int = ...)
                elif isinstance(stmt, ast.AnnAssign):
                    for name, ln, col in _flatten_target(stmt.target, stmt.lineno):
                        _add(name, ln, col)

                # Augmented assignment (a += 1)
                elif isinstance(stmt, ast.AugAssign):
                    if isinstance(stmt.target, ast.Name):
                        _add(stmt.target.id, stmt.lineno, stmt.target.col_offset + 1)

                # For-loop target (for x in ..., for a, b in ...)
                elif isinstance(stmt, ast.For):
                    for name, ln, col in _flatten_target(stmt.target, stmt.lineno):
                        _add(name, ln, col)
                    _walk_body(stmt.body)
                    _walk_body(stmt.orelse)

                # With statement (with open() as f:)
                elif isinstance(stmt, ast.With):
                    for item in stmt.items:
                        if item.optional_vars is not None:
                            for name, ln, col in _flatten_target(item.optional_vars, stmt.lineno):
                                _add(name, ln, col)
                    _walk_body(stmt.body)

                # Exception handler (except E as e:)
                elif isinstance(stmt, ast.ExceptHandler):
                    if stmt.name:
                        _add(stmt.name, stmt.lineno, stmt.col_offset + 1)

                # Try block — recurse into handlers and body
                elif isinstance(stmt, ast.Try):
                    _walk_body(stmt.body)
                    for handler in stmt.handlers:
                        _walk_body([handler])
                    _walk_body(stmt.orelse)
                    _walk_body(stmt.finalbody if hasattr(stmt, "finalbody") else [])

                # If/While — recurse
                elif isinstance(stmt, (ast.If, ast.While)):
                    _walk_body(stmt.body)
                    _walk_body(stmt.orelse)

                # Walrus operator inside expressions and comprehension loop variables
                # (both are sub-expression nodes reachable via ast.walk)
                for child in ast.walk(stmt):
                    if isinstance(child, ast.NamedExpr):
                        _add(child.target.id,
                             getattr(child.target, "lineno", stmt.lineno),
                             child.target.col_offset + 1)
                    elif isinstance(child, ast.comprehension):
                        for name, ln, col in _flatten_target(child.target, stmt.lineno):
                            _add(name, ln, col)

        _walk_body(func_node.body)
        return local_vars

    # ------------------------------------------------------------------
    # Build the qualified name prefix stack while walking the AST.
    # We do a manual recursive walk (not ast.walk) so we can track the
    # enclosing class chain for method/class-variable naming.
    # ------------------------------------------------------------------

    def _visit(node, class_stack):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            params = []
            for arg in node.args.args:
                params.append({
                    "name": arg.arg,
                    "line_number": arg.lineno,
                    "col_offset": arg.col_offset + 1,
                })
            for arg in node.args.posonlyargs + node.args.kwonlyargs:
                params.append({
                    "name": arg.arg,
                    "line_number": arg.lineno,
                    "col_offset": arg.col_offset + 1,
                })
            if node.args.vararg:
                a = node.args.vararg
                params.append({"name": f"*{a.arg}", "line_number": a.lineno, "col_offset": a.col_offset + 1})
            if node.args.kwarg:
                a = node.args.kwarg
                params.append({"name": f"**{a.arg}", "line_number": a.lineno, "col_offset": a.col_offset + 1})

            keyword_len = len("async def ") if isinstance(node, ast.AsyncFunctionDef) else len("def ")
            qualified_name = ".".join(class_stack + [node.name]) if class_stack else node.name

            summary["functions"].append({
                "name": qualified_name,
                "line_number": node.lineno,
                "col_offset": node.col_offset + keyword_len + 1,
                "parameters": params,
                "local_variables": collect_local_vars(node),
            })
            # Do NOT recurse into function body for class/function discovery here
            # (nested functions are handled by collect_local_vars skipping them,
            #  but we still want to find nested class definitions)
            for child in node.body:
                _visit(child, class_stack)

        elif isinstance(node, ast.ClassDef):
            qualified_class = ".".join(class_stack + [node.name])
            class_vars = []
            for stmt in node.body:
                if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                    continue  # handled separately
                if isinstance(stmt, ast.Assign):
                    for name, ln, col in _flatten_assign_targets(stmt.targets, stmt.lineno):
                        # Only plain Name targets at class body level → ClassName.varname
                        if "." not in name:
                            class_vars.append({"name": f"{qualified_class}.{name}", "line_number": ln, "col_offset": col})
                elif isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name):
                    class_vars.append({
                        "name": f"{qualified_class}.{stmt.target.id}",
                        "line_number": stmt.lineno,
                        "col_offset": stmt.target.col_offset + 1,
                    })

            summary["classes"].append({
                "name": qualified_class,
                "line_number": node.lineno,
                "col_offset": node.col_offset + len("class ") + 1,
                "class_variables": class_vars,
            })
            # Recurse into class body
            for child in node.body:
                _visit(child, class_stack + [node.name])

    for top_node in tree.body:
        _visit(top_node, [])

    # Module-level assignments (only top-level body)
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for name, ln, col in _flatten_assign_targets(node.targets, node.lineno):
                # Skip attribute targets (self.x etc.) at module level — unlikely but safe
                if "." not in name:
                    summary["module_variables"].append({
                        "name": name,
                        "line_number": ln,
                        "col_offset": col,
                    })
            # Also capture comprehension loop variables from the RHS
            if node.value is not None:
                for child in ast.walk(node.value):
                    if isinstance(child, ast.comprehension):
                        for name, ln, col in _flatten_target(child.target, node.lineno):
                            if "." not in name:
                                summary["module_variables"].append({
                                    "name": name,
                                    "line_number": ln,
                                    "col_offset": col,
                                })
        elif isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name):
                summary["module_variables"].append({
                    "name": node.target.id,
                    "line_number": node.lineno,
                    "col_offset": node.target.col_offset + 1,
                })

    return json.dumps(summary, indent=2)


def submit_type_annotations(annotations: list) -> str:
    """
    Validate annotation list structure and signal completion.
    Raises ValueError on schema violations.
    """
    if not isinstance(annotations, list):
        raise ValueError("annotations must be a list")

    for i, entry in enumerate(annotations):
        if not isinstance(entry, dict):
            raise ValueError(f"Entry {i} must be a dict, got {type(entry)}")
        for required_field in ("file", "line_number", "col_offset", "type"):
            if required_field not in entry:
                raise ValueError(f"Entry {i} missing required field: '{required_field}'")
        if not isinstance(entry["type"], list):
            raise ValueError(f"Entry {i}: 'type' must be a list of strings")
        if not isinstance(entry["line_number"], int):
            raise ValueError(f"Entry {i}: 'line_number' must be an integer")
        has_function = "function" in entry
        has_parameter = "parameter" in entry
        has_variable = "variable" in entry
        if not has_function and not has_parameter and not has_variable:
            raise ValueError(
                f"Entry {i}: must have at least one of 'function', 'parameter', or 'variable'"
            )

    return json.dumps({"status": "accepted", "count": len(annotations)})


def _build_skeleton(path: str) -> list:
    """
    Build a deterministic ordered list of annotation skeletons (all fields except 'type')
    by parsing the JSON output of get_ast_summary.  The ordering is:
      per function (source order): return entry, then parameters, then local variables
      then: class-level variables (source order)
      then: module-level variables (source order)
    Both generate_type_questions and submit_type_answers rely on this same ordering.
    """
    summary = json.loads(get_ast_summary(path))
    if "error" in summary:
        return []
    filename = summary["filename"]
    items = []

    for func in summary.get("functions", []):
        fname = func["name"]
        items.append({
            "file": filename,
            "line_number": func["line_number"],
            "col_offset": func["col_offset"],
            "function": fname,
        })
        for param in func.get("parameters", []):
            items.append({
                "file": filename,
                "line_number": param["line_number"],
                "col_offset": param["col_offset"],
                "function": fname,
                "parameter": param["name"],
            })
        for var in func.get("local_variables", []):
            items.append({
                "file": filename,
                "line_number": var["line_number"],
                "col_offset": var["col_offset"],
                "function": fname,
                "variable": var["name"],
            })

    for cls in summary.get("classes", []):
        for cv in cls.get("class_variables", []):
            items.append({
                "file": filename,
                "line_number": cv["line_number"],
                "col_offset": cv["col_offset"],
                "variable": cv["name"],
            })

    for mv in summary.get("module_variables", []):
        items.append({
            "file": filename,
            "line_number": mv["line_number"],
            "col_offset": mv["col_offset"],
            "variable": mv["name"],
        })

    return items


def _item_to_question(idx: int, item: dict) -> str:
    """Generate a natural language type-inference question for an annotation skeleton entry."""
    line = item["line_number"]
    if "parameter" in item:
        return (
            f"{idx}. What is the type of parameter '{item['parameter']}'"
            f" in function '{item['function']}' (line {line})?"
        )
    elif "variable" in item:
        func_ctx = f" inside '{item['function']}'" if "function" in item else ""
        return f"{idx}. What is the type of variable '{item['variable']}'{func_ctx} (line {line})?"
    else:
        return f"{idx}. What does function '{item['function']}' return (line {line})?"


def generate_type_questions(path: str) -> str:
    """
    Parse a Python file via its AST and return numbered type-inference questions
    for every function return, parameter, and variable in the file.
    Call submit_type_answers with this file path and your answers when done.
    """
    items = _build_skeleton(path)
    if not items:
        return "No type elements found in this file."

    lines = [
        f"Type questions for {Path(_validate_path(path)).name} ({len(items)} elements).",
        "For each question answer on its own line as:  N. type",
        "Use comma-separated types if an element can have multiple types: N. int, str",
        "",
    ]
    for i, item in enumerate(items, 1):
        lines.append(_item_to_question(i, item))
    return "\n".join(lines)


def submit_type_answers(path: str, answers: str) -> str:
    """
    Map numbered answers back to the skeleton generated by generate_type_questions.
    `answers` must be a newline-separated list of  'N. type'  lines (one per question).
    Multiple types for one element: 'N. int, str'.
    This ends the agent loop.
    """
    items = _build_skeleton(path)

    # Parse "N. type" or "N. type1, type2" lines
    answer_map: dict[int, list[str]] = {}
    for line in answers.strip().splitlines():
        m = re.match(r"^(\d+)\.\s*(.+)$", line.strip())
        if m:
            idx = int(m.group(1))
            types = [t.strip() for t in m.group(2).split(",") if t.strip()]
            answer_map[idx] = types

    missing = [i for i in range(1, len(items) + 1) if i not in answer_map]
    if missing:
        raise ValueError(
            f"Missing answers for question(s): {missing}. "
            f"Please provide an answer for every question number 1–{len(items)}."
        )

    annotations = []
    for i, item in enumerate(items, 1):
        entry = dict(item)
        entry["type"] = answer_map[i]
        annotations.append(entry)

    return json.dumps({"status": "accepted", "count": len(annotations), "annotations": annotations})


TOOL_DISPATCH = {
    "read_file": lambda args: read_file(**args),
    "list_directory": lambda args: list_directory(**args),
    "get_ast_summary": lambda args: get_ast_summary(**args),
    "generate_type_questions": lambda args: generate_type_questions(**args),
    "submit_type_answers": lambda args: submit_type_answers(**args),
    "submit_type_annotations": lambda args: submit_type_annotations(**args),
}

TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": (
                "Read the contents of a Python source file inside the benchmark directory. "
                "Use this to understand code logic before inferring types."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Absolute path to the file inside the container.",
                    }
                },
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_directory",
            "description": (
                "List files and subdirectories at the given path. "
                "Use this to discover helper modules imported by main.py."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Absolute path to the directory.",
                    }
                },
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_ast_summary",
            "description": (
                "Get a structured JSON summary of a Python file's AST. "
                "Returns all functions with their parameters and local variables, "
                "all classes, and all module-level variables — each with exact "
                "line_number and col_offset (1-indexed). "
                "Use this to determine the exact coordinates needed for the result JSON."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Absolute path to the Python file.",
                    }
                },
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "generate_type_questions",
            "description": (
                "Parse a Python file's AST and return numbered type-inference questions "
                "for every function return type, parameter, and variable in the file. "
                "Call this AFTER reading the source code. Then answer each question in "
                "plain text ('1. int', '2. str, None', ...) and call submit_type_answers."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Absolute path to the Python file to question.",
                    }
                },
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "submit_type_answers",
            "description": (
                "Submit your answers to the type questions generated by generate_type_questions. "
                "This ENDS the agent loop. "
                "'answers' must be a newline-separated list of 'N. type' lines — one per question. "
                "Use comma-separated types for elements that can have multiple types: 'N. int, str'."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Same file path passed to generate_type_questions.",
                    },
                    "answers": {
                        "type": "string",
                        "description": (
                            "Newline-separated answers, one per question number. "
                            "Example:\n1. int\n2. str\n3. MyClass\n4. int, None"
                        ),
                    },
                },
                "required": ["path", "answers"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "submit_type_annotations",
            "description": (
                "Submit your final type inference results. This ENDS the agent loop. "
                "The annotations list must follow TypeEvalPy format. "
                "Each entry must have: 'file' (string), 'line_number' (int), "
                "'col_offset' (int), 'type' (list of strings), and at least one of: "
                "'function' (for return types), 'parameter' + 'function' (for param types), "
                "or 'variable' (for variable types)."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "annotations": {
                        "type": "array",
                        "description": "List of type annotation facts in TypeEvalPy format.",
                        "items": {
                            "type": "object",
                            "properties": {
                                "file": {"type": "string"},
                                "line_number": {"type": "integer"},
                                "col_offset": {"type": "integer"},
                                "type": {
                                    "type": "array",
                                    "items": {"type": "string"},
                                },
                                "function": {"type": "string"},
                                "parameter": {"type": "string"},
                                "variable": {"type": "string"},
                            },
                            "required": ["file", "line_number", "col_offset", "type"],
                        },
                    }
                },
                "required": ["annotations"],
            },
        },
    },
]
