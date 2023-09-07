# TypeEvalPy: A Comprehensive Benchmarking Framework for Python Type Inference Tools

TypeEvalPy is a robust benchmarking framework designed to evaluate the accuracy of type inference tools for Python.

## Quick Start

### Environment Setup

1. **Install Dependencies and Set Up Virtual Environment**

   Run the following command to set up your virtual environment, install required packages, and add pre-commit hooks.

   ```bash
   ./setup.sh -i
   ```

2. **Activate Virtual Environment**

   To activate the virtual environment you've just created, execute:

   ```bash
   source .env/bin/activate
   ```

### Run the Benchmark Analysis

1. **Navigate to the `src` Directory**

   ```bash
   cd src
   ```

2. **Execute the Analyzer**

   Run the following command to start the benchmarking process:

   ```bash
   python main_runner.py
   ```

   The results will be generated in the `.results` folder within the root directory of the repository. Each results folder will have a timestamp, allowing you to easily track and compare different runs.
