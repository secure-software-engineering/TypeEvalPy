#!/usr/bin/env python3
"""
strip_types_resilient.py

Removes all type annotations from Python source files — even from files with *syntax errors*.

The tool uses a prioritized fallback chain:
1. **LibCST**: Fast and preserves formatting; fails on syntax errors.
2. **strip-hints**: Token-driven; works better with broken syntax than AST-based tools.
3. **Tokenize fallback**: Custom regex/token-based solution as a last-resort best-effort approach.

Dependencies:
- libcst
- strip-hints (>=0.1.13)
"""

from __future__ import annotations
import argparse, io, re, sys, token, tokenize
from pathlib import Path
import ast

# ────────────────────────────── LibCST strategy ───────────────────────────────

import libcst as cst  # Raises ParserSyntaxError for invalid syntax

def is_valid_syntax(code: str) -> bool:
    """
    Check if code is syntactically valid using Python's built-in `ast` parser.
    """
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False

class _StripCST(cst.CSTTransformer):
    """
    LibCST transformer class to remove:
    - Parameter annotations
    - Return type annotations
    - Annotated assignments (AnnAssign)
    """
    def leave_Param(self, original_node, updated_node):
        return updated_node.with_changes(annotation=None)

    def leave_FunctionDef(self, original_node, updated_node):
        return updated_node.with_changes(returns=None)

    def leave_AsyncFunctionDef(self, original_node, updated_node):
        return updated_node.with_changes(returns=None)

    def leave_AnnAssign(self, original_node, updated_node):
        if updated_node.value is None:
            return cst.RemovalSentinel.REMOVE
        return cst.Assign((cst.AssignTarget(target=updated_node.target),), updated_node.value)

def _via_libcst(code: str) -> str:
    """
    Attempt to strip annotations using LibCST (preserves formatting and comments).
    """
    try:
        mod = cst.parse_module(code)
        return mod.visit(_StripCST()).code
    except Exception as e:
        print(f"[libcst transformer failed] {type(e).__name__}: {e}", file=sys.stderr)
        raise

# ────────────────────────────── strip‑hints strategy ───────────────────────────────

def _via_strip_hints(code: str) -> str:
    """
    Use `strip-hints` to remove annotations in a token-based way.
    """
    from strip_hints import strip_string_to_string
    return strip_string_to_string(code, to_empty=False, no_ast=True)

# ────────────────────────────── tokenize fallback ───────────────────────────────

# Precompiled regex patterns for performance and clarity
PARAM_ANN = re.compile(r'(\b\w+\b)\s*:\s*[^,)=]+')                    # e.g., a: int → a
RETURN_ANN = re.compile(r'\s*->\s*[^:]+')                             # e.g., -> int
VAR_ANN_VAL = re.compile(r'^(\s*)([\w.]+)\s*:\s*[^=\n]+\s*=\s*')      # e.g., x: int = 42
VAR_ANN_BARE = re.compile(r'^\s*[\w.]+\s*:\s*[^=\n]+(\s*)(#.*)?$')    # e.g., x: int

def _via_tokenize(code: str) -> str:
    """
    Last-resort fallback that strips type annotations using regex patterns,
    while preserving formatting, indentation, and comments.
    """
    out_lines: list[str] = []
    for ln in code.splitlines():

        # --- Remove function signature annotations ---
        if ln.lstrip().startswith("def ") and "(" in ln:
            ln = RETURN_ANN.sub("", ln, count=1)
            head, rest = ln.split("(", 1)
            if ")" not in rest:
                return rest, ""  # Not a well-formed function, skip
            params, tail = rest.split(")", 1)
            params = PARAM_ANN.sub(r"\1", params)
            ln = f"{head}({params}){tail}"

        # --- Remove variable / attribute annotations ---
        is_header = ln.lstrip().startswith((
            "class ", "def ", "if ", "for ", "while ", "with ",
            "try ", "except ", "elif ", "else ", "finally "
        ))

        if not is_header and ":" in ln:
            if VAR_ANN_VAL.search(ln):        # Keep value, drop annotation
                ln = VAR_ANN_VAL.sub(r"\1\2 = ", ln)
            elif VAR_ANN_BARE.match(ln):      # Drop bare annotation line
                ln = ""

        out_lines.append(ln)

    return "\n".join(out_lines)

# ────────────────────────────── Dispatcher ───────────────────────────────

def strip(code: str) -> tuple[str, bool]:
    """
    Try all available methods to remove type annotations.

    Returns:
        A tuple of (stripped_code, used_fallback)
    """
    if not is_valid_syntax(code):
        print("[warn] Skipping LibCST due to invalid syntax", file=sys.stderr)
    else:
        try:
            return _via_libcst(code), False
        except Exception as e:
            print(f"[warn] LibCST failed ({type(e).__name__}: {e}) – trying strip‑hints", file=sys.stderr)

    try:
        return _via_strip_hints(code), True
    except Exception as e:
        print(f"[warn] strip‑hints failed ({type(e).__name__}) – falling back to tokenize", file=sys.stderr)

    return _via_tokenize(code), True

# ────────────────────────────── CLI entry point ───────────────────────────────

def main() -> None:
    """
    Main function for CLI usage.
    Reads a hardcoded input path, strips types, and writes to 'stripped.py'.
    """
    input_path = Path("/mnt/hf_cache/rashida_manytype4py/many-types-4-py-dataset/scripts/typehint_clean/typing_showcase.py")
    output_path = Path("stripped.py")

    src = input_path.read_text(encoding="utf-8", errors="replace")
    code, used_fallback = strip(src)
    output_path.write_text(code, encoding="utf-8")

if __name__ == "__main__":
    main()