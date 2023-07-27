import argparse
import json
import logging
import os
from pathlib import Path
from typing import *
import torch
import asyncio

from typet5.model import ModelWrapper
from typet5.train import PreprocessArgs
from typet5.utils import *
from typet5.function_decoding import (
    RolloutCtx,
    PreprocessArgs,
    DecodingOrders,
    AccuracyMetric,
)
from typet5.static_analysis import PythonProject, reorder_signature_map

import translator
import utils


# Create a logger
logger = logging.getLogger("runner")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("/tmp/typet5_log.log")
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def list_python_files(folder_path):
    python_files = sorted(Path(folder_path).rglob("*.py"))
    return python_files


def benchmark_root(path) -> Path:
    return Path(path)


def get_subfolders(root_path, max_levels=2):
    subfolders = []
    root_path_str = str(root_path)
    for root, dirs, files in os.walk(root_path_str):
        current_level = root.count(os.sep) - root_path_str.count(os.sep) + 1
        if current_level == 1:
            continue
        if current_level > max_levels:
            continue
        for dir_name in dirs:
            subfolder_path = Path(root) / dir_name
            subfolder_rel_path = subfolder_path.relative_to(root_path)
            subfolders.append(str(subfolder_rel_path))
    return subfolders


async def process_tool(args):
    # download or load the model
    wrapper = ModelWrapper.load_from_hub("MrVPlusOne/TypeT5-v7")
    device = torch.device(f"cuda" if torch.cuda.is_available() else "cpu")
    wrapper.to(device)
    logger.info("model loaded")

    # set up the rollout parameters
    rctx = RolloutCtx(model=wrapper)
    pre_args = PreprocessArgs()
    # Double-traversal decoding order, where the model can make corrections # to its previous predictions in the second pass
    decode_order = DecodingOrders.DoubleTraversal()
    subfolders = get_subfolders(benchmark_root(args.bechmark_path))
    error_count = 0
    for subfolder in subfolders:
        try:
            logger.info(f"Parsing project: {subfolder}")
            project = PythonProject.parse_from_root(
                benchmark_root(args.bechmark_path) / subfolder
            )
            eval_r = await rctx.evaluate_on_projects([project], pre_args, decode_order)
            eval_r.print_predictions()
            output_dir = benchmark_root(args.bechmark_path) / subfolder
            eval_r.print_predictions(True)
            logger.info(f"Predictions written to: {output_dir}")
        except Exception as e:
            logger.info(f"Command returned non-zero exit status: {e} for file: {file}")
            error_count += 1
    logger.info(f"Runner finished with errors:{error_count}")


def main_runner(args):
    os.chdir(benchmark_root(args.bechmark_path))
    # Run TypeT5
    asyncio.run(process_tool(args))
    # Translate output to TypeEvalPy format
    translator.main_translator(args)


if __name__ == "__main__":
    is_running_in_docker = utils.is_running_in_docker()
    if is_running_in_docker:
        print("Python is running inside a Docker container")
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--bechmark_path",
            help="Specify the benchmark path",
            default="/tmp/micro-benchmark",
        )

        args = parser.parse_args()
        main_runner(args)
    else:
        print("Python is not running inside a Docker container")
