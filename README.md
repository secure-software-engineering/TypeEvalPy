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

## 🛠️ Supported Tools

| Supported :white_check_mark:                             | In-progress :wrench:                                                 | Planned :bulb:                                        |
| -------------------------------------------------------- | -------------------------------------------------------------------- | ----------------------------------------------------- |
| [HeaderGen](https://github.com/secure-software-engineering/HeaderGen) | [Intellij PSI](https://plugins.jetbrains.com/docs/intellij/psi.html) | [MonkeyType](https://github.com/Instagram/MonkeyType) |
| [Jedi](https://github.com/davidhalter/jedi)              | [Pyre](https://github.com/facebook/pyre-check)                       | [Pyannotate](https://github.com/dropbox/pyannotate)   |
| [Pyright](https://github.com/microsoft/pyright)          | [PySonar2](https://github.com/yinwang0/pysonar2)                     |
| [HiTyper](https://github.com/JohnnyPeng18/HiTyper)       | [Pytype](https://github.com/google/pytype)                           |
| [Scalpel](https://github.com/SMAT-Lab/Scalpel/issues)    | [TypeT5](https://github.com/utopia-group/TypeT5)                     |
| [Type4Py](https://github.com/saltudelft/type4py)         |                                                                      |
| [GPT-4](https://openai.com/research/gpt-4)               |                                                                      |
| [Ollama](https://ollama.ai)                              |                                                                      |

---

---

## 🏆 TypeEvalPy Leaderboard

Below is a comparison showcasing exact matches across different tools, coupled with `top_n` predictions for ML-based tools.

| Rank | 🛠️ Tool                                                         | Top-n       | Function Return Type | Function Parameter Type | Local Variable Type | Total             |
| ---- | --------------------------------------------------------------- | ----------- | -------------------- | ----------------------- | ------------------- | ----------------- |
| 1    | **[HeaderGen](https://github.com/secure-software-engineering/HeaderGen)**    | 1           | 186                  | 56                      | 322                 | 564               |
| 2    | **[Jedi](https://github.com/davidhalter/jedi)**                 | 1           | 122                  | 0                       | 293                 | 415               |
| 3    | **[Pyright](https://github.com/microsoft/pyright)**             | 1           | 100                  | 8                       | 297                 | 405               |
| 4    | **[HiTyper](https://github.com/JohnnyPeng18/HiTyper)**          | 1<br>3<br>5 | 163<br>173<br>175    | 27<br>37<br>37          | 179<br>225<br>229   | 369<br>435<br>441 |
| 5    | **[HiTyper (static)](https://github.com/JohnnyPeng18/HiTyper)** | 1           | 141                  | 7                       | 102                 | 250               |
| 6    | **[Scalpel](https://github.com/SMAT-Lab/Scalpel/issues)**       | 1           | 155                  | 32                      | 6                   | 193               |
| 7    | **[Type4Py](https://github.com/saltudelft/type4py)**            | 1<br>3<br>5 | 39<br>103<br>109     | 19<br>31<br>31          | 99<br>167<br>174    | 157<br>301<br>314 |

_<sub>(Auto-generated based on the the analysis run on 20 Oct 2023)</sub>_

---

## 🏆🤖 TypeEvalPy LLM Leaderboard

Below is a comparison showcasing exact matches for LLMs.

| Rank | 🛠️ Tool                                                                                     | Function Return Type | Function Parameter Type | Local Variable Type | Total |
| ---- | ------------------------------------------------------------------------------------------- | -------------------- | ----------------------- | ------------------- | ----- |
| 1    | **[GPT-4](https://openai.com/research/gpt-4)**                                              | 225                  | 85                      | 465                 | 775   |
| 2    | **[codellama:13b-instruct](https://huggingface.co/docs/transformers/model_doc/code_llama)** | 199                  | 75                      | 425                 | 699   |
| 3    | **[GPT 3.5 Turbo](https://platform.openai.com/docs/models/gpt-3-5-turbo)**                  | 188                  | 73                      | 429                 | 690   |
| 4    | **[codellama:34b-instruct](https://huggingface.co/docs/transformers/model_doc/code_llama)** | 190                  | 52                      | 425                 | 667   |
| 5    | phind-codellama:34b-v2                                                                      | 182                  | 60                      | 399                 | 641   |
| 6    | codellama:7b-instruct                                                                       | 171                  | 72                      | 384                 | 627   |
| 7    | dolphin-mistral                                                                             | 184                  | 76                      | 356                 | 616   |
| 8    | codebooga                                                                                   | 186                  | 56                      | 354                 | 596   |
| 9    | llama2:70b                                                                                  | 168                  | 55                      | 342                 | 565   |
| 10   | **[HeaderGen](https://github.com/secure-software-engineering/HeaderGen)**                                | 186                  | 56                      | 321                 | 563   |
| 11   | wizardcoder:13b-python                                                                      | 170                  | 74                      | 317                 | 561   |
| 12   | llama2:13b                                                                                  | 153                  | 40                      | 283                 | 476   |
| 13   | mistral:instruct                                                                            | 155                  | 45                      | 250                 | 450   |
| 14   | mistral:v0.2                                                                                | 155                  | 45                      | 248                 | 448   |
| 15   | vicuna:13b                                                                                  | 153                  | 35                      | 260                 | 448   |
| 16   | vicuna:33b                                                                                  | 133                  | 29                      | 267                 | 429   |
| 17   | wizardcoder:7b-python                                                                       | 103                  | 48                      | 254                 | 405   |
| 18   | llama2:7b                                                                                   | 140                  | 34                      | 216                 | 390   |
| 19   | **[HiTyper](https://github.com/JohnnyPeng18/HiTyper)**                                      | 163                  | 27                      | 179                 | 369   |
| 20   | wizardcoder:34b-python                                                                      | 140                  | 43                      | 178                 | 361   |
| 21   | orca2:7b                                                                                    | 117                  | 27                      | 184                 | 328   |
| 22   | vicuna:7b                                                                                   | 131                  | 17                      | 172                 | 320   |
| 23   | orca2:13b                                                                                   | 113                  | 19                      | 166                 | 298   |
| 24   | tinyllama                                                                                   | 3                    | 0                       | 23                  | 26    |
| 25   | phind-codellama:34b-python                                                                  | 5                    | 0                       | 15                  | 20    |
| 26   | codellama:13b-python                                                                        | 0                    | 0                       | 0                   | 0     |
| 27   | codellama:34b-python                                                                        | 0                    | 0                       | 0                   | 0     |
| 28   | codellama:7b-python                                                                         | 0                    | 0                       | 0                   | 0     |

_<sub>(Auto-generated based on the the analysis run on 14 Jan 2024)</sub>_

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

### 🤝 Contributing

Thank you for your interest in contributing! To add support for a new tool, please utilize the Docker templates provided in our repository. After implementing and testing your tool, please submit a pull request (PR) with a descriptive message. Our maintainers will review your submission, and merge them.

---

### ⭐️ Show Your Support

Give a ⭐️ if this project helped you!
