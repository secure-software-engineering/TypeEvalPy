import os
import subprocess


def list_python_files(folder_path):
    python_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files


os.chdir("/tmp")
root_directory = "./micro-benchmark/python_features"

# Run `pytype' in the root directory for node installation

python_files = list_python_files(root_directory)
error_count = 0
# Run `pytype` for all files
for file_path in python_files:
    print(file_path)
    dir_path, file_name = os.path.split(file_path)
    pytype_stub = (
        "pytype -k --precise-return  --protocols --strict-parameter-checks"
        f" '{file_name}'"
    )
    try:
        subprocess.run(pytype_stub, shell=True, cwd=dir_path, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command returned non-zero exit status: {e.returncode}")
        error_count += 1
