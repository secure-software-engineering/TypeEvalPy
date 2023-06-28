import ast
import json
import os
from pytype import config
from pytype.tools.annotate_ast import annotate_ast


def list_python_files(folder_path):
    python_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files


def get_annotations_list(module, file):
    results = []
    current_class = None
    for node in ast.walk(module):
        if isinstance(node, ast.ClassDef):
            current_class = node.name
            # print(current_class)
        if hasattr(node, "resolved_type"):
            if isinstance(node, ast.FunctionDef):
                function = {
                    "file": file,
                    "line_number": node.lineno,
                    "function": node.name,
                    "type": [node.resolved_annotation],
                }
                if current_class:
                    function["function"] = f"{current_class}.{node.name}"
                results.append(function)
                for param in node.args.args:
                    parameter = {
                        "file": file,
                        "line_number": param.lineno,
                        "parameter": param.arg,
                        "function": node.name,
                        "type": [param.annotation],
                    }
                    if current_class:
                        function["function"] = f"{current_class}.{node.name}"
                    results.append(parameter)
            elif isinstance(node, ast.Attribute):
                print(node.attr)
                attribute = {
                    "file": file,
                    "line_number": node.lineno,
                    "variable": node.attr,
                    "type": [node.resolved_annotation],
                }
                if current_class:
                    attribute["variable"] = f"{current_class}.{node.attr}"
                results.append(attribute)

            elif isinstance(node, ast.Name):
                variable = {
                    "file": file,
                    "line_number": node.lineno,
                    "variable": node.id,
                    "type": [node.resolved_annotation],
                }
                results.append(variable)
            else:
                if hasattr(node, "id"):
                    print("Unkown object:", node.id)
                else:
                    print("Unknown node type")
    return results


os.chdir("/tmp")
folder_path = "./micro-benchmark"

python_files = list_python_files(folder_path)
pytype_options = config.Options.create(python_version=(3, 10))
error_count = 0
for file in python_files:
    try:
        print(file)
        dir_path, file_name = os.path.split(file)
        source = open(file).read()
        module = annotate_ast.annotate_source(source, ast, pytype_options)
        annotations_list = get_annotations_list(module, file_name)
        json_output = json.dumps(annotations_list, indent=4)
        # print(json_output)
        json_file_path = file.replace(".py", "_pytype_new.json")
        # print(json_file_path)
        with open(json_file_path, "w") as json_file:
            json.dump(annotations_list, json_file, indent=4)
    except Exception as e:
        print(e)
        error_count += 1
