import os
import json
import logging
from concurrent.futures import ProcessPoolExecutor, as_completed
from analysis_utils import format_type
from tqdm import tqdm
from multiprocessing import cpu_count
from threading import Lock
from collections import defaultdict
from prettytable import PrettyTable
import os
from pathlib import Path
import csv

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
TEST_DIR = os.path.join(
    SCRIPT_DIR, "results_analysis_tests/test/micro-benchmark/python_features"
)

def check_match(
    expected,
    out,
    top_n=1,
    is_ml=False,
    print_mismatch=False,
    metadata=None,
):
    """
    Check for both exact and partial matches between expected and out entries.
    Returns a tuple: (is_exact_match, is_partial_match).
    """
    metadata = metadata or {}

    # Check keys in `out` are present in `expected`
    if not all(
        x in expected
        for x in out.keys()
        if x not in {"type", "all_type_preds", "col_offset"}
    ):
        return False, False

    # Early exits for file and line number mismatches
    if expected.get("file") != out.get("file"):
        return False, False

    # if expected.get("line_number") != out.get("line_number"):
    #     return False, False

    # # Optional column offset check
    # if "col_offset" in expected and expected.get("col_offset") != out.get("col_offset"):
    #     return False, False

    # Match specific fields if present
    for key in ["function", "parameter", "variable"]:
        if key in expected and expected.get(key) != out.get(key):
            return False, False

    # Type matching logic
    if is_ml:
        _types = [x[0] for x in out.get("all_type_preds", [])]
    else:
        _types = out.get("type", [])

    type_formatted = format_type([_types])
    expected_type_formatted = format_type([expected.get("type", [])])

    # Remove single quotes from formatted types
    type_formatted = [
        [t.replace("'", "") for t in sublist] for sublist in type_formatted
    ]
    expected_type_formatted = [
        [t.replace("'", "") for t in sublist] for sublist in expected_type_formatted
    ]

    # Exact match check
    is_exact_match = any(
        sorted(expected_type_formatted) == [t_list] for t_list in type_formatted[:top_n]
    )

    # Partial match check
    expected_set = {t for sublist in expected_type_formatted for t in sublist}
    is_partial_match = any(
        expected_set.intersection(t_list) for t_list in type_formatted[:top_n]
    )

    if not (is_exact_match or is_partial_match) and print_mismatch:
        log_mismatch(metadata, expected, out, partial_match=True)

    return is_exact_match, is_partial_match


def log_mismatch(metadata, expected, out, partial_match):
    """
    Log mismatched cases for debugging or analysis.
    """
    print(f"\n\n##### Type mismatch! #####\nPartial matching: {partial_match}")
    tool_name = metadata.get("tool_name", "unknown_tool")
    mismatch_file = f"{tool_name}_mismatches_reasons.csv"
    with open(mismatch_file, "a") as f:
        f.write(
            ";".join(
                [
                    metadata.get("cat", "unknown_cat"),
                    metadata.get("type_category", "unknown_category"),
                    json.dumps(expected),
                    json.dumps(out),
                ]
            )
        )
        f.write("\n")

    print("Ground Truth:")
    print(json.dumps(expected, indent=4))
    print("Output:")
    print(json.dumps(out, indent=4))
    print("####################\n\n")


def sort_facts(data):
    """
    Sort facts based on line_number and ensure 'type' fields (if list) are sorted.
    """
    return sorted(data, key=lambda x: int(x.get("line_number", 0)))


def load_and_sort_json(file_path):
    """
    Load JSON from a file and sort the facts for consistent processing.
    """
    with open(file_path) as f:
        data = json.load(f)
    return sort_facts(data)


def measure_exact_matches(out, expected, tool_name=None, print_missed=False):
    """
    Measure exact and partial matches between two JSON files using indexing for efficiency.
    Additionally, count matches for function return types, parameter types, and variable types.
    """
    data_out = load_and_sort_json(out)
    data_expected = load_and_sort_json(expected)

    # Create index for data_out
    index = create_index(data_out)

    results = {
        "num_all": len(data_expected),
        "num_caught_exact": 0,
        "num_caught_partial": 0,
        "function_return": {"total": 0, "exact": 0, "partial": 0},
        "parameter_type": {"total": 0, "exact": 0, "partial": 0},
        "variable_type": {"total": 0, "exact": 0, "partial": 0},
    }

    progress_bar = tqdm(total=len(data_expected), desc="Processing facts", position=0)

    for fact_expected in data_expected:
        try:
            is_exact_match, is_partial_match = process_fact_comparison_with_index(
                fact_expected, index
            )
            if is_exact_match:
                results["num_caught_exact"] += 1
            elif is_partial_match:
                results["num_caught_partial"] += 1
            elif print_missed:
                log_missed_fact(tool_name, fact_expected)

            # Count specific types
            if (
                "function" in fact_expected
                and "parameter" not in fact_expected
                and "variable" not in fact_expected
            ):
                results["function_return"]["total"] += 1
                if is_exact_match:
                    results["function_return"]["exact"] += 1
                elif is_partial_match:
                    results["function_return"]["partial"] += 1
            if "parameter" in fact_expected:
                results["parameter_type"]["total"] += 1
                if is_exact_match:
                    results["parameter_type"]["exact"] += 1
                elif is_partial_match:
                    results["parameter_type"]["partial"] += 1
            if "variable" in fact_expected:
                results["variable_type"]["total"] += 1
                if is_exact_match:
                    results["variable_type"]["exact"] += 1
                elif is_partial_match:
                    results["variable_type"]["partial"] += 1

        except Exception as e:
            logging.error(f"Error processing fact: {fact_expected} - {e}")
        finally:
            progress_bar.update(1)

    progress_bar.close()
    return results


def measure_exact_for_builtins_matches(
    out, expected, tool_name=None, print_missed=False
):
    """
    Measure exact and partial matches between two JSON files using indexing for efficiency.
    Additionally, count matches for function return types, parameter types, and variable types.
    """
    data_out = load_and_sort_json(out)
    data_expected = load_and_sort_json(expected)

    # Create index for data_out
    index = create_index(data_out)

    results = {
        "num_all": 0,
        "num_caught_exact": 0,
        "num_caught_partial": 0,
        "function_return": {"total": 0, "exact": 0, "partial": 0},
        "parameter_type": {"total": 0, "exact": 0, "partial": 0},
        "variable_type": {"total": 0, "exact": 0, "partial": 0},
    }

    builtin_types = {
        "int",
        "float",
        "complex",
        "str",
        "list",
        "tuple",
        "range",
        "set",
        "frozenset",
        "dict",
        "bytes",
        "bytearray",
        "memoryview",
        "bool",
        "none",
    }

    progress_bar = tqdm(total=len(data_expected), desc="Processing facts", position=0)

    for fact_expected in data_expected:
        try:
            is_exact_match, is_partial_match = process_fact_comparison_with_index(
                fact_expected, index
            )

            expected_types = fact_expected.get("type", [])
            if not isinstance(expected_types, list):
                expected_types = [expected_types]  # Ensure it's a list

            for expected_type in expected_types:
                base_type = expected_type.split("[")[0].lower()
                if base_type not in builtin_types:
                    continue

                results["num_all"] += 1

                if is_exact_match:
                    results["num_caught_exact"] += 1
                elif is_partial_match:
                    results["num_caught_partial"] += 1
                elif print_missed:
                    log_missed_fact(tool_name, fact_expected)

                # Count specific types
                if (
                    "function" in fact_expected
                    and "parameter" not in fact_expected
                    and "variable" not in fact_expected
                ):
                    results["function_return"]["total"] += 1
                    if is_exact_match:
                        results["function_return"]["exact"] += 1
                    elif is_partial_match:
                        results["function_return"]["partial"] += 1
                if "parameter" in fact_expected:
                    results["parameter_type"]["total"] += 1
                    if is_exact_match:
                        results["parameter_type"]["exact"] += 1
                    elif is_partial_match:
                        results["parameter_type"]["partial"] += 1
                if "variable" in fact_expected:
                    results["variable_type"]["total"] += 1
                    if is_exact_match:
                        results["variable_type"]["exact"] += 1
                    elif is_partial_match:
                        results["variable_type"]["partial"] += 1

        except Exception as e:
            logging.error(f"Error processing fact: {fact_expected} - {e}")
        finally:
            progress_bar.update(1)

    progress_bar.close()
    return results


def process_fact_comparison(fact_expected, data_out):
    """
    Compare a single fact against all output facts to determine exact and partial matches.
    Returns the combined match results.
    """
    is_exact_match = False
    is_partial_match = False

    repo_name = fact_expected["file"]
    repo_out_data = [entry for entry in data_out if entry.get("file") == repo_name]

    for fact_out in repo_out_data:
        exact_match, partial_match = check_match(fact_expected, fact_out)
        is_exact_match = is_exact_match or exact_match
        is_partial_match = is_partial_match or partial_match

        # Break early if both matches are found
        if is_exact_match and is_partial_match:
            break

    return is_exact_match, is_partial_match


def create_index(data_out):
    """
    Create an index for data_out based on (file, line_number) and optionally other fields.
    """
    index = defaultdict(list)
    for fact_out in data_out:
        key = (fact_out.get("file"), fact_out.get("line_number"))
        index[key].append(fact_out)
    return index


def process_fact_comparison_with_index(fact_expected, index):
    """
    Compare a single fact against indexed output facts for matches.
    """
    is_exact_match = False
    is_partial_match = False

    # Get the relevant facts from the index
    key = (fact_expected.get("file"), fact_expected.get("line_number"))
    relevant_facts = index.get(key, [])

    # Compare only relevant facts
    for fact_out in relevant_facts:
        exact_match, partial_match = check_match(fact_expected, fact_out)
        is_exact_match = is_exact_match or exact_match
        is_partial_match = is_partial_match or partial_match

        # Break early if both matches are found
        if is_exact_match and is_partial_match:
            break

    return is_exact_match, is_partial_match


def analyze_top_5_most_questions_asked(out, expected):
    data_out = load_and_sort_json(out)
    data_expected = load_and_sort_json(expected)

    # Count entries for each file
    file_counts = defaultdict(int)
    for entry in data_expected:
        file_counts[entry.get("file")] += 1

    # Get top 5 files with the most entries
    top_5_files = sorted(file_counts.items(), key=lambda x: x[1], reverse=True)[:5]
    top_5_file_paths = [file[0] for file in top_5_files]

    # Filter data for the top 5 files
    filtered_data_out = [
        entry for entry in data_out if entry.get("file") in top_5_file_paths
    ]
    filtered_data_expected = [
        entry for entry in data_expected if entry.get("file") in top_5_file_paths
    ]

    # Create index for filtered data_out
    index = create_index(filtered_data_out)

    results = {
        "num_all": len(filtered_data_expected),
        "num_caught_exact": 0,
        "num_caught_partial": 0,
        "file_counts": {
            file_path: {"num_all": 0, "num_caught_exact": 0, "num_caught_partial": 0}
            for file_path in top_5_file_paths
        },
    }

    for fact_expected in filtered_data_expected:
        is_exact_match, is_partial_match = process_fact_comparison_with_index(
            fact_expected, index
        )
        file_path = fact_expected.get("file")
        results["file_counts"][file_path]["num_all"] += 1
        if is_exact_match:
            results["num_caught_exact"] += 1
            results["file_counts"][file_path]["num_caught_exact"] += 1
        elif is_partial_match:
            results["num_caught_partial"] += 1
            results["file_counts"][file_path]["num_caught_partial"] += 1

    return results


def analyze_unique_types(data_out, data_expected):
    """
    Analyze unique types in the output and expected data, ignoring builtin base types.
    """
    data_out = load_and_sort_json(data_out)
    data_expected = load_and_sort_json(data_expected)

    # Create index for data_out
    index = create_index(data_out)

    results = {}
    builtin_types = {
        "int",
        "float",
        "complex",
        "str",
        "list",
        "tuple",
        "range",
        "set",
        "frozenset",
        "dict",
        "bytes",
        "bytearray",
        "memoryview",
        "bool",
        "none",
    }

    typing_types = {
        "any",
        "optional",
        "union",
        "literal",
        "final",
        "classvar",
        "noreturn",
        "list",
        "tuple",
        "set",
        "frozenset",
        "dict",
        "deque",
        "defaultdict",
        "counter",
        "namedtuple",
        "typeddict",
        "callable",
        "iterator",
        "iterable",
        "generator",
        "asynciterator",
        "asynciterable",
        "coroutine",
        "contextmanager",
        "asynccontextmanager",
        "protocol",
        "type",
        "typevar",
    }

    for fact_expected in data_expected:
        try:
            is_exact_match, is_partial_match = process_fact_comparison_with_index(
                fact_expected, index
            )

            expected_types = fact_expected.get("type", [])
            if not isinstance(expected_types, list):
                expected_types = [expected_types]  # Ensure it's a list

            for expected_type in expected_types:
                base_type = expected_type.split("[")[0].lower()
                if base_type in builtin_types:
                    continue

                if base_type in typing_types:
                    continue

                if expected_type not in results:
                    results[expected_type] = {
                        "Type": expected_type,
                        "Total_facts": 0,
                        "Exact_facts": 0,
                    }

                results[expected_type]["Total_facts"] += 1
                if is_exact_match:
                    results[expected_type]["Exact_facts"] += 1

        except Exception as e:
            logging.error(f"Error processing fact: {fact_expected} - {e}")

    # Sort results by Total_facts and return top 5
    sorted_results = dict(
        sorted(results.items(), key=lambda item: item[1]["Total_facts"], reverse=True)
    )
    return sorted_results


# Get distribution of all types
# makes csv
# get the 0.1% percentage occurrence of each type
# do it on training set gt
# top 10 frequent types


def prepare_unified_json(results_dir):
    """
    Prepare a unified JSON file for all tools for easy comparison.
    """
    unified_out = []
    unified_expected = []

    for file_main in Path(results_dir).rglob("main.py"):
        file_name = os.path.relpath(file_main, results_dir)
        file_gt = file_main.parent / "main_gt.json"
        file_out = file_main.parent / "main_result.json"
        if file_out.exists():
            with open(file_out) as f:
                tool_data = json.load(f)
                for entry in tool_data:
                    entry["file"] = file_name
                    unified_out.append(entry)

        if file_gt.exists():
            with open(file_gt) as f:
                gt_data = json.load(f)
                for entry in gt_data:
                    entry["file"] = file_name
                    unified_expected.append(entry)

    #  store as file and return path instead
    unified_out_path = os.path.join("/tmp", "unified_out.json")
    unified_expected_path = os.path.join("/tmp", "unified_expected.json")
    with open(unified_out_path, "w") as f:
        json.dump(unified_out, f, indent=4)

    with open(unified_expected_path, "w") as f:
        json.dump(unified_expected, f, indent=4)

    return unified_out_path, unified_expected_path


def log_missed_fact(tool_name, fact_expected):
    """
    Log missed facts to a CSV file for further analysis.
    """
    if not tool_name:
        return

    missed_log_path = f"{tool_name}_not_found_reasons.csv"
    with open(missed_log_path, "a") as f:
        f.write(f";Missing Fact;{json.dumps(fact_expected)}\n")


def analyze_top_10_frequent_types(csv_file_path, data_out, data_expected):
    """
    Analyze the top 10 frequent types from a CSV file and check for exact matches with total facts and exact matches.
    """
    top_10_types = []

    # Read the CSV file and extract the top 10 frequent types
    with open(csv_file_path, mode="r") as file:
        csv_reader = csv.DictReader(file)
        sorted_types = sorted(
            (row for row in csv_reader if row["Count"].strip().isdigit()),
            key=lambda row: int(row["Count"].strip()),
            reverse=True,
        )
        top_10_types = [row["Type"] for row in sorted_types[:10]]

    # Load and sort JSON data
    data_out = load_and_sort_json(out)
    data_expected = load_and_sort_json(expected)

    # Create index for data_out
    index = create_index(data_out)

    # Check for exact matches with total facts and exact matches
    results = {"total_facts": 0, "exact_matches": 0, "top_10_types": []}

    for type_name in top_10_types:
        total_facts = 0
        exact_facts = 0

        for fact in data_expected:
            expected_type = fact.get("type", [])
            if isinstance(expected_type, list):
                expected_type = expected_type[0] if expected_type else None

            if expected_type == type_name:
                total_facts += 1
                is_exact_match, _ = process_fact_comparison_with_index(fact, index)
                if is_exact_match:
                    exact_facts += 1

        results["top_10_types"].append(
            {"Type": type_name, "Total_facts": total_facts, "Exact_facts": exact_facts}
        )
        results["total_facts"] += total_facts
        results["exact_matches"] += exact_facts

    return results


def analyze_rare_types(csv_file_path, data_out, data_expected):
    """
    Analyze the rare types from a CSV file and check for exact matches with total facts and exact matches.
    """
    rare_types = []

    # Read the CSV file and extract the rare types
    with open(csv_file_path, mode="r") as file:
        csv_reader = csv.DictReader(file)
        rare_types = [row["Type"] for row in csv_reader]

    # Load and sort JSON data
    data_out = load_and_sort_json(data_out)
    data_expected = load_and_sort_json(data_expected)

    # Create index for data_out
    index = create_index(data_out)

    # Check for exact matches with total facts and exact matches
    results = {"total_facts": 0, "exact_matches": 0, "rare_types": []}

    for type_name in rare_types:
        total_facts = 0
        exact_facts = 0

        for fact in data_expected:
            expected_type = fact.get("type", [])
            if isinstance(expected_type, list):
                expected_type = expected_type[0] if expected_type else None

            if expected_type == type_name:
                total_facts += 1
                is_exact_match, _ = process_fact_comparison_with_index(fact, index)
                if is_exact_match:
                    exact_facts += 1
                elif expected_type == "object":
                    print(fact)

        results["rare_types"].append(
            {"Type": type_name, "Total_facts": total_facts, "Exact_facts": exact_facts}
        )
        results["total_facts"] += total_facts
        results["exact_matches"] += exact_facts

    return results


# Output the result
if __name__ == "__main__":
    out = "/home/ssegpu/rashida/TypeEvalPy/results_new/finetuned-qwen2.5-Coder-7B-Instruct-without-any/rw-benchmark/test/test_result.json"
    expected = "/home/ssegpu/rashida/TypeEvalPy/results_new/finetuned-qwen2.5-Coder-7B-Instruct-without-any/rw-benchmark/test/test_gt.json"
    tool_name = ""

    # tools = {
    #     # "HiTyper": "/home/ssegpu/rashida/TypeEvalPy/results/results_25-02-25 19_06/hityperdl/micro-benchmark/repos",
    #     # "Type4Py": "/home/ssegpu/rashida/TypeEvalPy/results/results_26-02-25 09_26/type4py/micro-benchmark/repos",
    #     "h2": "/home/ssegpu/rashida/TypeEvalPy/results/results_26-02-25 12_30/hityperdl/micro-benchmark/repos"
    # }

    # for tool_name, results_dir in tools.items():
    #     if not results_dir:
    #         continue
    #     out, expected = prepare_unified_json(results_dir)

    results = measure_exact_matches(out, expected, tool_name=tool_name)
    results_builtins = measure_exact_for_builtins_matches(
        out, expected, tool_name=tool_name
    )

    results_qa = analyze_top_5_most_questions_asked(out, expected)
    results_unique_types = analyze_unique_types(out, expected)

    # Example usage
    csv_file_path = (
        "/home/ssegpu/rashida/TypeEvalPy/src/result_analyzer/.scrapy/top_10.csv"
    )
    results_top_10_frequent_types = analyze_top_10_frequent_types(
        csv_file_path, out, expected
    )

    rare_types_csv_file_path = (
        "/home/ssegpu/rashida/TypeEvalPy/src/result_analyzer/.scrapy/under_0_1.csv"
    )
    results_rare_types = analyze_rare_types(rare_types_csv_file_path, out, expected)

    # Top 10 Frequent Types Results
    table_top_10_frequent_types = PrettyTable()
    table_top_10_frequent_types.field_names = ["Type", "Total Facts", "Exact Facts"]

    for type_info in results_top_10_frequent_types["top_10_types"]:
        table_top_10_frequent_types.add_row(
            [type_info["Type"], type_info["Total_facts"], type_info["Exact_facts"]]
        )

    table_top_10_frequent_types.add_row(
        [
            "Total",
            results_top_10_frequent_types["total_facts"],
            results_top_10_frequent_types["exact_matches"],
        ]
    )

    print("Top 10 rare Types Results:")
    table_rare_types = PrettyTable()
    table_rare_types.field_names = ["Type", "Total Facts", "Exact Facts"]

    for type_info in results_rare_types["rare_types"]:
        table_rare_types.add_row(
            [type_info["Type"], type_info["Total_facts"], type_info["Exact_facts"]]
        )

    table_rare_types.add_row(
        [
            "Total",
            results_rare_types["total_facts"],
            results_rare_types["exact_matches"],
        ]
    )

    print("Top 10 unique Types Results:")
    table_unique_types = PrettyTable()
    table_unique_types.field_names = ["Type", "Total Facts", "Exact Facts"]

    for type_info in results_unique_types.values():
        table_unique_types.add_row(
            [type_info["Type"], type_info["Total_facts"], type_info["Exact_facts"]]
        )

    table_unique_types.add_row(
        [
            "Total",
            sum(
                [
                    type_info["Total_facts"]
                    for type_info in results_unique_types.values()
                ]
            ),
            sum(
                [
                    type_info["Exact_facts"]
                    for type_info in results_unique_types.values()
                ]
            ),
        ]
    )

    # Create a table for the results
    table = PrettyTable()
    table.field_names = ["Metric", "Value"]
    table.add_row(["Total Facts", results["num_all"]])
    table.add_row(["Exact Matches", results["num_caught_exact"]])
    table.add_row(["Partial Matches", results["num_caught_partial"]])
    table.add_row(["Function Return Total", results["function_return"]["total"]])
    table.add_row(["Function Return Exact", results["function_return"]["exact"]])
    table.add_row(["Function Return Partial", results["function_return"]["partial"]])
    table.add_row(["Parameter Type Total", results["parameter_type"]["total"]])
    table.add_row(["Parameter Type Exact", results["parameter_type"]["exact"]])
    table.add_row(["Parameter Type Partial", results["parameter_type"]["partial"]])
    table.add_row(["Variable Type Total", results["variable_type"]["total"]])
    table.add_row(["Variable Type Exact", results["variable_type"]["exact"]])
    table.add_row(["Variable Type Partial", results["variable_type"]["partial"]])

    # Create a table for the results_builtins
    table_builtins = PrettyTable()
    table_builtins.field_names = ["Metric", "Value"]
    table_builtins.add_row(["Total Facts", results_builtins["num_all"]])
    table_builtins.add_row(["Exact Matches", results_builtins["num_caught_exact"]])
    table_builtins.add_row(["Partial Matches", results_builtins["num_caught_partial"]])
    table_builtins.add_row(
        ["Function Return Total", results_builtins["function_return"]["total"]]
    )
    table_builtins.add_row(
        ["Function Return Exact", results_builtins["function_return"]["exact"]]
    )
    table_builtins.add_row(
        ["Function Return Partial", results_builtins["function_return"]["partial"]]
    )
    table_builtins.add_row(
        ["Parameter Type Total", results_builtins["parameter_type"]["total"]]
    )
    table_builtins.add_row(
        ["Parameter Type Exact", results_builtins["parameter_type"]["exact"]]
    )
    table_builtins.add_row(
        ["Parameter Type Partial", results_builtins["parameter_type"]["partial"]]
    )
    table_builtins.add_row(
        ["Variable Type Total", results_builtins["variable_type"]["total"]]
    )
    table_builtins.add_row(
        ["Variable Type Exact", results_builtins["variable_type"]["exact"]]
    )
    table_builtins.add_row(
        ["Variable Type Partial", results_builtins["variable_type"]["partial"]]
    )

    print(f"Tool Name: {tool_name}")
    print("Overall Results:")
    print(table)

    print("\nTop 5 Most Questions Asked Results:")
    table_qa = PrettyTable()
    table_qa.field_names = ["File", "Total Facts", "Exact Matches", "Partial Matches"]

    print("Tool Name: ", tool_name)
    print("Overall builtins Results:")
    print(table_builtins)

    total_facts = 0
    total_exact_matches = 0
    total_partial_matches = 0

    for file_path, counts in results_qa["file_counts"].items():
        table_qa.add_row(
            [
                file_path,
                counts["num_all"],
                counts["num_caught_exact"],
                counts["num_caught_partial"],
            ]
        )
        total_facts += counts["num_all"]
        total_exact_matches += counts["num_caught_exact"]
        total_partial_matches += counts["num_caught_partial"]

    table_qa.add_row(["Total", total_facts, total_exact_matches, total_partial_matches])

    print(table_qa)

    # Save the tables to a file
    analysis_file_path = "/home/ssegpu/rashida/TypeEvalPy/results_new/finetuned-qwen2.5-Coder-7B-Instruct-without-any/analysis_results.txt"
    os.makedirs(os.path.dirname(analysis_file_path), exist_ok=True)
    with open(analysis_file_path, "w") as f:
        f.write(f"Tool Name: {tool_name}\n")
        f.write("Overall Results:\n")
        f.write(str(table))
        f.write("\n\nTop 5 Most Questions Asked Results:\n")
        f.write(str(table_qa))
        f.write("\n\nTop 10 Frequent Types Results:\n")
        f.write(str(table_top_10_frequent_types))
        f.write("\n\nRare Types Results:\n")
        f.write(str(table_rare_types))
        f.write("\n\nUnique Types Results:\n")
        f.write(str(table_unique_types))
        f.write("\n\nOverall builtins Results:\n")
        f.write(str(table_builtins))
