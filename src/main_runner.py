import logging
import os
import shutil
import sys
import tarfile
import time
from argparse import ArgumentParser
from datetime import datetime
from io import BytesIO

import docker
import yaml

from main_analyze_results import run_results_analyzer
from runner_class import (
    HeaderGenRunner,
    HityperDLRunner,
    HityperRunner,
    JediRunner,
    OllamaRunner,
    PyrightRunner,
    ScalpelRunner,
    Type4pyRunner,
)
from utils import FileHandler

# Create a logger
logger = logging.getLogger("Main Runner")
logger.setLevel(logging.DEBUG)

log_file_handler = logging.FileHandler("main_runner.log")
log_file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
log_file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(log_file_handler)
logger.addHandler(console_handler)

KEEP_CONTAINERS_RUNNING = False

# Get config
CONFIG_FILE = "config.yaml"

if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, "r") as file:
        config = yaml.safe_load(file)
else:
    config = {}


def get_args():
    parser = ArgumentParser(description="Run various type evaluation tools.")
    parser.add_argument(
        "--runners",
        nargs="+",
        default=[
            "headergen",
            "pyright",
            "scalpel",
            "jedi",
            "hityper",
            "type4py",
            "hityperdl",
        ],
        help=(
            "List of runners to execute. Choices are:"
            "headergen, pyright, scalpel, jedi, hityper, type4py, hityperdl"
        ),
    )
    parser.add_argument(
        "--debug", action="store_true", help="Execute runners in debug mode."
    )
    parser.add_argument(
        "--nocache", action="store_true", help="Do not use docker image cache."
    )

    return parser.parse_args()


def main():
    args = get_args()
    host_results_path = (
        f"../results/results_{datetime.now().strftime('%d-%m-%y %H:%M')}"
    )

    available_runners = {
        "headergen": (
            HeaderGenRunner,
            {"debug": args.debug, "nocache": args.nocache},
        ),
        "pyright": (
            PyrightRunner,
            {"debug": False, "nocache": args.nocache},
        ),
        "scalpel": (
            ScalpelRunner,
            {"debug": False, "nocache": args.nocache},
        ),
        "hityper": (
            HityperRunner,
            {"debug": False, "nocache": args.nocache},
        ),
        "type4py": (
            Type4pyRunner,
            {"debug": False, "nocache": args.nocache},
        ),
        "hityperdl": (
            HityperDLRunner,
            {"debug": False, "nocache": args.nocache},
        ),
        "jedi": (
            JediRunner,
            {"debug": args.debug, "nocache": args.nocache},
        ),
        "ollama": (
            OllamaRunner,
            {"debug": args.debug, "nocache": args.nocache, "config": config},
        ),
        # PySonar2Runner,
        # PytypeRunner,
        # PyreRunner,
    }

    for runner_name in args.runners:
        if runner_name in available_runners:
            Runner, kwargs = available_runners[runner_name]
            runner_instance = Runner(host_results_path, **kwargs)
            runner_instance.run_tool_test()
        else:
            logger.error(f"Unknown runner: {runner_name}")
            sys.exit(-1)

    run_results_analyzer(host_results_path)

    shutil.move("main_runner.log", f"{str(host_results_path)}/main_runner.log")


if __name__ == "__main__":
    main()
