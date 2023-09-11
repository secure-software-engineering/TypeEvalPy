# TypeEvalPy: A Comprehensive Benchmarking Framework for Python Type Inference Tools

TypeEvalPy is a robust benchmarking framework designed to evaluate the accuracy of type inference tools for Python.

## Quick Start

### Environment Setup

1. **Install Dependencies and Set Up Virtual Environment**

   Run the following commands to set up your virtual environment and activate the virtual environment.

   ```bash
   python3 -m venv .env
   ```

   ```bash
   source .env/bin/activate
   ```

   ```bash
   pip install -r requirements.txt
   ```


### Run the Benchmark Analysis

1. **Navigate to the `src` Directory**

   ```bash
   cd src
   ```

2. **Execute the Analyzer**

   Run the following command to start the benchmarking process on all tools:

   ```bash
   python main_runner.py
   ```

   or

   Run analysis on specific tools

   ```
   python main_runner.py --runners headergen hityperdl
   ```

   Available options: headergen, pyright, scalpel, jedi, hityper, type4py, hityperdl

   The results will be generated in the `.results` folder within the root directory of the repository. Each results folder will have a timestamp, allowing you to easily track and compare different runs.
