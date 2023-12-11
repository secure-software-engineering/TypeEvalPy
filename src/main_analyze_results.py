import argparse
import json
import logging
import os
import shutil
from pathlib import Path
from statistics import mean
from subprocess import run
from tarfile import SUPPORTED_TYPES

from tabulate import tabulate

from result_analyzer import analysis_tables as analysis_tables
from result_analyzer import analysis_utils as utils

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
SUPPORTED_TOOLS = [
    "headergen",
    "pyright",
    "scalpel",
    "jedi",
    "hityper",
    "type4py",
    "hityperdl",
]
# Create a logger
logger = logging.getLogger("Result Analysis")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("results_analysis.log")
file_handler.setLevel(logging.DEBUG)

file_handler_info = logging.FileHandler("results_analysis_info.log")
file_handler_info.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
file_handler_info.setFormatter(formatter)

console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(file_handler_info)
logger.addHandler(console_handler)

logger.info("Result Analysis Started\n")


def compare_json_files(expected, out):
    with open(expected) as f:
        data_expected = json.load(f)
    with open(out) as f:
        data_out = json.load(f)

    data_expected = utils.sort_facts(data_expected)
    data_out = utils.sort_facts(data_out)

    total_entries = len(data_expected)
    total_matches = 0
    success_rate = 0
    partial_matches = 0
    marked_as_any = 0
    mismatch = 0
    missing_matches_list = []
    partial_matches_list = []
    out_fact_mismatch_list = []

    for fact_expected in data_expected:
        out_fact_matched = False
        out_fact_mismatch = None
        entry_match = False
        for fact_out in data_out:
            # Get full matches
            if utils.check_match(expected=fact_expected, out=fact_out):
                total_matches += 1
                out_fact_matched = True
                break
            # Check for partial match
            elif utils.check_match(
                expected=fact_expected, out=fact_out, partial_match=True
            ):
                partial_matches += 1
                partial_matches_list.append(fact_expected)

                out_fact_mismatch_list.append(fact_expected)
                out_fact_mismatch = fact_out.get("type", [])
                break
            # TODO: Add other cases here
            # elif all(
            #     [fact_expected[x] == fact_out[x] for x in fact_expected.keys() if x not in ["type",]
            # ):
            #     for _type in fact_expected.get("type", []):
            #         if _type in fact_out.get("type", []):
            #             partial_matches += 1
            elif all(
                x in fact_out and fact_out[x] == fact_expected[x]
                for x in fact_expected.keys()
                if x not in ["type", "col_offset"]
            ):
                entry_match = True
                break
            else:
                # logger.debug("No Matches")
                pass

        if not out_fact_matched:
            fact_expected["out_type"] = []
            if out_fact_mismatch:
                fact_expected["out_type"] = out_fact_mismatch
            elif entry_match:
                fact_expected["out_type"] = fact_out["type"]
            missing_matches_list.append(fact_expected)

    if total_matches:
        success_rate = (total_matches / total_entries) * 100

    results_dict = {
        "success_rate": success_rate,
        "missing_matches": missing_matches_list,
        "partial_matches": partial_matches,
        "partial_matches_list": partial_matches_list,
        "marked_as_any": marked_as_any,
    }

    return results_dict


def format_missing_matches(all_missing_matches):
    headers = [
        "File",
        "Line Number",
        "Function",
        "Parameter/Variable",
        "Actual Type",
        "Predicted Type",
    ]
    rows = []
    sum_functions = 0
    sum_params = 0
    sum_variables = 0
    sum_empty_out_types = 0
    sum_non_empty_out_types = 0

    for file_name, missing_matches in all_missing_matches.items():
        merged_cell = file_name
        num_entries = len(missing_matches)
        for i, entry in enumerate(missing_matches):
            line_number = entry.get("line_number", "")
            function = entry.get("function", "")
            param = entry.get("parameter", "")
            variable = entry.get("variable", "")
            types = ", ".join(entry.get("type", []))
            out_types = ", ".join(entry.get("out_type", []))
            rows.append(
                [
                    merged_cell if i == 0 else "",
                    line_number,
                    function,
                    param,
                    variable,
                    types,
                    out_types,
                ]
            )
            if function:
                if not param and not variable:
                    sum_functions += 1

            if param:
                sum_params += 1

            if variable:
                sum_variables += 1

            if not out_types:
                sum_empty_out_types += 1
            else:
                sum_non_empty_out_types += 1

    missing_matches_table = tabulate(rows, headers=headers, tablefmt="grid")

    total_missing_entries = sum(
        len(matches) for matches in all_missing_matches.values()
    )
    analysis_data = [
        total_missing_entries,
        sum_functions,
        sum_params,
        sum_variables,
        sum_empty_out_types,
        sum_non_empty_out_types,
    ]
    formatted_output = (
        "\nMissing matches:\n{}\nTotal error entries: {}\nErrors in function return"
        " type: {}\nErrors in param: {}\n/Errors in variables:{}\nMissing entries:"
        " {}\nMismatch entries: {}".format(
            missing_matches_table,
            total_missing_entries,
            sum_functions,
            sum_params,
            sum_variables,
            sum_empty_out_types,
            sum_non_empty_out_types,
        )
    )
    return formatted_output, analysis_data


def display_all_cats_data(all_cats_data):
    missing_headers = ["Category", "Missing Matches"]
    missing_rows = []
    analysis_data_headers = [
        "Category",
        "Total error entries",
        "Function return",
        "Param",
        "variables",
        "Missing entries",
        "Mismatch",
    ]
    missing_analysis_rows = []

    for cat_data in all_cats_data:
        category = cat_data["Category"]
        missing_matches = cat_data["Missing Matches"]
        # logger.debug(f"~~~~~~ Category : {category} ~~~~~~")
        formatted_output, analysis_data = format_missing_matches(missing_matches)
        missing_rows.append([category, formatted_output])
        missing_analysis_rows.append([category, *analysis_data])
    logger.debug("\nAll Categories Data:")
    logger.debug(
        tabulate(missing_analysis_rows, headers=analysis_data_headers, tablefmt="grid")
    )
    logger.debug(tabulate(missing_rows, headers=missing_headers, tablefmt="grid"))
    return missing_analysis_rows


def process_cat_dir(cat_dir, tool_name=None, print_mismatch=False):
    all_missing_matches = {}
    complete_passed = 0
    sound_passed = 0
    file_count = 0
    cat_precision_results = {}
    cat_recall_results = {}
    cat_precision_results_grouped = {}
    cat_recall_results_grouped = {}
    cat_only_cat_recall_grouped = {}

    for root, dirs, files in os.walk(cat_dir):
        test_files = [x.split(".py")[0] for x in files if x.endswith(".py")]
        logger.debug(
            "\n\n ################ ----------------------- ################# \n\n"
        )
        logger.debug(root.split("/")[-3:])

        if (
            root
            == "../results_28-07"
            " 10:46/headergen_dev/micro-benchmark/python_features/classes/imported_attr_access"
        ):
            # Debug point
            pass

        for test in test_files:
            logger.debug(f"File: {test}")
            if f"{test}_gt.json" in files:
                file_count += 1
                gt_file = os.path.abspath(os.path.join(root, f"{test}_gt.json"))
                dir_path = os.path.relpath(os.path.dirname(gt_file), cat_dir)
                file_name = dir_path + "/" + os.path.basename(gt_file)
                if f"{test}_result.json" in files:
                    result_file = os.path.abspath(
                        os.path.join(root, f"{test}_result.json")
                    )
                    results = compare_json_files(expected=gt_file, out=result_file)
                    complete_passed += utils.equal_complete(
                        expected=gt_file, out=result_file
                    )
                    sound_passed += utils.equal_sound(expected=gt_file, out=result_file)

                    cat_precision, cat_precision_grouped, only_cat_precision_grouped = (
                        utils.measure_precision(
                            expected=gt_file,
                            out=result_file,
                            tool_name=tool_name,
                            print_mismatch=print_mismatch,
                        )
                    )
                    cat_recall, cat_recall_grouped, only_cat_recall_grouped = (
                        utils.measure_recall(
                            expected=gt_file,
                            out=result_file,
                            tool_name=tool_name,
                            print_missed=print_mismatch,
                        )
                    )
                    cat_precision_results[
                        f"{os.path.basename(os.path.dirname(gt_file))}:{test}"
                    ] = cat_precision
                    cat_recall_results[
                        f"{os.path.basename(os.path.dirname(gt_file))}:{test}"
                    ] = cat_recall

                    cat_precision_results_grouped[
                        f"{os.path.basename(os.path.dirname(gt_file))}:{test}"
                    ] = cat_precision_grouped
                    cat_recall_results_grouped[
                        f"{os.path.basename(os.path.dirname(gt_file))}:{test}"
                    ] = cat_recall_grouped
                    cat_only_cat_recall_grouped[
                        f"{os.path.basename(os.path.dirname(gt_file))}:{test}"
                    ] = only_cat_recall_grouped
                    # logger.debug("Missing Matches:")
                    # logger.debug(json.dumps(results["missing_matches"], indent=4))

                    if file_name in all_missing_matches:
                        all_missing_matches[file_name].extend(
                            results["missing_matches"]
                        )
                    else:
                        all_missing_matches[file_name] = results["missing_matches"]

                else:
                    logger.debug(f"result file not {test}")
                    with open(gt_file) as f:
                        data_expected = json.load(f)
                    data_expected = utils.sort_facts(data_expected)
                    num_all = len(data_expected)
                    cat_recall = {
                        "num_all": num_all,
                        "num_caught_exact": 0,
                        "num_caught_partial": 0,
                    }
                    cat_recall_results[
                        f"{os.path.basename(os.path.dirname(gt_file))}:{test}"
                    ] = cat_recall
                    all_missing_matches[file_name] = data_expected
            else:
                logger.debug(f"gt file not found {test}")
    results_dict = {
        "all_missing_matches": all_missing_matches,
        "complete_passed": complete_passed,
        "sound_passed": sound_passed,
        "file_count": file_count,
        "cat_precision_results": cat_precision_results,
        "cat_recall_results": cat_recall_results,
        "cat_precision_results_grouped": cat_precision_results_grouped,
        "cat_recall_results_grouped": cat_recall_results_grouped,
        "only_cat_recall_grouped": cat_only_cat_recall_grouped,
    }
    return results_dict


def iterate_cats(test_suite_dir, tool_name=None):
    all_cats_data = []
    all_cat_sound_complete = []
    all_cat_exact = {}
    max_cat_length = 20
    header_format = "{:<25}{:<15}{:<15}{:<15}\t{:<15}"
    row_format = "{:<25}{:<15}{:<15}{:<15}\t{:<15}"

    logger.info("-" * 100)
    logger.info(
        header_format.format(
            "Category",
            "Complete",
            "Sound",
            "Precision T|Ex|Pa|Ex%|Pa%",
            "Recall T|Ex|Pa|Ex%|Pa%",
        )
    )
    logger.info("-" * 100)

    p_overall_total_facts = 0
    p_overall_total_caught = 0
    p_overall_total_caught_partial = 0

    r_overall_total_facts = 0
    r_overall_total_caught = 0
    r_overall_total_caught_partial = 0

    exact_match = {
        k: {
            "total_facts": 0,
            "total_caught": 0,
        }
        for k in utils.PYTHON_FEATURES_CATEGORIES
    }

    for cat in sorted(os.listdir(test_suite_dir)):
        cat_dir = os.path.join(test_suite_dir, cat)
        if os.path.isdir(cat_dir):
            # logger.info("Iterating category {}...".format(cat))
            results = process_cat_dir(cat_dir, tool_name=tool_name, print_mismatch=True)
            all_cat_exact[cat] = results
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

            # Calculate Precision values
            p_total_facts = 0
            p_total_caught = 0
            p_total_atleast_partial = 0

            list_precision_total = []
            list_precision_partial = []

            for _cat_stats, _precision_stats in results[
                "cat_precision_results"
            ].items():
                p_total_facts += _precision_stats["num_all"]
                p_total_caught += _precision_stats["num_caught_exact"]
                # Total atleast partial means both exact and partial matches
                p_total_atleast_partial += (
                    _precision_stats["num_caught_exact"]
                    + _precision_stats["num_caught_partial"]
                )

                if not float(_precision_stats["num_all"]) == 0:
                    list_precision_total.append(
                        float(_precision_stats["num_caught_exact"])
                        / float(_precision_stats["num_all"])
                    )

                    list_precision_partial.append(
                        float(
                            _precision_stats["num_caught_exact"]
                            + _precision_stats["num_caught_partial"]
                        )
                        / float(_precision_stats["num_all"])
                    )

            # Calculate Recall values
            r_total_facts = 0
            r_total_caught = 0
            r_total_atleast_partial = 0

            list_recall_total = []
            list_recall_partial = []

            for _cat_stats, _recall_stats in results["cat_recall_results"].items():
                r_total_facts += _recall_stats["num_all"]
                r_total_caught += _recall_stats["num_caught_exact"]
                # Total atleast partial means both exact and partial matches
                r_total_atleast_partial += (
                    _recall_stats["num_caught_exact"]
                    + _recall_stats["num_caught_partial"]
                )

                if not float(_recall_stats["num_all"]) == 0:
                    list_recall_total.append(
                        float(_recall_stats["num_caught_exact"])
                        / float(_recall_stats["num_all"])
                    )

                    list_recall_partial.append(
                        float(
                            _recall_stats["num_caught_exact"]
                            + _recall_stats["num_caught_partial"]
                        )
                        / float(_recall_stats["num_all"])
                    )
            exact_match[cat]["total_facts"] = r_total_facts
            exact_match[cat]["total_caught"] = r_total_caught
            p_overall_total_facts += p_total_facts
            p_overall_total_caught += p_total_caught
            p_overall_total_caught_partial += p_total_atleast_partial

            r_overall_total_facts += r_total_facts
            r_overall_total_caught += r_total_caught
            r_overall_total_caught_partial += r_total_atleast_partial
            logger.info(
                row_format.format(
                    cat[:max_cat_length],
                    f"[{results['complete_passed']}/{results['file_count']}]",
                    f"[{results['sound_passed']}/{results['file_count']}]",
                    (
                        f"{p_total_facts:3d}|{p_total_caught:3d}|{p_total_atleast_partial:3d}|{mean(list_precision_total) if list_precision_total else 0:.2f}|{mean(list_precision_partial) if list_precision_partial else 0:.2f}"
                    ),
                    (
                        f"\t{r_total_facts:3d}|{r_total_caught:3d}|{r_total_atleast_partial:3d}|{mean(list_recall_total) if list_recall_total else 0:.2f}|{mean(list_recall_partial) if list_recall_partial else 0:.2f}"
                    ),
                )
            )
            if results["all_missing_matches"]:
                pass
            else:
                logger.info("No missing matches.")

    exact_results_cat = {
        k_n: {
            k: {
                "r_overall_total_facts": 0,
                "r_overall_total_caught": 0,
                "r_overall_total_caught_partial": 0,
            }
            for k in utils.TYPE_CATEGORIES
        }
        for k_n in utils.PYTHON_FEATURES_CATEGORIES
    }
    if tool_name in utils.ML_TOOLS:
        for _cat, _results in all_cat_exact.items():
            for file_name, _cat_results in _results[
                "cat_recall_results_grouped"
            ].items():
                for _top_n, _i_results in _cat_results.items():
                    if _top_n != 1:
                        continue
                    for _type_cat in utils.TYPE_CATEGORIES:
                        exact_results_cat[_cat][_type_cat][
                            "r_overall_total_facts"
                        ] += _i_results[_type_cat]["num_all"]
                        exact_results_cat[_cat][_type_cat][
                            "r_overall_total_caught"
                        ] += _i_results[_type_cat]["num_caught_exact"]
                        exact_results_cat[_cat][_type_cat][
                            "r_overall_total_caught_partial"
                        ] += _i_results[_type_cat]["num_caught_partial"]
    else:
        for _cat, _results in all_cat_exact.items():
            for file_name, _cat_results in _results["only_cat_recall_grouped"].items():
                for _type_cat in utils.TYPE_CATEGORIES:
                    exact_results_cat[_cat][_type_cat][
                        "r_overall_total_facts"
                    ] += _cat_results[_type_cat]["num_all"]
                    exact_results_cat[_cat][_type_cat][
                        "r_overall_total_caught"
                    ] += _cat_results[_type_cat]["num_caught_exact"]
                    exact_results_cat[_cat][_type_cat][
                        "r_overall_total_caught_partial"
                    ] += _cat_results[_type_cat]["num_caught_partial"]
    totals = {
        "function_returns": {
            "r_overall_total_facts": 0,
            "r_overall_total_caught": 0,
            "r_overall_total_caught_partial": 0,
        },
        "function_parameters": {
            "r_overall_total_facts": 0,
            "r_overall_total_caught": 0,
            "r_overall_total_caught_partial": 0,
        },
        "local_variables": {
            "r_overall_total_facts": 0,
            "r_overall_total_caught": 0,
            "r_overall_total_caught_partial": 0,
        },
    }
    for category, value in exact_results_cat.items():
        for feature_type, stats in value.items():
            totals[feature_type]["r_overall_total_facts"] += stats[
                "r_overall_total_facts"
            ]
            totals[feature_type]["r_overall_total_caught"] += stats[
                "r_overall_total_caught"
            ]
            totals[feature_type]["r_overall_total_caught_partial"] += stats[
                "r_overall_total_caught_partial"
            ]
    exact_results_cat["totals"] = totals
    logger.info("-" * 100)
    total_complete_passed = sum(cat["complete"] for cat in all_cat_sound_complete)
    total_sound_passed = sum(cat["sound"] for cat in all_cat_sound_complete)
    total_file_count = sum(cat["file_count"] for cat in all_cat_sound_complete)
    logger.info(
        row_format.format(
            "Total",
            f"[{total_complete_passed}/{total_file_count}]",
            f"[{total_sound_passed}/{total_file_count}]",
            f"{p_overall_total_facts:4d}|{p_overall_total_caught:4d}|{p_overall_total_caught_partial:4d}|{float(p_overall_total_caught)/float(p_overall_total_facts):.2f}|{float(p_overall_total_caught_partial)/float(p_overall_total_facts):.2f}",
            f"\t{r_overall_total_facts:4d}|{r_overall_total_caught:4d}|{r_overall_total_caught_partial:4d}|{float(r_overall_total_caught)/float(r_overall_total_facts):.2f}|{float(r_overall_total_caught_partial)/float(r_overall_total_facts):.2f}",
        )
    )

    # Display all_missing_matches and cat values as one table
    return display_all_cats_data(all_cats_data), exact_match, exact_results_cat


def iterate_cats_sensitivities(test_suite_dir, tool_name=None):
    all_cats_data = []
    all_cat_sound_complete = []
    max_cat_length = 25
    header_format = "{:<30}{:<15}"
    row_format = "{:<30}{:<15}"
    sound_match = {
        k: {
            "sound_passed": 0,
            "file_count": 0,
        }
        for k in utils.SENSITIVITIES_CATEGORIES
    }

    logger.info("-" * 100)
    logger.info(header_format.format("Category", "Sound"))
    logger.info("-" * 100)

    for cat in sorted(os.listdir(test_suite_dir)):
        cat_dir = os.path.join(test_suite_dir, cat)
        if os.path.isdir(cat_dir):
            # logger.info("Iterating category {}...".format(cat))
            results = process_cat_dir(cat_dir, tool_name=tool_name, print_mismatch=True)

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

            logger.info(
                row_format.format(
                    cat[:max_cat_length],
                    f"[{results['sound_passed']}/{results['file_count']}]",
                )
            )
            sound_match[cat]["sound_passed"] = results["sound_passed"]
            sound_match[cat]["file_count"] = results["file_count"]
            if results["all_missing_matches"]:
                pass
            else:
                logger.info("No missing matches.")

    logger.info("-" * 100)
    total_complete_passed = sum(cat["complete"] for cat in all_cat_sound_complete)
    total_sound_passed = sum(cat["sound"] for cat in all_cat_sound_complete)
    total_file_count = sum(cat["file_count"] for cat in all_cat_sound_complete)
    logger.info(
        row_format.format(
            "Total",
            f"[{total_sound_passed}/{total_file_count}]",
        )
    )
    sound_match["Total"] = {
        "sound_passed": total_sound_passed,
        "file_count": total_file_count,
    }
    # Display all_missing_matches and cat values as one table
    return display_all_cats_data(all_cats_data), sound_match


def generate_sound_complete_data(test_suite_dir, tool_name=None):
    cat_sound_complete = {}
    cat_sound_totals = {"s": 0, "c": 0, "t": 0}

    for cat in sorted(os.listdir(test_suite_dir)):
        cat_dir = os.path.join(test_suite_dir, cat)
        if os.path.isdir(cat_dir):
            # logger.info("Iterating category {}...".format(cat))
            results = process_cat_dir(cat_dir, tool_name=tool_name)
            cat_sound_complete[cat] = {
                "complete": results["complete_passed"],
                "sound": results["sound_passed"],
                "file_count": results["file_count"],
            }

            cat_sound_totals["s"] += results["sound_passed"]
            cat_sound_totals["c"] += results["complete_passed"]
            cat_sound_totals["t"] += results["file_count"]

    return cat_sound_complete, cat_sound_totals


def generate_top_n_performance(test_suite_dir, tool_name=None):
    all_cats_data = {}
    all_cat_sound_complete = []
    cat_sound_complete = {}

    results_cat = {
        k_n: {
            k: {
                "p_overall_total_facts": 0,
                "p_overall_total_caught": 0,
                "p_overall_total_caught_partial": 0,
                "r_overall_total_facts": 0,
                "r_overall_total_caught": 0,
                "r_overall_total_caught_partial": 0,
            }
            for k in utils.TYPE_CATEGORIES
        }
        for k_n in utils.TOP_N
    }

    for _k in utils.TOP_N:
        results_cat[_k]["totals"] = {}
        results_cat[_k]["totals"]["p_total_facts"] = 0
        results_cat[_k]["totals"]["p_total_facts_caught"] = 0
        results_cat[_k]["totals"]["p_total_facts_partial"] = 0

    for cat in sorted(os.listdir(test_suite_dir)):
        cat_dir = os.path.join(test_suite_dir, cat)
        if os.path.isdir(cat_dir):
            # logger.info("Iterating category {}...".format(cat))
            results = process_cat_dir(cat_dir, tool_name=tool_name)
            cat_sound_complete[cat] = {
                "complete": results["complete_passed"],
                "sound": results["sound_passed"],
                "file_count": results["file_count"],
            }

            all_cat_sound_complete.append(cat_sound_complete)
            all_cats_data[cat] = results

    # Get total precision values
    for _cat, _results in all_cats_data.items():
        for _cat_results in _results["cat_precision_results_grouped"].values():
            for _top_n, _i_results in _cat_results.items():
                for _type_cat in utils.TYPE_CATEGORIES:
                    results_cat[_top_n][_type_cat][
                        "p_overall_total_facts"
                    ] += _i_results[_type_cat]["num_all"]
                    results_cat[_top_n][_type_cat][
                        "p_overall_total_caught"
                    ] += _i_results[_type_cat]["num_caught_exact"]
                    results_cat[_top_n][_type_cat][
                        "p_overall_total_caught_partial"
                    ] += _i_results[_type_cat]["num_caught_partial"]

    # Get total recall values
    for _cat, _results in all_cats_data.items():
        for _cat_results in _results["cat_recall_results_grouped"].values():
            for _top_n, _i_results in _cat_results.items():
                for _type_cat in utils.TYPE_CATEGORIES:
                    results_cat[_top_n][_type_cat][
                        "r_overall_total_facts"
                    ] += _i_results[_type_cat]["num_all"]
                    results_cat[_top_n][_type_cat][
                        "r_overall_total_caught"
                    ] += _i_results[_type_cat]["num_caught_exact"]
                    results_cat[_top_n][_type_cat][
                        "r_overall_total_caught_partial"
                    ] += _i_results[_type_cat]["num_caught_partial"]

    # Get exact match results
    exact_results_cat = {
        k_n: {
            k: {
                t: {
                    "r_overall_total_facts": 0,
                    "r_overall_total_caught": 0,
                    "r_overall_total_caught_partial": 0,
                }
                for t in utils.TYPE_CATEGORIES
            }
            for k in utils.PYTHON_FEATURES_CATEGORIES
        }
        for k_n in utils.TOP_N
    }

    for _cat, _results in all_cats_data.items():
        for cat, _cat_results in _results["cat_recall_results_grouped"].items():
            for _top_n, _i_results in _cat_results.items():
                for _type_cat in utils.TYPE_CATEGORIES:
                    exact_results_cat[_top_n][_cat][_type_cat][
                        "r_overall_total_facts"
                    ] += _i_results[_type_cat]["num_all"]
                    exact_results_cat[_top_n][_cat][_type_cat][
                        "r_overall_total_caught"
                    ] += _i_results[_type_cat]["num_caught_exact"]
                    exact_results_cat[_top_n][_cat][_type_cat][
                        "r_overall_total_caught_partial"
                    ] += _i_results[_type_cat]["num_caught_partial"]
    totals = {
        "function_returns": {"TOTAL_FACTS": 0, "TOTAL_CAUGHT": 0},
        "function_parameters": {"TOTAL_FACTS": 0, "TOTAL_CAUGHT": 0},
        "local_variables": {"TOTAL_FACTS": 0, "TOTAL_CAUGHT": 0},
    }

    # Loop through the data and calculate totals
    for key, value in exact_results_cat.items():
        for feature_type, feature_data in value.items():
            for category, stats in feature_data.items():
                totals[category]["TOTAL_FACTS"] += stats["r_overall_total_facts"]
                totals[category]["TOTAL_CAUGHT"] += stats["r_overall_total_caught"]

    formatted_data = {}

    # Create the formatted table with grouping
    for key, value in exact_results_cat.items():
        for feature_type, feature_data in value.items():
            for category, stats in feature_data.items():
                if feature_type not in formatted_data:
                    formatted_data[feature_type] = {}
                if key not in formatted_data[feature_type]:
                    formatted_data[feature_type][key] = []
                formatted_data[feature_type][key].append(
                    {
                        "Category": category,
                        "Total_Facts": stats["r_overall_total_facts"],
                        "Total_Caught": stats["r_overall_total_caught"],
                    }
                )
    analysis_tables.create_exact_top_n_table(formatted_data, tool_name)

    # Get totals of type categories
    for _top_n, _stats in results_cat.items():
        results_cat[_top_n]["totals"]["p_total_facts"] = sum(
            [_stats[_cat]["p_overall_total_facts"] for _cat in utils.TYPE_CATEGORIES]
        )
        results_cat[_top_n]["totals"]["p_total_facts_caught"] = sum(
            [_stats[_cat]["p_overall_total_caught"] for _cat in utils.TYPE_CATEGORIES]
        )
        results_cat[_top_n]["totals"]["p_total_facts_partial"] = sum(
            [
                _stats[_cat]["p_overall_total_caught_partial"]
                for _cat in utils.TYPE_CATEGORIES
            ]
        )
        results_cat[_top_n]["totals"]["r_total_facts"] = sum(
            [_stats[_cat]["r_overall_total_facts"] for _cat in utils.TYPE_CATEGORIES]
        )
        results_cat[_top_n]["totals"]["r_total_facts_caught"] = sum(
            [_stats[_cat]["r_overall_total_caught"] for _cat in utils.TYPE_CATEGORIES]
        )
        results_cat[_top_n]["totals"]["r_total_facts_partial"] = sum(
            [
                _stats[_cat]["r_overall_total_caught_partial"]
                for _cat in utils.TYPE_CATEGORIES
            ]
        )

        # Calculate p,r values for all categories
        for _cat in utils.TYPE_CATEGORIES:
            if results_cat[_top_n][_cat]["p_overall_total_facts"] != 0:
                results_cat[_top_n][_cat]["precision_perc"] = float(
                    results_cat[_top_n][_cat]["p_overall_total_caught"]
                ) / float(results_cat[_top_n][_cat]["p_overall_total_facts"])
            else:
                results_cat[_top_n][_cat]["precision_perc"] = 0.0

            if results_cat[_top_n][_cat]["r_overall_total_facts"] != 0:
                results_cat[_top_n][_cat]["recall_perc"] = float(
                    results_cat[_top_n][_cat]["r_overall_total_caught"]
                ) / float(results_cat[_top_n][_cat]["r_overall_total_facts"])
            else:
                results_cat[_top_n][_cat]["recall_perc"] = 0.0

            if results_cat[_top_n][_cat]["p_overall_total_facts"] != 0:
                results_cat[_top_n][_cat]["precision_partial_perc"] = float(
                    results_cat[_top_n][_cat]["p_overall_total_caught_partial"]
                    + results_cat[_top_n][_cat]["p_overall_total_caught"]
                ) / float(results_cat[_top_n][_cat]["p_overall_total_facts"])
            else:
                results_cat[_top_n][_cat]["precision_partial_perc"] = 0.0

            if results_cat[_top_n][_cat]["r_overall_total_facts"] != 0:
                results_cat[_top_n][_cat]["recall_partial_perc"] = float(
                    results_cat[_top_n][_cat]["r_overall_total_caught_partial"]
                    + results_cat[_top_n][_cat]["r_overall_total_caught"]
                ) / float(results_cat[_top_n][_cat]["r_overall_total_facts"])
            else:
                results_cat[_top_n][_cat]["recall_partial_perc"] = 0.0

        if results_cat[_top_n]["totals"]["p_total_facts"] != 0:
            results_cat[_top_n]["totals"]["precision_perc"] = float(
                results_cat[_top_n]["totals"]["p_total_facts_caught"]
            ) / float(results_cat[_top_n]["totals"]["p_total_facts"])
        else:
            results_cat[_top_n]["totals"]["precision_perc"] = 0.0

        if results_cat[_top_n]["totals"]["r_total_facts"] != 0:
            results_cat[_top_n]["totals"]["recall_perc"] = float(
                results_cat[_top_n]["totals"]["r_total_facts_caught"]
            ) / float(results_cat[_top_n]["totals"]["r_total_facts"])
        else:
            results_cat[_top_n]["totals"]["recall_perc"] = 0.0

        if results_cat[_top_n]["totals"]["p_total_facts"] != 0:
            results_cat[_top_n]["totals"]["precision_partial_perc"] = float(
                results_cat[_top_n]["totals"]["p_total_facts_partial"]
                + results_cat[_top_n]["totals"]["p_total_facts_caught"]
            ) / float(results_cat[_top_n]["totals"]["p_total_facts"])
        else:
            results_cat[_top_n]["totals"]["precision_partial_perc"] = 0.0

        if results_cat[_top_n]["totals"]["r_total_facts"] != 0:
            results_cat[_top_n]["totals"]["recall_partial_perc"] = float(
                results_cat[_top_n]["totals"]["r_total_facts_partial"]
                + results_cat[_top_n]["totals"]["r_total_facts_caught"]
            ) / float(results_cat[_top_n]["totals"]["r_total_facts"])
        else:
            results_cat[_top_n]["totals"]["recall_partial_perc"] = 0.0
    analysis_tables.create_top_n_table(results_cat, tool_name)
    return results_cat


def run_results_analyzer(args):
    if args.results_dir is None:
        dir_path = Path(SCRIPT_DIR) / "../results"
        directories = [
            f
            for f in dir_path.iterdir()
            if f.is_dir() and f.name.startswith("results_")
        ]
        directories.sort(key=lambda x: x.stat().st_mtime, reverse=True)
        # Get the latest directory
        results_dir = directories[0] if directories else None
    else:
        results_dir = Path(args.results_dir)

    tools_results = {}

    for item in results_dir.glob("*"):
        if item.is_file() or item.name == "analysis_results":
            # ignore
            pass
        elif item.is_dir():
            logger.info(f"Analyzing tool: {item.name}")
            tools_results[item.name] = {}

            logger.info(f"Analyzing Python Features")

            if item.name in utils.ML_TOOLS:
                tools_results[item.name]["top_n_results"] = generate_top_n_performance(
                    item / "micro-benchmark/python_features", tool_name=item.name
                )
            (
                tools_results[item.name]["error_result_data"],
                tools_results[item.name]["exact_match"],
                tools_results[item.name]["exact_match_category"],
            ) = iterate_cats(
                item / "micro-benchmark/python_features", tool_name=item.name
            )
            tools_results[item.name]["total_benchmark_data"] = utils.benchmark_count(
                item / "micro-benchmark/python_features"
            )
            # print(tools_results[item.name]["total_benchmark_data"])
            # print(tools_results[item.name]["error_result_data"])

            (
                tools_results[item.name]["sound_complete_data"],
                tools_results[item.name]["sound_complete_total_data"],
            ) = generate_sound_complete_data(
                item / "micro-benchmark/python_features", tool_name=item.name
            )

            logger.info(f"")
            logger.info(f"Analyzing Sensitivities")
            (
                tools_results[item.name]["sensitivity_error_result_data"],
                tools_results[item.name]["sensitivity_sound_data"],
            ) = iterate_cats_sensitivities(
                item / "micro-benchmark/analysis_sensitivities", tool_name=item.name
            )

    analysis_tables.analysis_sensitivities_table(tools_results)
    analysis_tables.error_result_table(tools_results, False)
    analysis_tables.exact_match_table(tools_results)
    analysis_tables.exact_match_category_table(tools_results)
    analysis_tables.create_sound_complete_table(
        tools_results
    )  # Create sound complete table
    tools_list = utils.ML_TOOLS + utils.STANDARD_TOOLS

    if len(tools_results) > 1:
        analysis_tables.create_comparison_table(tools_results)

    os.makedirs(results_dir / "analysis_results", exist_ok=True)
    results_dir = results_dir / "analysis_results"
    # Move logs
    # TODO: Improve generation of logs files
    shutil.move("results_analysis.log", f"{str(results_dir)}/results_analysis.log")
    shutil.move(
        "results_analysis_info.log", f"{str(results_dir)}/results_analysis_info.log"
    )
    shutil.move(
        "tools_error_result_data.csv",
        f"{str(results_dir)}/tools_error_result_data.csv",
    )
    shutil.move(
        "tools_sound_complete_data.csv",
        f"{str(results_dir)}/tools_sound_complete_data.csv",
    )
    shutil.move(
        "tools_exact_match_data.csv",
        f"{str(results_dir)}/tools_exact_match_data.csv",
    )
    shutil.move(
        "tools_exact_match_category_data.csv",
        f"{str(results_dir)}/tools_exact_match_category_data.csv",
    )
    shutil.move(
        "tools_sensitivities_data.csv",
        f"{str(results_dir)}/tools_sensitivities_data.csv",
    )

    os.makedirs(results_dir / "mismatches", exist_ok=True)
    os.makedirs(results_dir / "missing", exist_ok=True)
    os.makedirs(results_dir / "paper_tables", exist_ok=True)

    shutil.move(
        "paper_table_1.csv",
        f"{str(results_dir)}/paper_tables/paper_table_1.csv",
    )
    shutil.move(
        "paper_table_2.csv",
        f"{str(results_dir)}/paper_tables/paper_table_2.csv",
    )
    shutil.move(
        "paper_table_3.csv",
        f"{str(results_dir)}/paper_tables/paper_table_3.csv",
    )
    shutil.copy(
        f"{str(results_dir)}/tools_sound_complete_data.csv",
        f"{str(results_dir)}/paper_tables/paper_table_4.csv",
    )
    shutil.move(
        "paper_table_5.csv",
        f"{str(results_dir)}/paper_tables/paper_table_5.csv",
    )
    shutil.copy(
        f"{str(results_dir)}/tools_sensitivities_data.csv",
        f"{str(results_dir)}/paper_tables/paper_table_6.csv",
    )
    for tool in list(tools_results.keys()):
        shutil.move(
            f"{tool}_mismatches_reasons.csv",
            f"{str(results_dir)}/mismatches/{tool}_mismatches_reasons.csv",
        )
        shutil.move(
            f"{tool}_not_found_reasons.csv",
            f"{str(results_dir)}/missing/{tool}_not_found_reasons.csv",
        )

        if tool in utils.ML_TOOLS:
            shutil.move(
                f"top_n_table_{tool}.csv", f"{str(results_dir)}/top_n_table_{tool}.csv"
            )
            shutil.move(
                f"top_n_exact_match_table_{tool}.csv",
                f"{str(results_dir)}/top_n_exact_match_table_{tool}.csv",
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--results_dir",
        help="Specify the results path",
        default=None,
    )
    args = parser.parse_args()

    run_results_analyzer(args)
