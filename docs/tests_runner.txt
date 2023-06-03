# Script
# - Starts docker containers,
#   - Use docker API to spawn containers
#   - Can use ssh or someother interactive session
# - Runs tests from micro-benchmark
#  - Define a common interface for running tests
# - Translate result format to TypeEvalPy's format
# - Output to a common folder
# - Analysis of the results


class TypeEvalPyRunner:
    def __init__(self) -> None:
        self.dockerfile_name = ""

    def _spawn_docker_instance(self) -> None:
        pass

    def run_test_in_session(self) -> None:
        pass

    def translate_result_to_typeevalpy(self) -> None:
        pass


# class ScalpelRunner(TypeEvalPyRunner):
