from helpers import read_template, process_file, process_import_case
import os
import shutil
from pathlib import Path
import tqdm
import time
import json
import datetime

ROOT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

output_folder = (
    f"{ROOT_DIR}/autogen/data/autogen_typeevalpy_benchmark_{formatted_datetime}"
)
error_folder = f"{ROOT_DIR}/.scrapy/error"
benchmark_dir = f"{ROOT_DIR}/micro-benchmark-autogen-templates"
shutil.rmtree(output_folder, ignore_errors=True)
shutil.rmtree(error_folder, ignore_errors=True)


python_files = sorted(Path(benchmark_dir).rglob("*.py"))
files_analyzed = 0
error_count = 0
last_folder = ""
start_time = time.time()
total_start_time = time.time()
for file in tqdm.tqdm(python_files, desc="Processing files"):
    try:
        # print the folder path if its not the same as the last one
        if str(file.parent.parent.name) != last_folder:
            if last_folder:
                print(
                    f"Time taken for {last_folder}: {time.time() - start_time} seconds"
                )
            print(
                f"##################\nProcessing: {file.parent.parent.name}\n##################"
            )
            last_folder = str(file.parent.parent.name)
            start_time = time.time()

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


def get_fact_stats(json_files):
    total_annotations = 0
    total_types = 0
    total_col = 0
    rows = []
    sum_functions = 0
    sum_params = 0
    sum_variables = 0
    sum_empty_out_types = 0
    sum_non_empty_out_types = 0
    for json_file in json_files:
        with open(json_file, "r") as f:
            data = json.load(f)
            total_annotations += len(data)
            merged_cell = json_file
            for _t in data:
                total_types += len(_t["type"])
                if _t.get("col_offset"):
                    total_col += 1
                line_number = _t.get("line_number", "")
                function = _t.get("function", "")
                param = _t.get("parameter", "")
                variable = _t.get("variable", "")
                types = ", ".join(_t.get("type", []))
                rows.append(
                    [
                        merged_cell,
                        line_number,
                        function,
                        param,
                        variable,
                        types,
                    ]
                )
                if function:
                    if not param and not variable:
                        sum_functions += 1

                if param:
                    sum_params += 1

                if variable:
                    sum_variables += 1

    return (
        total_annotations,
        total_types,
        total_col,
        sum_functions,
        sum_params,
        sum_variables,
    )


# python_features
print("python_features")
print(
    "category | Overall annotations | Overall types | Overall functions | overall param"
    " | Overall variables"
)
python_features_dir = output_folder + "/python_features"
pf_overall_annotations = 0
pf_overall_types = 0
for cat in sorted(os.listdir(python_features_dir)):
    cat_dir = os.path.join(python_features_dir, cat)
    json_files = [_file for _file in sorted(Path(cat_dir).rglob("*_gt.json"))]

    _a, _t, _, sum_functions, sum_params, sum_variables = get_fact_stats(json_files)

    pf_overall_annotations += _a
    pf_overall_types += _t

    print(cat, _a, _t, sum_functions, sum_params, sum_variables)

print(pf_overall_annotations, pf_overall_types)

json_files = [_file for _file in sorted(Path(output_folder).rglob("*_gt.json"))]
python_files = [_file for _file in sorted(Path(output_folder).rglob("*.py"))]

print("\nOverall")
total_annotations = 0
total_types = 0
total_col = 0
for json_file in json_files:
    with open(json_file, "r") as f:
        data = json.load(f)
        total_annotations += len(data)
        for _t in data:
            total_types += len(_t["type"])
            if _t.get("col_offset"):
                total_col += 1


print(f"Total Python files: {len(python_files)}")
print(f"Total annotations: {total_annotations}")
print(f"Total types in annotations: {total_types}")

print(f"Total time taken: {time.time() - total_start_time} seconds")
