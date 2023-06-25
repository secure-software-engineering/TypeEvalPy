import json

# Load the main_gt.json and hityper.json files
with open("main_gt.json", "r") as main_gt_file:
    main_gt = json.load(main_gt_file)

with open("hityper.json", "r") as hityper_file:
    hityper = json.load(hityper_file)

# Iterate over the hityper output and format it according to the main_gt structure
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
with open("formatted.json", "w") as output_file:
    json.dump(formatted_output, output_file, indent=4)
