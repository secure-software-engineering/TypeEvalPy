from helpers import read_template, process_file
import os
import shutil
from pathlib import Path

SCRIPT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

output_folder = f"{SCRIPT_DIR}/.scrapy/test/test"
benchmark_dir = (
    f"{SCRIPT_DIR}/micro-benchmark-autogen-templates/python_features/builtins/functools"
)
shutil.rmtree(f"{SCRIPT_DIR}/.scrapy/test", ignore_errors=True)
file = Path(
    "/home/ashwin/TypeEvalPy_AutoBench/micro-benchmark-autogen-templates/python_features/builtins/map/main.py"
)


def call_files():
    python_files = sorted(Path(benchmark_dir).rglob("*.py"))
    files_analyzed = 0
    error_count = 0
    for file in python_files:
        try:
            print(file)
            template_data = read_template(file)
            process_file(
                *template_data,
                str(file.parent).replace(benchmark_dir, ""),
                output_folder,
            )

        except Exception as e:
            print(e)
            pass


def call_file():
    template_data = read_template(file)
    process_file(
        *template_data, str(file.parent).replace(benchmark_dir, ""), output_folder
    )


# call_file()
call_files()
