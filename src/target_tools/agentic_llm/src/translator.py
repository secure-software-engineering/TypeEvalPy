import json
import re


def _extract_class_name(text: str) -> str:
    """Extract type name from '<class 'int'>' style strings."""
    match = re.search(r"<class '([^']+)'>", text)
    return match.group(1) if match else text


def _strip_generics(text: str) -> str:
    """Strip generic parameters: 'List[int]' -> 'List', 'dict[str, int]' -> 'dict'."""
    return re.sub(r"\[.*\]", "", text).strip()


def _extract_common_patterns(text: str) -> str:
    """Extract type names from verbose LLM response patterns."""
    pattern = (
        r"<class '(\w+)'>|<function.*>|Return type of `.*?`: (\w+)"
        r"|Return type: (\w+)|The return type of '.*?' is (\w+)"
        r"|The type of '.*?' is a? (\w+)|Type of `.*?`: (\w+)"
        r"|Type of `.*?` is `(\w+)`|`.*?` return type: `(\w+)`"
        r"|`(\w+)`: `\w+`|column \d+: `(\w+)`|column \d+ is '(\w+)'"
        r"|type of '.*?': `(\w+)`"
    )
    matches = re.findall(pattern, text)
    if matches:
        for match in matches:
            found = [m for m in match if m]
            if found:
                return found[0]
    return text


_PIPELINE = [_extract_class_name, _extract_common_patterns, _strip_generics]

_TYPE_MAPPING = {
    "integer": "int",
    "string": "str",
    "boolean": "bool",
    "dictonary": "dict",   # preserving original typo from llms/translator.py
    "dictionary": "dict",
    "method": "callable",
    "func": "callable",
    "function": "callable",
    "lambda": "callable",
    "none": "None",
    "nonetype": "None",
    "notype": "None",
    "list": "list",
    "tuple": "tuple",
    "set": "set",
    "dict": "dict",
    "float": "float",
    "int": "int",
    "str": "str",
    "bool": "bool",
    "bytes": "bytes",
}


def _normalize_type(t: str) -> str:
    """Apply the full normalization pipeline to a single type string."""
    for fn in _PIPELINE:
        t = fn(t)
    t = t.strip()
    lower = t.lower()
    if lower in _TYPE_MAPPING:
        return _TYPE_MAPPING[lower]
    # Preserve module-qualified names (e.g. itertools.count, to_import.A) as-is
    return t


def translate_content(data) -> list:
    """
    Normalize type strings in annotation list to TypeEvalPy canonical names.
    Accepts either a list of dicts or a JSON string.
    Returns a normalized list.
    """
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON input: {e}")

    if not isinstance(data, list):
        raise ValueError(f"Expected a list, got {type(data)}")

    for entry in data:
        if "type" in entry and isinstance(entry["type"], list):
            entry["type"] = [_normalize_type(t) for t in entry["type"]]
        elif "type" not in entry:
            entry["type"] = []

    return data
