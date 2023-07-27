import argparse
import logging
from pathlib import Path
from sys import stdout

import translator
import utils

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
    # TODO: get list of queries lineno, col_offset from the ground truth
    # TODO: Send request for file
    # http://localhost:8088/?file_path=/tmp/micro-benchmark/python_features/args/assigned_call/main.py&lineno=3&col_offset=4&func_name=main

    # _url = "http://0.0.0.0:8088/?file_path={file_path}&lineno={lineno}&col_offset={col_offset}&func_name={func_name}"
    # x = requests.get(
    #     _url.format(
    #         file_path=filename,
    #         lineno=node.lineno - 1,
    #         col_offset=node.end_col_offset - 1,
    #         func_name=func_name,
    #     )
    # )

    utils.parse_python_code(code)
    # Process file here and return results
    pass


def main_runner(args):
    python_files = list_python_files(args.bechmark_path)
    error_count = 0
    for file in python_files:
        try:
            # TODO: Run the inference here and gather results in /tmp/results
            inferred = process_file(file)

            # TODO: Translate the results into TypeEvalPy format
            result_file_path = "<path to file>"
            translated = translator.translate_content(result_file_path)

            # TODO: Save translated file to the same folder /tmp/results

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
        file_path = "/mnt/Projects/PhD/Research/Student-Thesis/4_type_inference_benchmark(Sam)/git_sources/master-thesis-of-samkutty/.scrapy/micro-benchmark/python_features/classes/base_class_calls_child/main.py"
        process_file(file_path)
