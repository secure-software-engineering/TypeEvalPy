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

    with open("paper_table_3.csv", "w", newline="") as csvfile:
        fieldnames = ["Tool_name", "Sound", "Complete"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for tool_name, tool_data in stats.items():
            sound_value = f"{tool_data['sound_complete_total_data']['s']}/{tool_data['sound_complete_total_data']['t']}"
            complete_value = f"{tool_data['sound_complete_total_data']['c']}/{tool_data['sound_complete_total_data']['t']}"
            writer.writerow(
                {
                    "Tool_name": tool_name,
                    "Sound": sound_value,
                    "Complete": complete_value,
                }
            )


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
    # Sort stats based on total_caught
    stats = utils.sort_stats(stats)

    with open(f"tools_exact_match_data.csv", "w", newline="") as csvfile:
        fieldnames = ["Category", "Total facts"]
        for x in list(stats.keys()):
            fieldnames.extend(list((f"{x.capitalize()}",)))

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

        row = ["Total"]
        total = sum(
            stats[tool_names[0]]["exact_match"][category]["total_facts"]
            for category in categories
        )
        row.extend([total])
        for tool in tool_names:
            row.extend(
                [
                    sum(
                        stats[tool]["exact_match"][category]["total_caught"]
                        for category in categories
                    )
                ]
            )
        writer.writerow(row)


def exact_match_category_table(stats):
    # Sort stats based on total_caught
    stats = utils.sort_stats(stats)

    headers = ["Tool Name"]
    tool_names = list(stats.keys())
    categories = list(stats[tool_names[0]]["exact_match_category"].keys())
    type_categories = list(
        list(stats[tool_names[0]]["exact_match_category"].values())[0].keys()
    )

    # Add headers for each combination of category and type_category
    for category in categories:
        for type_category in type_categories:
            header = f"{category}_{type_category}"
            headers.append(header)

    rows = []

    # Generate Table 1
    table1_rows = []
    table1_headers = (
        ["Tool"] + [type_category for type_category in type_categories] + ["Total"]
    )
    for tool_name in tool_names:
        row_values = [tool_name]

        tool_total = 0
        for type_category in type_categories:
            value = stats[tool_name]["exact_match_category"]["totals"][type_category][
                "r_overall_total_caught"
            ]
            tool_total += value
            row_values.append(str(value))

        row_values.append(str(tool_total))
        table1_rows.append(row_values)

    with open("paper_table_1.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(table1_headers)
        writer.writerows(table1_rows)

    # Iterate through tool_names and add the values to the rows
    for tool_name in tool_names:
        row_values = [tool_name]

        for category in categories:
            for type_category in type_categories:
                value = stats[tool_name]["exact_match_category"][category][
                    type_category
                ]["r_overall_total_caught"]
                row_values.append(str(value))

        rows.append(row_values)

    with open("tools_exact_match_category_data.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)
        writer.writerows(rows)

    # Add headers for each combination of tool and type_category
    headers = ["Category"]
    for tool_name in tool_names:
        for type_category in type_categories:
            header = f"{tool_name}_{type_category}"
            headers.append(header)

    rows = []
    for category in stats[tool_names[0]]["exact_match_category"].keys():
        row_values = [category]

        for tool_name in tool_names:
            for type_category in type_categories:
                value = stats[tool_name]["exact_match_category"][category][
                    type_category
                ]["r_overall_total_caught"]
                row_values.append(str(value))

        rows.append(row_values)

    with open("paper_table_2.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)
        writer.writerows(rows)


def create_comparison_table(stats, tools):
    # Sort stats based on total_caught
    headers = ["Tool Name"]
    stats = utils.sort_stats(stats)
    tool_names = [tool for tool in stats.keys() if tool in tools]
    categories = list(stats[tool_names[0]]["exact_match_category"].keys())
    type_categories = list(
        list(stats[tool_names[0]]["exact_match_category"].values())[0].keys()
    )

    # Add headers for each combination of category and type_category
    for category in categories:
        for type_category in type_categories:
            header = f"{category}_{type_category}"
            headers.append(header)

    rows = []

    table1_rows = []
    table1_headers = (
        ["Tool", "Top_n"]
        + [type_category for type_category in type_categories]
        + ["Total"]
    )
    for tool_name in tool_names:
        if tool_name in utils.ML_TOOLS:
            for n in utils.TOP_N:
                tool_total = 0
                row_values = [tool_name]
                row_values.append(n)
                top_n = stats[tool_name]["top_n_results"].get(n, {})
                for type_category in type_categories:
                    value = top_n.get(type_category, 0)["r_overall_total_caught"]
                    tool_total += value
                    row_values.append(str(value))
                row_values.append(str(tool_total))
                table1_rows.append(row_values)
        else:
            row_values = [tool_name]
            row_values.append("1")
            tool_total = 0
            for type_category in type_categories:
                value = stats[tool_name]["exact_match_category"]["totals"][
                    type_category
                ]["r_overall_total_caught"]
                tool_total += value
                row_values.append(str(value))
            row_values.append(str(tool_total))
            table1_rows.append(row_values)

    with open("paper_table_5.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(table1_headers)
        writer.writerows(table1_rows)


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
