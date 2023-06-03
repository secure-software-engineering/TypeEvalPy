# Script
# - Starts docker containers,
#   - Use docker API to spawn containers
#   - Can use ssh or someother interactive session
# - Runs tests from micro-benchmark
#  - Define a common interface for running tests
# - Translate result format to TypeEvalPy's format
# - Output to a common folder
# - Analysis of the results

import os
import tarfile

import docker


class TypeEvalPyRunner:
    def __init__(self) -> None:
        self.docker_client = docker.from_env()
        self.dockerfile_name = ""

    # Build a Docker image from a Dockerfile
    def _build_docker_image(self, dockerfile_path):
        image, _ = self.docker_client.images.build(
            path=dockerfile_path, tag=self.dockerfile_name
        )
        return image

    # Use the Docker API to spawn a container from an image
    def _spawn_docker_instance(self, image_name):
        container = self.docker_client.containers.run(
            image_name, detach=True, stdin_open=True, tty=True
        )
        return container

    # Copy the micro-benchmark directory into the container
    def _copy_files(self, container, src, dst):
        os.chdir(os.path.dirname(src))
        srcname = os.path.basename(src)
        tar = tarfile.open(src + ".tar", mode="w")
        try:
            tar.add(srcname)
        finally:
            tar.close()

        data = open(src + ".tar", "rb").read()
        container.put_archive(os.path.dirname(dst), data)

    # Run the tool on a Python file inside the container
    def _run_tool_on_python_file(self, container, python_file_path):
        if not container.attrs["State"]["Running"]:
            container.start()

        result = container.exec_run(f"python {python_file_path}")
        test_output = result.output.decode("utf-8")
        return test_output

    def run_test_in_session(self, dockerfile_path, script_path) -> None:
        # Build the Docker image
        self._build_docker_image(dockerfile_path)

        # Spawn a Docker container from the image
        container = self._spawn_docker_instance(self.dockerfile_name)

        # Copy the micro-benchmark directory into the container
        src = "../micro-benchmark"
        dst = "/micro-benchmark"
        self._copy_files(container, src, dst)

        # Copy the script to the container
        self._copy_files(container, script_path, script_path)

        # Execute the script inside the container
        container.exec_run(f"python {script_path}")
        # Stop and remove the container
        container.stop()
        container.remove()

    def _get_python_files(self, directory):
        # Recursively get a list of Python files in a directory
        python_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".py"):
                    python_files.append(
                        os.path.relpath(os.path.join(root, file), directory)
                    )
        return python_files

    def translate_result_to_typeevalpy(self) -> None:
        pass


class ScalpelRunner(TypeEvalPyRunner):
    def __init__(self) -> None:
        super().__init__()
        self.dockerfile_path = "target_tools/scalpel"
        self.dockerfile_name = "scalpel"

    def run_tool_test(self) -> None:
        # Run the code inside the container
        script = """

import json
import os

from scalpel.typeinfer.typeinfer import TypeInference


def list_python_files(folder_path):
    python_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files


folder_path = "../micro-benchmark/python_features"

python_files = list_python_files(folder_path)

for file in python_files:
    print(file)
    inferer = TypeInference(name=file, entry_point=file)
    inferer.infer_types()
    inferred = inferer.get_types()
    print(inferred)
    json_file_path = file.replace(".py", "_scalpel.json")

    if os.path.exists(json_file_path):
        print(f"JSON file already exists: {json_file_path}")
        continue

    with open(json_file_path, "w") as json_file:
        inferred_serializable = [
            {k: list(v) if isinstance(v, set) else v for k, v in d.items()}
            for d in inferred
        ]
        json.dump(inferred_serializable, json_file, indent=4)

"""
        # Create a temporary script file
        script_path = "/tmp/script.py"
        with open(script_path, "w") as f:
            f.write(script)

        self.run_test_in_session(self.dockerfile_path, script_path)


runner = ScalpelRunner()
runner.run_tool_test()
