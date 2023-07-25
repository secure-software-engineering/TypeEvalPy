import os
import json
import re


def is_running_in_docker():
    """Check if Python is running inside a Docker container."""
    return (
        os.path.exists("/.dockerenv")
        or os.environ.get(  # Check if the /.dockerenv file exists
            "DOCKER_CONTAINER", False
        )
        or os.environ.get(  # Check if DOCKER_CONTAINER environment variable is set
            "DOCKER_IMAGE_NAME", False
        )  # Check if DOCKER_IMAGE_NAME environment variable is set
    )


def format_type(type):
    pattern = r"Callable\(.*?\)\[.*?,\s*typing\.(\w+)]"
    match = re.search(pattern, type)
    if match:
        type = match.group(1)
    return type


def generate_json_file(filename, type_info):
    # Generate JSON file with type information
    json_data = json.dumps(type_info, indent=4)
    with open(filename, "w") as file:
        file.write(json_data)
