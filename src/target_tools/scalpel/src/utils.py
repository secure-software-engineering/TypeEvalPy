import json
import os


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


def keep_unique_dicts(dicts):
    seen = set()
    unique_dicts = []
    for d in dicts:
        json_str = json.dumps(d, sort_keys=True)
        if json_str not in seen:
            seen.add(json_str)
            unique_dicts.append(d)
    return unique_dicts
