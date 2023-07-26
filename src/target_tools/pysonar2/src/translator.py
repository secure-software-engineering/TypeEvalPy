import argparse
import json
import os
from pathlib import Path
from bs4 import BeautifulSoup


def list_json_files(folder_path):
    python_files = sorted(Path(folder_path).rglob("*.json"))
    return python_files


def extract_values(html):
    soup = BeautifulSoup(html, "html.parser")
    values = []

    spans = soup.find_all("span", class_="lineno")
    for span in spans:
        line_number = int(span.text.strip())

        link = span.find_next("a")
        element = link.text.strip()

        type_value = link.get("title").split(" -> ")[-1].split(" -> ")
        type_value = [value.strip() for value in type_value]
        values.append(
            {
                "file": "main.py",
                "line_number": line_number,
                "element": element,
                "type": type_value,
            }
        )
    return values


def translate_content(file_path):
    html_file_path = str(file_path).replace(".py", ".py.html")
    json_file_path = str(file_path).replace(".py", "_gt.json")
    with open(json_file_path, "r") as json_file:
        expected_results = json.load(json_file)

    with open(html_file_path, "r") as html_file:
        html = html_file.read()

    html_values = extract_values(html)
    results = []
    for expected_result in expected_results:
        for html_value in html_values:
            if expected_result.get("line_number") == html_value.get("line_number"):
                if expected_result.get("variable") or expected_result.get("parameter"):
                    if (
                        expected_result.get("variable") == html_value.get("element")
                    ) or (
                        expected_result.get("parameter") == html_value.get("element")
                    ):
                        result = expected_result.copy()
                        result["type"] = html_value.get("type")
                        results.append(result)
                else:
                    if expected_result.get("function") == html_value.get("element"):
                        result = expected_result.copy()
                        result["type"] = html_value.get("type")
                        results.append(result)
    return results


def main_translator(args):
    json_files = list_json_files(args.bechmark_path)
    error_count = 0
    for file in json_files:
        try:
            # Run the inference here and gather results in /tmp/results
            translated = translate_content(file)

        except Exception as e:
            print(f"Command returned non-zero exit status: {e} for file: {file}")
            error_count += 1

    print(f"Runner finished with errors:{error_count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--bechmark_path",
        help="Specify the benchmark path",
        default="/tmp/micro-benchmark",
    )

    args = parser.parse_args()
    main_translator(args)
