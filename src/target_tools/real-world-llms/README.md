# 🧠 TypeEvalPy: Type Inference Evaluation for Python

This adapter provides tools for:
- Preprocessing the [ManyTypes4Py](https://github.com/saltudelft/many-types-4-py) dataset
- Running type inference using large language models (LLMs)
- Analyzing and evaluating results on real-world Python benchmarks

---

## 📦 1. Data Preprocessing

Start by downloading and preparing the [ManyTypes4Py](https://github.com/saltudelft/many-types-4-py) dataset.

### Steps:

1. Clone the dataset repository:
   ```bash
   git clone https://github.com/saltudelft/many-types-4-py
   cd many-types-4-py

2.	Run the preprocessing script to generate ground truth files for training, validation, and testing:

```bash
python3 prepare_dataset.py
```

This will create the required train, test, and valid files with annotated types.


## 🚀 2. Running Model Inference

Use the `runner.py` script to run inference using various LLMs on your benchmark dataset.

```bash
python3.10 runner.py \
--bechmark_path /mnt/hf_cache/rashida_manytype4py/many-types-4-py-dataset/rw-benchmark \
--prompt_id prompt_template_questions_based_2 \
--models codestral-v0.1-22b qwen2.5-Coder-7B-Instruct \
--hf_token <your_huggingface_token> \
--openai_key <your_openai_api_key> \
--enable_streaming True \
--models_config /home/ssegpu/rashida/TypeEvalPy/src/target_tools/real-world-llms/src/models_config.yaml \
--results_dir /home/ssegpu/rashida/TypeEvalPy/results
```

🔑 Note: Replace <your_huggingface_token> and <your_openai_api_key> with your actual API credentials.

## 📊 3. Result Evaluation

After inference is complete, go to result_analyzer module and evaluate the predictions using:

```bash
python3 large_scale_analysis.py
```

This will generate ```analysis.txt``` in the model results.