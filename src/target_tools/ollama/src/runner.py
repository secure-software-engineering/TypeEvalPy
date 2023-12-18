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


class TypeEvalPySchema(BaseModel):
    file: str
    line_number: int
    type: List[str]
    function: Optional[str] = None
    parameter: Optional[str] = None
    variable: Optional[str] = None


PROMPTS_MAP = {
    "json_based_1": prompts.json_based_1,
    "json_based_2": prompts.json_based_2,
    "questions_based_1": prompts.questions_based_1,
    "questions_based_2": prompts.questions_based_2,
    "questions_based_3": prompts.questions_based_3,
    "questions_based_4": prompts.questions_based_4,
}

# Create a logger
logger = logging.getLogger("runner")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("/tmp/ollama_log.log", mode="w")
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
        "questions_based_2",
        "questions_based_3",
        "questions_based_4",
    ]:
        questions_from_json = utils.generate_questions_from_json(json_filepath)

        prompt = PromptTemplate(
            template=PROMPTS_MAP[prompt_id],
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
    elif prompt_id in ["json_based_1", "json_based_2"]:
        parser = PydanticOutputParser(pydantic_object=TypeEvalPySchema)

        prompt = PromptTemplate(
            template=PROMPTS_MAP[prompt_id],
            input_variables=["code", "filename"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        prompt_data = {"code": code, "filename": Path(code_path).name}
    else:
        logger.error("ERROR! Prompt not found!")
        sys.exit(-1)

    _input = prompt.format_prompt(**prompt_data)

    return _input.to_string()


def process_file(file_path, llm, openai_llm, prompt_id):
    try:
        json_filepath = str(file_path).replace(".py", "_gt.json")
        result_filepath = str(file_path).replace(".py", f"_result.json")

        if USE_MULTIPROCESSING_FOR_TERMINATION:
            # Queue for communication between processes
            queue = multiprocessing.Queue()

            # Create a process for llm.invoke
            process = multiprocessing.Process(
                target=invoke_llm,
                args=(llm, get_prompt(prompt_id, file_path, json_filepath), queue),
            )
            process.start()

            # Wait for the process to finish with a timeout (e.g., 60 seconds)
            process.join(timeout=REQUEST_TIMEOUT)

            if process.is_alive():
                logger.info(f"Timeout occurred for {file_path}")
                process.terminate()  # Terminate the process if it's still running
                process.join()
                logger.info(f"{file_path} failed: Not a valid JSON")
                raise utils.TimeoutException("json")

            result = queue.get_nowait()

            if isinstance(result, Exception):
                raise result

            output = result
        else:
            output = llm.invoke(get_prompt(prompt_id, file_path, json_filepath))

        if isinstance(llm, ChatOpenAI):
            output = output.content

        # TODO: Include this in langchain pipeline
        output = re.sub(r"```json", "", output)
        output = re.sub(r"```", "", output)

        if AUTOFIX_WITH_OPENAI:
            new_parser = OutputFixingParser.from_llm(parser=parser, llm=openai_llm)
            output = new_parser.parse(output)

    except Exception as e:
        # traceback.print_exc()
        logger.error(f"{file_path} failed: {e}")
        raise

    logger.info(output)

    # TODO: Improve the way this is done. Some plugin based design.
    if prompt_id in ["questions_based_2", "questions_based_3", "questions_based_4"]:
        answers_json = utils.generate_json_from_answers(json_filepath, output)
        translated_json = translator.translate_content(answers_json)
    else:
        translated_json = translator.translate_content(output)

    is_valid_json = utils.generate_json_file(result_filepath, translated_json)
    if not is_valid_json:
        logger.info(f"{file_path} failed: Not a valid JSON")
        raise utils.JsonException("json")


def main_runner(args):
    model_name = "text-davinci-003"
    temperature = 0.0
    openai_llm = OpenAI(
        model_name=model_name, temperature=temperature, openai_api_key=args.openai_key
    )
    runner_start_time = time.time()
    for model in args.ollama_models:
        error_count = 0
        timeout_count = 0
        json_count = 0
        files_analyzed = 0

        # Create result folder for model specific results
        bechmark_path = Path(args.bechmark_path)
        results_src = bechmark_path
        if args.results_dir is None:
            results_dst = bechmark_path.parent / model / bechmark_path.name
        else:
            results_dst = Path(args.results_dir) / model / bechmark_path.name
            os.makedirs(results_dst, exist_ok=True)

        utils.copy_folder(results_src, results_dst)

        python_files = list_python_files(results_dst)

        if not model.startswith(("gpt-", "ft:gpt-")):
            if utils.is_ollama_online(args.ollama_url):
                logger.info("Ollama is online!")
            else:
                logger.error("Ollama server is not online!!!")
                sys.exit(-1)

        for file in python_files:
            # Recreating llm object each iteration since we might force terminate in thread
            # Maybe there is another better way to do this
            if model.startswith(("gpt-", "ft:gpt-")):
                # OpenAI models
                if "instruct" in model:
                    llm = OpenAI(
                        model_name=model,
                        temperature=temperature,
                        openai_api_key=args.openai_key,
                    )
                else:
                    llm = ChatOpenAI(
                        model_name=model,
                        temperature=temperature,
                        openai_api_key=args.openai_key,
                    )

            else:
                llm = Ollama(
                    model=model,
                    callback_manager=(
                        CallbackManager([StreamingStdOutCallbackHandler()])
                        if ENABLE_STREAMING
                        else None
                    ),
                    temperature=temperature,
                    timeout=REQUEST_TIMEOUT,
                )
                llm.base_url = args.ollama_url

            prompt_start_time = time.time()
            try:
                logger.info(file)
                logger.info(model)
                process_file(file, llm, openai_llm, args.prompt_id)

            except Exception as e:
                logger.info(
                    f"Command returned non-zero exit status: {e} for file: {file}"
                )
                error_count += 1
                if isinstance(e, utils.JsonException):
                    json_count += 1
                elif isinstance(e, utils.TimeoutException):
                    timeout_count += 1

            files_analyzed += 1
            logger.info(
                f"\n\nProgress: {files_analyzed}/{len(python_files)} | Total Errors /"
                f" JSON Errors / Timeouts: {error_count},{json_count},{timeout_count} |"
                f" PromptTime: {time.time()-prompt_start_time}\n\n"
            )

        logger.info(
            f"Model {model} finished in {time.time()-runner_start_time:.2f} seconds"
        )
        logger.info("Running translator")
        translator.main_translator(results_dst)

    logger.info(
        f"Runner finished in {time.time()-runner_start_time:.2f} seconds, with errors:"
        f" {error_count} | JSON errors: {json_count}"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--bechmark_path",
        help="Specify the benchmark path",
        default="/tmp/micro-benchmark",
    )

    parser.add_argument(
        "--results_dir",
        help="Specify the benchmark path",
        default=None,
    )

    parser.add_argument(
        "--ollama_url", help="Specify the ollama server url", required=True
    )

    parser.add_argument("--prompt_id", help="Specify the prompt ID", required=True)

    parser.add_argument(
        "--ollama_models",
        nargs="+",
        type=str,
        help="Space-separated list of ollama models",
        required=True,
    )

    parser.add_argument("--openai_key", help="Openai API key", required=True)

    args = parser.parse_args()
    main_runner(args)
