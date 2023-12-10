import os
import json


def process_file(file_path):
    with open(file_path, "r") as f:
        return f.read()


def process_json_data(json_data):
    return json.loads(json_data)


def process_folder(folder_path, output_file):
    with open(output_file, "w") as output:
        for root, dirs, files in os.walk(folder_path):
            messages = []

            system_message = {
                "role": "system",
                "content": (
                    "Perform the following tasks: 1. Infer the types of various Python"
                    " elements like function parameters, local variables, and function"
                    " return types with the highest probability. 2. Provide your"
                    " response in a valid JSON array of objects. Do not provide any"
                    " additional information except the JSON object."
                ),
            }
            messages.append(system_message)
            print("Analysing:", root)
            for file_name in files:
                file_path = os.path.join(root, file_name)

                if file_name.endswith(".py"):
                    code = process_file(file_path)
                    user_message = {
                        "role": "user",
                        "content": f"'{file_name}':\n\n```\n{code}\n```",
                    }
                    messages.append(user_message)

                elif file_name.endswith(".json"):
                    assistant_content = process_file(file_path)
                    data = process_json_data(assistant_content)
                    assistant_message = {
                        "role": "assistant",
                        "content": json.dumps(data),
                    }
                    messages.append(assistant_message)

            # Write messages to the output file
            if any(entry.get("role") == "user" for entry in messages):
                output.write(
                    json.dumps({"messages": messages}, separators=(",", ":")) + "\n"
                )


folder_path = "training_set"
output_file = "output.jsonl"
process_folder(folder_path, output_file)
