import os
import json
import logging
from concurrent.futures import ProcessPoolExecutor, as_completed
from analysis_utils import format_type
from tqdm import tqdm
from multiprocessing import cpu_count
from threading import Lock
from collections import defaultdict

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
    """
    data_out = load_and_sort_json(out)
    data_expected = load_and_sort_json(expected)

    # Create index for data_out
    index = create_index(data_out)

    results = {
        "num_all": len(data_expected),
        "num_caught_exact": 0,
        "num_caught_partial": 0,
        "num_caught_exact_ignore_any": 0,
    }

    lock = Lock()
    progress_bar = tqdm(total=len(data_expected), desc="Processing facts", position=0)

    # Process comparisons in parallel
    with ProcessPoolExecutor(max_workers=max(cpu_count() - 1, 1)) as executor:
        futures = {
            executor.submit(
                process_fact_comparison_with_index, fact_expected, index
            ): fact_expected
            for fact_expected in data_expected
        }

        for future in tqdm(
            as_completed(futures), total=len(futures), desc="Matching facts"
        ):
            fact_expected = futures[future]  # Retrieve the corresponding fact
            try:
                is_exact_match, is_partial_match = future.result()
                with lock:
                    if is_exact_match:
                        results["num_caught_exact"] += 1
                        results["num_caught_exact_ignore_any"] += 1
                    elif is_partial_match:
                        results["num_caught_partial"] += 1
                    elif print_missed:
                        log_missed_fact(tool_name, fact_expected)
                    if fact_expected.get("type") == ["Any"]:
                        results["num_caught_exact_ignore_any"] += 1
                    progress_bar.update(1)
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
    # Test the function
    for folder in os.listdir(TEST_DIR):
        print(folder)
        out = f"{TEST_DIR}/{folder}/test1/main_result.json"
        expected = f"{TEST_DIR}/{folder}/test1/main_gt.json"
        results = measure_exact_matches(out, expected)
        print(results)

    out = "/home/ssegpu/rashida/TypeEvalPy/results/codestral-v0.1-22b/rw-benchmark/test/test_result.json"
    expected = "/home/ssegpu/rashida/TypeEvalPy/results/codestral-v0.1-22b/rw-benchmark/test/test_gt.json"
    tool_name = "codestral-v0.1-22b"

    results = measure_exact_matches(out, expected, tool_name=tool_name)
    print(results)
