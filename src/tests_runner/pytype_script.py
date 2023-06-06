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
root_directory = "./micro-benchmark"

# Run `pyright' in the root directory for node installation

python_files = list_python_files(root_directory)

# Run `pyright` for all files
for file_path in python_files:
    print(file_path)
    dir_path, file_name = os.path.split(file_path)
    pyright_stub = (
        "pytype -k --precise-return  --protocols --strict-parameter-checks"
        f" '{file_name}'"
    )
    subprocess.run(pyright_stub, shell=True, cwd=dir_path, check=True)
