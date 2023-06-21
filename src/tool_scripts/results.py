import json
import os
from tabulate import tabulate


def compare_json_files(gt_file, tool_file):
    with open(gt_file) as f:
        gt_data = json.load(f)
    with open(tool_file) as f:
        tool_data = json.load(f)

    total_entries = len(gt_data)
    total_matches = 0
    missing_matches = []

    for gt_entry in gt_data:
        gt_type = gt_entry.get("type", [])
        tool_entry_match = False

        for tool_entry in tool_data:
            if gt_entry == tool_entry:
                tool_type = tool_entry.get("type", [])
                if gt_type == tool_type:
                    total_matches += 1
                    tool_entry_match = True
                    break

        if not tool_entry_match:
            missing_matches.append(gt_entry)

    success_rate = (total_matches / total_entries) * 100
    print("Success rate for file:", gt_file, "is:", success_rate)
    return success_rate, missing_matches


def iterate_cats(test_suite_dir):
    for cat in sorted(os.listdir(test_suite_dir)):
        cat_dir = os.path.join(test_suite_dir, cat)
        if os.path.isdir(cat_dir):
            print("Iterating category {}...".format(cat))
            all_missing_matches = {}

            for root, dirs, files in os.walk(cat_dir):
                try:
                    gt_file = None
                    tool_file = None

                    for file in files:
                        if file.endswith(".json"):
                            file_path = os.path.join(root, file)
                            if "gt" in file.lower():
                                gt_file = file_path
                            elif "jedi" in file.lower():
                                tool_file = file_path

                    if gt_file and tool_file:
                        success_rate, missing_matches = compare_json_files(
                            gt_file, tool_file
                        )

                        # Group missing matches by file name
                        dir_path = os.path.relpath(os.path.dirname(gt_file), cat_dir)
                        file_name = dir_path + "/" + os.path.basename(gt_file)
                        if file_name in all_missing_matches:
                            all_missing_matches[file_name].extend(missing_matches)
                        else:
                            all_missing_matches[file_name] = missing_matches

                except Exception as e:
                    print(e)

            if all_missing_matches:
                headers = [
                    "File",
                    "Line Number",
                    "Function",
                    "Parameter/Variable",
                    "Type",
                ]
                rows = []
                for file_name, missing_matches in all_missing_matches.items():
                    merged_cell = file_name
                    num_entries = len(missing_matches)
                    for i, entry in enumerate(missing_matches):
                        line_number = entry.get("line_number", "")
                        function = entry.get("function", "")
                        param_variable = entry.get(
                            "parameter", entry.get("variable", "")
                        )
                        types = ", ".join(entry.get("type", []))
                        rows.append(
                            [
                                merged_cell if i == 0 else "",
                                line_number,
                                function,
                                param_variable,
                                types,
                            ]
                        )

                print("\nMissing matches:")
                print(tabulate(rows, headers=headers, tablefmt="grid"))
                print(
                    "\nTotal missing entries:"
                    f" {sum(len(matches) for matches in all_missing_matches.values())}"
                )
            else:
                print("No missing matches.")

            print("-" * 50)


test_suite_dir = "micro-benchmark/python_features"
iterate_cats(test_suite_dir)
