<p align="center">
<img src="TypeEvalPy.jpg" width="75%" align="center">
<br>

<h3 align="center"> A Micro-benchmarking Framework for Python Type Inference Tools </h3>
</p>

## 📌 **Features**:

- 📜 Contains **154 code snippets** to test and benchmark.
- 🏷 Offers **845 type annotations** across a diverse set of Python functionalities.
- 📂 Organized into **18 distinct categories** targeting various Python features.
- 🚢 Seamlessly manages the execution of **containerized tools**.
- 🔄 Efficiently transforms inferred types into a **standardized format**.
- 📊 Automatically produces **meaningful metrics** for in-depth assessment and comparison.

### [New] TypeEvalPy Autogen

- 🤖 **Autogenerates code snippets** and ground truth to scale the benchmark based on the original `TypeEvalPy` benchmark.
- 📈 The autogen benchmark now contains:
  - **Python files**: 7121
  - **Type annotations**: 78373

## 🛠️ Supported Tools

| Supported :white_check_mark:                                          | In-progress :wrench:                                                 | Planned :bulb:                                        |
| --------------------------------------------------------------------- | -------------------------------------------------------------------- | ----------------------------------------------------- |
| [HeaderGen](https://github.com/secure-software-engineering/HeaderGen) | [Intellij PSI](https://plugins.jetbrains.com/docs/intellij/psi.html) | [MonkeyType](https://github.com/Instagram/MonkeyType) |
| [Jedi](https://github.com/davidhalter/jedi)                           | [Pyre](https://github.com/facebook/pyre-check)                       | [Pyannotate](https://github.com/dropbox/pyannotate)   |
| [Pyright](https://github.com/microsoft/pyright)                       | [PySonar2](https://github.com/yinwang0/pysonar2)                     |
| [HiTyper](https://github.com/JohnnyPeng18/HiTyper)                    | [Pytype](https://github.com/google/pytype)                           |
| [Scalpel](https://github.com/SMAT-Lab/Scalpel/issues)                 | [TypeT5](https://github.com/utopia-group/TypeT5)                     |
| [Type4Py](https://github.com/saltudelft/type4py)                      |                                                                      |
| [GPT](https://openai.com)                                             |                                                                      |
| [Ollama](https://ollama.ai)                                           |                                                                      |
| [RightTyper](https://github.com/RightTyper/RightTyper)                |                                                                      |

---

## 🏆 TypeEvalPy Leaderboard

Below is a comparison showcasing exact matches across different tools and LLMs on the Autogen benchmark.

| Rank | 🛠️ Tool                                                                                        | Function Return Type | Function Parameter Type | Local Variable Type | Total |
| ---- | ---------------------------------------------------------------------------------------------- | -------------------- | ----------------------- | ------------------- | ----- |
| 1    | **[mistral-large-it-2407-123b](https://huggingface.co/mistralai/Mistral-Large-Instruct-2407)** | 16701                | 728                     | 57550               | 74979 |
| 2    | **[qwen2-it-72b](https://huggingface.co/Qwen/Qwen2-72B-Instruct)**                             | 16488                | 629                     | 55160               | 72277 |
| 3    | **[llama3.1-it-70b](https://huggingface.co/meta-llama/Meta-Llama-3.1-70B-Instruct)**           | 16648                | 580                     | 54445               | 71673 |
| 4    | **[gemma2-it-27b](https://huggingface.co/google/gemma-2-27b-it)**                              | 16342                | 599                     | 49772               | 66713 |
| 5    | **[codestral-v0.1-22b](https://huggingface.co/mistralai/Codestral-22B-v0.1)**                  | 16456                | 706                     | 49379               | 66541 |
| 6    | **[codellama-it-34b](https://huggingface.co/meta-llama/CodeLlama-34b-Instruct-hf)**            | 15960                | 473                     | 48957               | 65390 |
| 7    | **[mistral-nemo-it-2407-12.2b](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407)**  | 16221                | 526                     | 48439               | 65186 |
| 8    | **[mistral-v0.3-it-7b](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3)**            | 16686                | 472                     | 47935               | 65093 |
| 9    | **[phi3-medium-it-14b](https://huggingface.co/microsoft/Phi-3-medium-128k-instruct)**          | 16802                | 467                     | 45121               | 62390 |
| 10   | **[llama3.1-it-8b](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct)**             | 16125                | 492                     | 44313               | 60930 |
| 11   | **[codellama-it-13b](https://huggingface.co/meta-llama/CodeLlama-13b-Instruct-hf)**            | 16214                | 479                     | 43021               | 59714 |
| 12   | **[phi3-small-it-7.3b](https://huggingface.co/microsoft/Phi-3-small-128k-instruct)**           | 16155                | 422                     | 38093               | 54670 |
| 13   | **[qwen2-it-7b](https://huggingface.co/Qwen/Qwen2-7B-Instruct)**                               | 15684                | 313                     | 38109               | 54106 |
| 14   | **[HeaderGen](https://github.com/ashwinprasadme/headergen)**                                   | 14086                | 346                     | 36370               | 50802 |
| 15   | **[phi3-mini-it-3.8b](https://huggingface.co/microsoft/Phi-3-mini-128k-instruct)**             | 15908                | 320                     | 30341               | 46569 |
| 16   | **[phi3.5-mini-it-3.8b](https://huggingface.co/microsoft/Phi-3.5-mini-instruct)**              | 15763                | 362                     | 28694               | 44819 |
| 17   | **[codellama-it-7b](https://huggingface.co/meta-llama/CodeLlama-7b-Instruct-hf)**              | 13779                | 318                     | 29346               | 43443 |
| 18   | **[Jedi](https://github.com/davidhalter/jedi)**                                                | 13160                | 0                       | 15403               | 28563 |
| 19   | **[Scalpel](https://github.com/SMAT-Lab/Scalpel/issues)**                                      | 15383                | 171                     | 18                  | 15572 |
| 20   | **[gemma2-it-9b](https://huggingface.co/google/gemma-2-9b-it)**                                | 1611                 | 66                      | 5464                | 7141  |
| 21   | **[Type4Py](https://github.com/saltudelft/type4py)**                                           | 3143                 | 38                      | 2243                | 5424  |
| 22   | **[tinyllama-1.1b](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)**                | 1514                 | 28                      | 2699                | 4241  |
| 23   | **[mixtral-v0.1-it-8x7b](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1)**        | 3235                 | 33                      | 377                 | 3645  |
| 24   | **[phi3.5-moe-it-41.9b](https://huggingface.co/microsoft/Phi-3.5-MoE-instruct)**               | 3090                 | 25                      | 273                 | 3388  |
| 25   | **[gemma2-it-2b](https://huggingface.co/google/gemma-2-2b-it)**                                | 1497                 | 41                      | 1848                | 3386  |

_<sub>(Auto-generated based on the the analysis run on 30 Aug 2024)</sub>_

---

## :whale: Running with Docker

### 1️⃣ Clone the repo

```bash
git clone https://github.com/secure-software-engineering/TypeEvalPy.git
```

### 2️⃣ Build Docker image

```bash
docker build -t typeevalpy .
```

### 3️⃣ Run TypeEvalPy

🕒 Takes about 30mins on first run to build Docker containers.

📂 Results will be generated in the `results` folder within the root directory of the repository.
Each results folder will have a timestamp, allowing you to easily track and compare different runs.

<details>
  <summary><b>Correlation of CSV Files Generated to Tables in ICSE Paper</b></summary>
Here is how the auto-generated CSV tables relate to the paper's tables:

- **Table 1** in the paper is derived from three auto-generated CSV tables:

  - `paper_table_1.csv` - details Exact matches by type category.
  - `paper_table_2.csv` - lists Exact matches for 18 micro-benchmark categories.
  - `paper_table_3.csv` - provides Sound and Complete values for tools.

- **Table 2** in the paper is based on the following CSV table:
  - `paper_table_5.csv` - shows Exact matches with top_n values for machine learning tools.

Additionally, there are CSV tables that are _not_ included in the paper:

- `paper_table_4.csv` - containing Sound and Complete values for 18 micro-benchmark categories.
- `paper_table_6.csv` - featuring Sensitivity analysis.
</details>

```bash
docker run \
      -v /var/run/docker.sock:/var/run/docker.sock \
      -v ./results:/app/results \
      typeevalpy
```

🔧 **Optionally**, run analysis on specific tools:

```bash
docker run \
      -v /var/run/docker.sock:/var/run/docker.sock \
      -v ./results:/app/results \
      typeevalpy --runners headergen scalpel
```

📊 Run analysis on custom benchmarks:

Here, running with the autogen benchmark on HeaderGen

```bash
docker run \
      -v /var/run/docker.sock:/var/run/docker.sock \
      -v ./results:/app/results \
      typeevalpy \
      --runners headergen \
      --custom_benchmark_dir /app/autogen_typeevalpy_benchmark
```

🛠️ Available options: `headergen`, `pyright`, `scalpel`, `jedi`, `hityper`, `type4py`, `hityperdl`

### 🤖 Running TypeEvalPy with LLMs

TypeEvalPy integrates with LLMs through Ollama, streamlining their management. Begin by setting up your environment:

- Create Configuration File: Copy the `config_template.yaml` from the src directory and rename it to `config.yaml`.

In the `config.yaml`, configure in the following:

- `openai_key`: your key for accessing OpenAI's models.
- `ollama_url`: the URL for your Ollama instance. For simplicity, we recommend deploying Ollama using their Docker container. [Get started with Ollama here](https://hub.docker.com/r/ollama/ollama).
- `prompt_id`: set this to `questions_based_2` for optimal performance, based on our tests.
- `ollama_models`: select a list of model tags from the [Ollama library](https://ollama.com/library). For better operation, ensure the model is pre-downloaded with the `ollama pull` command.

With the `config.yaml` configured, run the following command:

```bash
docker run \
      -v /var/run/docker.sock:/var/run/docker.sock \
      -v ./results:/app/results \
      typeevalpy --runners ollama
```

---

<details>
  <summary><b>Running From Source...</b></summary>

## 1. 📥 Installation

1.  **Clone the repo**

    ```bash
    git clone https://github.com/secure-software-engineering/TypeEvalPy.git
    ```

2.  **Install Dependencies and Set Up Virtual Environment**

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

## 2. 🚀 Usage: Running the Analysis

1.  **Navigate to the `src` Directory**

    ```bash
    cd src
    ```

2.  **Execute the Analyzer**

    Run the following command to start the benchmarking process on all tools:

    ```bash
    python main_runner.py
    ```

    or

    Run analysis on specific tools

    ```
    python main_runner.py --runners headergen scalpel
    ```

</details>

---

## Running TypeEvalPy Autogen

To generate an extended version of the original TypeEvalPy benchmark to include many more Python types, run the following commands:

1.  **Navigate to the `autogen` Directory**

    ```bash
    cd autogen
    ```

2.  **Execute the Generation Script**

    Run the following command to start the generation process:

    ```bash
    python generate_typeevalpy_dataset.py
    ```

This will generate a folder in the repo root with the autogen benchmark with the current date.

---

### Running TypeEvalPy with ManyType4Py dataset

To run the LLM based Type Inference for ManyType4Py dataset, please follow the guide here : [src/target_tools/real-world-llms/README.md](src/target_tools/real-world-llms/README.md)

---

### 🤝 Contributing

Thank you for your interest in contributing! To add support for a new tool, please utilize the Docker templates provided in our repository. After implementing and testing your tool, please submit a pull request (PR) with a descriptive message. Our maintainers will review your submission, and merge them.

To get started with integrating your tool, please follow the guide here: [docs/Tool_Integration_Guide.md](docs/Tool_Integration_Guide.md)

---

### ⭐️ Show Your Support

Give a ⭐️ if this project helped you!
