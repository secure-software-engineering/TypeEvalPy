from helpers import read_template, process_file, process_import_case
import os
import shutil
from pathlib import Path

SCRIPT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

output_folder = f"{SCRIPT_DIR}/.scrapy/test/"
benchmark_dir = (
    f"{SCRIPT_DIR}/.scrapy/micro-benchmark-autogen-templates/python_features"
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
            # ignore if not main.py
            if file.name != "main.py":
                print(f">> Ignoring: {file}")
                continue

            template_data = read_template(file)
            if template_data["replacement_mode"] == "Imports":
                process_import_case(
                    name=template_data["name"],
                    data_types=template_data["data_types"],
                    code_template=template_data["code_template"],
                    json_template=template_data["json_template"],
                    file_path=str(file.parent).replace(benchmark_dir, ""),
                    file_parent=str(file.parent),
                    output_folder=output_folder,
                )
            else:
                process_file(
                    name=template_data["name"],
                    data_types=template_data["data_types"],
                    code_template=template_data["code_template"],
                    json_template=template_data["json_template"],
                    file_path=str(file.parent).replace(benchmark_dir, ""),
                    output_folder=output_folder,
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
