import argparse
import csv
import json
import os
import sys
from collections import Counter

not_found_counter = []


def read_json(path):
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return json.loads(f.read())


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


def write_results(data, results_path):
    header = ["Project", "Precision", "Recall"]
    prec_sum = 0
    rec_sum = 0
    cnt = 0
    with open(results_path, "w+") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(header)
        for project, dt in data.items():
            writer.writerow([project, dt["precision"], dt["recall"]])
            try:
                float(dt["precision"])
                float(dt["recall"])
                prec_sum += dt["precision"]
                rec_sum += dt["recall"]
                cnt += 1
            except:
                continue
        writer.writerow(["Average", round(prec_sum / cnt, 1), round(rec_sum / cnt, 1)])

        print(
            "Precision:",
            round(prec_sum / cnt, 1),
            "Recall:",
            round(rec_sum / cnt, 1),
            "\n",
        )


def compare(notebooks_path, actual_path, expected_path, results_path):
    projects = [
        nb.split(".ipynb")[0]
        for nb in sorted(os.listdir(notebooks_path))
        if nb.endswith(".ipynb")
    ]

    prec_sum = 0
    rec_sum = 0
    cnt = 0
    data = {}
    for project in projects:
        # print("\n# Project: ", project)
        actual = read_json(os.path.join(actual_path, project + "-cs.json"))
        expected = read_json(os.path.join(expected_path, project + ".json"))

        if not actual or not expected:
            data[project] = {"precision": "-", "recall": "-"}
            continue

        precision = measure_precision(actual, expected)
        recall = measure_recall(actual, expected)
        data[project] = {
            "precision": round(precision * 100, 1),
            "recall": round(recall * 100, 1),
        }

        # print("\n")
    write_results(data, results_path)


def main(test_suite_dir, results_dir):
    benchmark_path = test_suite_dir
    results_path = results_dir

    notebooks_path = f"{benchmark_path}/notebooks"
    hg_path = f"{results_path}/annotated_notebooks"
    ground_truth_path = f"{benchmark_path}/ground_truth"

    hg_results = os.path.join(results_path, "headergen_callsites_eval.csv")

    print("\nComparing Callsites for Real-world Benchmark...")
    compare(notebooks_path, hg_path, ground_truth_path, hg_results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Annotation Comparison")
    parser.add_argument(
        "--test_suite_dir",
        type=str,
        default="/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_LLM/.scrapy/trials_cs_line_1_gpt4/gpt-4/snippets",
    )
    parser.add_argument(
        "--results_dir",
        type=str,
        default="/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_LLM/.scrapy/trials_cs_line_1_gpt4",
    )

    args = parser.parse_args()

    main(args.test_suite_dir, args.results_dir)
