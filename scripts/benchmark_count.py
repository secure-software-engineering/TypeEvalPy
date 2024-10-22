import json
import os
from pathlib import Path

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
microbench_folder_path = f"{ROOT_DIR}/autogen_typeevalpy_benchmark"


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
python_features_dir = microbench_folder_path + "/python_features"
pf_overall_annotations = 0
pf_overall_types = 0
overall_functions = 0
overall_params = 0
overall_variables = 0
for cat in sorted(os.listdir(python_features_dir)):
    cat_dir = os.path.join(python_features_dir, cat)
    json_files = [_file for _file in sorted(Path(cat_dir).rglob("*_gt.json"))]

    _a, _t, _, sum_functions, sum_params, sum_variables = get_fact_stats(json_files)

    pf_overall_annotations += _a
    pf_overall_types += _t
    overall_functions += sum_functions
    overall_params += sum_params
    overall_variables += sum_variables
    print(cat, _a, _t, sum_functions, sum_params, sum_variables)

print(pf_overall_annotations, pf_overall_types)
# print names
print("overall_functions", "overall_params", "overall_variables")
print(overall_functions, overall_params, overall_variables)

# analysis_sensitivities
print("\nanalysis_sensitivities")
print(
    "category | Overall annotations | Overall types | Overall functions | overall param"
    " | Overall variables"
)
python_features_dir = microbench_folder_path + "/analysis_sensitivities"
as_overall_annotations = 0
as_overall_types = 0
for cat in sorted(os.listdir(python_features_dir)):
    cat_dir = os.path.join(python_features_dir, cat)
    json_files = [_file for _file in sorted(Path(cat_dir).rglob("*_gt.json"))]

    _a, _t, _, sum_functions, sum_params, sum_variables = get_fact_stats(json_files)

    as_overall_annotations += _a
    as_overall_types += _t

    print(cat, _a, _t, sum_functions, sum_params, sum_variables)

print(as_overall_annotations, as_overall_types)

json_files = [
    _file for _file in sorted(Path(microbench_folder_path).rglob("*_gt.json"))
]
python_files = [_file for _file in sorted(Path(microbench_folder_path).rglob("*.py"))]


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
print(f"Total col_offset in annotations: {total_col}/{total_annotations}")
