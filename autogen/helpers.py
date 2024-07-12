import itertools
import json
import os
import random
import re
import shutil

from pathlib import Path

SCRIPT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


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
    elif chosen_type == "set":
        return (
            "set(" + ", ".join(str(random.randint(1, 100)) for _ in range(3)) + ")",
            "set",
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
        # make the number of data_types equal to the number of placeholders by duplicating the data_types
        data_types = data_types * (len(placeholders) // len(data_types) + 1)
        data_types = data_types[: len(placeholders)]
        # If there are more placeholders than data types, use combinations_with_replacement
        return itertools.permutations(data_types, len(placeholders))
    else:
        # Otherwise, use permutations
        return itertools.permutations(data_types, len(placeholders))

def get_additional_facts(data_type, item, value):
    # Hard coded based on generate_value_for_type generation
    facts = []
    if data_type in ["list", "tuple", "set"]:
        for i in range(3):
            item_new = item.copy()
            item_new["type"] = ["int"]
            item_new["variable"] = f"{item['variable']}[{i}]"
            facts.append(item_new)
    elif data_type == "dict":
        for k in eval(value).keys():
            item_new = item.copy()
            item_new["type"] = ["int"]
            item_new["variable"] = f"{item['variable']}['{k}']"
            facts.append(item_new)

    return facts


def is_variable_fact(item):
    # TODO: parameter type is not supported yet, although it is a variable fact
    return True if "variable" in item else False

def replace_placeholders_and_generate_json(code, json_template_str, data_type_mapping):
    """Replace placeholders with values for their respective types and update JSON"""
    placeholder_values = {}
    for placeholder, data_type in data_type_mapping.items():
        value, _ = generate_value_for_type(data_type)
        placeholder_values[placeholder] = value
        code = code.replace(placeholder, str(value))

    json_template = json.loads(json_template_str)
    additional_facts = []
    seen_additional_facts = set()

    for item in json_template["ground_truth"]:
        for placeholder, data_type in data_type_mapping.items():
            if placeholder in item["type"]:
                for i in range(len(item["type"])):
                    if item["type"][i] == placeholder:
                        if is_variable_fact(item) and f"{item['variable']}_{item['line_number']}_{item['col_offset']}" not in seen_additional_facts:
                            seen_additional_facts.add(f"{item['variable']}_{item['line_number']}_{item['col_offset']}")
                            if data_type in ["list", "set", "dict", "tuple"]:
                                additional_facts.append(get_additional_facts(data_type, item, placeholder_values[placeholder]))

                        item["type"][i] = data_type


        # make type an unique list
        item["type"] = list(set(item["type"]))


    # merge additional facts with json_template["ground_truth"]
    for facts in additional_facts:
        json_template["ground_truth"] += facts

    # Sort json by line_number
    json_template["ground_truth"] = sorted(json_template["ground_truth"], key=lambda x: x["line_number"])

    return code, json_template


def save_files(
    code, json_data, output_folder, case_name, type_name, case_number, file_path
):
    """Modified to include case name in the folder path"""
    case_folder = output_folder + file_path + "_" + type_name
    os.makedirs(case_folder, exist_ok=True)

    code_file_path = os.path.join(case_folder, f"{case_name}.py")
    json_file_path = os.path.join(case_folder, f"{case_name}_gt.json")

    with open(code_file_path, "w") as file:
        file.write(code)
    # print(f"Saved Python code to {code_file_path}")

    with open(json_file_path, "w") as file:
        json.dump(json_data, file, indent=4)
    # print(f"Saved JSON ground truth to {json_file_path}")


def read_template(file_path):
    """Read template files and return a list of templates"""
    json_template_path = str(file_path).replace(".py", "_gt.json")

    with open(json_template_path, "r") as file:
        content_str = file.read()
        content = json.loads(content_str)

    with open(file_path, "r") as file:
        code_content = file.read()

    name = file_path.stem
    replacement_mode = content["replacement_mode"]
    data_types = content["type_replacements"]
    code_template = code_content
    json_template = content_str

    return name, replacement_mode, data_types, code_template, json_template


def process_file(
    name,
    template_type,
    data_types,
    code_template,
    json_template,
    file_path,
    output_folder,
):
    print(f"Processing file {file_path}")
    case_number = 1
    total_cases = 1
    error_count = 0
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
                file_path,
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
                file_path,
            )
            total_cases += 1

    case_number += 1
