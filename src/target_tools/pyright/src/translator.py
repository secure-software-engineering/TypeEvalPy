import argparse
import json
import os
import re
from pathlib import Path


def check_result_files(directory):
    total_errors = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith("_result.json"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as json_file:
                    data = json.load(json_file)

                data, errors_in_file = remove_invalid_entries(data, file_path)
                total_errors += errors_in_file

                with open(file_path, "w") as json_file:
                    json.dump(data, json_file, indent=2)
    return total_errors


def remove_invalid_entries(data, file_path):
    errors_in_file = 0
    updated_data = []
    for entry in data:
        if is_valid_entry(entry):
            entry = format_none(entry)
            updated_data.append(entry)
        else:
            errors_in_file += 1
            print(f"Removed entry from {file_path}: {entry}")

    data[:] = updated_data
    return data, errors_in_file


def format_none(entry):
    for i in range(len(entry["type"])):
        entry["type"][i] = re.sub(r"\bNone\b", "Nonetype", entry["type"][i])
    return entry


def is_valid_entry(entry):
    has_parameter = "parameter" in entry
    has_function = "function" in entry
    has_type = "type" in entry
    has_variable = "variable" in entry
    if has_type and not (has_function or has_variable):
        return False

    elif has_parameter and not has_function:
        return False
    return True


def main_translator(args):
    error_count = check_result_files(args.bechmark_path)
    print(f"Translator found errors and fixed :{error_count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--bechmark_path",
        help="Specify the benchmark path",
        default="/tmp/micro-benchmark",
    )

    args = parser.parse_args()
    main_translator(args)
