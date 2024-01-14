import argparse
import json
import logging
import multiprocessing
import os
import re
import shutil
import sys
import time
import traceback
from pathlib import Path
from sys import stdout
from typing import List, Optional

import prompts
import translator
import utils
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.llms import Ollama, OpenAI
from langchain.output_parsers import OutputFixingParser, PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain.pydantic_v1 import BaseModel

AUTOFIX_WITH_OPENAI = False
ENABLE_STREAMING = True
REQUEST_TIMEOUT = 60
USE_MULTIPROCESSING_FOR_TERMINATION = True

# Create a logger
logger = logging.getLogger("runner")
logger.setLevel(logging.DEBUG)

if utils.is_running_in_docker():
    file_handler = logging.FileHandler("/tmp/ollama_callgraph_log.log", mode="w")
else:
    file_handler = logging.FileHandler("ollama_callgraph_log.log", mode="w")

file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler(stdout)
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def invoke_llm(llm, prompt, queue):
    try:
        output = llm.invoke(prompt)
        queue.put(output)
    except Exception as e:
        queue.put(e)


def list_python_files(folder_path):
    python_files = sorted(Path(folder_path).rglob("*.py"))
    return python_files


def get_prompt(prompt_id, code_path, json_filepath, answers_placeholders=True):
    # with open(json_filepath, "r") as file:
    #     data = json.load(file)
    with open(code_path, "r") as file:
        code = file.read()
        # Remove comments from code but keep line number structure
        code = "\n".join(
            [line if not line.startswith("#") else "#" for line in code.split("\n")]
        )

    if prompt_id in [
        "questions_based_1",
    ]:
        questions_from_json = utils.generate_questions_from_json(json_filepath)
        prompt_template = eval(f"prompts.{prompt_id}")

        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["code", "questions", "answers"],
        )

        prompt_data = {
            "code": code,
            "questions": "\n".join(questions_from_json),
            "answers": (
                "\n".join([f"{x}." for x in range(1, len(questions_from_json) + 1)])
                if answers_placeholders
                else ""
            ),
        }
    else:
        logger.error("ERROR! Prompt not found!")
        sys.exit(-1)

    _input = prompt.format_prompt(**prompt_data)

    return _input.to_string()


def process_file(file_path, prompt_id):
    file_start_time = time.time()
    try:
        code_filepath = os.path.join(file_path, "main.py")
        json_filepath = os.path.join(file_path, "callgraph.json")
        result_filepath = os.path.join(file_path, f"main_result.json")
        result_dump_filepath = os.path.join(file_path, f"prompt_response_dump.txt")

        prompt = get_prompt(prompt_id, code_filepath, json_filepath)

        with open(result_dump_filepath, "w") as file:
            file.write(prompt)

    except Exception as e:
        # traceback.print_exc()
        logger.error(f"{code_filepath} failed: {e}")
        raise

    # TODO: Improve the way this is done. Some plugin based design.
    # if prompt_id in ["questions_based_1"]:
    #     translated_json = utils.generate_json_from_answers(json_filepath, output)
    # else:
    #     translated_json = output

    # is_valid_json = utils.generate_json_file(result_filepath, translated_json)
    # if not is_valid_json:
    #     logger.info(f"{code_filepath} failed: Not a valid JSON")
    #     raise utils.JsonException("json")


def main_runner():
    # Create result folder for model specific results
    bechmark_path = Path("snippets")

    for cat in sorted(os.listdir(bechmark_path)):
        if cat in ["context_sensitive", "external", "task_test"]:
            continue

        print("Iterating category {}...".format(cat))
        files_analyzed = 0

        tests = os.listdir(os.path.join(bechmark_path, cat))
        for test in tests:
            print(f"Running {test}...")
            file = os.path.join(bechmark_path, cat, test)
            process_file(file, "questions_based_1")


if __name__ == "__main__":
    main_runner()
