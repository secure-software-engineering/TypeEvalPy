import json
import os
import subprocess


def list_python_files(folder_path):
    python_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files


def format_json(main_gt_file, hityper_file, final_gt_file):
    # Iterate over the hityper output and format it according to the main_gt structure
    with open(main_gt_file, "r") as main_gt_file:
        main_gt = json.load(main_gt_file)

    with open(hityper_file, "r") as hityper_file:
        hityper = json.load(hityper_file)
    formatted_output = []
    for key, value in hityper.items():
        function_name, class_name = key.split("@")  # Get the identifier from the key
        if class_name == "global":
            function_name = function_name
        else:
            function_name = f"{class_name}.{function_name}"
        for item in value:
            for gt_item in main_gt:
                formatted_item = {}
                if item["category"] == "local" and "variable" in gt_item:
                    if function_name == "global":
                        if gt_item["variable"] == item["name"]:
                            formatted_item = {
                                "file": gt_item["file"],
                                "line_number": gt_item["line_number"],
                                "variable": gt_item["variable"],
                                "type": item["type"],
                            }
                            formatted_output.append(formatted_item)
                    elif "function" in gt_item and gt_item["function"] == function_name:
                        if gt_item["variable"] == item["name"]:
                            formatted_item = {
                                "file": gt_item["file"],
                                "line_number": gt_item["line_number"],
                                "function": gt_item["function"],
                                "variable": gt_item["variable"],
                                "type": item["type"],
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
                            "type": item["type"],
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
                            "type": item["type"],
                        }
                        formatted_output.append(formatted_item)
    # Write the formatted output to main_gt.json
    with open(final_gt_file, "w") as output_file:
        json.dump(formatted_output, output_file, indent=4)


root_directory = "/tmp/micro-benchmark/python_features"


python_files = list_python_files(root_directory)
error_count = 0
# Run `hityper` for all files
for file_path in python_files:
    print(file_path)
    dir_path, file_name = os.path.split(file_path)
    hitype_cmd = f"hityper infer -s ./{file_name} -p ."
    try:
        subprocess.run(hitype_cmd, shell=True, cwd=dir_path, check=True)
        hityper_file = (
            dir_path + "/._" + file_name.replace(".py", "_INFERREDTYPES.json")
        )
        main_gt_file = dir_path + "/" + file_name.replace(".py", "_gt.json")
        final_gt_file = dir_path + "/" + file_name.replace(".py", "_hityper.json")
        format_json(main_gt_file, hityper_file, final_gt_file)
    except Exception as e:
        print(f"Command returned non-zero exit status: {e}")
        error_count += 1
print("Error count", error_count)
