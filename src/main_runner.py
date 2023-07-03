import logging
import os
import tarfile
import time
from datetime import datetime
from io import BytesIO

import docker

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


class FileHandler:
    def _copy_files_to_container(self, container, src, dst):
        # Create tar of micro-bench folder
        temp_path = "/tmp/temp.tar"
        with tarfile.open(temp_path, "w:gz") as tar:
            base_folder = os.path.basename(src)
            tar.add(src, arcname=base_folder)

        with open(temp_path, "rb") as file:
            data = file.read()
            container.put_archive(dst, data)

    def _copy_files_from_container(self, container, src, dst):
        stream, _ = container.get_archive(src)
        stream_bytes = b"".join(stream)
        stream_bytes_io = BytesIO(stream_bytes)

        tar = tarfile.open(fileobj=stream_bytes_io)
        tar.extractall(path=dst)
        tar.close()

    def _list_python_files(self, directory):
        python_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".py"):
                    python_files.append(
                        os.path.relpath(os.path.join(root, file), directory)
                    )
        return python_files


class TypeEvalPyRunner:
    def __init__(self, tool_name, dockerfile_path):
        self.docker_client = docker.from_env()
        self.tool_name = tool_name
        self.dockerfile_path = dockerfile_path
        self.dockerfile_name = tool_name
        self.test_runner_script_path = f"/tmp/src/runner.py"
        self.host_results_path = f"./results_{datetime.now().strftime('%d-%m %H:%M')}"

        if not os.path.exists(self.host_results_path):
            os.makedirs(self.host_results_path)

    def _build_docker_image(self):
        logger.info("Building image")
        image, _ = self.docker_client.images.build(
            path=self.dockerfile_path, tag=self.dockerfile_name
        )
        return image

    def _spawn_docker_instance(self):
        logger.info("Creating container")
        container = self.docker_client.containers.run(
            self.dockerfile_name,
            detach=True,
            stdin_open=True,
            tty=True,
        )
        return container

    def _run_test_in_session(self, result_path="/tmp/micro-benchmark"):
        logger.info("#####################################################")
        logger.info(f"Running : {self.tool_name}")
        self._build_docker_image()
        container = self._spawn_docker_instance()

        file_handler = FileHandler()
        src = "../micro-benchmark"
        dst = "/tmp"
        file_handler._copy_files_to_container(container, src, dst)

        logger.info("Type inferring...")
        start_time = time.time()
        _, response = container.exec_run(
            f"python {self.test_runner_script_path}", stream=True
        )
        for line in response:
            logger.info(line)

        end_time = time.time()
        execution_time = end_time - start_time
        logger.info(f"Execution time: {execution_time} seconds")

        file_handler._copy_files_from_container(
            container, result_path, f"{self.host_results_path}/{self.tool_name}"
        )

        container.stop()
        container.remove()


class ScalpelRunner(TypeEvalPyRunner):
    def __init__(self):
        super().__init__("scalpel", "./target_tools/scalpel")

    def run_tool_test(self):
        self._run_test_in_session()


class PyreRunner(TypeEvalPyRunner):
    def __init__(self):
        super().__init__("pyre", "./target_tools/pyre")

    def run_tool_test(self):
        self._run_test_in_session()


class PyrightRunner(TypeEvalPyRunner):
    def __init__(self):
        super().__init__("pyright", "./target_tools/pyright")

    def run_tool_test(self):
        self._run_test_in_session("/tmp/typings")


class PytypeRunner(TypeEvalPyRunner):
    def __init__(self):
        super().__init__("pytype", "./target_tools/pytype")

    def run_tool_test(self):
        self._run_test_in_session()


class JediRunner(TypeEvalPyRunner):
    def __init__(self):
        super().__init__("jedi", "./target_tools/jedi")

    def run_tool_test(self):
        self._run_test_in_session()


class HityperRunner(TypeEvalPyRunner):
    def __init__(self):
        super().__init__("hityper", "./target_tools/hityper")

    def run_tool_test(self):
        self._run_test_in_session()


def main():
    runner = ScalpelRunner()
    runner.run_tool_test()

    runner = JediRunner()
    runner.run_tool_test()

    runner = PyrightRunner()
    runner.run_tool_test()

    runner = PytypeRunner()
    runner.run_tool_test()

    runner = PyreRunner()
    runner.run_tool_test()

    runner = HityperRunner()
    runner.run_tool_test()


if __name__ == "__main__":
    main()
