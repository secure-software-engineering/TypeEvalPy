import argparse
import json
import logging
import multiprocessing
import subprocess
import time
from pathlib import Path
from sys import stdout

import requests
import translator
import utils

# Create a logger
logger = logging.getLogger("runner")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("/tmp/headergen_log.log")
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler(stdout)
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

MAX_RETRY_COUNT = 3


def list_python_files(folder_path):
    python_files = sorted(Path(folder_path).rglob("*.py"))
    return python_files


def process_file(file_path):
    try:
        base_url = "http://0.0.0.0:54068/get_types"
        params = {
            "file_path": str(file_path),
        }
        url = (
            base_url + "?" + "&".join(f"{key}={value}" for key, value in params.items())
        )
        print("Checking in URL:", url)

        response = requests.get(url)

        return response.json()
    except Exception as e:
        logger.info(f"{file_path} failed: {e}")
        raise


def main_runner(args):
    python_files = list_python_files(args.bechmark_path)
    files_analyzed = 0
    error_count = 0
    for file in python_files:
        try:
            logger.info(file)

            inferred = process_file(file)
            inferred = translator.enrich_with_col_offsets(file, inferred)

            json_file_path = str(file).replace(".py", "_result.json")

            with open(json_file_path, "w") as json_file:
                inferred_serializable = inferred
                json.dump(inferred_serializable, json_file, sort_keys=True, indent=4)

        except Exception as e:
            logger.info(f"Command returned non-zero exit status: {e} for file: {file}")
            error_count += 1

        files_analyzed += 1
        logger.info(f"Progress: {files_analyzed}/{len(python_files)}")

    logger.info(f"Runner finished with errors:{error_count}")


def run_headergen_server():
    retry_count = 0
    while retry_count < MAX_RETRY_COUNT:
        try:
            subprocess.run(["headergen", "server"], check=True)
        except Exception as e:
            logger.info(f"Attempt {retry_count+1} failed: {e}")
            retry_count += 1


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

        with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
            server_process = multiprocessing.Process(target=run_headergen_server)
            server_process.start()
            time.sleep(10)

            args = parser.parse_args()
            main_runner(args)

            server_process.terminate()
            server_process.join()

    else:
        print("Python is not running inside a Docker container")
        file_path = "/mnt/Projects/PhD/Research/Student-Thesis/4_type_inference_benchmark(Sam)/git_sources/master-thesis-of-samkutty/.scrapy/micro-benchmark/python_features/args/assigned_call/main.py"
        process_file(file_path)
