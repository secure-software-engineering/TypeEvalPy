import argparse
import logging
from pathlib import Path
from sys import stdout

import subprocess
import translator
import utils
import json

# Create a logger
logger = logging.getLogger("runner")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("/tmp/<tool_name>_log.log")
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


def pysonar2_runner(directory):
    directory_name = "/app/pysonar2"
    pysonar2_command = [
        "java",
        "-jar",
        "target/pysonar-2.1.3.jar",
        f"{directory}",
        f"{directory}",
    ]
    pysonar2_process = subprocess.Popen(pysonar2_command, cwd=directory_name)
    pysonar2_process.wait()


def main_runner(args):
    python_files = list_python_files(args.bechmark_path)
    error_count = 0
    pysonar2_runner(args.bechmark_path)
    for file in python_files:
        try:
            translated = translator.translate_content(file)
            result_file_path = str(file).replace(".py", "_result.json")
            with open(result_file_path, "w") as json_file:
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
        print("Python is not running inside a Docker container")
