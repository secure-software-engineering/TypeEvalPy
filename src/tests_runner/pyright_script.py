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
for file in python_files:
    print(file)
    module_name = file.replace(".py", "")
    module_name = module_name.replace("./micro-benchmark", "micro-benchmark")
    pyright_stub = f"pyright --createstub '{module_name}'"
    subprocess.run(pyright_stub, shell=True, check=True)
