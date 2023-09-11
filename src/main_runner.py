import logging
import os
import tarfile
import time
from datetime import datetime
from io import BytesIO

import docker

from result_analyzer.main_analyze_results import run_results_analyzer

# Create a logger
logger = logging.getLogger("Main Runner")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("main_runner.log")
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

KEEP_CONTAINERS_RUNNING = False


class FileHandler:
    def copy_files_to_container(self, container, src, dst):
        # Create tar of micro-bench folder
        temp_path = "/tmp/temp.tar"
        with tarfile.open(temp_path, "w:gz") as tar:
            base_folder = os.path.basename(src)
            tar.add(src, arcname=base_folder)

        with open(temp_path, "rb") as file:
            data = file.read()
            container.put_archive(dst, data)

    def copy_files_from_container(self, container, src, dst):
        stream, _ = container.get_archive(src)
        stream_bytes = b"".join(stream)
        stream_bytes_io = BytesIO(stream_bytes)

        tar = tarfile.open(fileobj=stream_bytes_io)
        tar.extractall(path=dst)
        tar.close()

    def list_python_files(self, directory):
        python_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".py"):
                    python_files.append(
                        os.path.relpath(os.path.join(root, file), directory)
                    )
        return python_files


class TypeEvalPyRunner:
    def __init__(
        self,
        tool_name,
        dockerfile_path,
        host_results_path,
        dockerfile_name="Dockerfile",
        volumes={},
    ):
        self.docker_client = docker.from_env()
        self.tool_name = tool_name
        self.dockerfile_path = dockerfile_path
        self.dockerfile_name = dockerfile_name
        self.test_runner_script_path = f"/tmp/src/runner.py"
        self.host_results_path = host_results_path
        self.volumes = volumes

        if not os.path.exists(self.host_results_path):
            os.makedirs(self.host_results_path)

    def _build_docker_image(self):
        logger.info("Building image")
        image, _ = self.docker_client.images.build(
            path=self.dockerfile_path,
            tag=self.tool_name,
            dockerfile=self.dockerfile_name,
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

    def _run_test_in_session(self, result_path="/tmp/micro-benchmark"):
        logger.info("#####################################################")
        logger.info(f"Running : {self.tool_name}")
        self._build_docker_image()
        self.container = self.spawn_docker_instance()

        file_handler = FileHandler()
        src = "../micro-benchmark"
        dst = "/tmp"
        file_handler.copy_files_to_container(self.container, src, dst)

        self.setup_benchmark_external_library()

        logger.info("Type inferring...")
        start_time = time.time()
        _, response = self.container.exec_run(
            f"python {self.test_runner_script_path}", stream=True
        )
        for line in response:
            logger.info(line)

        end_time = time.time()
        execution_time = end_time - start_time
        logger.info(f"Execution time: {execution_time} seconds")

        file_handler.copy_files_from_container(
            self.container, result_path, f"{self.host_results_path}/{self.tool_name}"
        )

        if not KEEP_CONTAINERS_RUNNING:
            self.container.stop()
            time.sleep(5)
            self.container.remove()

    def run_tool_test(self):
        self._run_test_in_session()


class ScalpelRunner(TypeEvalPyRunner):
    def __init__(self, host_results_path):
        super().__init__("scalpel", "./target_tools/scalpel", host_results_path)


class PyreRunner(TypeEvalPyRunner):
    def __init__(self, host_results_path):
        super().__init__("pyre", "./target_tools/pyre", host_results_path)


class PyrightRunner(TypeEvalPyRunner):
    def __init__(self, host_results_path):
        super().__init__("pyright", "./target_tools/pyright", host_results_path)


class PytypeRunner(TypeEvalPyRunner):
    def __init__(self, host_results_path):
        super().__init__("pytype", "./target_tools/pytype", host_results_path)


class JediRunner(TypeEvalPyRunner):
    def __init__(self, host_results_path, debug=False):
        if debug:
            super().__init__(
                "jedi_dev",
                "./target_tools/jedi",
                host_results_path,
                dockerfile_name="Dockerfile",
                volumes={
                    os.path.abspath("./target_tools/jedi/src"): {
                        "bind": "/tmp/src",
                        "mode": "rw",
                    }
                },
            )
        else:
            super().__init__("jedi", "./target_tools/jedi", host_results_path)


class HityperRunner(TypeEvalPyRunner):
    def __init__(self, host_results_path):
        super().__init__("hityper", "./target_tools/hityper", host_results_path)


class HityperDLRunner(TypeEvalPyRunner):
    def __init__(self, host_results_path):
        super().__init__("hityperdl", "./target_tools/hityperdl", host_results_path)

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
    def __init__(self, host_results_path, debug=False):
        if debug:
            super().__init__(
                "headergen_dev",
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
            super().__init__("headergen", "./target_tools/headergen", host_results_path)


class PySonar2Runner(TypeEvalPyRunner):
    def __init__(self, host_results_path):
        super().__init__("pysonar2", "./target_tools/pysonar2", host_results_path)


class Type4pyRunner(TypeEvalPyRunner):
    def __init__(self, host_results_path):
        super().__init__("type4py", "./target_tools/type4py", host_results_path)

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


def main():
    host_results_path = f"../results/results_{datetime.now().strftime('%d-%m %H:%M')}"

    runner_classes = [
        (HeaderGenRunner, {"debug": False}),
        PyrightRunner,
        ScalpelRunner,
        HityperRunner,
        Type4pyRunner,
        HityperDLRunner,  # For the top n predictions from DL model(Type4py) used by HiTyper
        (JediRunner, {"debug": False}),
        # PySonar2Runner,
        # PytypeRunner,
        # PyreRunner,
    ]

    for Runner in runner_classes:
        if isinstance(Runner, tuple):
            runner_class, kwargs = Runner
            runner_instance = runner_class(host_results_path, **kwargs)
        else:
            runner_instance = Runner(host_results_path)

        runner_instance.run_tool_test()

    run_results_analyzer()

    os.rename("main_runner.log", f"{str(host_results_path)}/main_runner.log")


if __name__ == "__main__":
    main()
