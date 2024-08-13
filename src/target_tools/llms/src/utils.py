import json
import os
import re
import shutil
import sys
import yaml

import requests
import logging
import prompts


logger = logging.getLogger("runner")
logger.setLevel(logging.DEBUG)


class JsonException(Exception):
    pass


class TimeoutException(Exception):
    pass


def is_ollama_online(server_url):
    try:
        res = requests.get(server_url)
        # Check if the request was successful
        if res.status_code == 200:
            # Check the content of the response
            if res.text == "Ollama is running":
                return True
        return False
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the request
        print(f"An error occurred: {e}")
        return False


def copy_folder(src, dst):
    """
    Copies a folder from the source (src) to the destination (dst).

    :param src: Source folder path
    :param dst: Destination folder path
    """
    # Check if the source directory exists
    if not os.path.exists(src):
        print(f"Source folder {src} does not exist.")
        return

    # Check if the destination directory exists, if so, remove it
    if os.path.exists(dst):
        shutil.rmtree(dst)
        print(f"Existing folder at {dst} has been removed.")

    # Copy the folder
    shutil.copytree(src, dst, dirs_exist_ok=True)
    print(f"Folder copied from {src} to {dst}")


def is_running_in_docker():
    """Check if Python is running inside a Docker container."""
    return (
        os.path.exists("/.dockerenv")
        or os.environ.get(  # Check if the /.dockerenv file exists
            "DOCKER_CONTAINER", False
        )
        or os.environ.get(  # Check if DOCKER_CONTAINER environment variable is set
            "DOCKER_IMAGE_NAME", False
        )  # Check if DOCKER_IMAGE_NAME environment variable is set
    )


def generate_json_file(filename, type_info):
    # Generate JSON file with type information
    try:
        if isinstance(type_info, list):
            pass
        else:
            type_info = json.loads(type_info)
        is_valid_json = True
    except Exception as e:
        is_valid_json = False
        print(f"Not a valid JSON: {e}")

    json_data = json.dumps(type_info, indent=4)
    with open(filename, "w") as file:
        file.write(json_data)

    return is_valid_json


def generate_json_from_answers(gt_json_file, answers):
    try:
        with open(gt_json_file, "r") as file:
            gt_data = json.load(file)

        pattern = re.compile(r"^\s*(\d+)\.\s+(.+)\s*$", re.MULTILINE)
        parsed_answers = pattern.findall(answers)

        parsed_answers = {int(x) - 1: y for x, y in parsed_answers}
        # if len(gt_data) != len(parsed_answers):
        #     return []

        answers_json_data = []
        for fact in range(len(gt_data)):
            _result = gt_data[fact]
            _result.pop("type")
            if fact in parsed_answers:
                _result["type"] = [x.strip() for x in parsed_answers[fact].split(",")]
                answers_json_data.append(_result)

        return answers_json_data
    except Exception as e:
        print("Error generating json from questions")
        print(e)
        return []


def generate_answers_for_fine_tuning(json_file):
    # Read and parse the JSON file
    with open(json_file, "r") as file:
        data = json.load(file)

    counter = 1
    answers = []
    for fact in data:
        answers.append(f"{counter}. {', '.join(fact['type'])}")
        counter += 1

    return "\n".join(answers)


def generate_questions_from_json(json_file):
    # Read and parse the JSON file
    with open(json_file, "r") as file:
        data = json.load(file)

    questions = []

    for entry in data:
        file = entry["file"]
        line_number = entry["line_number"]
        col_offset = entry["col_offset"]

        # Generate different questions based on the content of each entry
        # Function Return type
        if "function" in entry and "parameter" not in entry and "variable" not in entry:
            question = (
                "What is the return type of the function"
                f" '{entry['function']}' at line {line_number}, column"
                f" {col_offset}?"
            )
        # Function Parameter type
        elif "parameter" in entry:
            question = (
                f"What is the type of the parameter '{entry['parameter']}' at line"
                f" {line_number}, column {col_offset}, within the function"
                f" '{entry['function']}'?"
            )
        # Variable in a function type
        elif "variable" in entry and "function" not in entry:
            question = (
                f"What is the type of the variable '{entry['variable']}' at line"
                f" {line_number}, column {col_offset}?"
            )
        elif "variable" in entry and "function" in entry:
            question = (
                f"What is the type of the variable '{entry['variable']}' at line"
                f" {line_number}, column {col_offset}, within the function"
                f" '{entry['function']}'?"
            )
        else:
            print("ERROR! Type could not be converted to types")
        questions.append(question)

    if len(data) != len(questions):
        print("ERROR! Type questions length does not match json length")
        sys.exit(-1)

    questions = [f"{x}. {y}" for x, y in zip(range(1, len(questions) + 1), questions)]
    return questions


def load_models_config(config_path):
    models_config = {"models": {}, "custom_models": {}}
    with open(config_path, "r") as file:
        config_data = yaml.safe_load(file)
        for model_data in config_data["models"]:
            models_config["models"][model_data["name"]] = model_data
        for model_data in config_data["custom_models"]:
            models_config["custom_models"][model_data["name"]] = model_data

    return models_config


def get_prompt(prompt_id, file_path, answers_placeholders=True, use_system_prompt=True):
    json_filepath = str(file_path).replace(".py", "_gt.json")

    # with open(json_filepath, "r") as file:
    #     data = json.load(file)
    with open(file_path, "r") as file:
        code = file.read()
        # Remove comments from code but keep line number structure
        code = "\n".join(
            [line if not line.startswith("#") else "#" for line in code.split("\n")]
        )

    if prompt_id in [
        "prompt_template_questions_based_2",
    ]:
        questions_from_json = generate_questions_from_json(json_filepath)

        prompt = eval(f"prompts.{prompt_id}")

        prompt_data = {
            "code": code,
            "questions": "\n".join(questions_from_json),
            "answers": (
                "\n".join([f"{x}." for x in range(1, len(questions_from_json) + 1)])
                if answers_placeholders
                else ""
            ),
        }

        if use_system_prompt:
            prompt[1]["content"] = prompt[1]["content"].format(**prompt_data)
        else:
            prompt[0]["content"] = prompt[0]["content"].format(**prompt_data)

    else:
        logger.error("ERROR! Prompt not found!")
        sys.exit(-1)

    return prompt


# Example usage:
# loader = ConfigLoader("models_config.yaml")
# loader.load_config()
# models = loader.get_models()
# for model in models:
#     print(model.name, model.model_path)
