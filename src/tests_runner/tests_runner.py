import os
import tarfile
from io import BytesIO

import docker


class FileHandler:
    def _copy_files_to_container(self, container, src, dst):
        original_directory = os.getcwd()
        src_dirname = os.path.dirname(src)
        src_basename = os.path.basename(src)

        if os.path.isfile(src):
            os.chdir(src_dirname)
        else:
            os.chdir(os.path.dirname(src))

        tar = tarfile.open(src_basename + ".tar", mode="w")
        try:
            tar.add(src_basename)
        finally:
            tar.close()

        data = open(src + ".tar", "rb").read()
        container.put_archive(os.path.dirname(dst), data)
        os.chdir(original_directory)

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
        self.script_path = f"./{self.tool_name}_script.py"
        self.docker_script_path = f"/tmp/{self.tool_name}_script.py"

    def _build_docker_image(self):
        image, _ = self.docker_client.images.build(
            path=self.dockerfile_path, tag=self.dockerfile_name
        )
        return image

    def _spawn_docker_instance(self):
        container = self.docker_client.containers.run(
            self.dockerfile_name, detach=True, stdin_open=True, tty=True
        )
        return container

    def _run_test_in_session(self):
        self._build_docker_image()
        container = self._spawn_docker_instance()
        file_handler = FileHandler()
        src = "../../micro-benchmark"
        dst = "/tmp/micro-benchmark"
        file_handler._copy_files_to_container(container, src, dst)
        file_handler._copy_files_to_container(
            container, self.script_path, self.docker_script_path
        )
        container.exec_run(f"python {self.docker_script_path}")
        file_handler._copy_files_from_container(
            container, "/tmp/micro-benchmark", self.dockerfile_path
        )
        container.stop()
        container.remove()


class ScalpelRunner(TypeEvalPyRunner):
    def __init__(self):
        super().__init__("scalpel", "../target_tools/scalpel")

    def run_tool_test(self):
        self._run_test_in_session()


class PyreRunner(TypeEvalPyRunner):
    def __init__(self):
        super().__init__("pyre", "../target_tools/pyre")

    def run_tool_test(self):
        self._run_test_in_session()


def main():
    runner = ScalpelRunner()
    runner.run_tool_test()

    runner = PyreRunner()
    runner.run_tool_test()


if __name__ == "__main__":
    main()
