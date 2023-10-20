# TypeEvalPy: A Micro-benchmarking Framework for Python Type Inference Tools

<p align="center">
<img src="TypeEvalPy.jpg" width="60%" align="center">
</p>


## 📌 **Key Features**:
- 📜 Contains **154 code snippets** to test and benchmark.
- 🏷 Offers **845 type annotations** across a diverse set of Python functionalities.
- 📂 Organized into **18 distinct categories** targeting various Python features.
- 🚢 Seamlessly manages the execution of **containerized tools**.
- 🔄 Efficiently transforms inferred types into a **standardized format**.
- 📊 Produces **meaningful metrics** for in-depth assessment and comparison.

---

## 🏆 TypeEvalPy Leaderboard

Below is a comparison showcasing exact matches across different tools, coupled with `top_n` predictions for our ML-based tools.

[INSERT_TABLE_HERE]

---

## 📥 Installation

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

---

## 🚀 Usage: Running the Analysis

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

---

### 🤝 Contributing

Thank you for your interest in contributing! To add support for a new tool, please utilize the Docker templates provided in our repository. After implementing and testing your tool, please submit a pull request (PR) with a descriptive message. Our maintainers will review your submission, and merge them.

---

### ⭐️ Show Your Support

Give a ⭐️ if this project helped you!
