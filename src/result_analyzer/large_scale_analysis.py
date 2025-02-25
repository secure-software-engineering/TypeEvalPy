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

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
TEST_DIR = os.path.join(
    SCRIPT_DIR, "results_analysis_tests/test/micro-benchmark/python_features"
)

TOP_5_LARGEST_PROMPTS = [
    'repos/ChrisCummins/phd/system/machines/mirrored_directory_test.py',
    'repos/cmdmnt/commandment/commandment/dep/dep.py',
    'repos/sara0871/sara0871.topics-scilkit-leam/homeassistant/components/vacuum/__init__.py',
    'repos/zspatter/network-simulation/tests/test_network.py',
    'repos/cabalamat/frambozenapp/app/bozen/mondoc.py'
]

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

    if expected.get("line_number") != out.get("line_number"):
        return False, False

    # Optional column offset check
    if "col_offset" in expected and expected.get("col_offset") != out.get("col_offset"):
        return False, False

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
            is_exact_match, is_partial_match = process_fact_comparison_with_index(fact_expected, index)
            if is_exact_match:
                results["num_caught_exact"] += 1
            elif is_partial_match:
                results["num_caught_partial"] += 1
            elif print_missed:
                log_missed_fact(tool_name, fact_expected)

            # Count specific types
            if "function" in fact_expected and "parameter" not in fact_expected and "variable" not in fact_expected:
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

def measure_exact_matches_ignoring_builtin_types(out, expected, tool_name=None, print_missed=False):
    """
    Measure exact and partial matches between two JSON files using indexing for efficiency.
    Additionally, count matches for function return types, parameter types, and variable types.
    Ignore builtin types during the comparison.
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

    builtin_types = {"int", "float", "str", "bool", "list", "dict", "set", "tuple", "none"}

    progress_bar = tqdm(total=len(data_expected), desc="Processing facts", position=0)

    for fact_expected in data_expected:
        expected_type = fact_expected.get("type", [])
        if isinstance(expected_type, list):
            expected_type = expected_type[0] if expected_type else None

        # Skip builtin types
        if expected_type.lower() in builtin_types:
            continue

        results["num_all"] += 1

        try:
            is_exact_match, is_partial_match = process_fact_comparison_with_index(fact_expected, index)
            if is_exact_match:
                results["num_caught_exact"] += 1
            elif is_partial_match:
                results["num_caught_partial"] += 1
            elif print_missed:
                log_missed_fact(tool_name, fact_expected)

            # Count specific types
            if "function" in fact_expected and "parameter" not in fact_expected and "variable" not in fact_expected:
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
    filtered_data_out = [entry for entry in data_out if entry.get("file") in top_5_file_paths]
    filtered_data_expected = [entry for entry in data_expected if entry.get("file") in top_5_file_paths]

    # Create index for filtered data_out
    index = create_index(filtered_data_out)

    results = {
        "num_all": len(filtered_data_expected),
        "num_caught_exact": 0,
        "num_caught_partial": 0,
        "file_counts": {file_path: {"num_all": 0, "num_caught_exact": 0, "num_caught_partial": 0} for file_path in top_5_file_paths}
    }

    for fact_expected in filtered_data_expected:
        is_exact_match, is_partial_match = process_fact_comparison_with_index(fact_expected, index)
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
    Analyze unique types in the output and expected data.
    """
    data_out = load_and_sort_json(data_out)
    data_expected = load_and_sort_json(data_expected)

    # Create index for data_out
    index = create_index(data_out)

    results = {}

    for fact_expected in data_expected:
        try:
            is_exact_match, is_partial_match = process_fact_comparison_with_index(fact_expected, index)
            
            expected_types = fact_expected.get("type", [])
            if not isinstance(expected_types, list):
                expected_types = [expected_types]  # Ensure it's a list

            for expected_type in expected_types:
                nested_level = expected_type.count('[')
                if nested_level >= 2:
                    if expected_type not in results:
                        results[expected_type] = {"Type": expected_type, "Total_facts": 0, "Exact_facts": 0}

                    results[expected_type]["Total_facts"] += 1
                    if is_exact_match:
                        results[expected_type]["Exact_facts"] += 1

        except Exception as e:
            logging.error(f"Error processing fact: {fact_expected} - {e}")

    # Sort results by Total_facts and return top 5
    sorted_results = dict(sorted(results.items(), key=lambda item: item[1]["Total_facts"], reverse=True)[:5])
    return results

def log_missed_fact(tool_name, fact_expected):
    """
    Log missed facts to a CSV file for further analysis.
    """
    if not tool_name:
        return

    missed_log_path = f"{tool_name}_not_found_reasons.csv"
    with open(missed_log_path, "a") as f:
        f.write(f";Missing Fact;{json.dumps(fact_expected)}\n")

# Output the result
if __name__ == "__main__":
    out = "/home/ssegpu/rashida/TypeEvalPy/results/qwen2.5-Coder-7B-Instruct-without-any/rw-benchmark/test/test_result.json"
    expected = "/home/ssegpu/rashida/TypeEvalPy/results/qwen2.5-Coder-7B-Instruct-without-any/rw-benchmark/test/test_gt.json"
    tool_name = "qwen2.5-Coder-7B-Instruct-without-any"

    results = measure_exact_matches(out, expected, tool_name=tool_name)
    results_qa = analyze_top_5_most_questions_asked(out, expected)
    results_unique_types = analyze_unique_types(out, expected)
    results_without_builtin_types = measure_exact_matches_ignoring_builtin_types(out, expected, tool_name=tool_name)

    # Create a table for the results without builtin types
    table_without_builtin_types = PrettyTable()
    table_without_builtin_types.field_names = ["Metric", "Value"]
    table_without_builtin_types.add_row(["Total Facts", results_without_builtin_types["num_all"]])
    table_without_builtin_types.add_row(["Exact Matches", results_without_builtin_types["num_caught_exact"]])
    table_without_builtin_types.add_row(["Partial Matches", results_without_builtin_types["num_caught_partial"]])
    table_without_builtin_types.add_row(["Function Return Total", results_without_builtin_types["function_return"]["total"]])
    table_without_builtin_types.add_row(["Function Return Exact", results_without_builtin_types["function_return"]["exact"]])
    table_without_builtin_types.add_row(["Function Return Partial", results_without_builtin_types["function_return"]["partial"]])
    table_without_builtin_types.add_row(["Parameter Type Total", results_without_builtin_types["parameter_type"]["total"]])
    table_without_builtin_types.add_row(["Parameter Type Exact", results_without_builtin_types["parameter_type"]["exact"]])
    table_without_builtin_types.add_row(["Parameter Type Partial", results_without_builtin_types["parameter_type"]["partial"]])
    table_without_builtin_types.add_row(["Variable Type Total", results_without_builtin_types["variable_type"]["total"]])
    table_without_builtin_types.add_row(["Variable Type Exact", results_without_builtin_types["variable_type"]["exact"]])
    table_without_builtin_types.add_row(["Variable Type Partial", results_without_builtin_types["variable_type"]["partial"]])

    print("Results Ignoring Builtin Types:")
    print(table_without_builtin_types)

    table_unique_types = PrettyTable()
    table_unique_types.field_names = ["Type", "Total Facts", "Exact Facts"]

    total_types = 0
    total_facts = 0
    total_exact_facts = 0

    for type_info in results_unique_types.values():
        table_unique_types.add_row([type_info["Type"], type_info["Total_facts"], type_info["Exact_facts"]])
        total_types += 1
        total_facts += type_info["Total_facts"]
        total_exact_facts += type_info["Exact_facts"]

    table_unique_types.add_row(["Total", total_facts, total_exact_facts])

    print(table_unique_types)

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

    print(f"Tool Name: {tool_name}")
    print("Overall Results:")
    print(table)
    print("\nTop 5 Most Questions Asked Results:")
    table_qa = PrettyTable()
    table_qa.field_names = ["File", "Total Facts", "Exact Matches", "Partial Matches"]

    total_facts = 0
    total_exact_matches = 0
    total_partial_matches = 0

    for file_path, counts in results_qa["file_counts"].items():
        table_qa.add_row([file_path, counts["num_all"], counts["num_caught_exact"], counts["num_caught_partial"]])
        total_facts += counts["num_all"]
        total_exact_matches += counts["num_caught_exact"]
        total_partial_matches += counts["num_caught_partial"]

    table_qa.add_row(["Total", total_facts, total_exact_matches, total_partial_matches])

    print(table_qa)
    
    # Save the tables to a file
    analysis_file_path = "/home/ssegpu/rashida/TypeEvalPy/results/qwen2.5-Coder-7B-Instruct-without-any/analysis_results.txt"
    os.makedirs(os.path.dirname(analysis_file_path), exist_ok=True)
    with open(analysis_file_path, "w") as f:
        f.write(f"Tool Name: {tool_name}\n")
        f.write("Overall Results:\n")
        f.write(str(table))
        f.write("\n\nTop 5 Most Questions Asked Results:\n")
        f.write(str(table_qa))
        f.write("\n\nUnique Types Results:\n")
        f.write(str(table_unique_types))
        f.write("\n\nResults Ignoring Builtin Types:\n")
        f.write(str(table_without_builtin_types))
        