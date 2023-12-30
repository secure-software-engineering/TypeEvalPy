import argparse
import csv
import json
import os
import subprocess
import sys
from pathlib import Path


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


def get_python_files(test):
    return sorted(Path(test).rglob("*.py"))


def write_csv(res_file, data):
    header = ["Category", "Num-Cases", "Complete", "Sound"]
    with open(res_file, "w+") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(header)
        for cat in sorted(data.keys()):
            writer.writerow(
                [cat, data[cat]["all"], data[cat]["complete"], data[cat]["sound"]]
            )


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

        data[cat] = {
            "complete": complete_passed,
            "sound": sound_passed,
            "all": len(tests),
        }
        overall_complete += complete_passed
        overall_sound += sound_passed
        all_tests += len(tests)
    write_csv(results_file, data)


def do_test_hg(test):
    cs_path = os.path.join(test, "linesCallSite.json")
    results_path = os.path.join(test, "main_result.json")

    with open(results_path) as f:
        out_cs = json.loads(f.read())

    with open(cs_path) as f:
        expected_cs = json.loads(f.read())

    return do_sorted(out_cs), do_sorted(expected_cs)


def main(test_suite_dir, results_dir):
    hg_results = os.path.join(results_dir, "headergen_micro_benchmark_eval.csv")

    print("-" * 40)
    print("Iterating categories for Headergen")
    print("-" * 40)
    iterate_cats(test_suite_dir, None, hg_results, do_test_hg)
    print("\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Microbenchmark")
    parser.add_argument(
        "--test_suite_dir",
        type=str,
        # default="/app/HeaderGen/callsites-jupyternb-micro-benchmark/snippets",
        default="/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_LLM/.scrapy/trials_cs_line_1_gpt4/gpt-4/snippets",
    )
    parser.add_argument(
        "--results_dir",
        type=str,
        default="/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_LLM/.scrapy/trials_cs_line_1_gpt4",
    )

    args = parser.parse_args()

    main(args.test_suite_dir, args.results_dir)
