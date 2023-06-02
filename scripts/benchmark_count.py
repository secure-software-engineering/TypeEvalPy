import json
from pathlib import Path

microbench_folder_path = "../micro-benchmark/python_features"

json_files = [_file for _file in sorted(Path(microbench_folder_path).rglob("*.json"))]
python_files = [_file for _file in sorted(Path(microbench_folder_path).rglob("*.py"))]

total_data_length = 0
for json_file in json_files:
    with open(json_file, "r") as f:
        data = json.load(f)
        total_data_length += len(data)

print(f"Total Python files: {len(python_files)}")
print(f"Total type annotations: {total_data_length}")
