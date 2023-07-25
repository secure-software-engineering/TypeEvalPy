import json
import logging
import os
from pathlib import Path
from statistics import mean

import analysis_tables
import analysis_utils as utils
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
                        partial_matches += 1
                        partial_matches_list.append(fact_expected)
                        break

                if "any" in fact_out.get("type", []):
                    marked_as_any += 1
                else:
                    mismatch += 1
                    # logger.info("Total mismatch?")

                out_fact_mismatch_list.append(fact_expected)
                out_fact_mismatch = fact_out.get("type", [])
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
            fact_expected["out_type"] = []
            if out_fact_mismatch:
                fact_expected["out_type"] = out_fact_mismatch

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


def process_cat_dir(cat_dir, tool_name=None):
    all_missing_matches = {}
    complete_passed = 0
    sound_passed = 0
    file_count = 0
    cat_precision_results = {}
    cat_recall_results = {}
    cat_precision_results_grouped = {}
    cat_recall_results_grouped = {}

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
                    complete_passed += utils.equal_complete(
                        expected=gt_file, out=result_file
                    )
                    sound_passed += utils.equal_sound(expected=gt_file, out=result_file)

                    cat_precision, cat_precision_grouped, only_cat_precision_grouped = (
                        utils.measure_precision(
                            expected=gt_file, out=result_file, tool_name=tool_name
                        )
                    )
                    cat_recall, cat_recall_grouped, only_cat_recall_grouped = (
                        utils.measure_recall(
                            expected=gt_file, out=result_file, tool_name=tool_name
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

                    # logger.debug("Missing Matches:")
                    # logger.debug(json.dumps(results["missing_matches"], indent=4))

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
        "cat_precision_results": cat_precision_results,
        "cat_recall_results": cat_recall_results,
        "cat_precision_results_grouped": cat_precision_results_grouped,
        "cat_recall_results_grouped": cat_recall_results_grouped,
    }
    return results_dict


def iterate_cats(test_suite_dir, tool_name=None):
    all_cats_data = []
    all_cat_sound_complete = []
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

    for cat in sorted(os.listdir(test_suite_dir)):
        cat_dir = os.path.join(test_suite_dir, cat)
        if os.path.isdir(cat_dir):
            # logger.info("Iterating category {}...".format(cat))
            results = process_cat_dir(cat_dir, tool_name=tool_name)

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

            # Calculate Precision values
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
    display_all_cats_data(all_cats_data)


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
            results_cat[_top_n][_cat]["precision_perc"] = float(
                results_cat[_top_n][_cat]["p_overall_total_caught"]
            ) / float(results_cat[_top_n][_cat]["p_overall_total_facts"])

            results_cat[_top_n][_cat]["recall_perc"] = float(
                results_cat[_top_n][_cat]["r_overall_total_caught"]
            ) / float(results_cat[_top_n][_cat]["r_overall_total_facts"])

            results_cat[_top_n][_cat]["precision_partial_perc"] = float(
                results_cat[_top_n][_cat]["p_overall_total_caught_partial"]
                + results_cat[_top_n][_cat]["p_overall_total_caught"]
            ) / float(results_cat[_top_n][_cat]["p_overall_total_facts"])

            results_cat[_top_n][_cat]["recall_partial_perc"] = float(
                results_cat[_top_n][_cat]["r_overall_total_caught_partial"]
                + results_cat[_top_n][_cat]["r_overall_total_caught_partial"]
            ) / float(results_cat[_top_n][_cat]["r_overall_total_facts"])

        results_cat[_top_n]["totals"]["precision_perc"] = float(
            results_cat[_top_n]["totals"]["p_total_facts_caught"]
        ) / float(results_cat[_top_n]["totals"]["p_total_facts"])

        results_cat[_top_n]["totals"]["recall_perc"] = float(
            results_cat[_top_n]["totals"]["r_total_facts_caught"]
        ) / float(results_cat[_top_n]["totals"]["r_total_facts"])

        results_cat[_top_n]["totals"]["precision_partial_perc"] = float(
            results_cat[_top_n]["totals"]["p_total_facts_partial"]
            + results_cat[_top_n]["totals"]["p_total_facts_caught"]
        ) / float(results_cat[_top_n]["totals"]["p_total_facts"])

        results_cat[_top_n]["totals"]["recall_partial_perc"] = float(
            results_cat[_top_n]["totals"]["r_total_facts_partial"]
            + results_cat[_top_n]["totals"]["r_total_facts_caught"]
        ) / float(results_cat[_top_n]["totals"]["r_total_facts"])

    analysis_tables.create_top_n_table(results_cat, tool_name)


if __name__ == "__main__":
    # results_dir = Path("./results_analysis_tests")
    results_dir = None
    if results_dir is None:
        dir_path = Path("../")
        directories = [
            f
            for f in dir_path.iterdir()
            if f.is_dir() and f.name.startswith("results_")
        ]
        directories.sort(key=lambda x: x.stat().st_mtime, reverse=True)
        # Get the latest directory
        results_dir = directories[0] if directories else None

    tools_results = {}

    for item in results_dir.glob("*"):
        if item.is_file():
            # ignore
            pass
        elif item.is_dir():
            logger.info(f"Analyzing tool: {item.name}")
            tools_results[item.name] = {}

            logger.info(f"Analyzing Python Features")

            if item.name in utils.ML_TOOLS:
                generate_top_n_performance(
                    item / "micro-benchmark/python_features", tool_name=item.name
                )
            iterate_cats(item / "micro-benchmark/python_features", tool_name=item.name)

            (
                tools_results[item.name]["sound_complete_data"],
                tools_results[item.name]["sound_complete_total_data"],
            ) = generate_sound_complete_data(
                item / "micro-benchmark/python_features", tool_name=item.name
            )

            logger.info(f"Analyzing Sensitivities")
            iterate_cats(
                item / "micro-benchmark/analysis_sensitivities", tool_name=item.name
            )

    # Create sound complete table
    analysis_tables.create_sound_complete_table(tools_results)

    # Move logs
    os.rename("results_analysis.log", f"{str(results_dir)}/results_analysis.log")
