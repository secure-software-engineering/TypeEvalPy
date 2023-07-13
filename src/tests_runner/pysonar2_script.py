from bs4 import BeautifulSoup
import json
import os
import subprocess


def list_python_files(folder_path):
    python_files = []
    for root, Readme, files in os.walk(os.path.abspath(folder_path)):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
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
    # print(json.dumps(values, indent=4))
    return values


def pysonar_results(json_file_path, html_file_path):
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


current_directory = os.getcwd()
print("Current directory:", current_directory)
folder_path = "/tmp/micro-benchmark/python_features"
directory_name = "/app/pysonar2"
pysonar2_command = [
    "java",
    "-jar",
    "target/pysonar-2.1.3.jar",
    "/tmp/micro-benchmark/python_features/",
    "/tmp/micro-benchmark/python_features/",
]
pysonar2_process = subprocess.Popen(pysonar2_command, cwd=directory_name)
pysonar2_process.wait()
python_files = list_python_files(folder_path)

for file in python_files:
    try:
        print(file)
        html_file_path = file.replace(".py", ".py.html")
        json_file_path = file.replace(".py", "_gt.json")
        result_file_path = file.replace(".py", "_pysonar2.json")
        result = pysonar_results(json_file_path, html_file_path)
        with open(result_file_path, "w") as json_file:
            json.dump(result, json_file, indent=4)

            # print(json.dumps(output, indent=4))
    except Exception as e:
        print(e)
