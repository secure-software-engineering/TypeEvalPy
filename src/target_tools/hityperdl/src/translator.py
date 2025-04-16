import argparse
import json
import os
import re
from pathlib import Path


def list_json_files(folder_path):
    python_files = sorted(Path(folder_path).rglob("*.json"))
    return python_files


def normalize_type(type_str, nested_level=0):
    """
    Normalize the type string by removing module prefixes and simplifying typing constructs.
    Example: 'builtins.str' -> 'str',
             'typing.Tuple[builtins.str, builtins.float]' -> 'Tuple[str, float]',
             'musictaxonomy.spotify.models.spotifyuser' -> 'SpotifyUser',
             'List[List[Tuple[str]]]' -> 'List[List[Any]]' if nested level > 2.
    """

    if type_str is None:
        return None

    # Remove extra quotes if present
    if type_str.startswith('"') and type_str.endswith('"'):
        type_str = type_str.strip('"')

    # Mapping of module prefixes to remove
    type_mappings = {
        "builtins.": "",
        "typing.": "",
    }
    # Additional type mappings
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
        "Text": "str",
    }

    if type_str is None:
        return None

    # Replace module prefixes
    for prefix, replacement in type_mappings.items():
        type_str = type_str.replace(prefix, replacement)

    # Apply additional type mappings
    type_str = additional_type_mappings.get(type_str, type_str)

    # Handle generic types (e.g., Tuple[], List[], Dict[])
    if "[" in type_str and "]" in type_str:
        base_type, generic_content = type_str.split("[", 1)
        generic_content = generic_content.rsplit("]", 1)[0]
        # Process the generic parameters recursively
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

        # If nested level is greater than 0, replace with Any
        if nested_level > 0:
            normalized_params = ["Any"]
        else:
            normalized_params = [
                normalize_type(param, nested_level + 1) for param in generic_params
            ]

        return f"{base_type}[{', '.join(normalized_params)}]"

    # Handle fully qualified names by extracting the last segment
    if "." in type_str:
        return type_str.split(".")[-1]

    # Return the simplified type
    return type_str


def translate_content(file_path):
    dir_path, file_name = os.path.split(file_path)
    hityper_file = dir_path + "/._" + file_name.replace(".py", "_INFERREDTYPES.json")
    main_gt_file = str(file_path).replace(".py", "_gt.json")

    with open(main_gt_file, "r") as main_gt_file:
        main_gt = json.load(main_gt_file)

    with open(hityper_file, "r") as hityper_file:
        hityper = json.load(hityper_file)
    formatted_output = []

    def convert_type(type_str):
        type_str = re.sub(r"typing\.", "", type_str)  # Remove "typing."
        type_str = re.sub(r"Text", r"str", type_str)  # Convert "Text" to "str"
        type_str = re.sub(r"None", r"Nonetype", type_str)  # Convert None to Nonetype
        return type_str

    for key, value in hityper.items():
        function_name, class_name = key.split("@")  # Get the identifier from the key
        if class_name == "global":
            function_name = function_name
        else:
            function_name = f"{class_name}.{function_name}"
        for item in value:
            if not item["type"]:
                continue
            for gt_item in main_gt:
                formatted_item = {}
                if item["category"] == "local" and "variable" in gt_item:
                    if function_name == "global":
                        if gt_item["variable"] == item["name"]:
                            formatted_item = {
                                "file": gt_item["file"],
                                "line_number": gt_item["line_number"],
                                "variable": gt_item["variable"],
                                "type": [normalize_type(item["type"][0])],
                                "all_type_preds": [
                                    [normalize_type(type_item)]
                                    for type_item in item["type"]
                                ],
                            }
                            formatted_output.append(formatted_item)
                    elif "function" in gt_item and gt_item["function"] == function_name:
                        if gt_item["variable"] == item["name"]:
                            formatted_item = {
                                "file": gt_item["file"],
                                "line_number": gt_item["line_number"],
                                "function": gt_item["function"],
                                "variable": gt_item["variable"],
                                "type": [normalize_type(item["type"][0])],
                                "all_type_preds": [
                                    [normalize_type(type_item)]
                                    for type_item in item["type"]
                                ],
                            }
                            formatted_output.append(formatted_item)
                elif item["category"] == "arg" and "parameter" in gt_item:
                    if (
                        "function" in gt_item
                        and gt_item["function"] == function_name
                        and gt_item["parameter"] == item["name"]
                    ):
                        formatted_item = {
                            "file": gt_item["file"],
                            "line_number": gt_item["line_number"],
                            "function": gt_item["function"],
                            "parameter": gt_item["parameter"],
                            "type": [normalize_type(item["type"][0])],
                            "all_type_preds": [
                                [normalize_type(type_item)]
                                for type_item in item["type"]
                            ],
                        }
                        formatted_output.append(formatted_item)
                elif item["category"] == "return":
                    if (
                        "function" in gt_item
                        and gt_item["function"] == function_name
                        and not any(key in gt_item for key in ["variable", "parameter"])
                    ):
                        formatted_item = {
                            "file": gt_item["file"],
                            "line_number": gt_item["line_number"],
                            "function": gt_item["function"],
                            "type": [normalize_type(item["type"][0])],
                            "all_type_preds": [
                                [normalize_type(type_item)]
                                for type_item in item["type"]
                            ],
                        }
                        formatted_output.append(formatted_item)
    return formatted_output


def main_translator(args):
    json_files = list_json_files(args.bechmark_path)
    error_count = 0
    for file in json_files:
        try:
            # Run the inference here and gather results in /tmp/results
            translated = translate_content(file)

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
