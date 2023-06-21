import json
import subprocess
import os


def query_pyre(folder_name, attribute):
    print(attribute)
    # Perform Pyre Check query on the attribute
    result = subprocess.run(
        ["pyre", "query", f"type({attribute})"],
        capture_output=True,
        text=True,
        cwd=folder_name,
    )

    # Parse the query result and extract the type information
    try:
        print(result)
        query_output = json.loads(result.stdout)
        attribute_type = query_output["response"]["type"]
        attribute_type = attribute_type.lstrip("typing.")
        print(attribute_type)
        return attribute_type
    except (json.JSONDecodeError, KeyError):
        return None


def analyze_files(file_list):
    type_info = []

    for file_data in file_list:
        file_path = file_data["file"]
        gt_data = file_data["data"]

        directory_name, filename = os.path.split(file_path)
        with open(gt_data, "r") as gt_file:
            attributes = json.load(gt_file)
            pyre_config_file = os.path.join(directory_name, ".pyre_configuration")
            if not os.path.exists(pyre_config_file):
                pyre_init_command = ["pyre", "init"]
                pyre_init_process = subprocess.Popen(
                    pyre_init_command, stdin=subprocess.PIPE, cwd=directory_name
                )
                pyre_init_process.communicate(
                    input="Y\n.\n.\n".encode()
                )  # Provide "Y" and "." as answers to prompts

                # Run `pyre` command
            pyre_command = ["pyre"]
            pyre_process = subprocess.Popen(pyre_command, cwd=directory_name)
            pyre_process.wait()
            for attribute in attributes:
                if "function" in attribute:
                    func = attribute["function"]
                    attribute_type = query_pyre(
                        directory_name, filename.replace(".py", "") + "." + func
                    )
                    if attribute_type:
                        type_info.append(
                            {
                                "file": os.path.basename(filename),
                                "line_number": attribute["line_number"],
                                "function": func,
                                "type": [attribute_type],
                            }
                        )

                if "parameter" in attribute:
                    param = attribute["parameter"]
                    func = attribute["function"]
                    attribute_type = query_pyre(
                        directory_name, f"{filename.replace('.py', '')}.{func}.{param}"
                    )
                    if attribute_type:
                        type_info.append(
                            {
                                "file": os.path.basename(filename),
                                "line_number": attribute["line_number"],
                                "parameter": param,
                                "function": func,
                                "type": [attribute_type],
                            }
                        )

                if "variable" in attribute:
                    variable = attribute["variable"]
                    attribute_type = query_pyre(
                        directory_name, filename.replace(".py", "") + "." + variable
                    )
                    if attribute_type:
                        attribute_type = attribute_type.lstrip(
                            f"{os.path.basename(filename.replace('.py', ''))}."
                        )
                        type_info.append(
                            {
                                "file": os.path.basename(filename),
                                "line_number": attribute["line_number"],
                                "variable": variable,
                                "type": [attribute_type],
                            }
                        )

    return type_info


def generate_json_file(filename, type_info):
    # Generate JSON file with type information
    json_data = json.dumps(type_info, indent=4)
    with open(filename, "w") as file:
        file.write(json_data)


def list_python_files(folder_path):
    python_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files


def pyre_main():
    folder_path = "/tmp/micro-benchmark/python_features"

    python_files = list_python_files(folder_path)

    for python_file in python_files:
        # Analyze the Python file
        try:
            print(python_file)
            gt_file_path = python_file.replace(".py", "_gt.json")

            file_data = {"file": python_file, "data": gt_file_path}
            type_info = analyze_files([file_data])

            # Generate JSON file with type information
            json_filepath = python_file.replace(".py", "_pyre.json")
            print(json_filepath)
            generate_json_file(json_filepath, type_info)
        except Exception as e:
            print(e)


pyre_main()
