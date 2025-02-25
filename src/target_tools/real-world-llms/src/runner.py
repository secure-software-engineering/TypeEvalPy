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
import psutil  # Add this import

import prompts
import translator
import utils
import vllm_helpers
import transformers_helpers
import openai_helpers

from vllm import LLM, SamplingParams
from vllm.lora.request import LoRARequest
import gc
import torch
from tqdm import tqdm
import result_translator  # Import the translation module
from datetime import datetime  # Import datetime for timestamp generation


AUTOFIX_WITH_OPENAI = False
REQUEST_TIMEOUT = 60
USE_MULTIPROCESSING_FOR_TERMINATION = True
MAX_TOKENS = 64
TEMPARATURE = 0.001
MAX_NEW_TOKENS = 1024

PROMPTS_MAP = {
    "json_based_1": prompts.json_based_1,
    "json_based_2": prompts.json_based_2,
    "questions_based_1": prompts.questions_based_1,
    "questions_based_2": prompts.questions_based_2,
    "questions_based_3": prompts.questions_based_3,
    "questions_based_4": prompts.questions_based_4,
    "questions_based_2_ft": prompts.questions_based_2_ft,
}

# Set max_split_size_mb to avoid memory fragmentation
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:128"

script_dir = Path(__file__).parent
# Create a logger
logger = logging.getLogger("runner")
logger.setLevel(logging.INFO)

if utils.is_running_in_docker():
    file_handler = logging.FileHandler("/tmp/llm_log.log", mode="w")
else:
    file_handler = logging.FileHandler("llm_log.log", mode="w")

file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler(stdout)
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Set the PYTORCH_CUDA_ALLOC_CONF environment variable
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:128"


def log_memory_usage():
    """Logs the current memory usage of the system and CUDA."""
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    logger.debug(f"System memory usage: {mem_info.rss / (1024 ** 3):.2f} GB")

    if torch.cuda.is_available():
        for i in range(torch.cuda.device_count()):
            logger.debug(f"CUDA memory usage for device {i}:")
            logger.debug(
                f"  Allocated: {torch.cuda.memory_allocated(i) / (1024 ** 3):.2f} GB"
            )
            logger.debug(
                f"  Cached: {torch.cuda.memory_reserved(i) / (1024 ** 3):.2f} GB"
            )


# def calculate_memory_approximation(token_count, base_memory=0.1, token_memory=0.0001):
#     """
#     Approximate the memory required for a batch based on the token count.
#     :param token_count: Total number of tokens in the batch.
#     :param base_memory: Base memory required for processing (in GB).
#     :param token_memory: Memory required per token (in GB).
#     :return: Approximated memory required (in GB).
#     """
#     return base_memory + (token_count * token_memory)


def get_available_gpu_memory():
    """Returns the available GPU memory in GB."""
    if torch.cuda.is_available():
        available_memory = torch.cuda.get_device_properties(
            0
        ).total_memory - torch.cuda.memory_allocated(0)
        return available_memory / (1024**3)
    return 0


# def calculate_best_batch_size(prompts, token_limit, max_memory=40):
#     """
#     Calculate the best batch size based on token limit and memory constraints.
#     :param prompts: List of prompts.
#     :param token_limit: Maximum number of tokens per batch.
#     :param max_memory: Maximum memory available for processing (in GB).
#     :return: Best batch size.
#     """
#     sorted_prompts = sorted(prompts, key=lambda x: utils.get_token_count(x))
#     batch_size = 1
#     current_token_count = 0
#     current_memory = 0

#     for prompt in sorted_prompts:
#         token_count = utils.get_token_count(prompt)
#         memory_approx = calculate_memory_approximation(current_token_count + token_count)

#         if current_token_count + token_count > token_limit or memory_approx > max_memory:
#             break

#         current_token_count += token_count
#         current_memory = memory_approx
#         batch_size += 1

#     # Adjust batch size based on actual GPU memory usage
#     available_memory = get_available_gpu_memory()
#     while True:
#         try:
#             # Try to allocate a tensor of the given batch size
#             _ = torch.randn(batch_size, 3, 224, 224).cuda()
#             if available_memory < current_memory:
#                 batch_size = batch_size // 2
#                 torch.cuda.empty_cache()
#             else:
#                 break
#         except RuntimeError as e:
#             if 'out of memory' in str(e):
#                 batch_size = batch_size // 2
#                 torch.cuda.empty_cache()
#             else:
#                 raise e

#     print(f"Available GPU memory: {available_memory:.2f} GB")

#     return batch_size


def get_prompt_mapping(
    result_dir, prompt_template, use_system_prompt=False, token_limit=4096
):
    """
    Traverse the directory structure, pair .json and _gt.json files,
    and generate a combined id_mapping using get_prompt_mapping logic.
    """
    base_path = Path(result_dir)
    id_mapping = {}
    idx = 0

    # Walk through train, test, valid folders
    for subfolder in ["test"]:
        folder_path = base_path / subfolder
        if not folder_path.exists():
            continue

        # Get .json and _gt.json files
        code_json_files = sorted(folder_path.glob("*.json"))
        gt_json_files = sorted(folder_path.glob("*_gt.json"))

        # Ensure files are paired correctly
        json_pairs = {}
        for code_json in code_json_files:
            # Find the corresponding _gt.json
            gt_json = folder_path / f"{code_json.stem}_gt.json"
            if gt_json.exists():
                json_pairs[code_json] = gt_json

        # Process each pair
        for code_json, gt_json in json_pairs.items():
            result_json_path = code_json.with_name(code_json.stem + "_result.json")
            existing_results = {}

            # Check if the result JSON file exists and load existing results
            if result_json_path.exists():
                with open(result_json_path, "r") as result_file:
                    existing_results = json.load(result_file)

            # Create a set of existing file paths for quick lookup
            existing_files = {entry["file"] for entry in existing_results}

            with open(code_json, "r") as code_file:
                code_data = json.load(code_file)

            with open(gt_json, "r") as gt_file:
                gt_data = json.load(gt_file)

            # Create gt_mapping
            gt_mapping = {}
            for entry in gt_data:
                file_path = entry["file"]
                if file_path not in gt_mapping:
                    gt_mapping[file_path] = []
                gt_mapping[file_path].append(entry)

            # Process the code and generate prompts
            for project_name, project_info in code_data.items():
                src_files = project_info.get("src_files", {})

                for file_path, file_info in src_files.items():
                    source_code = file_info.get("source_code", "")

                    if source_code == "":
                        continue

                    # Skip if the file is already present in existing results
                    if file_path in existing_files:
                        continue

                    # Fetch the typing information for the file from gt_mapping
                    type_info_list = gt_mapping.get(file_path, [])
                    if len(type_info_list) == 0:
                        continue

                    # Generate the prompt
                    prompt = utils.get_prompt(
                        prompt_template,
                        source_code,
                        type_info_list,
                        use_system_prompt=use_system_prompt,
                        file_path=file_path,
                        token_limit=token_limit,
                    )

                    if prompt is None:
                        continue

                    # Store the result in id_mapping
                    id_mapping[idx] = {
                        "project_name": project_name,
                        "file_path": file_path,
                        "json_filepath": str(gt_json),
                        "result_filepath": str(result_json_path),
                        "result_dump_filepath": str(
                            code_json.with_name(code_json.stem + "_result_dump.txt")
                        ),
                        "prompt": prompt,
                    }
                    idx += 1

    return id_mapping


def create_result_json_file_from_answers(file_info, output_raw, prompt_template):
    # Clean the raw output
    output = re.sub(r"```json", "", output_raw)
    output = re.sub(r"```", "", output)
    output = re.sub(r"<\|assistant\|>\\n", "", output)

    # For codestral as it returns whole sentence
    # type_inference = re.search(r"(\w+Type)", output)
    # if type_inference:
    #     output = type_inference.group(1)
    # else:
    #     output = "Unknown"

    # Append raw output to the dump file for debugging
    with open(file_info["result_dump_filepath"], "a") as f:
        f.write(output_raw + "\n")

    # Generate and translate content based on the prompt template
    if prompt_template in [
        "prompt_template_questions_based_2",
    ]:
        answers_json = utils.generate_json_from_answers(
            file_info["file_path"], file_info["json_filepath"], output
        )
        translated_json = translator.translate_content(answers_json)
    else:
        translated_json = translator.translate_content(output)

    # Load existing results if the file exists
    existing_results = []
    if os.path.exists(file_info["result_filepath"]):
        with open(file_info["result_filepath"], "r") as f:
            try:
                existing_results = json.load(f)
            except json.JSONDecodeError:
                logger.warning(
                    f"Invalid JSON in {file_info['result_filepath']}. Starting fresh."
                )

    # Append new results to the existing ones
    if isinstance(translated_json, list):
        existing_results.extend(translated_json)
    else:
        existing_results.append(translated_json)

    # Save the combined results back to the result file
    is_valid_json = utils.generate_json_file(
        file_info["result_filepath"], existing_results
    )

    if not is_valid_json:
        logger.error(f"{file_info['file_path']} failed: Not a valid JSON")
        raise utils.JsonException("json")

    logger.debug(f"Accessed {file_info['file_path']} successfully.")
    logger.debug(f"Results appended to {file_info['result_filepath']} successfully.")


def create_result_json_file_from_code(file_info, output_raw, prompt_template):
    # Ensure output_raw is a string to prevent TypeError
    if not isinstance(output_raw, str):
        output_raw = str(output_raw) if output_raw is not None else ""

    # Clean up the output by removing unnecessary formatting
    code = re.search(r"```(?:.*?)\n(.*?)```", output_raw, re.DOTALL)

    if code:
        output_cleaned = code.group(1).strip()
    else:
        output_cleaned = re.sub(r"```json|```|<\|assistant\|>\\n", "", output_raw)

    # Save the raw output to the result dump filepath
    with open(file_info["result_dump_filepath"], "w") as f:
        f.write(output_raw)

    # Determine the filename, falling back if "filename" key is missing
    filename = file_info["json_filepath"]
    if filename is None:
        # Generate a fallback filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        fallback_dir = "outputs"  # You may specify any preferred directory
        os.makedirs(fallback_dir, exist_ok=True)
        filename = os.path.join(fallback_dir, f"output_{timestamp}.json")
        logger.warning(
            f"'filename' key missing in file_info; saving output to {filename}"
        )

    # Directly translate the cleaned source code output to JSON annotations
    translated_json = result_translator.translate_output_to_annotations(
        output_cleaned, filename
    )

    # Validate and save the translated JSON to the final result file
    result_filepath = file_info.get("result_filepath", filename)
    if utils.generate_json_file(result_filepath, translated_json):
        logger.debug(
            f"Processed file: {file_info.get('file_path', filename)} successfully."
        )
    else:
        logger.error(f"{file_info.get('file_path', filename)} failed: Not a valid JSON")
        raise utils.JsonException("json")


def list_json_files(folder_path):
    json_files = sorted(Path(folder_path).rglob("*.json"))
    return json_files


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

    id_mapping = get_prompt_mapping(prompt_template, python_files, use_system_prompt)

    prompts = [x["prompt"] for x in id_mapping.values()]

    processed_prompts = engine.tokenizer.tokenizer.apply_chat_template(
        prompts, tokenize=False, add_generation_template=True
    )

    request_outputs = vllm_helpers.process_requests(
        engine, processed_prompts, sampling_params, lora_request
    )

    for r_output in request_outputs:
        file_info = id_mapping[int(r_output.request_id)]

        output_raw = r_output.outputs[0].text
        create_result_json_file(file_info, output_raw, prompt_template)


def model_evaluation_transformers(
    model_name,
    prompt_template,
    json_files,
    pipe,
    results_dst,
    use_system_prompt=False,
    initial_batch_size=32,
    token_limit=3000,
    max_memory=65,
):
    id_mapping = get_prompt_mapping(
        results_dst, prompt_template, use_system_prompt, token_limit
    )

    prompt_id_mapping_pairs = [(x["prompt"], x) for x in id_mapping.values()]
    sorted_prompt_id_mapping_pairs = sorted(
        prompt_id_mapping_pairs, key=lambda x: utils.get_token_count(x[0])
    )
    sorted_prompts = [pair[0] for pair in sorted_prompt_id_mapping_pairs]
    sorted_id_mapping = [pair[1] for pair in sorted_prompt_id_mapping_pairs]

    progress_bar = tqdm(total=len(sorted_prompts), desc="Processing Prompts")
    
    i = 0
    batch_size = initial_batch_size

    while i < len(sorted_prompts):
        current_batch = []
        current_token_count = 0

        while (
            i < len(sorted_prompts)
            and current_token_count + utils.get_token_count(sorted_prompts[i])
            <= token_limit * batch_size
        ):
            prompt_token_count = utils.get_token_count(sorted_prompts[i])
            logger.debug(f"Prompt {sorted_id_mapping[i]['file_path']}: {prompt_token_count} tokens")
            current_batch.append(sorted_prompts[i])
            current_token_count += prompt_token_count
            i += 1

        log_memory_usage()
        
        try:
            request_outputs = transformers_helpers.process_requests(
                pipe,
                current_batch,
                max_new_tokens=MAX_NEW_TOKENS,
                batch_size=len(current_batch),
            )

            for id, r_output in enumerate(request_outputs):
                file_info = sorted_id_mapping[id + i - len(current_batch)]
                output_raw = r_output[0]["generated_text"][-1]["content"]
                create_result_json_file_from_answers(
                    file_info, output_raw, prompt_template
                )

            progress_bar.update(len(current_batch))
            del request_outputs, current_batch
            gc.collect()
            torch.cuda.empty_cache()
        
        except torch.cuda.OutOfMemoryError as e:
            logger.error(f"CUDA out of memory error while processing batch starting at index {i - len(current_batch)}")
            logger.error(f"Error details: {e}")
            # logger.error(f"Batch details: {[sorted_id_mapping[i - len(current_batch) + j]['file_path'] for j in range(len(current_batch))]}")
            log_memory_usage()
            torch.cuda.empty_cache()
            
            batch_size = max(1, batch_size - 3)  # Reduce batch size but ensure it's at least 1
            i -= len(current_batch)  # Roll back the index to retry from unprocessed prompts
            print(f"Reducing batch size to {batch_size}")
            continue  # Retry with a smaller batch size

    log_memory_usage()
    progress_bar.close()


def model_evaluation_openai(
    model_name,
    prompt_template,
    openai_key,
    python_files,
    results_dst,
    use_system_prompt=False,
):

    id_mapping = get_prompt_mapping(prompt_template, json_files, use_system_prompt)

    # id_mapping = get_prompt_mapping(prompt_template, '/home/pysse/TypeEvalPy/src/target_tools/real-world-llms/src/real-world-dataset/train.json','/home/pysse/TypeEvalPy/src/target_tools/real-world-llms/src/real-world-dataset/train_translated.json' , use_system_prompt)

    prompts = [x["prompt"] for x in id_mapping.values()]

    utils.get_prompt_cost(prompts)
    utils.dump_ft_jsonl(id_mapping, f"{results_dst}/ft_dataset_{model_name}.jsonl")
    utils.dump_batch_prompt_jsonl(
        id_mapping,
        f"{results_dst}/batch_prompt_{model_name}.jsonl",
        model=model_name,
    )

    request_outputs = openai_helpers.process_requests(
        model_name,
        prompts,
        openai_key,
        max_new_tokens=MAX_NEW_TOKENS,
        max_workers=1,
    )

    for id, r_output in enumerate(request_outputs):
        file_info = id_mapping[id]

        # Store raw output from LLM
        output_raw = r_output
        create_result_json_file(file_info, output_raw, prompt_template)


def main_runner(args, runner_config, models_to_run, openai_models_models_to_run):
    runner_start_time = time.time()
    for model in models_to_run:
        error_count = 0
        timeout_count = 0
        json_count = 0
        files_analyzed = 0
        model_start_time = 0  # Initialize model_start_time here

        # Create result folder for model specific results
        bechmark_path = Path(args.bechmark_path)
        results_src = bechmark_path
        if args.results_dir is None:
            results_dst = bechmark_path.parent / model["name"] / bechmark_path.name
        else:
            results_dst = Path(args.results_dir) / model["name"] / bechmark_path.name
            os.makedirs(results_dst, exist_ok=True)

        utils.copy_folder(results_src, results_dst)

        json_files = list_json_files(results_dst)

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
            model_start_time = time.time()
            model_evaluation_vllm(
                model["name"],
                args.prompt_id,
                json_files,
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
            if model["lora_repo"] is None:
                model_path = model["model_path"]
                lora_repo = None
            else:
                model_path = model["model_path"]
                lora_repo = model["lora_repo"]

            pipe = None
            try:
                pipe = transformers_helpers.load_model_and_configurations(
                    args.hf_token, model_path, model["quantization"], TEMPARATURE, lora_repo
                )
                model_start_time = time.time()
                model_evaluation_transformers(
                    model["name"],
                    args.prompt_id,
                    json_files,
                    pipe,
                    results_dst,
                    use_system_prompt=model["use_system_prompt"],
                    initial_batch_size=model["batch_size"],
                    token_limit=model["max_model_len"],
                )

            except Exception as e:
                logger.error(f"Error in model {model['name']}: {e}")
                error_count += 1
                traceback.print_exc()
            finally:
                if pipe is not None:
                    del pipe
                gc.collect()
                torch.cuda.empty_cache()

        logger.info(
            f"Model {model['name']} finished in {time.time()-model_start_time:.2f} seconds"
        )
        logger.info("Running translator")
        translator.main_translator(results_dst)

    # running gpt models
    for model in openai_models_models_to_run:
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

        python_files = list_json_files(results_dst)

        python_files = python_files[:2]

        model_start_time = time.time()
        model_evaluation_openai(
            model["name"],
            args.prompt_id,
            args.openai_key,
            python_files,
            results_dst,
            use_system_prompt=model["use_system_prompt"],
        )

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

    parser.add_argument(
        "--openai_key", help="Specify the OpenAI Auth Key", required=False
    )

    parser.add_argument("--prompt_id", help="Specify the prompt ID", required=True)

    parser.add_argument(
        "--models_config",
        type=str,
        default=f"{script_dir}/models_config.yaml",
    )

    parser.add_argument(
        "--models",
        nargs="+",
        type=str,
        help="Space-separated list of models",
    )

    parser.add_argument(
        "--custom_models",
        nargs="+",
        type=str,
        help="Space-separated list of custom models",
    )

    parser.add_argument(
        "--openai_models",
        nargs="+",
        type=str,
        help="Space-separated list of openai models",
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
    runner_config = utils.load_runner_config(parser.parse_args().models_config)

    models_to_run = []
    openai_models_models_to_run = []
    # check if args.models are in models_config

    if args.models:
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

    if args.openai_models:
        for model in args.openai_models:
            if model not in models_config["openai_models"]:
                logger.error(f"Model {model} not found in models_config")
                sys.exit(-1)
            else:
                openai_models_models_to_run.append(
                    models_config["openai_models"][model]
                )

    torch.cuda.empty_cache()
    main_runner(args, runner_config, models_to_run, openai_models_models_to_run)

# example usage:
"""
python3.10 runner.py \
--bechmark_path /mnt/hf_cache/rashida_manytype4py/many-types-4-py-dataset/rw-benchmark \
--prompt_id prompt_template_questions_based_2 \
--models finetuned-codestral-v0.1-22b \
--hf_token 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 \
--openai_key token \
--enable_streaming True \
--models_config /home/ssegpu/rashida/TypeEvalPy/src/target_tools/real-world-llms/src/models_config.yaml \
--results_dir /home/ssegpu/rashida/TypeEvalPy/results

python runner.py \
--bechmark_path /home/ssegpu/TypeEvalPy/TypeEvalPy/autogen_typeevalpy_benchmark \
--prompt_id prompt_template_questions_based_2 \
--models llama3.1-it:8b \
--hf_token  \
--openai_key token \
--enable_streaming True \
--models_config /home/ssegpu/TypeEvalPy/TypeEvalPy/src/target_tools/llms/src/models_config.yaml \
--results_dir /home/ssegpu/TypeEvalPy/TypeEvalPy/.scrapy/results_full_1
"""
