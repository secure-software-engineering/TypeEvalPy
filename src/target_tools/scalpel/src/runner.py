import argparse
import json
import logging
import os
from pathlib import Path

from scalpel.typeinfer.typeinfer import TypeInference

# Create a logger
logger = logging.getLogger("runner")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("/tmp/scalpel_log.log")
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def list_python_files(folder_path):
    python_files = sorted(Path(folder_path).rglob("*.py"))
    return python_files


def main_runner(args):
    python_files = list_python_files(args.bechmark_path)
    error_count = 0
    for file in python_files:
        try:
            logger.info(file)
            inferer = TypeInference(name=file, entry_point=file)
            inferer.infer_types()
            inferred = inferer.get_types()
            json_file_path = str(file).replace(".py", "_result.json")

            with open(json_file_path, "w") as json_file:
                inferred_serializable = [
                    {k: list(v) if isinstance(v, set) else v for k, v in d.items()}
                    for d in inferred
                ]
                json.dump(inferred_serializable, json_file, indent=4)
        except Exception as e:
            logger.info(f"Command returned non-zero exit status: {e} for file: {file}")
            error_count += 1

    logger.info(f"Runner finished with errors:{error_count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--bechmark_path",
        help="Specify the benchmark path",
        default="/tmp/micro-benchmark",
    )

    args = parser.parse_args()
    main_runner(args)
