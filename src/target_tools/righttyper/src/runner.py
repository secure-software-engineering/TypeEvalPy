import argparse
import json
import logging
from pathlib import Path
from sys import stdout

import translator
import utils

# Create a logger
logger = logging.getLogger("runner")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("/tmp/righttyper_log.log")
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler(stdout)
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def list_python_files(folder_path):
    return sorted([
        path
        for path in folder_path.rglob("*.py")
        if (path.parent / (path.stem + "_gt.json")).exists()
    ])


def process_file(file_path, benchmark_path):
    import subprocess
    import sys
    # using Python 3.10 syntax avoids typing.Self, which TypeEvalPy doesn't expect
    subprocess.run(
        [sys.executable, "-m", "righttyper",
         "--no-output-files", "--json-output",
         "--no-sampling", "--use-top-pct=100", "--no-simplify-type-sets",
         "--python-version=3.10",
         "--root", benchmark_path, file_path],
        cwd=file_path.parent,
        check=False,    # many snippets exit with an exception, etc.
    )
    (file_path.parent / "righttyper.log").unlink()


def main_runner(args):
    benchmark_path = Path(args.bechmark_path)
    python_files = list_python_files(benchmark_path)
    error_count = 0
    for file in python_files:
        try:
            logger.info(file)
            # Run the inference here and gather results in /tmp/results
            process_file(file, benchmark_path)
            result_file = file.parent / "righttyper.json"
            with result_file.open("r") as f:
                result = json.load(f)

            # save RightTyper's data
            result_file.rename(file.parent / (file.stem + "_rt.json"))

            # Translate the results into TypeEvalPy format
            translated = translator.process_annotations(result, file.parent, strip_generics=True)

            # Save translated file to the same folder /tmp/results
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
            "--bechmark_path",  # misspelled in the original
            help="Specify the benchmark path",
            default="/tmp/micro-benchmark",
        )

        args = parser.parse_args()
        main_runner(args)
    else:
        print("Python is not running inside a Docker container")
        file_path = ""
        process_file(file_path)
