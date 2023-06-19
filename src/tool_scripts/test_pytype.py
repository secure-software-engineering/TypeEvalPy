import ast
import json
import subprocess
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
        if hasattr(node, "resolved_type"):
            if isinstance(node, ast.ClassDef):
                current_class = node.name
            if isinstance(node, ast.FunctionDef):
                function = {
                    "file": file,
                    "line_number": node.lineno,
                    "function": node.name,
                    "type": [node.resolved_annotation],
                }
                results.append(function)

                if current_class:
                    function["function"] = f"{current_class}.{node.name}"

                for param in node.args.args:
                    parameter = {
                        "file": file,
                        "line_number": param.lineno,
                        "parameter": param.arg,
                        "function": node.name,
                        "type": [node.resolved_annotation],
                    }
                    if current_class:
                        function["function"] = f"{current_class}.{node.name}"
                    results.append(parameter)

            elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                variable = {
                    "file": file,
                    "line_number": node.lineno,
                    "variable": node.id,
                    "type": [node.resolved_annotation],
                }
                results.append(variable)

    return results


folder_path = "./micro-benchmark/python_features"

python_files = list_python_files(folder_path)
pytype_options = config.Options.create(python_version=(3, 10))
for file in python_files:
    dir_path, file_name = os.path.split(file)
    source = open(file).read()
    module = annotate_ast.annotate_source(source, ast, pytype_options)

    annotations_list = get_annotations_list(module, file_name)
    json_output = json.dumps(annotations_list, indent=4)
    print(json_output)
    json_file_path = file.replace(".py", "_pytype_new.json")

    with open(json_file_path, "w") as json_file:
        json.dump(annotations_list, json_file, indent=4)
