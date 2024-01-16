# Project Tool Integration using Docker Template

## Overview

This guide describes the steps to add a new tool to the  TypeEvalPy project using. To integrate the tool into the project, create a specific folder within the `target_tools` directory. The folder should contain a `src` directory, a Dockerfile, and a `requirements.txt` file. Additionally, the new tool should also be added to the `runner_class` by extending the base class `TypeEvalPyRunner`, and the path to the tools folder location should be provided while extending the base class.

## Steps

## 1. Create Tool Structure

Create a folder for the new tool inside the `target_tools` directory. The structure should be as follows:

```plaintext
 target_tools/
 │
 └── * new_tool */
         ├── src/
         ├── Dockerfile
         └── requirements.txt
```

### Src directory
 ```plaintext
src/
   ├── runner.py
   ├── translator.py
   └── util.py
```

#### Runner
The `runner.py` file contains the code responsible for performing the type inference. This module interacts with the input, executes the tool-specific logic, and produces the type inference results.


#### Translator
The `translator.py` file contains the code to convert the output received from the tool to the TypeEvalPy standard format. This is crucial for ensuring consistency in the output format across different tools. the main components for the translator system are as follows.

The `translate_content(file_path)` function reads a JSON file, performs the actual translation from the tools output to the format acceptable by `TypeEvalPy`, and returns the modified content.

The `main_translator(args)` function orchestrates the translation process. It retrieves JSON files, attempts translation, prints errors, and displays the total error count.


#### Utils
The `util.py` file consists of utility functions that can be shared across different modules in the tool. These functions can include common functionalities that are not specific to the core logic of type inference or translation.

## 2: Docker Configuration

The `Dockerfile` stores the Docker settings for the new tool and this folder should be situated within the tool directory, and contain instructions on specifying the necessary setup steps, setting the working directory, installing dependencies, copying the source code, and defining the entry point. The docker file within the `docker_template` contains all the configs that should be covered. Below are the exmaple steps from the docker template.

####  Pull Python Base Image

```dockerfile
FROM python:3.10-slim-bullseye
```

#### Set Environment Variables

```dockerfile
ENV PYTHONDONTWRITEBYTECODE 1 \
    && ENV PYTHONUNBUFFERED 1
```

####  Set Work Directory

```dockerfile
WORKDIR /app
```

#### Install Dependencies

```dockerfile
RUN apt-get update \
   && apt-get -y install gcc
```

```dockerfile
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
    && pip install -r requirements.txt
```

####  Copy Source Code

```dockerfile
COPY src /tmp/src
```

####  Keep Container Alive

```dockerfile
CMD ["bash"]
```

This Dockerfile serves as a starting point for a containerized Python environment. Customize it based on your project's requirements.


## 3: Requirements File
Inside the new_tool folder, create a requirements.txt file listing the tool-specific dependencies, which can be installed to effectively setup the new type evaluation tool.


## 4 : Adding the tool in the Runner Class

After setting up the folder structure, add the tool to the runner by creating a new class for the tool that is being added which extends the base class `TypeEvalPyRunner`. The `TypeEvalPyRunner` class is a Python class that facilitates the execution and benchmarking of a specified tool within a Docker container, handling image building, container creation, external library setup, test execution, result retrieval, and container cleanup. The functions in the base class can be modified as per required or new functions can also added to the new class.

To add a new tool to the project, follow these steps:

###  Create a New Runner Class

Define a new class for the tool runner, similar to existing ones. The class should include a \`run_tool_test\` method for performing tool-specific tests.

```python
class NewToolRunner(TypeEvalPyRunner):
    def __init__(self, host_results_path, debug=False, nocache=False):
        super().__init__(
            "new_tool", "./target_tools/new_tool", host_results_path, nocache=nocache
        )
```

###  Update `get_args` Function

If the new tool requires additional command-line arguments, update the `get_args` function to include those arguments.

```python
parser.add_argument(
    "--new_tool-arg",
    type=str,
    help="Additional argument for the new tool.",
)
```

Make sure to handle the new argument appropriately in the `args` object.

### Update `available_runners` Dictionary in `main` Function

Add an entry for the new tool runner in the `available_runners` dictionary.

```python
"new_tool": (
    NewToolRunner,
    {"debug": args.debug, "nocache": args.nocache, "config": config},
),
```

Replace `"new_tool"` with the actual name for the new tool.


###  Handle Configuration (Optional)

If the new tool requires additional configuration options, handle them appropriately. For example, update the `config` parameter in the runner class.