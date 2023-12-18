import itertools
import json
import os
import random
import re
import shutil

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))


def generate_value_for_type(chosen_type):
    """Generate a random value and its corresponding data type"""

    if chosen_type == "int":
        return random.randint(1, 100), "int"
    elif chosen_type == "float":
        return round(random.uniform(1, 100), 2), "float"
    elif chosen_type == "str":
        return (
            '"' + "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=5)) + '"',
            "str",
        )
    elif chosen_type == "bool":
        return random.choice(["True", "False"]), "bool"
    elif chosen_type == "list":
        return (
            "[" + ", ".join(str(random.randint(1, 100)) for _ in range(3)) + "]",
            "list",
        )
    elif chosen_type == "dict":
        keys = [
            '"' + "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=5)) + '"'
            for _ in range(3)
        ]
        values = [str(random.randint(1, 100)) for _ in range(3)]
        return "{" + ", ".join(f"{k}: {v}" for k, v in zip(keys, values)) + "}", "dict"
    elif chosen_type == "tuple":
        return (
            "(" + ", ".join(str(random.randint(1, 100)) for _ in range(3)) + ")",
            "tuple",
        )
    elif chosen_type == "exception":
        exceptions = ["ValueError", "TypeError", "IndexError", "KeyError", "Exception"]
        return random.choice(exceptions), "exception"


def find_placeholders(code_or_json):
    """Find unique placeholders in the code or JSON"""
    placeholders = set(re.findall(r"<value\d+>", code_or_json))
    return sorted(list(placeholders))


def generate_data_type_permutations(placeholders, data_types):
    """Generate unique permutations of data types for the placeholders"""
    if len(placeholders) > len(data_types):
        # If there are more placeholders than data types, use combinations_with_replacement
        return itertools.combinations(data_types, len(placeholders))
    else:
        # Otherwise, use permutations, Avoid this case
        return itertools.permutations(data_types, len(placeholders))


def replace_placeholders_and_generate_json(code, json_template_str, data_type_mapping):
    """Replace placeholders with values for their respective types and update JSON"""
    for placeholder, data_type in data_type_mapping.items():
        value, _ = generate_value_for_type(data_type)
        code = code.replace(placeholder, str(value))

    json_template = json.loads(json_template_str)
    for item in json_template:
        for placeholder, data_type in data_type_mapping.items():
            if placeholder in item["type"]:
                item["type"] = [data_type]

    return code, json_template


def save_files(code, json_data, output_folder, case_name, type_name, case_number):
    """Modified to include case name in the folder path"""
    case_folder = os.path.join(
        output_folder, f"{case_number:03}_{case_name}_{type_name}"
    )
    os.makedirs(case_folder, exist_ok=True)

    code_file_path = os.path.join(case_folder, "main.py")
    json_file_path = os.path.join(case_folder, "main_gt.json")

    with open(code_file_path, "w") as file:
        file.write(code)
    # print(f"Saved Python code to {code_file_path}")

    with open(json_file_path, "w") as file:
        json.dump(json_data, file, indent=4)
    # print(f"Saved JSON ground truth to {json_file_path}")


def read_templates(directory):
    """Read all template files in a directory and return a list of templates"""
    templates = []
    for file_name in os.listdir(directory):
        if file_name.endswith(".txt"):  # Filter only text files
            with open(os.path.join(directory, file_name), "r") as file:
                content = file.read()

            parts = content.split("\n# ")
            name = parts[0].replace("# Name: ", "").strip()
            template_type = parts[1].replace("Type: ", "").strip()
            data_types = parts[2].replace("Data Types: ", "").strip().split(", ")
            code_template = parts[3].split("Python Code Template\n", 1)[1].strip()
            json_template = parts[4].split("JSON Template", 1)[1].strip()
            templates.append(
                (name, template_type, data_types, code_template, json_template)
            )
    return templates


# Example usage
output_folder = f"{SCRIPT_DIR}/generated_dataset"
templates = read_templates(f"{SCRIPT_DIR}/templates")

shutil.rmtree(output_folder, ignore_errors=True)

case_number = 1
total_cases = 1
error_count = 0
for name, template_type, data_types, code_template, json_template in templates:
    if template_type == "Simple":
        # Handling for simple templates
        for data_type in data_types:
            data_type_mapping = {"<value>": data_type}
            replaced_code, json_data = replace_placeholders_and_generate_json(
                code_template, json_template, data_type_mapping
            )
            try:
                result = exec(replaced_code)
            except Exception as e:
                if data_type == "exception":
                    print(
                        "Skipping errror report as the data_type is exception for"
                        f" '{name}_{data_type}'"
                    )
                else:
                    print(f"Error executing script '{name}_{data_type}'")
                    print(f"Error : {e}")
                    error_count += 1
                    continue
            save_files(
                replaced_code,
                json_data,
                output_folder,
                name,
                data_type,
                f"{case_number}_{total_cases}",
            )
            total_cases += 1
    elif template_type == "Complex":
        # Handling for complex templates
        placeholders = find_placeholders(code_template + json_template)
        for data_type_combo in generate_data_type_permutations(
            placeholders, data_types
        ):
            data_type_mapping = {
                ph: dt for ph, dt in zip(placeholders, data_type_combo)
            }
            type_name = "_".join(data_type_combo)
            replaced_code, json_data = replace_placeholders_and_generate_json(
                code_template, json_template, data_type_mapping
            )
            try:
                result = exec(replaced_code)
            except Exception as e:
                if "exception" in type_name:
                    print(
                        "Skipping errror report as the data_type is exception for"
                        f" '{name}_{type_name}'"
                    )
                else:
                    print(f"Error executing script '{name}_{type_name}'")
                    print(f"Error : {e}")
                    error_count += 1
                    continue
            save_files(
                replaced_code,
                json_data,
                output_folder,
                name,
                type_name,
                f"{case_number}_{total_cases}",
            )
            total_cases += 1

    case_number += 1


print(f"\nSummary:")
print(
    f"Genarated {total_cases-1} datasets from {case_number-1} templates and saved to"
    f" {output_folder}"
)
print(f"Scripts with errors: {error_count}")
