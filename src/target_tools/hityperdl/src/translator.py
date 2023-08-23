import argparse
import json
import os
import re
from pathlib import Path


def list_json_files(folder_path):
    python_files = sorted(Path(folder_path).rglob("*.json"))
    return python_files


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
                                "type": [convert_type(item["type"][0])],
                                "all_type_preds": [
                                    [convert_type(type_item)]
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
                                "type": [convert_type(item["type"][0])],
                                "all_type_preds": [
                                    [convert_type(type_item)]
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
                            "type": [convert_type(item["type"][0])],
                            "all_type_preds": [
                                [convert_type(type_item)] for type_item in item["type"]
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
                            "type": [convert_type(item["type"][0])],
                            "all_type_preds": [
                                [convert_type(type_item)] for type_item in item["type"]
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
