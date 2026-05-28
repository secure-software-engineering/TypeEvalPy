import argparse
import ast
import json
import os
from collections import defaultdict
from pathlib import Path


def list_json_files(folder_path):
    python_files = sorted(Path(folder_path).rglob("*.json"))
    return python_files


def build_position_map(source_path):
    """Map (name, line_number) -> [1-indexed col_offsets] for every name
    occurrence in the source. Scalpel's runner doesn't emit col_offset, but
    for any (name, line) it gives us, the column is determined by the source.
    We keep all candidates so the enrichment can skip ambiguous cases."""
    positions = defaultdict(list)
    try:
        with open(source_path) as f:
            tree = ast.parse(f.read())
    except Exception:
        return positions

    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            positions[(node.id, node.lineno)].append(node.col_offset + 1)
        elif isinstance(node, ast.arg):
            positions[(node.arg, node.lineno)].append(node.col_offset + 1)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            prefix = (
                "async def " if isinstance(node, ast.AsyncFunctionDef) else "def "
            )
            positions[(node.name, node.lineno)].append(
                node.col_offset + len(prefix) + 1
            )
        elif isinstance(node, ast.ClassDef):
            positions[(node.name, node.lineno)].append(
                node.col_offset + len("class ") + 1
            )
    return positions


def _lookup_name(entry):
    """Return the source-level name to look up for this entry's position."""
    if "variable" in entry:
        name = entry["variable"]
        for sep in ("[", "."):
            if sep in name:
                name = name.split(sep, 1)[0]
                break
        return name
    if "parameter" in entry:
        return entry["parameter"]
    if "function" in entry:
        return entry["function"].rsplit(".", 1)[-1]
    return None


def enrich_with_col_offsets(source_path, entries):
    """Augment entries with col_offset by looking up the position of each
    entry's identifying name in the source file. Skip ambiguous cases
    (multiple candidates) so we never guess a position."""
    positions = build_position_map(source_path)
    for entry in entries:
        if "col_offset" in entry:
            continue
        name = _lookup_name(entry)
        if name is None:
            continue
        cands = sorted(set(positions.get((name, entry["line_number"]), [])))
        if len(cands) == 1:
            entry["col_offset"] = cands[0]
    return entries


def main_translator(args):
    json_files = list_json_files(args.bechmark_path)
    error_count = 0
    for file in json_files:
        try:
            # Run the inference here and gather results in /tmp/results
            pass

        except Exception as e:
            print(f"Command returned non-zero exit status: {e} for file: {file}")
            error_count += 1

    print(f"Runner finished with errors:{error_count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--bechmark_path",
        help="Specify the benchmark path",
        default="/tmp/micro-benchmark",
    )

    args = parser.parse_args()
    main_translator(args)
