import argparse
import csv
import json
import os
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

not_found_counter = []


def do_sorted(d):
    s = {}
    for n in d:
        s[str(n)] = sorted(d[n])
    return s


def get_subdirs(item):
    return os.listdir(item)


def equal_sound(out, expected):
    for item in expected:
        if not item in out:
            return False
        for edge in expected[item]:
            if not edge in out[item]:
                return False

    return True


def equal_complete(out, expected):
    for item in out:
        if not item in expected:
            continue
        for edge in out[item]:
            if not edge in expected[item]:
                return False

    return True


def measure_exact_matches(actual, expected):
    num_all = 0
    num_exact_matches = 0
    # print("Recall...")
    for node in expected:
        num_all += len(expected[node])
        for item in expected[node]:
            if actual.get(node, None) == None:
                not_found_counter.append(item)
                # print(node, ": ", item)
                continue
            if item in actual[node]:
                num_exact_matches += 1
            else:
                not_found_counter.append(item)
                # print(node, ": ", item)
    if num_all == 0:
        num_all = 1
    return num_exact_matches, num_all


def measure_precision(actual, expected):
    num_all = 0
    num_caught = 0
    # print("Precision...")
    for node in actual:
        num_all += len(actual[node])
        for item in actual[node]:
            if expected.get(node, None) == None:
                continue
            if item in expected[node]:
                num_caught += 1
            else:
                # print(node, ": ", item)
                pass

    if num_all == 0:
        num_all = 1

    return float(num_caught) / float(num_all)


def measure_recall(actual, expected):
    num_all = 0
    num_caught = 0
    # print("Recall...")
    for node in expected:
        num_all += len(expected[node])
        for item in expected[node]:
            if actual.get(node, None) == None:
                not_found_counter.append(item)
                # print(node, ": ", item)
                continue
            if item in actual[node]:
                num_caught += 1
            else:
                not_found_counter.append(item)
                # print(node, ": ", item)
    if num_all == 0:
        num_all = 1
    return float(num_caught) / float(num_all)


def get_python_files(test):
    return sorted(Path(test).rglob("*.py"))


def write_csv(res_file, data):
    header = ["Category", "Num-Cases", "Complete", "Sound", "Exact matches", "Num-all"]

    # Initialize totals
    total_num_cases = 0
    total_complete = 0
    total_sound = 0
    total_exact_matches = 0
    total_num_all = 0

    with open(res_file, "w+") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(header)

        for cat in sorted(data.keys()):
            # Extract data for readability
            num_cases = data[cat]["all"]
            complete = data[cat]["complete"]
            sound = data[cat]["sound"]
            exact_matches = data[cat]["exact_matches"]
            num_all = data[cat]["num_all"]

            # Write row data
            writer.writerow([cat, num_cases, complete, sound, exact_matches, num_all])

            # Accumulate totals
            total_num_cases += num_cases
            total_complete += complete
            total_sound += sound
            total_exact_matches += exact_matches
            total_num_all += num_all

        # Write totals row
        writer.writerow(
            [
                "Total",
                total_num_cases,
                total_complete,
                total_sound,
                total_exact_matches,
                total_num_all,
            ]
        )

    data["total"] = {
        "total_num_cases": total_num_cases,
        "total_complete": total_complete,
        "total_sound": total_sound,
        "total_exact_matches": total_exact_matches,
        "total_num_all": total_num_all,
    }

    return data


def iterate_cats(test_suite_dir, ex, results_file, do_test):
    overall_complete = 0
    overall_sound = 0
    all_tests = 0
    data = {}
    for cat in sorted(get_subdirs(test_suite_dir)):
        if cat in ["context_sensitive", "dynamic", "external", "task_test"]:
            continue

        # # Debug
        # ['args', 'assignments', 'builtins', 'classes', 'context_sensitive', 'decorators', 'dicts', 'direct_calls', 'dynamic', 'exceptions', 'external', 'flow_sensitive', 'functions', 'generators', 'imports', 'kwargs', 'lambdas', 'lists', 'mro', 'returns', 'task_test']
        # if cat not in ["returns"]:
        #     continue

        print("Iterating category {}...".format(cat))
        complete_passed = 0
        sound_passed = 0
        tests = get_subdirs(os.path.join(test_suite_dir, cat))
        tests_pnr = {}
        cat_exact_matches = {"exact_matches": 0, "num_all": 0}
        for test in tests:
            print(f"Running {test}...")
            test_path = os.path.join(test_suite_dir, cat, test)

            _result_actual, _result_expected = do_test(test_path)

            if equal_complete(_result_actual, _result_expected):
                complete_passed += 1
            else:
                # print(f"##- Not Complete {test}")
                pass

            if equal_sound(_result_actual, _result_expected):
                sound_passed += 1
            else:
                pass

            tests_pnr.setdefault(cat, {}).setdefault(test, {})

            tests_pnr[cat][test]["precision"] = measure_precision(
                _result_actual, _result_expected
            )
            tests_pnr[cat][test]["recall"] = measure_recall(
                _result_actual, _result_expected
            )

            tests_pnr[cat][test]["exact_matches"], tests_pnr[cat][test]["num_all"] = (
                measure_exact_matches(_result_actual, _result_expected)
            )

            cat_exact_matches["exact_matches"] += tests_pnr[cat][test]["exact_matches"]
            cat_exact_matches["num_all"] += tests_pnr[cat][test]["num_all"]

        data[cat] = {
            "complete": complete_passed,
            "sound": sound_passed,
            "all": len(tests),
            "tests_pnr": tests_pnr[cat],
            "exact_matches": cat_exact_matches["exact_matches"],
            "num_all": cat_exact_matches["num_all"],
        }
        overall_complete += complete_passed
        overall_sound += sound_passed
        all_tests += len(tests)

    return write_csv(results_file, data)


def do_test_hg(test):
    cs_path = os.path.join(test, "linesCallSite.json")
    results_path = os.path.join(test, "main_result.json")

    try:
        with open(results_path) as f:
            out_cs = json.loads(f.read())
    except Exception as e:
        print(f"Result file not found! {test}")
        out_cs = {}

    try:
        with open(cs_path) as f:
            expected_cs = json.loads(f.read())
    except Exception as e:
        print(f"Expected file not found! {test}")
        expected_cs = {}

    return do_sorted(out_cs), do_sorted(expected_cs)


def write_totals(totals_csv, overall_data):
    header = [
        "model",
        "total_num_cases",
        "total_complete",
        "total_sound",
        "total_exact_matches",
        "total_num_all",
    ]

    with open(totals_csv, "w+") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(header)

        for model, data in sorted(
            overall_data.items(),
            key=lambda x: x[1]["total_exact_matches"],
            reverse=True,
        ):
            # Extract data for readability
            num_cases = data["total_num_cases"]
            complete = data["total_complete"]
            sound = data["total_sound"]
            exact_matches = data["total_exact_matches"]
            num_all = data["total_num_all"]

            # # Write row data
            writer.writerow([model, num_cases, complete, sound, exact_matches, num_all])


def main(test_suite_dir, results_dir):
    overall_data = {}
    for model in sorted(get_subdirs(test_suite_dir)):
        model_test_suite_dir = os.path.join(test_suite_dir, model, "snippets")
        hg_results = os.path.join(results_dir, f"{model}_micro_benchmark_eval.csv")
        print("-" * 40)
        print("Iterating categories for Headergen")
        print("-" * 40)
        data = iterate_cats(model_test_suite_dir, None, hg_results, do_test_hg)
        overall_data[model] = data["total"]
        print("\n")

    totals_csv = os.path.join(results_dir, f"totals_micro_benchmark_eval.csv")
    write_totals(totals_csv, overall_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Microbenchmark")
    parser.add_argument(
        "--test_suite_dir",
        type=str,
        # default="/app/HeaderGen/callsites-jupyternb-micro-benchmark/snippets",
        default="/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_LLM/results/callsites/cs_trial_1",
    )
    parser.add_argument(
        "--results_dir",
        type=str,
        default="/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_LLM/.scrapy/cs_trials_1",
    )

    args = parser.parse_args()

    os.makedirs(args.results_dir, exist_ok=True)

    main(args.test_suite_dir, args.results_dir)
