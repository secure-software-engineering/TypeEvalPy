import os
import json


from jedi_type_inference import TypeInferenceJedi


def list_python_files(folder_path):
    python_files = []
    for root, Readme, files in os.walk(os.path.abspath(folder_path)):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files


folder_path = "/tmp/micro-benchmark/python_features"

python_files = list_python_files(folder_path)
print(python_files)
error_count = 0
for file in python_files:
    try:
        print(file)
        inferer = TypeInferenceJedi(name=file, entry_point=file)
        inferer.infer_types()
        inferred = inferer.get_types()
        print(inferred)
        json_file_path = file.replace(".py", "_jedi.json")

        if os.path.exists(json_file_path):
            print(f"JSON file already exists: {json_file_path}")
            continue

        with open(json_file_path, "w") as json_file:
            inferred_serializable = [
                {k: list(v) if isinstance(v, set) else v for k, v in d.items()}
                for d in inferred
            ]
            json.dump(inferred_serializable, json_file, indent=4)
    except Exception as e:
        print(f"Command returned non-zero exit status: {e}")
        error_count += 1
