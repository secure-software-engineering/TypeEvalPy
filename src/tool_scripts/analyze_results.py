import json
import logging
import os
from pathlib import Path

from tabulate import tabulate

# Create a logger
logger = logging.getLogger("Result Analysis")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("results_analysis.log")
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info("Result Analysis Started\n")


def compare_json_files(expected, out):
    with open(expected) as f:
        data_expected = json.load(f)
    with open(out) as f:
        data_out = json.load(f)

    data_expected = sorted(data_expected, key=lambda x: x["line_number"])
    data_out = sorted(data_out, key=lambda x: x["line_number"])

    total_entries = len(data_expected)
    total_matches = 0
    success_rate = 0
    partial_matches = 0
    missing_matches_list = []
    partial_matches_list = []

    for fact_expected in data_expected:
        out_fact_matched = False
        out_fact_partially_matched = None
        for fact_out in data_out:
            # Get full matches
            if fact_expected == fact_out:
                total_matches += 1
                out_fact_matched = True
                break
            # Check if everything else matches except "type"
            elif (fact_expected.keys() == fact_out.keys()) and all(
                [
                    fact_expected.get(x) == fact_out.get(x)
                    for x in fact_expected.keys()
                    if x != "type"
                ]
            ):
                for _type in fact_expected.get("type", []):
                    if _type in fact_out.get("type", []):
                        out_fact_partially_matched = fact_out.get("type", [])
                        partial_matches += 1
                        partial_matches_list.append(fact_expected)
                        break

            # TODO: Add other cases here
            # elif all(
            #     [fact_expected[x] == fact_out[x] for x in fact_expected.keys() if x not in ["type",]
            # ):
            #     for _type in fact_expected.get("type", []):
            #         if _type in fact_out.get("type", []):
            #             partial_matches += 1
            else:
                # logger.debug("No Matches")
                pass

        if not out_fact_matched:
            if out_fact_partially_matched:
                fact_expected["out_type"] = out_fact_partially_matched
            else:
                fact_expected["out_type"] = []

            missing_matches_list.append(fact_expected)

    if total_matches:
        success_rate = (total_matches / total_entries) * 100

    results_dict = {
        "success_rate": success_rate,
        "missing_matches": missing_matches_list,
        "partial_matches": partial_matches,
        "partial_matches_list": partial_matches_list,
    }

    return results_dict


def equal_sound(out, expected):
    """
    No False Negatives in the output.
    i.e., all facts in the ground truth should be contained in the output
    """
    with open(out) as f:
        data_out = json.load(f)
    with open(expected) as f:
        data_expected = json.load(f)

    data_out = sorted(data_out, key=lambda x: x["line_number"])
    data_expected = sorted(data_expected, key=lambda x: x["line_number"])

    for fact_expected in data_expected:
        fact_expected_exists = False
        for fact_out in data_out:
            if fact_out == fact_expected:
                fact_expected_exists = True
                break

        if not fact_expected_exists:
            # A false negative is found
            return 0

    # No false negatives
    return 1


def equal_complete(out, expected):
    """
    No False Positives in the output.
    i.e., all facts in the output should be contained in the ground truth
    """
    with open(out) as f:
        data_out = json.load(f)
    with open(expected) as f:
        data_expected = json.load(f)

    data_out = sorted(data_out, key=lambda x: x["line_number"])
    data_expected = sorted(data_expected, key=lambda x: x["line_number"])

    for fact_out in data_out:
        fact_out_exists = False
        for fact_expected in data_expected:
            if fact_out == fact_expected:
                fact_out_exists = True
                break

        if not fact_out_exists:
            # A false positive is found
            return 0

    # No false positives
    return 1


def format_missing_matches(all_missing_matches):
    headers = [
        "File",
        "Line Number",
        "Function",
        "Parameter/Variable",
        "Type",
        "Out Type",
    ]
    rows = []

    for file_name, missing_matches in all_missing_matches.items():
        merged_cell = file_name
        num_entries = len(missing_matches)
        for i, entry in enumerate(missing_matches):
            line_number = entry.get("line_number", "")
            function = entry.get("function", "")
            param_variable = entry.get("parameter", entry.get("variable", ""))
            types = ", ".join(entry.get("type", []))
            out_types = ", ".join(entry.get("out_type", []))
            rows.append(
                [
                    merged_cell if i == 0 else "",
                    line_number,
                    function,
                    param_variable,
                    types,
                    out_types,
                ]
            )

    missing_matches_table = tabulate(rows, headers=headers, tablefmt="grid")
    total_missing_entries = sum(
        len(matches) for matches in all_missing_matches.values()
    )

    formatted_output = "\nMissing matches:\n{}\nTotal missing entries: {}".format(
        missing_matches_table, total_missing_entries
    )
    return formatted_output


def display_all_cats_data(all_cats_data):
    headers = ["Category", "Missing Matches"]
    rows = []

    for cat_data in all_cats_data:
        category = cat_data["Category"]
        missing_matches = cat_data["Missing Matches"]

        rows.append([category, format_missing_matches(missing_matches)])

    logger.debug("\nAll Categories Data:")
    logger.debug(tabulate(rows, headers=headers, tablefmt="grid"))


def process_cat_dir(cat_dir):
    all_missing_matches = {}
    complete_passed = 0
    sound_passed = 0
    file_count = 0
    for root, dirs, files in os.walk(cat_dir):
        # logger.info(files)
        test_files = [x.split(".py")[0] for x in files if x.endswith(".py")]
        for test in test_files:
            if f"{test}_gt.json" in files:
                file_count += 1
                if f"{test}_result.json" in files:
                    gt_file = os.path.abspath(os.path.join(root, f"{test}_gt.json"))
                    result_file = os.path.abspath(
                        os.path.join(root, f"{test}_result.json")
                    )
                    results = compare_json_files(expected=gt_file, out=result_file)
                    complete_passed += equal_complete(expected=gt_file, out=result_file)
                    sound_passed += equal_sound(expected=gt_file, out=result_file)
                    logger.debug("Missing Matches:")
                    logger.debug(json.dumps(results["missing_matches"], indent=4))

                    dir_path = os.path.relpath(os.path.dirname(gt_file), cat_dir)
                    file_name = dir_path + "/" + os.path.basename(gt_file)
                    if file_name in all_missing_matches:
                        all_missing_matches[file_name].extend(
                            results["missing_matches"]
                        )
                    else:
                        all_missing_matches[file_name] = results["missing_matches"]

                else:
                    logger.debug(f"result file not {test}")
            else:
                logger.debug(f"gt file not found {test}")

    results_dict = {
        "all_missing_matches": all_missing_matches,
        "complete_passed": complete_passed,
        "sound_passed": sound_passed,
        "file_count": file_count,
    }
    return results_dict


def iterate_cats(test_suite_dir):
    all_cats_data = []
    all_cat_sound_complete = []
    max_cat_length = 15
    header_format = "{:<15}{:<15}{:<15}"
    row_format = "{:<15}{:<15}{:<15}"

    print("-" * 50)
    print(header_format.format("Category", "Complete", "Sound"))
    print("-" * 50)
    for cat in sorted(os.listdir(test_suite_dir)):
        cat_dir = os.path.join(test_suite_dir, cat)
        if os.path.isdir(cat_dir):
            # print("Iterating category {}...".format(cat))
            results = process_cat_dir(cat_dir)

            cat_data = {
                "Category": cat,
                "Missing Matches": results["all_missing_matches"],
            }
            all_cats_data.append(cat_data)
            cat_sound_complete = {
                "complete": results["complete_passed"],
                "sound": results["sound_passed"],
                "file_count": results["file_count"],
            }
            all_cat_sound_complete.append(cat_sound_complete)
            print(
                row_format.format(
                    cat[:max_cat_length],
                    f"[{results['complete_passed']}/{results['file_count']}]",
                    f"[{results['sound_passed']}/{results['file_count']}]",
                )
            )
            if results["all_missing_matches"]:
                pass
            else:
                print("No missing matches.")

    print("-" * 50)
    total_complete_passed = sum(cat["complete"] for cat in all_cat_sound_complete)
    total_sound_passed = sum(cat["sound"] for cat in all_cat_sound_complete)
    total_file_count = sum(cat["file_count"] for cat in all_cat_sound_complete)
    print(
        row_format.format(
            "Total",
            f"[{total_complete_passed}/{total_file_count}]",
            f"[{total_sound_passed}/{total_file_count}]",
        )
    )

    # Display all_missing_matches and cat values as one table
    display_all_cats_data(all_cats_data)


if __name__ == "__main__":
    results_dir = Path("../results_03-07 21:18")

    for item in results_dir.glob("*"):
        if item.is_file():
            # ignore
            pass
        elif item.is_dir():
            logger.info(f"Analyzing tool: {item.name}")
            logger.info(f"Analyzing Python Features")
            iterate_cats(item / "micro-benchmark/python_features")
            # logger.info(f"Analyzing Sensitivities")
            # iterate_cats(item / "micro-benchmark/analysis_sensitivities")
