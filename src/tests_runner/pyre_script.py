import os
import subprocess


def list_python_files(folder_path):
    python_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files


root_directory = "/tmps"

# Check if `.pyre_configuration` file exists
pyre_config_file = os.path.join(root_directory, ".pyre_configuration")
if not os.path.exists(pyre_config_file):
    # Run `pyre init` in the root directory
    pyre_init_command = ["pyre", "init"]
    pyre_init_process = subprocess.Popen(
        pyre_init_command, stdin=subprocess.PIPE, cwd=root_directory
    )
    pyre_init_process.communicate(
        input="Y\n.\n.\n".encode()
    )  # Provide "Y" and "." as answers to prompts

    # Run `pyre` command
    pyre_command = ["pyre"]
    pyre_process = subprocess.Popen(pyre_command, cwd=root_directory)
    pyre_process.wait()

python_files = list_python_files(root_directory)

# Run `pyre query` for all files
for file in python_files:
    print(file)

    pyre_output_file = file.replace(".py", "_pyre.json")

    if os.path.exists(pyre_output_file):
        print(f"JSON file already exists: {pyre_output_file}")
        continue

    pyre_query = f"pyre query \"types(path='{file}')\" | jq . > {pyre_output_file}"
    subprocess.run(pyre_query, shell=True, cwd=root_directory, check=True)

    print(f"Pyre JSON file created: {pyre_output_file}")
