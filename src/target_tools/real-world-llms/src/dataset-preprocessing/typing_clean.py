#!/usr/bin/env python3

# pip install libcst strip_hints
#!/usr/bin/env python3
"""
strip_types_resilient.py  –  Remove all type annotations even from
files that contain *syntax errors*.

Priority chain:
  1. LibCST  (fast, keeps formatting)
  2. strip‑hints  (token‑driven, preserves columns)
  3. tokenize heuristic  (last‑ditch, best‑effort)
"""
from __future__ import annotations
import argparse, io, re, sys, token, tokenize
from pathlib import Path
import re

# ───────────────────── LibCST pass ──────────────────────
import libcst as cst                      # raises ParserSyntaxError on bad files 

import ast

def is_valid_syntax(code: str) -> bool:
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False
        
class _StripCST(cst.CSTTransformer):
    def leave_Param(self,o,u):  return u.with_changes(annotation=None)
    def leave_FunctionDef(self,o,u):  return u.with_changes(returns=None)
    def leave_AsyncFunctionDef(self,o,u):  return u.with_changes(returns=None)
    def leave_AnnAssign(self,o,u):
        if u.value is None:
            return cst.RemovalSentinel.REMOVE
        return cst.Assign((cst.AssignTarget(target=u.target),), u.value)

def _via_libcst(code: str) -> str:
    try:
        mod = cst.parse_module(code)
        return mod.visit(_StripCST()).code
    except Exception as e:
        print(f"[libcst transformer failed] {type(e).__name__}: {e}", file=sys.stderr)
        raise  # to allow fallback to strip-hints

# ───────────────────── strip‑hints pass ─────────────────
def _via_strip_hints(code:str)->str:
    from strip_hints import strip_string_to_string  # needs ≥0.1.13
    return strip_string_to_string(code, to_empty=False, no_ast=True)

# ───────────────────── tokenize fallback ────────────────
_ann_start = re.compile(
    r"""
    (?:->)            # function returns
    |[:]              # parameter / var annotation
    """, re.VERBOSE
)


def _via_tokenize(code: str) -> str:
    """
    Fast, syntax‑error‑tolerant removal of *all* type hints that still
    preserves indentation, comments and blank lines.

    ✦ handles…
      • parameter annotations inside `def ...(`‑clauses
      • return annotations (`-> Type`) in function signatures
      • variable / attribute annotations (`x: int = 5`,  `x: int`)
    ✦ leaves alone every other colon – class headers, dict literals, slices …
    """
    # pre‑compiled patterns = speed + readability
    PARAM_ANN = re.compile(r'(\b\w+\b)\s*:\s*[^,)=]+')          # a: int  → a
    RETURN_ANN = re.compile(r'\s*->\s*[^:]+')                  # -> List[int] :
    VAR_ANN_VAL = re.compile(r'^(\s*)([\w.]+)\s*:\s*[^=\n]+\s*=\s*')  # x: int = 5
    VAR_ANN_BARE = re.compile(r'^\s*[\w.]+\s*:\s*[^=\n]+(\s*)(#.*)?$')# x: int

    out_lines: list[str] = []
    for ln in code.splitlines():

        # --- remove annotations in *function headers* -----------------
        if ln.lstrip().startswith("def ") and "(" in ln:
            ln = RETURN_ANN.sub("", ln, count=1)                # return type
            head, rest = ln.split("(", 1)
            if ")" not in rest:
                return rest, ""  # Or handle it in a way that fits your logic
            params, tail = rest.split(")", 1)
            params = PARAM_ANN.sub(r"\1", params)               # each “name: type”
            ln = f"{head}({params}){tail}"

        # --- variable / attribute annotations -------------------------
        is_header = ln.lstrip().startswith(
            ("class ", "def ", "if ", "for ", "while ", "with ",
             "try ", "except ", "elif ", "else ", "finally ")
        )
        if not is_header and ":" in ln:
            if VAR_ANN_VAL.search(ln):                          # keep the value
                ln = VAR_ANN_VAL.sub(r"\1\2 = ", ln)
            elif VAR_ANN_BARE.match(ln):                        # nothing but a hint
                ln = ""                                         # drop the line

        out_lines.append(ln)

    return "\n".join(out_lines)


# ───────────────────── dispatch chain ───────────────────
def strip(code: str) -> tuple[str, bool]:
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

# ───────────────────── CLI glue ─────────────────────────
def main()->None:
    input_path = Path("/mnt/hf_cache/rashida_manytype4py/many-types-4-py-dataset/scripts/typehint_clean/typing_showcase.py")
    output_path = Path("stripped.py")

    src = input_path.read_text(encoding="utf-8", errors="replace")
    code, used_fallback = strip(src)
    output_path.write_text(code, encoding="utf-8")

if __name__ == "__main__":
    main()
