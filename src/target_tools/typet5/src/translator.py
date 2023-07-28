import argparse
import json
import os
from pathlib import Path


def list_txt_files(folder_path):
    txt_files = sorted(Path(folder_path).rglob("*.txt"))
    return txt_files


def translate_content(file_path):
    result_list = []
    with open(file_path, "r") as file:
        lines = file.readlines()
    file_name = os.path.splitext(os.path.basename(file_path))[0] + ".py"
    for line in lines:
        parts = line.strip().split(" - Location: ")
        attribute_info = parts[0]
        location = int(parts[1])

        if "->" in attribute_info:
            function_info = attribute_info.split("->")
            function_name = function_info[0]
            return_type = function_info[1]
            if ":(" in function_name and ")" in function_name:
                params_str = function_name.split(":(")[1].split(")")[0]
                params = [param.strip() for param in params_str.split(",")]
                for param in params:
                    param_name, param_type = param.split(":")
                    result_list.append(
                        {
                            "file": str(file_name),
                            "line_number": location,
                            "function": function_name.split(":(")[0],
                            "parameter": param_name,
                            "type": [param_type],
                        }
                    )
            result_list.append(
                {
                    "file": str(file_name),
                    "line_number": location,
                    "function": function_name.split(":(")[0],
                    "type": [return_type],
                }
            )
        else:
            attribute_name, attribute_type = attribute_info.split(":")
            result_list.append(
                {
                    "file": str(file_name),
                    "line_number": location,
                    "variable": attribute_name,
                    "type": [attribute_type],
                }
            )

    return result_list


def main_translator(args):
    txt_files = list_txt_files(args.bechmark_path)
    error_count = 0
    for file in txt_files:
        try:
            # Run the inference here and gather results in /tmp/results
            print(file)
            translated = translate_content(file)
            output_file = str(file).replace(".txt", "_result.json")

            with open(output_file, "w") as outfile:
                json.dump(translated, outfile, indent=4)
            print(f"Predictions translated to: {outfile}")
        except Exception as e:
            print(f"Command returned non-zero exit status: {e} for file: {file}")
            error_count += 1

    print(f"Translator finished with errors:{error_count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--bechmark_path",
        help="Specify the benchmark path",
        default="/tmp/micro-benchmark",
    )

    args = parser.parse_args()
    main_translator(args)
