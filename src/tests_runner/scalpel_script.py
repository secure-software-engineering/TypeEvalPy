import json
import os

from scalpel.typeinfer.typeinfer import TypeInference


def list_python_files(folder_path):
    python_files = []
    for root, files in os.walk(os.path.abspath(folder_path)):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files


folder_path = "/tmp/micro-benchmark/"

python_files = list_python_files(folder_path)

for file in python_files:
    print(file)
    inferer = TypeInference(name=file, entry_point=file)
    inferer.infer_types()
    inferred = inferer.get_types()
    print(inferred)
    json_file_path = file.replace(".py", "_scalpel.json")

    if os.path.exists(json_file_path):
        print(f"JSON file already exists: {json_file_path}")
        continue

    with open(json_file_path, "w") as json_file:
        inferred_serializable = [
            {k: list(v) if isinstance(v, set) else v for k, v in d.items()}
            for d in inferred
        ]
        json.dump(inferred_serializable, json_file, indent=4)
