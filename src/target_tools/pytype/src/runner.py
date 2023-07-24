import argparse
import logging
from pathlib import Path
from sys import stdout

import utils
import ast
import json
import os
from pytype import config
from pytype.tools.annotate_ast import annotate_ast

# Create a logger
logger = logging.getLogger("runner")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("/tmp/pytype_log.log")
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler(stdout)
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def list_python_files(folder_path):
    python_files = sorted(Path(folder_path).rglob("*.py"))
    return python_files


def process_file(module, file):
    results = []
    current_class = None
    for node in ast.walk(module):
        if isinstance(node, ast.ClassDef):
            current_class = node.name
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
                    logger.error("Unkown object:", node.id)
                else:
                    logger.error("Unknown node type")
    return results


def main_runner(args):
    python_files = list_python_files(args.bechmark_path)
    error_count = 0
    pytype_options = config.Options.create(python_version=(3, 10))
    for file in python_files:
        try:
            dir_path, file_name = os.path.split(file)
            source = open(file).read()
            module = annotate_ast.annotate_source(source, ast, pytype_options)
            annotations_list = process_file(module, file_name)
            json_file_path = str(file).replace(".py", "_result.json")
            with open(json_file_path, "w") as json_file:
                json.dump(annotations_list, json_file, indent=4)
        except Exception as e:
            logger.info(f"Command returned non-zero exit status: {e} for file: {file}")
            error_count += 1

    logger.info(f"Runner finished with errors:{error_count}")


if __name__ == "__main__":
    is_running_in_docker = utils.is_running_in_docker()
    if is_running_in_docker:
        print("Python is running inside a Docker container")
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--bechmark_path",
            help="Specify the benchmark path",
            default="/tmp/micro-benchmark",
        )

        args = parser.parse_args()
        main_runner(args)
    else:
        print("Python is not running inside a Docker container")
        file_path = ""
        process_file(file_path)
