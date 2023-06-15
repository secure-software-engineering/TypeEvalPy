import os
import subprocess
import ast
import json


def list_python_files(folder_path):
    python_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files


def parse_type_hint(node):
    if isinstance(node, ast.Name):
        return node.id
    elif isinstance(node, ast.Subscript):
        return parse_type_hint(node.value)
    elif isinstance(node, ast.Attribute):
        return parse_type_hint(node.value) + "." + node.attr
    elif isinstance(node, ast.Call):
        return parse_type_hint(node.func)
    elif isinstance(node, ast.Constant):
        return node.value
    return None


def parse_pyi_file(pyi_file):
    with open(pyi_file, "r") as file:
        tree = ast.parse(file.read())

    results = []
    current_class = None
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            current_class = node.name
            print(current_class)

        if isinstance(node, ast.FunctionDef):
            function = {
                "file": pyi_file,
                "line_number": node.lineno,
                "function": node.name,
                "type": [],
            }
            results.append(function)

            if current_class:
                function["function"] = f"{current_class}.{node.name}"

            if node.returns:
                return_type = parse_type_hint(node.returns)
                if return_type is not None:
                    function["type"].append(return_type)

            for param in node.args.args:
                parameter = {
                    "file": pyi_file,
                    "line_number": param.lineno,
                    "parameter": param.arg,
                    "function": node.name,
                    "type": [],
                }
                if current_class:
                    function["function"] = f"{current_class}.{node.name}"
                results.append(parameter)

        if isinstance(node, ast.AnnAssign):
            if isinstance(node.annotation, ast.Name):
                variable = {
                    "file": pyi_file,
                    "line_number": node.lineno,
                    "variable": node.target.id,
                    "type": [node.annotation.id],
                }
                results.append(variable)

    return results


def convert_pyi_to_gt_pytype(pyi_file, gt_pytype_file):
    results = parse_pyi_file(pyi_file)
    with open(gt_pytype_file, "w") as file:
        json.dump(results, file, indent=4)


def format_json(gt_file, gt_pytype_file, output_file):
    with open(gt_file, "r") as gt_file:
        gt_data = json.load(gt_file)

    with open(gt_pytype_file, "r") as gt_pytype_file:
        gt_pytype_data = json.load(gt_pytype_file)

    updated_gt_data = []
    for pytype_entry in gt_pytype_data:
        for i, gt_entry in enumerate(gt_data):
            flag = True
            for k in pytype_entry.keys():
                if k not in ["type", "file", "line_number"]:
                    if pytype_entry.get(k) != gt_entry.get(k):
                        flag = False
            if flag:
                gt_data[i]["type"] = pytype_entry["type"]
                updated_gt_data.append(gt_data[i])
                break
    with open(output_file, "w") as output_file:
        json.dump(updated_gt_data, output_file, indent=4)


os.chdir(".")
root_directory = "./micro-benchmark/python_features/functions/default"

# Run `pytype' in the root directory for node installation

python_files = list_python_files(root_directory)
error_count = 0
# Run `pytype` for all files
for file_path in python_files:
    print(file_path)
    dir_path, file_name = os.path.split(file_path)
    pytype_stub = (
        "pytype -k --precise-return  --protocols --strict-parameter-checks"
        f" '{file_name}'"
    )
    try:
        subprocess.run(pytype_stub, shell=True, cwd=dir_path, check=True)
        stub_file = dir_path + "/.pytype/pyi/" + file_name.replace(".py", ".pyi")
        pytype_json_path = file_path.replace(".py", "_pytype.json")
        pytype_final_json_path = file_path.replace(".py", "_pytype_final.json")
        gt_json_path = file_path.replace(".py", "_gt.json")
        convert_pyi_to_gt_pytype(stub_file, pytype_json_path)
        format_json(gt_json_path, pytype_json_path, pytype_final_json_path)
    except Exception as e:
        print(f"Command returned non-zero exit status: {e}")
        error_count += 1
print("Error count", error_count)
