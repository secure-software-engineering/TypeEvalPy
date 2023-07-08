from bs4 import BeautifulSoup
import json


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


# Load expected results from JSON file
json_file_path = "main_gt.json"

with open(json_file_path, "r") as json_file:
    expected_results = json.load(json_file)

# Example usage
html_file_path = "main.py.html"

with open(html_file_path, "r") as html_file:
    html = html_file.read()

html_values = extract_values(html)

for expected_result in expected_results:
    for html_value in html_values:
        if expected_result.get("line_number") == html_value.get("line_number"):
            if expected_result.get("variable") or expected_result.get("parameter"):
                if (expected_result.get("variable") == html_value.get("element")) or (
                    expected_result.get("parameter") == html_value.get("element")
                ):
                    result = expected_result.copy()
                    result["type"] = html_value.get("type")
                    print(result)
            else:
                if expected_result.get("function") == html_value.get("element"):
                    result = expected_result.copy()
                    result["type"] = html_value.get("type")
                    print(result)
