import json


def parse_main_txt(file_path):
    result_list = []
    with open(file_path, "r") as file:
        lines = file.readlines()

    for line in lines:
        parts = line.strip().split(" - Location: ")
        attribute_info = parts[0]
        location = int(parts[1])

        if "->" in attribute_info:
            function_info = attribute_info.split("->")
            function_name = function_info[0]
            return_type = function_info[1]
            result_list.append(
                {
                    "file": "main.py",
                    "line_number": location,
                    "function": function_name,
                    "type": [return_type],
                }
            )
        else:
            attribute_name, attribute_type = attribute_info.split(":")
            result_list.append(
                {
                    "file": "main.py",
                    "line_number": location,
                    "variable": attribute_name,
                    "type": [attribute_type],
                }
            )

    return result_list


def main():
    input_file = "/tmp/micro-benchmark/python_features/classes/abstract_class/main.txt"
    output_file = (
        "/tmp/micro-benchmark/python_features/classes/abstract_class/results.json"
    )

    parsed_data = parse_main_txt(input_file)

    with open(output_file, "w") as outfile:
        json.dump(parsed_data, outfile, indent=4)


if __name__ == "__main__":
    main()
