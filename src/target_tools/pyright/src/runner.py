import argparse
import logging
from pathlib import Path
from sys import stdout
import subprocess
import threading
import time

import translator
import utils
import json
import requests

# Create a logger
logger = logging.getLogger("runner")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("/tmp/pyright_log.log")
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


def process_file(file_path):
    json_filepath = str(file_path).replace(".py", "_gt.json")
    result_filepath = str(file_path).replace(".py", "_result.json")
    file_result = []
    base_url = "http://localhost:8088/"
    params = {
        "file_path": str(file_path),
        "lineno": 0,
        "col_offset": 0,
        "func_name": "",
    }
    with open(json_filepath, "r") as file:
        data = json.load(file)
    for entry in data:
        if "line_number" in entry:
            params["lineno"] = entry["line_number"] - 1
        if "col_offset" in entry:
            params["col_offset"] = entry["col_offset"] - 1
        if "function" in entry:
            params["func_name"] = entry["function"]
        url = (
            base_url + "?" + "&".join(f"{key}={value}" for key, value in params.items())
        )
        print("Checking in URL:", url)

        response = requests.get(url)
        hover_result = response.json()
        file_result.append(hover_result)

    utils.generate_json_file(result_filepath, file_result)

    # utils.parse_python_code(code)
    # Process file here and return results
    pass


def run_pyright_client():
    subprocess.run(["python", "/tmp/src/pyright_client.py"], check=True)


def main_runner(args):
    python_files = list_python_files(args.bechmark_path)
    server_thread = threading.Thread(target=run_pyright_client)
    server_thread.start()
    time.sleep(10)
    error_count = 0
    for file in python_files:
        try:
            print("\n Type checking for file :", file)
            inferred = process_file(file)
        except Exception as e:
            logger.info(f"Command returned non-zero exit status: {e} for file: {file}")
            error_count += 1
    server_thread.join()
    logger.info(f"Runner finished with errors:{error_count}")


if __name__ == "__main__":
    is_running_in_docker = utils.is_running_in_docker()
    if is_running_in_docker:
        print("Python is running inside a Docker container")
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--bechmark_path",
            help="Specify the benchmark path",
            default="/tmp/micro-benchmark/",
        )

        args = parser.parse_args()
        main_runner(args)
    else:
        print("Python is not running inside a Docker container")
        file_path = "/mnt/Projects/PhD/Research/Student-Thesis/4_type_inference_benchmark(Sam)/git_sources/master-thesis-of-samkutty/.scrapy/micro-benchmark/python_features/classes/base_class_calls_child/main.py"
        process_file(file_path)
