import argparse
import json
import os
from pathlib import Path


def list_python_files(folder_path):
    python_files = sorted(Path(folder_path).rglob("*.py"))
    return python_files


def main_runner(args):
    python_files = list_python_files(args.bechmark_path)
    error_count = 0
    for file in python_files:
        try:
            # Run the inference here and gather results in /tmp/results
            pass

        except Exception as e:
            print(f"Command returned non-zero exit status: {e} for file: {file}")
            error_count += 1

    print(f"Runner finished with errors:{error_count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--bechmark_path",
        help="Specify the benchmark path",
        default="/tmp/micro-benchmark",
    )

    args = parser.parse_args()
    main_runner(args)
