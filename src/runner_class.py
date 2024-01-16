import logging
import docker
import time
import os
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


class TypeEvalPyRunner:
    def __init__(
        self,
        tool_name,
        dockerfile_path,
        host_results_path,
        dockerfile_name="Dockerfile",
        volumes={},
        nocache=False,
    ):
        self.docker_client = docker.from_env()
        self.tool_name = tool_name
        self.dockerfile_path = dockerfile_path
        self.dockerfile_name = dockerfile_name
        self.test_runner_script_path = f"/tmp/src/runner.py"
        self.benchmark_path = "/tmp/micro-benchmark"
        self.host_results_path = host_results_path
        self.volumes = volumes
        self.nocache = nocache

        self.file_handler = FileHandler()

        if not os.path.exists(self.host_results_path):
            os.makedirs(self.host_results_path)

    def _build_docker_image(self):
        logger.info("Building image")
        image, _ = self.docker_client.images.build(
            path=self.dockerfile_path,
            tag=self.tool_name,
            dockerfile=self.dockerfile_name,
            nocache=self.nocache,
        )
        return image

    def spawn_docker_instance(self):
        logger.info("Creating container")
        container = self.docker_client.containers.run(
            self.tool_name, detach=True, stdin_open=True, tty=True, volumes=self.volumes
        )
        return container

    def setup_benchmark_external_library(self):
        _, response = self.container.exec_run(
            f"pip install typeevalpy-external-module", stream=True
        )

    def run_test_in_session(self):
        _, response = self.container.exec_run(
            f"python {self.test_runner_script_path}", stream=True
        )
        for line in response:
            logger.info(line)

    def copy_results_from_container(self):
        self.file_handler.copy_files_from_container(
            self.container,
            self.benchmark_path,
            f"{self.host_results_path}/{self.tool_name}",
        )

    def run_tool_test(self):
        logger.info("#####################################################")
        logger.info(f"Running : {self.tool_name}")
        self._build_docker_image()
        self.container = self.spawn_docker_instance()

        src = "../micro-benchmark"
        dst = "/tmp"
        self.file_handler.copy_files_to_container(self.container, src, dst)

        self.setup_benchmark_external_library()

        logger.info("Type inferring...")
        start_time = time.time()

        self.run_test_in_session()

        end_time = time.time()
        execution_time = end_time - start_time
        logger.info(f"Execution time: {execution_time} seconds")

        self.copy_results_from_container()

        if not KEEP_CONTAINERS_RUNNING:
            self.container.stop()
            time.sleep(5)
            self.container.remove()


class ScalpelRunner(TypeEvalPyRunner):
    def __init__(self, host_results_path, debug=False, nocache=False):
        super().__init__(
            "scalpel", "./target_tools/scalpel", host_results_path, nocache=nocache
        )


class PyreRunner(TypeEvalPyRunner):
    def __init__(self, host_results_path, debug=False, nocache=False):
        super().__init__(
            "pyre", "./target_tools/pyre", host_results_path, nocache=nocache
        )


class PyrightRunner(TypeEvalPyRunner):
    def __init__(self, host_results_path, debug=False, nocache=False):
        super().__init__(
            "pyright", "./target_tools/pyright", host_results_path, nocache=nocache
        )


class PytypeRunner(TypeEvalPyRunner):
    def __init__(self, host_results_path, debug=False, nocache=False):
        super().__init__(
            "pytype", "./target_tools/pytype", host_results_path, nocache=nocache
        )


class JediRunner(TypeEvalPyRunner):
    def __init__(self, host_results_path, debug=False, nocache=False):
        if debug:
            super().__init__(
                "jedi",
                "./target_tools/jedi",
                host_results_path,
                dockerfile_name="Dockerfile",
                volumes={
                    os.path.abspath("./target_tools/jedi/src"): {
                        "bind": "/tmp/src",
                        "mode": "rw",
                    }
                },
                nocache=nocache,
            )
        else:
            super().__init__(
                "jedi", "./target_tools/jedi", host_results_path, nocache=nocache
            )


class HityperRunner(TypeEvalPyRunner):
    def __init__(self, host_results_path, debug=False, nocache=False):
        super().__init__(
            "hityper", "./target_tools/hityper", host_results_path, nocache=nocache
        )


class HityperDLRunner(TypeEvalPyRunner):
    def __init__(self, host_results_path, debug=False, nocache=False):
        super().__init__(
            "hityperdl", "./target_tools/hityperdl", host_results_path, nocache=nocache
        )

    def spawn_docker_instance(self):
        logger.info("Creating container")
        container = self.docker_client.containers.run(
            self.tool_name,
            detach=True,
            stdin_open=True,
            tty=True,
            ports={"5010": 5001},
        )
        time.sleep(5)  # wait fot server to start
        return container


class HeaderGenRunner(TypeEvalPyRunner):
    def __init__(self, host_results_path, debug=False, nocache=False):
        if debug:
            super().__init__(
                "headergen",
                "./target_tools/headergen",
                host_results_path,
                dockerfile_name="Dockerfile.dev",
                volumes={
                    "/mnt/Projects/PhD/Research/HeaderGen/git_sources/HeaderGen_github/": {
                        "bind": "/app/HeaderGen",
                        "mode": "ro",
                    }
                },
            )
        else:
            super().__init__(
                "headergen",
                "./target_tools/headergen",
                host_results_path,
                nocache=nocache,
            )


class PySonar2Runner(TypeEvalPyRunner):
    def __init__(self, host_results_path, debug=False, nocache=False):
        super().__init__(
            "pysonar2", "./target_tools/pysonar2", host_results_path, nocache=nocache
        )


class Type4pyRunner(TypeEvalPyRunner):
    def __init__(self, host_results_path, debug=False, nocache=False):
        super().__init__(
            "type4py", "./target_tools/type4py", host_results_path, nocache=nocache
        )

    def spawn_docker_instance(self):
        logger.info("Creating container")
        container = self.docker_client.containers.run(
            self.tool_name,
            detach=True,
            stdin_open=True,
            tty=True,
            ports={"5010": 5001},
        )
        time.sleep(5)  # wait fot server to start
        return container


class OllamaRunner(TypeEvalPyRunner):
    def __init__(self, host_results_path, config, debug=False, nocache=False):
        super().__init__(
            "ollama", "./target_tools/ollama", host_results_path, nocache=nocache
        )
        self.config = config

    def run_test_in_session(self):
        command_to_run = [
            "python",
            self.test_runner_script_path,
            "--bechmark_path",
            self.benchmark_path,
            "--openai_key",
            self.config["ollama"]["openai_key"],
            "--ollama_url",
            self.config["ollama"]["ollama_url"],
            "--prompt_id",
            self.config["ollama"]["prompt_id"],
            "--ollama_models",
        ]
        command_to_run.extend(self.config["ollama"]["ollama_models"])

        _, response = self.container.exec_run(" ".join(command_to_run), stream=True)
        for line in response:
            logger.info(line)

    def copy_results_from_container(self):
        for model in self.config["ollama"]["ollama_models"]:
            model_results_path = f"/tmp/{model}/micro-benchmark"
            self.file_handler.copy_files_from_container(
                self.container,
                model_results_path,
                f"{self.host_results_path}/{model}",
            )
