import os


def is_running_in_docker():
    """Check if Python is running inside a Docker container."""
    return (
        os.path.exists("/.dockerenv")
        or os.environ.get("DOCKER_CONTAINER", False)
        or os.environ.get("DOCKER_IMAGE_NAME", False)
    )
