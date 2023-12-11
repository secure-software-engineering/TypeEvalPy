import argparse
import json
import os
import re
from pathlib import Path

import utils


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
        "method": "callable",
        "func": "callable",
        "function": "callable",
        "none": "Nonetype",
    }

    try:
        if isinstance(data, str):
            data = json.loads(data)
    except Exception as e:
        print(f"Not a valid JSON: {e}")
        raise utils.JsonException

    for entry in data:
        if "type" in entry:
            processed_types = [translate_pipeline(t, functions) for t in entry["type"]]

            translated_types = [
                type_mapping[t.lower()] if t.lower() in type_mapping else t
                for t in entry["type"]
            ]
            entry["type"] = translated_types
        else:
            entry["type"] = []

    return data


def list_json_files(folder_path):
    python_files = sorted(Path(folder_path).rglob("*.json"))
    return python_files


def main_translator(args):
    json_files = list_json_files(args.bechmark_path)
    error_count = 0
    for file in json_files:
        print(f"Processing: {file}")
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

    print(f"Runner finished with errors:{error_count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--bechmark_path",
        help="Specify the benchmark path",
        default=None,
    )

    args = parser.parse_args()
    main_translator(args)
