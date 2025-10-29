#!/usr/bin/env python3
from __future__ import annotations
import argparse
import ast
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import libcst as cst

# ---------------- Type string normalization ----------------

_RENDER_MODULE = cst.Module(body=())

def _code(expr: cst.BaseExpression) -> str:
    return _RENDER_MODULE.code_for_node(expr).strip()

_NAME_MAP = {
    'typing.Callable': 'callable',
    'typing.Iterator': 'generator',
    'typing.Type': 'type',
    'None': 'Nonetype',
}

def normalize_types(type_str: str, *, strip_generics: bool = False) -> list[str]:
    """
    Parse type_str and return a list of top-level alternates.
    If strip_generics=True, collapse generics so that e.g. list[int] -> 'list',
    typing.Callable[[int], None] -> 'typing.Callable'.
    """
    s = type_str.strip()
    if not s:
        return [""]

    try:
        expr = cst.parse_expression(s)
    except Exception:
        return [s]

    def _cst_qualified_name(node: cst.BaseExpression) -> str | None:
        if isinstance(node, cst.Name):
            return node.value
        if isinstance(node, cst.Attribute):
            parts = []
            cur: cst.BaseExpression | None = node
            while isinstance(cur, cst.Attribute):
                parts.append(cur.attr.value)
                cur = cur.value
            if isinstance(cur, cst.Name):
                parts.append(cur.value)
                return ".".join(reversed(parts))
        return None

    def _is_typing_name(name: str | None, base: str) -> bool:
        return bool(name) and (name == base or name == f"typing.{base}")

    # Split only at TOP-LEVEL unions (| and typing.Union[...])
    def split_top_level(e: cst.BaseExpression) -> list[cst.BaseExpression]:
        if isinstance(e, cst.BinaryOperation) and isinstance(e.operator, cst.BitOr):
            return split_top_level(e.left) + split_top_level(e.right)
        if isinstance(e, cst.Subscript):
            base_name = _cst_qualified_name(e.value)
            if _is_typing_name(base_name, "Union"):
                alts: list[cst.BaseExpression] = []
                for sl in e.slice:
                    if isinstance(sl, cst.SubscriptElement) and isinstance(sl.slice, cst.Index):
                        alts.extend(split_top_level(sl.slice.value))
                return alts
        return [e]

    # Desugar Optional[T] -> [T, None], Annotated[T, ...] -> [T]
    def desugar(e: cst.BaseExpression) -> list[cst.BaseExpression]:
        if isinstance(e, cst.Subscript):
            base_name = _cst_qualified_name(e.value)
            if _is_typing_name(base_name, "Annotated"):
                if e.slice:
                    first = e.slice[0]
                    if isinstance(first, cst.SubscriptElement) and isinstance(first.slice, cst.Index):
                        return desugar(first.slice.value)
                return [e]
            if _is_typing_name(base_name, "Optional"):
                if e.slice:
                    first = e.slice[0]
                    if isinstance(first, cst.SubscriptElement) and isinstance(first.slice, cst.Index):
                        return desugar(first.slice.value) + [cst.Name("None")]
                return [e]
        return [e]

    top_level_parts = split_top_level(expr)
    desugared: list[cst.BaseExpression] = []
    for p in top_level_parts:
        desugared.extend(desugar(p))

    # Optionally collapse generics/subscripts to just their base name
    out: list[str] = []
    for part in desugared:
        if strip_generics:
            if isinstance(part, cst.Subscript):
                name = _cst_qualified_name(part.value)

                if name is None:
                    name = _code(part)
            else:
                name = _code(part)

            if name in _NAME_MAP:
                name = _NAME_MAP[name]

            if name.startswith("main."):
                name = name[5:]

            out.append(name)
        else:
            out.append(_code(part))
    return out


# ---------------- AST utilities ----------------

import ast
from pathlib import Path
from typing import Dict, List, Optional, Tuple

class FuncIndex(ast.NodeVisitor):
    """
    Index positions for functions and methods by qualified name.

    Keys look like:
      - "func" for top-level functions
      - "MyClass.method" for methods
      - "outer.inner" for nested functions
      - "MyClass.method.inner" for nested functions inside methods

    Stored (0-based cols):
      - func_params[qname][param] -> (lineno, col)
      - func_name_pos[qname] -> (lineno, col_of_function_name)
    """

    def __init__(self, src: str):
        self.func_params: Dict[str, Dict[str, Tuple[int, int]]] = {}
        self.func_name_pos: Dict[str, Tuple[int, int]] = {}
        self._lines = src.splitlines()
        self._name_stack: List[str] = []

    def _qualified(self, name: str) -> str:
        parts: List[str] = self._name_stack + [name]
        return ".".join(parts)

    def visit_ClassDef(self, node: ast.ClassDef):
        self._name_stack.append(node.name)
        self.generic_visit(node)
        self._name_stack.pop()

    def visit_FunctionDef(self, node: ast.FunctionDef):
        self._record_function(node)
        self._name_stack.append(node.name)
        self.generic_visit(node)
        self._name_stack.pop()

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        self._record_function(node)
        self._name_stack.append(node.name)
        self.generic_visit(node)
        self._name_stack.pop()

    def _record_function(self, node: ast.FunctionDef | ast.AsyncFunctionDef):
        qname = self._qualified(node.name)

        # Collect parameter positions
        param_map: Dict[str, Tuple[int, int]] = {}

        def add_arg(a: Optional[ast.arg]):
            if not a:
                return
            ln = getattr(a, "lineno", getattr(node, "lineno", 1))
            co = getattr(a, "col_offset", getattr(node, "col_offset", 0))
            param_map[a.arg] = (ln, co)

        args = getattr(node, "args", None)
        if args:
            for a in getattr(args, "posonlyargs", []):
                add_arg(a)
            for a in getattr(args, "args", []):
                add_arg(a)
            add_arg(getattr(args, "vararg", None))
            for a in getattr(args, "kwonlyargs", []):
                add_arg(a)
            add_arg(getattr(args, "kwarg", None))

        self.func_params[qname] = param_map

        # Use the column where the function name begins (not 'def' / 'async')
        lineno = getattr(node, "lineno", 1)
        line = self._lines[lineno - 1] if 1 <= lineno <= len(self._lines) else ""
        def_col = getattr(node, "col_offset", 0)

        search_start = max(def_col - 2, 0)
        def_index = line.find("def", search_start)
        if def_index == -1:
            def_index = line.find("def")

        name_index = -1
        if def_index != -1:
            name_index = line.find(node.name, def_index + 3)
        if name_index == -1:
            name_index = def_col  # fallback

        self.func_name_pos[qname] = (lineno, name_index)


def index_functions(file_path: Path) -> FuncIndex:
    src = file_path.read_text(encoding="utf-8")
    tree = ast.parse(src, filename=str(file_path))
    idx = FuncIndex(src)
    idx.visit(tree)
    return idx

# ---------------- Core processing ----------------

def simplify_path(file_str: str, root: Path|None = None) -> str:
    """
    Try to make file path relative to current working directory.
    If not possible, return absolute resolved path.
    """
    p = Path(file_str).resolve()
    if root is None:
        root = Path.cwd()
    try:
        return str(p.relative_to(root))
    except ValueError:
        return str(p)

def process_annotations(spec: dict, root: Path|None = None, *, strip_generics: bool = False) -> List[dict]:
    out: List[dict] = []

    files = spec.get("files", {})
    if not isinstance(files, dict):
        raise ValueError('Top-level must contain "files": { ... }')

    for file_str, file_info in files.items():
        file_path = Path(file_str)
        if not file_path.exists():
            print(f"warning: {file_path} does not exist; skipping", file=sys.stderr)
            continue

        try:
            idx = index_functions(file_path)
        except SyntaxError as e:
            print(f"error: cannot parse {file_path}: {e}", file=sys.stderr)
            continue

        functions = (file_info or {}).get("functions", {})
        if not isinstance(functions, dict):
            continue

        simplified_file = simplify_path(file_str, root)

        for func_name, fdesc in functions.items():
            if not isinstance(fdesc, dict):
                continue

            func_ln, func_name_col = idx.func_name_pos.get(func_name, (1, 0))

            # Parameters
            args_desc = fdesc.get("args", {})
            if isinstance(args_desc, dict):
                for param_name, type_str in args_desc.items():
                    types = normalize_types(str(type_str), strip_generics=strip_generics)
                    ln, co = idx.func_params.get(func_name, {}).get(
                        param_name,
                        (func_ln, func_name_col),
                    )
                    out.append({
                        "file": simplified_file,
                        "line_number": ln,
                        "col_offset": co+1,
                        "function": func_name,
                        "parameter": param_name,
                        "type": types,
                    })

            # Function return
            retval = fdesc.get("retval")
            if retval is not None:
                types = normalize_types(str(retval), strip_generics=strip_generics)
                out.append({
                    "file": simplified_file,
                    "line_number": func_ln,
                    "col_offset": func_name_col+1,
                    "function": func_name,
                    "type": types,
                })

    return out


# ---------------- CLI ----------------

def main():
    ap = argparse.ArgumentParser(description="Read types from JSON; use AST only for positions. Function col_offset = start of function name.")
    ap.add_argument("input_json", help="Path to JSON file with function/type info")
    ap.add_argument("-o", "--output", help="Write output JSON to this file (default: stdout)")
    args = ap.parse_args()

    spec_path = Path(args.input_json)
    spec = json.loads(spec_path.read_text(encoding="utf-8"))

    records = process_annotations(spec)
    out = json.dumps(records, indent=2, ensure_ascii=False)

    if args.output:
        Path(args.output).write_text(out, encoding="utf-8")
    else:
        print(out)

if __name__ == "__main__":
    main()
