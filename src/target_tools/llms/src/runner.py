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
import vllm_helpers
from vllm import LLM, SamplingParams
from vllm.lora.request import LoRARequest
import gc
import torch


AUTOFIX_WITH_OPENAI = False
REQUEST_TIMEOUT = 60
USE_MULTIPROCESSING_FOR_TERMINATION = True
MAX_TOKENS = 64
TEMPARATURE = 0.001

PROMPTS_MAP = {
    "json_based_1": prompts.json_based_1,
    "json_based_2": prompts.json_based_2,
    "questions_based_1": prompts.questions_based_1,
    "questions_based_2": prompts.questions_based_2,
    "questions_based_3": prompts.questions_based_3,
    "questions_based_4": prompts.questions_based_4,
    "questions_based_2_ft": prompts.questions_based_2_ft,
}

# Create a logger
logger = logging.getLogger("runner")
logger.setLevel(logging.DEBUG)

if utils.is_running_in_docker():
    file_handler = logging.FileHandler("/tmp/ollama_log.log", mode="w")
else:
    file_handler = logging.FileHandler("ollama_log.log", mode="w")

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
    python_files = sorted(Path(folder_path).rglob("main.py"))
    return python_files


def process_file(file_path, llm, openai_llm, prompt_id):
    file_start_time = time.time()
    try:
        json_filepath = str(file_path).replace(".py", "_gt.json")
        result_filepath = str(file_path).replace(".py", f"_result.json")
        result_dump_filepath = str(file_path).replace(".py", f"_result_dump.txt")

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

        with open(result_dump_filepath, "w") as file:
            file.write(output)

        # TODO: Include this in langchain pipeline
        output = re.sub(r"```json", "", output)
        output = re.sub(r"```", "", output)

        if AUTOFIX_WITH_OPENAI:
            new_parser = OutputFixingParser.from_llm(parser=parser, llm=openai_llm)
            output = new_parser.parse(output)

        logger.info(
            "File processed for model"
            f" {llm.model if getattr(llm, 'model', False) else llm.model_name} finished"
            f" in: {time.time()-file_start_time:.2f}"
        )

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


def model_evaluation_vllm(
    model_name,
    prompt_template,
    python_files,
    engine,
    results_dst,
    use_system_prompt=False,
    lora_request=None,
    sampling_params=None,
):

    results_dump_file = results_dst / f"{model_name}_results_dump.csv"

    id_mapping = {
        idx: {
            "file_path": file_path,
            "json_filepath": str(file_path).replace(".py", "_gt.json"),
            "result_filepath": str(file_path).replace(".py", f"_result.json"),
            "result_dump_filepath": str(file_path).replace(".py", f"_result_dump.txt"),
            "prompt": utils.get_prompt(
                prompt_template, file_path, use_system_prompt=use_system_prompt
            ),
        }
        for idx, file_path in enumerate(python_files)
    }

    prompts = [x["prompt"] for x in id_mapping.values()]

    processed_prompts = engine.tokenizer.tokenizer.apply_chat_template(
        prompts, tokenize=False, add_generation_template=True
    )

    request_outputs = vllm_helpers.process_requests(
        engine, processed_prompts, sampling_params, lora_request
    )

    for r_output in request_outputs:
        # TODO: map result filepaths here and continue
        file_info = id_mapping[int(r_output.request_id)]

        output_raw = r_output.outputs[0].text
        output = re.sub(r"```json", "", output_raw)
        output = re.sub(r"```", "", output)
        output = re.sub(r"<\|assistant\|>\\n", "", output)

        with open(file_info["result_dump_filepath"], "w") as f:
            f.write(output_raw)

        # TODO: Improve the way this is done. Some plugin based design.
        if prompt_template in [
            "prompt_template_questions_based_2",
        ]:
            answers_json = utils.generate_json_from_answers(
                file_info["json_filepath"], output
            )
            translated_json = translator.translate_content(answers_json)
        else:
            translated_json = translator.translate_content(output)

        is_valid_json = utils.generate_json_file(
            file_info["result_filepath"], translated_json
        )
        if not is_valid_json:
            logger.info(f"{file_info['file_path']} failed: Not a valid JSON")
            raise utils.JsonException("json")

        logger.info(f"Processed file: {file_info['file_path']}")


def main_runner(args, models_to_run):
    runner_start_time = time.time()
    for model in models_to_run:
        error_count = 0
        timeout_count = 0
        json_count = 0
        files_analyzed = 0

        # Create result folder for model specific results
        bechmark_path = Path(args.bechmark_path)
        results_src = bechmark_path
        if args.results_dir is None:
            results_dst = bechmark_path.parent / model["name"] / bechmark_path.name
        else:
            results_dst = Path(args.results_dir) / model["name"] / bechmark_path.name
            os.makedirs(results_dst, exist_ok=True)

        utils.copy_folder(results_src, results_dst)

        python_files = list_python_files(results_dst)

        # TODO: Kick off the vllm llm deployment

        model_start_time = time.time()
        if model["use_vllms_for_evaluation"]:
            engine = vllm_helpers.initialize_engine(
                model["model_path"],
                model["quantization"],
                model["lora_repo"],
                model["max_model_len"],
            )
            lora_request = None
            if model["lora_repo"] is not None:
                lora_request = LoRARequest(
                    f"{model['name']}-lora", 1, model["lora_repo"]
                )

            sampling_params = SamplingParams(
                temperature=TEMPARATURE, top_p=0.95, max_tokens=MAX_TOKENS
            )

            model_evaluation_vllm(
                model["name"],
                args.prompt_id,
                python_files,
                engine,
                results_dst,
                use_system_prompt=model["use_system_prompt"],
                lora_request=lora_request,
                sampling_params=sampling_params,
            )

            del engine
            gc.collect()
            torch.cuda.empty_cache()
        else:
            pass

        logger.info(
            f"Model {model['name']} finished in {time.time()-model_start_time:.2f} seconds"
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

    parser.add_argument("--hf_token", help="Specify the hf token", required=True)

    parser.add_argument("--prompt_id", help="Specify the prompt ID", required=True)

    parser.add_argument(
        "--models_config",
        type=str,
        default="models_config.json",
    )

    parser.add_argument(
        "--models",
        nargs="+",
        type=str,
        help="Space-separated list of models",
        required=True,
    )

    parser.add_argument(
        "--custom_models",
        nargs="+",
        type=str,
        help="Space-separated list of custom models",
    )

    parser.add_argument(
        "--enable_streaming",
        help="If LLM response should be streamed",
        type=bool,
        default=False,
    )

    args = parser.parse_args()

    # Set HF token
    os.environ["HF_TOKEN"] = args.hf_token

    models_config = utils.load_models_config(parser.parse_args().models_config)

    models_to_run = []
    # check if args.models are in models_config
    for model in args.models:
        if model not in models_config["models"]:
            logger.error(f"Model {model} not found in models_config")
            sys.exit(-1)
        else:
            models_to_run.append(models_config["models"][model])

    # check if args.custom_models are in models_config
    if args.custom_models:
        for model in args.custom_models:
            if model not in models_config["custom_models"]:
                logger.error(f"Model {model} not found in models_config")
                sys.exit(-1)
            else:
                models_to_run.append(models_config["custom_models"][model])

    main_runner(args, models_to_run)

# example usage:
# python runner.py --bechmark_path /tmp/micro-benchmark \
# --ollama_url http://localhost:8000 \
# --prompt_id questions_based_2 \
# --ollama_models gpt-3.5-turbo gpt-3.5-turbo-instruct gpt-3.5-turbo-instruct-ft
# --openai_key <openai_key>
# --enable_streaming False
