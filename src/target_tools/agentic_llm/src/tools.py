import ast
import json
import os
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


def read_file(path: str) -> str:
    """Read the contents of a Python source file."""
    resolved = _validate_path(path)
    with open(resolved, "r", encoding="utf-8") as f:
        return f.read()


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

    # Collect function-level assignments per function node
    def collect_local_vars(func_node):
        local_vars = []
        for child in ast.walk(func_node):
            if child is func_node:
                continue
            if isinstance(child, ast.Assign):
                for target in child.targets:
                    if isinstance(target, ast.Name):
                        local_vars.append({
                            "name": target.id,
                            "line_number": child.lineno,
                            "col_offset": target.col_offset + 1,
                        })
            elif isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                # Don't descend into nested functions
                break
        return local_vars

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            params = []
            for arg in node.args.args:
                params.append({
                    "name": arg.arg,
                    "line_number": arg.lineno,
                    "col_offset": arg.col_offset + 1,
                })
            # posonlyargs, kwonlyargs, vararg, kwarg
            for arg in node.args.posonlyargs + node.args.kwonlyargs:
                params.append({
                    "name": arg.arg,
                    "line_number": arg.lineno,
                    "col_offset": arg.col_offset + 1,
                })
            if node.args.vararg:
                a = node.args.vararg
                params.append({
                    "name": f"*{a.arg}",
                    "line_number": a.lineno,
                    "col_offset": a.col_offset + 1,
                })
            if node.args.kwarg:
                a = node.args.kwarg
                params.append({
                    "name": f"**{a.arg}",
                    "line_number": a.lineno,
                    "col_offset": a.col_offset + 1,
                })

            # node.col_offset points to 'def'/'async'; name starts after the keyword + space
            keyword_len = len("async def ") if isinstance(node, ast.AsyncFunctionDef) else len("def ")
            summary["functions"].append({
                "name": node.name,
                "line_number": node.lineno,
                "col_offset": node.col_offset + keyword_len + 1,  # +keyword_len to skip past keyword, +1 for 1-indexing
                "parameters": params,
                "local_variables": collect_local_vars(node),
            })

        elif isinstance(node, ast.ClassDef):
            summary["classes"].append({
                "name": node.name,
                "line_number": node.lineno,
                "col_offset": node.col_offset + len("class ") + 1,  # skip 'class ' keyword, +1 for 1-indexing
            })

    # Module-level assignments (only top-level body)
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    summary["module_variables"].append({
                        "name": target.id,
                        "line_number": node.lineno,
                        "col_offset": target.col_offset + 1,
                    })
        elif isinstance(node, (ast.AnnAssign,)):
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


TOOL_DISPATCH = {
    "read_file": lambda args: read_file(**args),
    "list_directory": lambda args: list_directory(**args),
    "get_ast_summary": lambda args: get_ast_summary(**args),
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
