# Integrating a New Tool into TypeEvalPy Using Docker Template

## Introduction

This document outlines the process for incorporating a new tool into the TypeEvalPy framework. Integration involves creating a dedicated directory structure within the `target_tools` folder, configuring Docker, and extending the `TypeEvalPyRunner` class to accommodate the new tool.

## Step-by-Step Guide

### Step 1: Set Up the Tool's Directory Structure

Begin by creating a new directory for your tool in the `target_tools` folder. The directory should include a `src` folder, a Dockerfile, and a `requirements.txt` file for dependencies. Simply start by duplicating the `docker_template` folder. Here's how your structure should look:

```
target_tools/
└── new_tool/
    ├── src/
    ├── Dockerfile
    └── requirements.txt
```

Within the `src` directory, include the following files:

- `runner.py`: Handles type inference operations.
- `translator.py`: Transforms the tool's output into TypeEvalPy's standard format.
- `util.py`: Provides utility functions for common tasks across modules.

**Key Components:**

- **Runner:** The `runner.py` executes tool logic and outputs type inference results.
- **Translator:** The `translator.py` includes functions like `translate_content(file_path)` for converting tool outputs to TypeEvalPy format and `main_translator(args)` for managing the translation process.
- **Utils:** The `util.py` contains shared utility functions.

### Step 2: Configure Docker

Place a Dockerfile within your tool's directory to define the environment. It should specify the base image, environment variables, work directory, dependencies, and source code copying.

The provided Dockerfile template in `docker_template` outlines the basic setup for a Python-based tool environment. Modify it according to your specific project needs.

### Step 3: List Dependencies

Create a `requirements.txt` file inside your `new_tool` directory. This file should enumerate all necessary Python packages required by your new tool.

### Step 4: Integrate the Tool with the Runner Class

Extend the `TypeEvalPyRunner` base class to include your tool. This involves setting up a new runner class, handling tool-specific command-line arguments, and registering the tool in the main execution flow.

**Implementation Steps:**

1. **Define a New Runner Class:** Create a class that inherits from `TypeEvalPyRunner`, specifying tool details and any necessary initialization parameters.

    ```python
    class NewToolRunner(TypeEvalPyRunner):
        def __init__(self, host_results_path, debug=False, nocache=False):
            super().__init__("new_tool", "./target_tools/new_tool", host_results_path, nocache=nocache)
    ```

2. **Update Command-Line Arguments:** If your tool requires special arguments, enhance the `get_args` function to include them.

3. **Register the New Tool:** Add your new tool to the `available_runners` dictionary within the main function to ensure it's recognized and runnable.

    ```python
    "new_tool": (
        NewToolRunner,
        {"debug": args.debug, "nocache": args.nocache, "config": config},
    ),
    ```

4. **Configuration Handling:** If additional configuration is needed, adjust the runner class to manage these settings effectively.

This guide provides a structured approach to adding new tools to the TypeEvalPy project, ensuring seamless integration and functionality within the existing framework.

### Step 5: Make sure the results are translated into TypeEvalPy schema

The output of your tool should match the JSON schema of TypeEvalPy. The pydantic schema is available in the following file: [docs/TypeEvalPy_JSON_schema.py](docs/TypeEvalPy_JSON_schema.py)
