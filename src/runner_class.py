import logging
import os
import time

import docker

from utils import FileHandler

# Create a logger
logger = logging.getLogger("Main Runner")

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
        custom_benchmark_dir=None,
    ):
        self.docker_client = docker.from_env()
        self.tool_name = tool_name
        self.dockerfile_path = dockerfile_path
        self.dockerfile_name = dockerfile_name
        self.test_runner_script_path = f"/tmp/src/runner.py"
        self.benchmark_path = "/tmp/micro-benchmark"

        if custom_benchmark_dir:
            self.local_benchmark_path = custom_benchmark_dir
        else:
            self.local_benchmark_path = os.path.abspath("../micro-benchmark")

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

        src = self.local_benchmark_path
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
    def __init__(
        self,
        host_results_path,
        debug=False,
        nocache=False,
        custom_benchmark_dir=None,
    ):
        super().__init__(
            "scalpel",
            "./target_tools/scalpel",
            host_results_path,
            nocache=nocache,
            custom_benchmark_dir=custom_benchmark_dir,
        )


class PyreRunner(TypeEvalPyRunner):
    def __init__(
        self,
        host_results_path,
        debug=False,
        nocache=False,
        custom_benchmark_dir=None,
    ):
        super().__init__(
            "pyre",
            "./target_tools/pyre",
            host_results_path,
            nocache=nocache,
            custom_benchmark_dir=custom_benchmark_dir,
        )


class PyrightRunner(TypeEvalPyRunner):
    def __init__(
        self,
        host_results_path,
        debug=False,
        nocache=False,
        custom_benchmark_dir=None,
    ):
        super().__init__(
            "pyright",
            "./target_tools/pyright",
            host_results_path,
            nocache=nocache,
            custom_benchmark_dir=custom_benchmark_dir,
        )


class PytypeRunner(TypeEvalPyRunner):
    def __init__(
        self,
        host_results_path,
        debug=False,
        nocache=False,
        custom_benchmark_dir=None,
    ):
        super().__init__(
            "pytype",
            "./target_tools/pytype",
            host_results_path,
            nocache=nocache,
            custom_benchmark_dir=custom_benchmark_dir,
        )


class JediRunner(TypeEvalPyRunner):
    def __init__(
        self,
        host_results_path,
        debug=False,
        nocache=False,
        custom_benchmark_dir=None,
    ):
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
                custom_benchmark_dir=custom_benchmark_dir,
            )
        else:
            super().__init__(
                "jedi",
                "./target_tools/jedi",
                host_results_path,
                nocache=nocache,
                custom_benchmark_dir=custom_benchmark_dir,
            )


class HityperRunner(TypeEvalPyRunner):
    def __init__(
        self,
        host_results_path,
        debug=False,
        nocache=False,
        custom_benchmark_dir=None,
    ):
        super().__init__(
            "hityper",
            "./target_tools/hityper",
            host_results_path,
            nocache=nocache,
            custom_benchmark_dir=custom_benchmark_dir,
        )


class HityperDLRunner(TypeEvalPyRunner):
    def __init__(
        self,
        host_results_path,
        debug=False,
        nocache=False,
        custom_benchmark_dir=None,
    ):
        super().__init__(
            "hityperdl",
            "./target_tools/hityperdl",
            host_results_path,
            nocache=nocache,
            custom_benchmark_dir=custom_benchmark_dir,
        )

    def spawn_docker_instance(self):
        logger.info("Creating container")
        container = self.docker_client.containers.run(
            self.tool_name,
            runtime="nvidia",
            detach=True,
            stdin_open=True,
            tty=True,
            ports={"5010": 5001},
        )
        time.sleep(5)  # wait fot server to start
        return container


class HeaderGenRunner(TypeEvalPyRunner):
    def __init__(
        self,
        host_results_path,
        debug=False,
        nocache=False,
        custom_benchmark_dir=None,
    ):
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
                    },
                },
                custom_benchmark_dir=custom_benchmark_dir,
            )
        else:
            super().__init__(
                "headergen",
                "./target_tools/headergen",
                host_results_path,
                nocache=nocache,
                custom_benchmark_dir=custom_benchmark_dir,
            )


class PySonar2Runner(TypeEvalPyRunner):
    def __init__(
        self,
        host_results_path,
        debug=False,
        nocache=False,
        custom_benchmark_dir=None,
    ):
        super().__init__(
            "pysonar2",
            "./target_tools/pysonar2",
            host_results_path,
            nocache=nocache,
            custom_benchmark_dir=custom_benchmark_dir,
        )


class Type4pyRunner(TypeEvalPyRunner):
    def __init__(
        self,
        host_results_path,
        debug=False,
        nocache=False,
        custom_benchmark_dir=None,
    ):
        super().__init__(
            "type4py",
            "./target_tools/type4py",
            host_results_path,
            nocache=nocache,
            custom_benchmark_dir=custom_benchmark_dir,
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
    def __init__(
        self,
        host_results_path,
        config,
        debug=False,
        nocache=False,
        custom_benchmark_dir=None,
    ):
        super().__init__(
            "ollama",
            "./target_tools/ollama",
            host_results_path,
            nocache=nocache,
            custom_benchmark_dir=custom_benchmark_dir,
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


class LLMRunner(TypeEvalPyRunner):
    def __init__(
        self,
        host_results_path,
        config,
        debug=False,
        nocache=False,
        custom_benchmark_dir=None,
    ):
        super().__init__(
            "llms",
            "./target_tools/llms",
            host_results_path,
            nocache=nocache,
            custom_benchmark_dir=custom_benchmark_dir,
            volumes={
                os.path.abspath("/mnt/hf_cache/huggingface"): {
                    "bind": "/root/.cache/huggingface",
                    "mode": "rw",
                }
            },
        )
        self.config = config

    def run_test_in_session(self):
        command_to_run = [
            "python",
            self.test_runner_script_path,
            "--bechmark_path",
            self.benchmark_path,
            "--hf_token",
            self.config["llm"]["hf_token"],
            "--openai_key",
            self.config["llm"]["openai_key"],
            "--prompt_id",
            self.config["llm"]["prompt_id"],
        ]

        for i in ["models", "custom_models", "openai_models"]:
            if self.config["llm"][i]:
                command_to_run.append(f"--{i}")
                command_to_run.extend(self.config["llm"][i])

        _, response = self.container.exec_run(" ".join(command_to_run), stream=True)
        for line in response:
            logger.info(line)

    def copy_results_from_container(self):
        for i in ["models", "custom_models", "openai_models"]:
            if self.config["llm"][i]:
                for model in self.config["llm"][i]:
                    model_results_path = f"/tmp/{model}/micro-benchmark"
                    self.file_handler.copy_files_from_container(
                        self.container,
                        model_results_path,
                        f"{self.host_results_path}/{model}",
                    )

    def spawn_docker_instance(self):
        logger.info("Creating container")
        container = self.docker_client.containers.run(
            self.tool_name,
            detach=True,
            stdin_open=True,
            tty=True,
            volumes=self.volumes,
            runtime="nvidia",
            device_requests=[
                docker.types.DeviceRequest(
                    count=-1, capabilities=[["gpu"]]
                )  # Request all available GPUs
            ],
        )
        return container


class RightTyperRunner(TypeEvalPyRunner):
    def __init__(
        self,
        host_results_path,
        config,
        debug=False,
        nocache=False,
        custom_benchmark_dir=None,
    ):
        super().__init__(
            "righttyper",
            "./target_tools/righttyper",
            host_results_path,
            nocache=nocache,
            custom_benchmark_dir=custom_benchmark_dir,
        )
        self.config = config
