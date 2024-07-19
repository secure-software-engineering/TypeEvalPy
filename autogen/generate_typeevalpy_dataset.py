from helpers import read_template, process_file, process_import_case
import os
import shutil
from pathlib import Path
import tqdm

SCRIPT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

output_folder = f"{SCRIPT_DIR}/.scrapy/generated_typeevalpy_dataset"
error_folder = f"{SCRIPT_DIR}/.scrapy/error"
benchmark_dir = f"{SCRIPT_DIR}/micro-benchmark-autogen-templates/python_features"
shutil.rmtree(output_folder, ignore_errors=True)
shutil.rmtree(error_folder, ignore_errors=True)


python_files = sorted(Path(benchmark_dir).rglob("*.py"))
files_analyzed = 0
error_count = 0
last_folder = ""
for file in tqdm.tqdm(python_files, desc="Processing files"):
    try:
        # print the folder path if its not the same as the last one
        if str(file.parent.parent.name) != last_folder:
            print(
                f"##################\nProcessing: {file.parent.parent.name}\n##################"
            )
            last_folder = str(file.parent.parent.name)

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
