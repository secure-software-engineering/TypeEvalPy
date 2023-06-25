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
        print("here")
        print(item)
        for gt_item in main_gt:
            if "function" in gt_item and gt_item["function"] == function_name:
                formatted_item = {
                    "file": gt_item["file"],
                    "line_number": gt_item["line_number"],
                    "function": gt_item["function"],
                    "type": item["type"],
                }
                if "variable" in gt_item and item["category"] == "local":
                    formatted_item["variable"] = gt_item["variable"]
                elif "parameter" in gt_item and item["category"] == "arg":
                    formatted_item["parameter"] = gt_item["parameter"]
                formatted_output.append(formatted_item)
            elif "variable" in gt_item and gt_item["variable"] == item["name"]:
                formatted_item = {
                    "file": gt_item["file"],
                    "line_number": gt_item["line_number"],
                    "variable": gt_item["variable"],
                    "type": item["type"],
                }
                formatted_output.append(formatted_item)
        print(formatted_output)
# Write the formatted output to main_gt.json
with open("formatted.json", "w") as output_file:
    json.dump(formatted_output, output_file, indent=4)
