import argparse
import json
import os
import re
from pathlib import Path
import utils


def normalize_type(type_str):
    """
    Normalize the type string by removing module prefixes and simplifying typing constructs.
    Example: 'builtins.str' -> 'str',
             'typing.Tuple[builtins.str, builtins.float]' -> 'Tuple[str, float]',
             'musictaxonomy.spotify.models.spotifyuser' -> 'SpotifyUser'.
    """
    # Mapping of module prefixes to remove
    type_mappings = {
        "builtins.": "",
        "typing.": "",
    }

    if type_str is None:
        return None
        
    # Replace module prefixes
    for prefix, replacement in type_mappings.items():
        type_str = type_str.replace(prefix, replacement)

    # Handle generic types (e.g., Tuple[], List[], Dict[])
    if "[" in type_str and "]" in type_str:
        base_type, generic_content = type_str.split("[", 1)
        # Process the generic parameters recursively
        generic_params = generic_content.rstrip("]").split(", ")
        normalized_params = [normalize_type(param) for param in generic_params]
        return f'{base_type}[{", ".join(normalized_params)}]'

    # Handle fully qualified names by extracting the last segment
    if "." in type_str:
        return type_str.split(".")[-1]

    # Return the simplified type
    return type_str


def merge_and_normalize_type(type_list):
    """
    Merges fragmented type strings and applies normalization.
    Handles cases like:
    ['Sequence[Union[float', 'Vector]]'] -> 'Sequence[Union[float, Vector]]'
    """
    if not type_list or not isinstance(type_list, list):
        return []

    # Merge fragments into a single string
    full_type = "".join(type_list).replace(" ", "")

    # Normalize the merged string
    normalized = normalize_type(full_type)
    return [normalized]


def translate_pipeline(text, functions):
    for func in functions:
        text = func(text)
    return text


def extract_class_name(text):
    match = re.search(r"<class '([^']+)'>", text)
    return match.group(1) if match else text


def extract_common_patterns(text):
    try:
        # Adjusted regular expression to match the specific patterns as instructed
        pattern = (
            r"\<class '(\w+)'\>|\<function.*\>|Return type of `.*?`:"
            r" (\w+)|Return type: (\w+)|The return type of '.*?' is (\w+)|The type of"
            r" '.*?' is a (\w+)|Type of `.*?`: (\w+)|Type of `.*?` is `(\w+)`|`.*?`"
            r" return type: `(\w+)`|`.*?` is a function call that returns an (\w+)"
            r" value|`(\w+)`: `\w+`|column \d+: `(\w+)`|column \d+ is '(\w+)'|type of"
            r" '.*?': `(\w+)`"
        )

        # Extracting the types with the adjusted pattern
        extracted_types = []
        matches = re.findall(pattern, text)
        if matches:
            for match in matches:
                # Filter out empty matches and add the found type
                found_types = [m for m in match if m]
                if found_types:
                    return found_types[0]
        else:
            return text

    except Exception as e:
        return text


# Create a list of functions to apply
functions = [extract_class_name, extract_common_patterns]


def translate_content(data):
    type_mapping = {
        "integer": "int",
        "string": "str",
        "dictonary": "dict",
        "method": "Callable",
        "func": "Callable",
        "function": "Callable",
        "none": "None",
        "Nonetype": "None",
        "nonetype": "None",
        "object": "Any",
        "NoneType": "None",
    }

    try:
        if isinstance(data, str):
            data = json.loads(data)
    except Exception as e:
        print(f"Not a valid JSON: {e}")
        raise utils.JsonException

    for entry in data:
        if "type" in entry:
            # Merge and normalize the types
            merged_types = merge_and_normalize_type(entry["type"])
            # Apply the pipeline and normalize the types
            processed_types = [translate_pipeline(t, functions) for t in merged_types]
            normalized_types = [normalize_type(t) for t in processed_types]
            # Map types to their common forms
            translated_types = [
                type_mapping[t.lower()] if t and t.lower() in type_mapping else t
                for t in processed_types
            ]
            entry["type"] = translated_types
        else:
            entry["type"] = []

    return data


def list_json_files(folder_path):
    python_files = sorted(Path(folder_path).rglob("*.json"))
    return python_files


def main_translator(benchmark_path):
    json_files = list_json_files(benchmark_path)
    error_count = 0
    for file in json_files:
        try:
            with open(file) as f:
                data = json.load(f)

            # Run the inference here and gather results in /tmp/results
            translated = translate_content(data)

            json_data = json.dumps(translated, indent=4)
            with open(file, "w") as file:
                file.write(json_data)

        except Exception as e:
            print(f"Command returned non-zero exit status: {e} for file: {file}")
            error_count += 1

    print(f"Translator finished with errors:{error_count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--benchmark_path", help="Specify the benchmark path", required=True
    )

    args = parser.parse_args()
    main_translator(args.benchmark_path)