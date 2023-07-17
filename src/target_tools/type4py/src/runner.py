import argparse
import json
import logging
from pathlib import Path
from sys import stdout

import requests
import translator
import utils

# Create a logger
logger = logging.getLogger("runner")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("/tmp/type4py_log.log")
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler(stdout)
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

API_URL = "http://localhost:5010/api/predict?tc=0"


def list_python_files(folder_path):
    python_files = sorted(Path(folder_path).rglob("*.py"))
    return python_files


def parse_type_prediction(pred: list[list]) -> str:
    if pred:
        return pred[0][0]
    else:
        return "Unknown"


def process_file(file_path):
    # Process file here and return results
    with open(file_path) as f:
        code = f.read()
        response = requests.post(API_URL, code, verify=False)

    data = response.json()

    if data.get("error") is not None:
        logger.error(data["error"])
        output = []
    else:
        output = data

    return output


def main_runner(args):
    python_files = list_python_files(args.bechmark_path)
    error_count = 0
    for file in python_files:
        try:
            logger.info(file)
            inferred = process_file(file)

            translated = translator.translate_content(inferred)

            json_file_path = str(file).replace(".py", "_result.json")

            with open(json_file_path, "w") as json_file:
                json.dump(translated, json_file, indent=4)

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
        API_URL = "https://type4py.com/api/predict?tc=0"
        print("Python is not running inside a Docker container")
        file_path = "/mnt/Projects/PhD/Research/Student-Thesis/4_type_inference_benchmark(Sam)/git_sources/master-thesis-of-samkutty/micro-benchmark/python_features/returns/multiple_types/main.py"
        inferred = process_file(file_path)
        translated = translator.translate_content(inferred)
