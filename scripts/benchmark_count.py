import json
from pathlib import Path

microbench_folder_path = "../micro-benchmark/"

json_files = [_file for _file in sorted(Path(microbench_folder_path).rglob("*.json"))]
python_files = [_file for _file in sorted(Path(microbench_folder_path).rglob("*.py"))]

total_annotations = 0
total_types = 0
for json_file in json_files:
    with open(json_file, "r") as f:
        data = json.load(f)
        total_annotations += len(data)
        for _t in data:
            total_types += len(_t["type"])

print(f"Total Python files: {len(python_files)}")
print(f"Total annotations: {total_annotations}")
print(f"Total types in annotations: {total_types}")
