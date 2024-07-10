from helpers import read_template, process_file
import os
import shutil
from pathlib import Path

SCRIPT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

output_folder = f"{SCRIPT_DIR}/.scrapy/generated_typeevalpy_dataset"
benchmark_dir = f"{SCRIPT_DIR}/.scrapy/micro-benchmark-autogen-templates"
shutil.rmtree(output_folder, ignore_errors=True)


python_files = sorted(Path(benchmark_dir).rglob("*.py"))
files_analyzed = 0
error_count = 0
for file in python_files:
    try:
        print(file)
        template_data = read_template(file)
        process_file(
            *template_data, str(file.parent).replace(benchmark_dir, ""), output_folder
        )

    except Exception as e:
        print(e)
        pass
