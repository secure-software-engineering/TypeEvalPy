import csv
import json

import result_analyzer.analysis_utils as utils


def error_result_table(stats, total_stats=True):
    with open(f"tools_error_result_data.csv", "w", newline="") as csvfile:
        fieldnames = [
            "Micro-benchmark Category",
        ]
        for x in list(stats.keys()):
            fieldnames.extend(
                list(
                    (
                        f"{x}_total",
                        f"{x}_fn",
                        f"{x}_param",
                        f"{x}_var",
                        f"{x}_miss",
                        f"{x}_diff",
                    )
                )
            )

        writer = csv.writer(
            csvfile,
            delimiter=",",
            quotechar="|",
            quoting=csv.QUOTE_MINIMAL,
        )
        writer.writerow(fieldnames)
        cat_based_dict = {}
        for _tool, _tool_values in stats.items():
            for value in _tool_values["error_result_data"]:
                category = value[0]
                if category not in cat_based_dict:
                    cat_based_dict[category] = []
                cat_based_dict[category].extend(value[1:])

        # For printing total benchmark data
        if total_stats:
            tool_count = 0
            for _tool, _tool_values in stats.items():
                for value in _tool_values["total_benchmark_data"]:
                    category = value[0]
                    if category not in cat_based_dict:
                        cat_based_dict[category] = []
                    """cat_based_dict[category][
                        4 + tool_count
                    ] = (  # Total missing errors/ Total errors
                        f"{cat_based_dict[category][4+ tool_count]}/{cat_based_dict[category][0+ tool_count]}"
                    )
                    cat_based_dict[category][
                        5 + tool_count
                    ] = (  # Total mismatch errors/ Total errors
                        f"{cat_based_dict[category][5+ tool_count]}/{cat_based_dict[category][0+ tool_count]}"
                    )"""
                    cat_based_dict[category][
                        0 + tool_count
                    ] = (  # Total errors/ Total annotations
                        f"{cat_based_dict[category][0+ tool_count]}/{value[1]}"
                    )
                    cat_based_dict[category][
                        1 + tool_count
                    ] = (  # Total function errors/ Total function annotations
                        f"{cat_based_dict[category][1+ tool_count]}/{value[2]}"
                    )
                    cat_based_dict[category][
                        2 + tool_count
                    ] = (  # Total parameter errors/ Total parameter annotations
                        f"{cat_based_dict[category][2+ tool_count]}/{value[3]}"
                    )
                    cat_based_dict[category][
                        3 + tool_count
                    ] = (  # Total variable errors/ Total variable annotations
                        f"{cat_based_dict[category][3+ tool_count]}/{value[4]}"
                    )
                tool_count += 6

        for category, values in cat_based_dict.items():
            row = [category]
            row.extend(values)
            writer.writerow(row)


def create_sound_complete_table(stats):
    with open(f"tools_sound_complete_data.csv", "w", newline="") as csvfile:
        fieldnames = [
            "Micro-benchmark Category",
        ]

        for x in list(stats.keys()):
            fieldnames.extend(list((f"{x}_s", f"{x}_c")))

        writer = csv.writer(
            csvfile,
            delimiter=",",
            quotechar="|",
            quoting=csv.QUOTE_MINIMAL,
        )

        cat_based_dict = {
            k: {k_t: {"s": "[0/0]", "c": "[0/0]"} for k_t in stats.keys()}
            for k in list(stats[next(iter(stats))]["sound_complete_data"].keys())
            + ["total"]
        }

        writer.writerow(fieldnames)
        for _tool, _tool_values in stats.items():
            for _cat, _cat_values in _tool_values["sound_complete_data"].items():
                cat_based_dict[_cat][_tool][
                    "s"
                ] = f"{_cat_values['sound']}/{_cat_values['file_count']}"
                cat_based_dict[_cat][_tool][
                    "c"
                ] = f"{_cat_values['complete']}/{_cat_values['file_count']}"

            cat_based_dict["total"][_tool][
                "s"
            ] = f"{stats[_tool]['sound_complete_total_data']['s']}/{stats[_tool]['sound_complete_total_data']['t']}"
            cat_based_dict["total"][_tool][
                "c"
            ] = f"{stats[_tool]['sound_complete_total_data']['c']}/{stats[_tool]['sound_complete_total_data']['t']}"

        for _cat, _cat_values in cat_based_dict.items():
            _row = [_cat]
            for _tool, _tool_values in _cat_values.items():
                _row += [_tool_values["s"]] + [_tool_values["c"]]

            writer.writerow(_row)


def create_top_n_table(stats, tool_name):
    with open(f"top_n_table_{tool_name}.csv", "w", newline="") as csvfile:
        fieldnames = [
            "Type Category",
            "Top-n Predictions",
            "Exact Match P.",
            "Exact Match R.",
            "Partial Match P.",
            "Partial Match R.",
        ]
        writer = csv.writer(
            csvfile,
            delimiter=",",
            quotechar="|",
            quoting=csv.QUOTE_MINIMAL,
        )

        cat_based_dict = {
            k_cat: {
                k: {
                    "exact_p": 0.0,
                    "exact_r": 0.0,
                    "partial_p": 0.0,
                    "partial_r": 0.0,
                }
                for k in utils.TOP_N
            }
            for k_cat in utils.TYPE_CATEGORIES + ["totals"]
        }

        for _top_n, _top_n_values in stats.items():
            for _cat, _cat_values in _top_n_values.items():
                exact_p = (
                    _cat_values["precision_perc"]
                    if _cat_values.get("precision_perc")
                    else 0.0
                )
                exact_r = (
                    _cat_values["recall_perc"]
                    if _cat_values.get("recall_perc")
                    else 0.0
                )
                partial_p = (
                    _cat_values["precision_partial_perc"]
                    if _cat_values.get("precision_partial_perc")
                    else 0.0
                )
                partial_r = (
                    _cat_values["recall_partial_perc"]
                    if _cat_values.get("recall_partial_perc")
                    else 0.0
                )

                cat_based_dict[_cat][_top_n]["exact_p"] = exact_p
                cat_based_dict[_cat][_top_n]["exact_r"] = exact_r
                cat_based_dict[_cat][_top_n]["partial_p"] = partial_p
                cat_based_dict[_cat][_top_n]["partial_r"] = partial_r

        writer.writerow(fieldnames)
        for _cat, _cat_values in cat_based_dict.items():
            for _top_n, _top_n_values in _cat_values.items():
                writer.writerow(
                    [
                        _cat,
                        f"Top-{_top_n}",
                        f"{_top_n_values['exact_p']:.2f}",
                        f"{_top_n_values['exact_r']:.2f}",
                        f"{_top_n_values['partial_p']:.2f}",
                        f"{_top_n_values['partial_r']:.2f}",
                    ]
                )


def create_exact_top_n_table(exact_results_cat, tool_name):
    csv_file = f"top_n_exact_match_table_{tool_name}.csv"

    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            ["PYTHON Feature", "TOPN", "CATEGORY", "TOTAL_FACTS", "TOTAL_CAUGHT"]
        )

        for feature_type, topn_data in exact_results_cat.items():
            for topn, categories in topn_data.items():
                first_row = True
                for category_data in categories:
                    category = category_data["Category"]
                    total_facts = category_data["Total_Facts"]
                    total_caught = category_data["Total_Caught"]

                    # First row of each group
                    if first_row:
                        writer.writerow(
                            [feature_type, topn, category, total_facts, total_caught]
                        )
                        first_row = False
                    else:
                        writer.writerow(["", "", category, total_facts, total_caught])

                total_facts_group = sum(
                    category_data["Total_Facts"] for category_data in categories
                )
                total_caught_group = sum(
                    category_data["Total_Caught"] for category_data in categories
                )
                writer.writerow(
                    ["", "", "totals", total_facts_group, total_caught_group]
                )


def exact_match_table(stats):
    with open(f"tools_exact_match_data.csv", "w", newline="") as csvfile:
        fieldnames = ["Micro-benchmark Category", "Total_facts"]
        for x in list(stats.keys()):
            fieldnames.extend(list((f"{x}_exact",)))

        writer = csv.writer(
            csvfile,
            delimiter=",",
            quotechar="|",
            quoting=csv.QUOTE_MINIMAL,
        )
        writer.writerow(fieldnames)
        tool_names = list(stats.keys())
        categories = list(stats[tool_names[0]]["exact_match"].keys())
        for category in categories:
            row = [category]
            row.extend([stats[tool_names[0]]["exact_match"][category]["total_facts"]])
            for tool in tool_names:
                row.extend([stats[tool]["exact_match"][category]["total_caught"]])
            writer.writerow(row)


def analysis_sensitivities_table(stats):
    with open(f"tools_sensitivities_data.csv", "w", newline="") as csvfile:
        fieldnames = [
            "Category",
            "Total Files",
        ]
        for x in list(stats.keys()):
            fieldnames.extend(list((f"{x}_sound",)))

        writer = csv.writer(
            csvfile,
            delimiter=",",
            quotechar="|",
            quoting=csv.QUOTE_MINIMAL,
        )
        writer.writerow(fieldnames)
        tool_names = list(stats.keys())
        categories = list(stats[tool_names[0]]["sensitivity_sound_data"].keys())
        for category in categories:
            row = [category]
            row.extend(
                [stats[tool_names[0]]["sensitivity_sound_data"][category]["file_count"]]
            )
            for tool in tool_names:
                row.extend(
                    [stats[tool]["sensitivity_sound_data"][category]["sound_passed"]]
                )
            writer.writerow(row)
