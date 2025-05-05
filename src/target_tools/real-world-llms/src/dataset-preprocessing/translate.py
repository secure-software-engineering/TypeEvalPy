import argparse
import json
import os
import re
from pathlib import Path
import utils

def normalize_type(type_str, nested_level=0):
    """
    Normalize type strings by:
    - Removing module prefixes like 'builtins.' or 'typing.'
    - Mapping ambiguous or inconsistent type names to standard Python types
    - Simplifying nested generics (e.g., List[List[Tuple[str]]]) into general types like Any beyond a certain depth

    Args:
        type_str (str): The type string to normalize.
        nested_level (int): Current nesting depth, used to replace deep generics with 'Any'.

    Returns:
        str: A cleaned and normalized type string.
    """
    if type_str is None:
        return None

    # Remove quotes
    if type_str.startswith('"') and type_str.endswith('"'):
        type_str = type_str.strip('"')
        
    type_mappings = {
        "builtins.": "",
        "typing.": "",
    }

    # Known incorrect or inconsistent types to correct
    additional_type_mappings = {
        "integer": "int",
        "string": "str",
        "dictonary": "dict",
        "method": "Callable",
        "func": "Callable",
        "function": "Callable",
        "none": "None",
        "Nonetype": "None",
        "nonetype": "None",
        "NoneType": "None",
    }

    # Replace module prefixes
    for prefix, replacement in type_mappings.items():
        type_str = type_str.replace(prefix, replacement)

    # Apply known mappings
    type_str = additional_type_mappings.get(type_str, type_str)

    # Handle generic types (e.g. List[str], Tuple[int, float])
    if "[" in type_str and "]" in type_str:
        base_type, generic_content = type_str.split("[", 1)
        generic_content = generic_content.rsplit("]", 1)[0]

        # Parse inner parameters
        generic_params = []
        bracket_level = 0
        param = ""
        for char in generic_content:
            if char == "[":
                bracket_level += 1
                param += char
            elif char == "]":
                bracket_level -= 1
                param += char
            elif char == "," and bracket_level == 0:
                generic_params.append(param.strip())
                param = ""
            else:
                param += char
        if param:
            generic_params.append(param.strip())

        # Replace deep nested types with 'Any'
        if nested_level > 0:
            normalized_params = ["Any"]
        else:
            normalized_params = [normalize_type(param, nested_level + 1) for param in generic_params]

        return f"{base_type}[{', '.join(normalized_params)}]"

    # Strip fully-qualified names
    if "." in type_str:
        return type_str.split(".")[-1]

    return type_str


def translate_pipeline(text, functions):
    """
    Applies a pipeline of text transformation functions in sequence.

    Args:
        text (str): The text to process.
        functions (list): List of functions to apply.

    Returns:
        str: Transformed text.
    """
    for func in functions:
        text = func(text)
    return text


def extract_class_name(text):
    """
    Extracts class name from a string representation like "<class 'int'>".

    Args:
        text (str): Input string.

    Returns:
        str: Extracted class name or the original text.
    """
    match = re.search(r"<class '([^']+)'>", text)
    return match.group(1) if match else text


def extract_common_patterns(text):
    """
    Attempts to extract type information from a string using various regex patterns.

    Args:
        text (str): Natural language or formatted description.

    Returns:
        str: First matching type string or original text if none matched.
    """
    try:
        pattern = (
            r"\<class '(\w+)'\>|\<function.*\>|Return type of `.*?`:"
            r" (\w+)|Return type: (\w+)|The return type of '.*?' is (\w+)|The type of"
            r" '.*?' is a (\w+)|Type of `.*?`: (\w+)|Type of `.*?` is `(\w+)`|`.*?`"
            r" return type: `(\w+)`|`.*?` is a function call that returns an (\w+)"
            r" value|`(\w+)`: `\w+`|column \d+: `(\w+)`|column \d+ is '(\w+)'|type of"
            r" '.*?': `(\w+)`"
        )

        matches = re.findall(pattern, text)
        if matches:
            for match in matches:
                found_types = [m for m in match if m]
                if found_types:
                    return found_types[0]
        return text
    except Exception:
        return text


# Define the transformation pipeline
functions = [extract_class_name, extract_common_patterns]


def translate_content(data):
    """
    Converts inconsistent type annotations in JSON data to normalized Python types.

    Args:
        data (str or list): A JSON string or already-loaded list of dictionaries.

    Returns:
        list: Data with normalized 'type' fields.
    """
    try:
        if isinstance(data, str):
            data = json.loads(data)
    except Exception as e:
        print(f"Not a valid JSON: {e}")
        raise utils.JsonException

    for entry in data:
        if "type" in entry:
            entry["type"] = [normalize_type(entry["type"][0])]
        else:
            entry["type"] = []

    return data


def list_json_files(folder_path):
    """
    Recursively finds all `.json` files in a given folder.

    Args:
        folder_path (str or Path): Directory to search.

    Returns:
        list: List of Path objects for all `.json` files.
    """
    return sorted(Path(folder_path).rglob("*.json"))


def main_translator(benchmark_path):
    """
    Entry point for processing all JSON files in a dataset directory.
    Normalizes types in each file and overwrites the original file.

    Args:
        benchmark_path (str): Path to the root of the dataset to process.
    """
    json_files = list_json_files(benchmark_path)
    error_count = 0

    for file in json_files:
        try:
            with open(file) as f:
                data = json.load(f)

            translated = translate_content(data)

            json_data = json.dumps(translated, indent=4)
            with open(file, "w") as file:
                file.write(json_data)

        except Exception as e:
            print(f"Command returned non-zero exit status: {e} for file: {file}")
            error_count += 1

    print(f"Translator finished with errors: {error_count}")


if __name__ == "__main__":
    # Command-line interface to pass the benchmark path
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--benchmark_path", help="Specify the benchmark path", required=True
    )
    args = parser.parse_args()
    main_translator(args.benchmark_path)