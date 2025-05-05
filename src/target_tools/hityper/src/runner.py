import argparse
import json
import logging
import subprocess
import os
from pathlib import Path
from sys import stdout

import translator
import utils

# Create a logger
logger = logging.getLogger("runner")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("/tmp/hityper_log.log")
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
    base_repo_folder = "/mnt/hf_cache/rashida_manytype4py/many-types-4-py-dataset"
    file_path = os.path.join(base_repo_folder, file_path)
    dir_path, file_name = os.path.split(file_path)
    hitype_cmd = f"hityper infer -s ./{file_name} -p ."
    subprocess.run(
        hitype_cmd,
        shell=True,
        cwd=dir_path,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def main_runner(args):

    with open(args.bechmark_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    # Extract .py files
    python_files = []

    for repo, repo_data in data.items():
        if "src_files" in repo_data:
            python_files.extend(repo_data["src_files"].keys())

    error_count = 0
    error_list = []
    for file in python_files:
        try:
            # logger.debug(file)
            process_file(file)

            # Translate the results into TypeEvalPy format
            translated = translator.translate_content(file)

            json_file_path = str(file).replace(".py", "_result.json")
            with open(json_file_path, "w") as json_file:
                json.dump(translated, json_file, sort_keys=True, indent=4)

        except Exception as e:
            logger.info(f"Command returned non-zero exit status: {e} for file: {file}")
            error_list.append(file)
            error_count += 1

    logger.info(f"Runner finished with errors:{error_count}")
    logger.info("Error files")
    # for file in error_list:
    #    print("\n", file)


if __name__ == "__main__":
    is_running_in_docker = utils.is_running_in_docker()
    if is_running_in_docker:
        print("Python is running inside a Docker container")
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--bechmark_path",
            help="Specify the benchmark path",
            default="repos",
        )

        args = parser.parse_args()
        main_runner(args)
    else:
        print("Python is not running inside a Docker container")

        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--bechmark_path",
            help="Specify the benchmark path",
            default="/home/ssegpu/rashida/TypeEvalPy/src/target_tools/hityper/rw-benchmark/test/test.json",
        )

        args = parser.parse_args()
        main_runner(args)
