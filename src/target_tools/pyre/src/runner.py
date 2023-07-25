import argparse
import logging
from pathlib import Path
from sys import stdout

import json
import subprocess
import os
import translator
import utils

# Create a logger
logger = logging.getLogger("runner")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("/tmp/pyre_log.log")
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


def query_pyre(folder_name, attribute):
    # Perform Pyre Check query on the attribute
    result = subprocess.run(
        ["pyre", "query", f"type({attribute})"],
        capture_output=True,
        text=True,
        cwd=folder_name,
    )

    # Parse the query result and extract the type information
    try:
        query_output = json.loads(result.stdout)
        attribute_type = query_output["response"]["type"]
        attribute_type = attribute_type.lstrip("typing.")
        return attribute_type
    except (json.JSONDecodeError, KeyError):
        return None


def process_file(file_path):
    type_info = []
    pyfile_path = file_path["file"]
    gt_data = file_path["data"]

    directory_name, filename = os.path.split(pyfile_path)
    with open(gt_data, "r") as gt_file:
        attributes = json.load(gt_file)
        pyre_config_file = os.path.join(directory_name, ".pyre_configuration")
        if not os.path.exists(pyre_config_file):
            pyre_init_command = ["pyre", "init"]
            pyre_init_process = subprocess.Popen(
                pyre_init_command,
                stdin=subprocess.PIPE,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
                cwd=directory_name,
            )
            pyre_init_process.communicate(
                input="Y\n.\n.\n".encode()
            )  # Provide "Y" and "." as answers to prompts

        # Run `pyre` command
        pyre_command = ["pyre"]
        pyre_process = subprocess.Popen(
            pyre_command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            cwd=directory_name,
        )
        pyre_process.wait()
        for attribute in attributes:
            if "function" in attribute:
                func = attribute["function"]
                attribute_type = query_pyre(
                    directory_name, filename.replace(".py", "") + "." + func
                )
                if attribute_type:
                    attribute_type = utils.format_type(attribute_type)
                    type_info.append(
                        {
                            "file": os.path.basename(filename),
                            "line_number": attribute["line_number"],
                            "function": func,
                            "type": [attribute_type],
                        }
                    )

            if "parameter" in attribute:
                param = attribute["parameter"]
                func = attribute["function"]
                attribute_type = query_pyre(
                    directory_name, f"{filename.replace('.py', '')}.{func}.{param}"
                )
                if attribute_type:
                    type_info.append(
                        {
                            "file": os.path.basename(filename),
                            "line_number": attribute["line_number"],
                            "parameter": param,
                            "function": func,
                            "type": [attribute_type],
                        }
                    )

            if "variable" in attribute:
                variable = attribute["variable"]
                attribute_type = query_pyre(
                    directory_name, filename.replace(".py", "") + "." + variable
                )
                if attribute_type:
                    attribute_type = attribute_type.lstrip(
                        f"{os.path.basename(filename.replace('.py', ''))}."
                    )
                    type_info.append(
                        {
                            "file": os.path.basename(filename),
                            "line_number": attribute["line_number"],
                            "variable": variable,
                            "type": [attribute_type],
                        }
                    )

    return type_info


def main_runner(args):
    python_files = list_python_files(args.bechmark_path)
    error_count = 0
    for file in python_files:
        try:
            gt_file_path = str(file).replace(".py", "_gt.json")

            file_data = {"file": file, "data": gt_file_path}
            type_info = process_file(file_data)
            json_filepath = str(file).replace(".py", "_result.json")
            utils.generate_json_file(json_filepath, type_info)
            print("Output written to", json_filepath)

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
