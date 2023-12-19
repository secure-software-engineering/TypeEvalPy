# %%
# https://blog.ovhcloud.com/fine-tuning-llama-2-models-using-a-single-gpu-qlora-and-ai-notebooks/

# %%
# pip install huggingface_hub trl transformers accelerate peft datasets bitsandbytes einops wandb scipy ipywidgets

# %% [markdown]
# ## Imports

# %%
import argparse
import bitsandbytes as bnb
from datasets import load_dataset
from functools import partial
import os
import time
import logging
from sys import stdout
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training, AutoPeftModelForCausalLM
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, set_seed, Trainer, TrainingArguments, BitsAndBytesConfig, \
    DataCollatorForLanguageModeling, Trainer, TrainingArguments
from datasets import load_dataset

# %%
logger = logging.getLogger("runner")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("llama_fine_tuning.log", mode="w")
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler(stdout)
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# %% [markdown]
# ### Test CUDA

# %%
import torch
use_cuda = torch.cuda.is_available()
device = torch.device("cuda" if use_cuda else "cpu")
logger.info(f"Using device: {device}")

# %% [markdown]
# ## Login to huggingface
# When prompted, paste the HF access token you created earlier.
# 

# %%
from huggingface_hub import login
import os
login(os.getenv("OLLAMA_TOKEN"))

# %% [markdown]
# ## Load dataset 

# %%
dataset_name = "ashwinprasadme/typeevalpy_finetuning"
dataset = load_dataset(dataset_name, split="train", token=True)

logger.info(f'Number of prompts: {len(dataset)}')
logger.info(f'Column names are: {dataset.column_names}')

# %% [markdown]
# ## Dataset preparation functions

# %%
# SOURCE https://github.com/databrickslabs/dolly/blob/master/training/trainer.py
def get_max_length(model):
    conf = model.config
    max_length = None
    for length_setting in ["n_positions", "max_position_embeddings", "seq_length"]:
        max_length = getattr(model.config, length_setting, None)
        if max_length:
            logger.info(f"Found max lenth: {max_length}")
            break
    if not max_length:
        max_length = 1024
        logger.info(f"Using default max length: {max_length}")
    return max_length


def preprocess_batch(batch, tokenizer, max_length):
    """
    Tokenizing a batch
    """
    return tokenizer(
        batch["text"],
        max_length=max_length,
        truncation=True,
    )


# SOURCE https://github.com/databrickslabs/dolly/blob/master/training/trainer.py
def preprocess_dataset(tokenizer: AutoTokenizer, max_length: int, seed, dataset: str):
    """Format & tokenize it so it is ready for training
    :param tokenizer (AutoTokenizer): Model Tokenizer
    :param max_length (int): Maximum number of tokens to emit from tokenizer
    """
    
    # Add prompt to each sample
    logger.info("Preprocessing dataset...")
    
    # Apply preprocessing to each batch of the dataset & and remove 'instruction', 'context', 'response', 'category' fields
    _preprocessing_function = partial(preprocess_batch, max_length=max_length, tokenizer=tokenizer)
    dataset = dataset.map(
        _preprocessing_function,
        batched=True,
    )

    # Filter out samples that have input_ids exceeding max_length
    dataset = dataset.filter(lambda sample: len(sample["input_ids"]) < max_length)
    
    # Shuffle dataset
    dataset = dataset.shuffle(seed=seed)

    return dataset

# %% [markdown]
# ## Training functions

# %%
def load_model(model_name, bnb_config):
    n_gpus = torch.cuda.device_count()
    max_memory = f'{40960}MB'

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=bnb_config,
        device_map="auto", # dispatch efficiently the model on the available ressources
        max_memory = {i: max_memory for i in range(n_gpus)},
        offload_folder="offload"
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=True)

    # Needed for LLaMA tokenizer
    tokenizer.pad_token = tokenizer.eos_token

    return model, tokenizer


def create_bnb_config():
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
    )

    return bnb_config


def create_peft_config(modules):
    """
    Create Parameter-Efficient Fine-Tuning config for your model
    :param modules: Names of the modules to apply Lora to
    """
    config = LoraConfig(
        r=16,  # dimension of the updated matrices
        lora_alpha=64,  # parameter for scaling
        target_modules=modules,
        lora_dropout=0.1,  # dropout probability for layers
        bias="none",
        task_type="CAUSAL_LM",
    )

    return config


def find_all_linear_names(model):
    cls = bnb.nn.Linear4bit #if args.bits == 4 else (bnb.nn.Linear8bitLt if args.bits == 8 else torch.nn.Linear)
    lora_module_names = set()
    for name, module in model.named_modules():
        if isinstance(module, cls):
            names = name.split('.')
            lora_module_names.add(names[0] if len(names) == 1 else names[-1])

    if 'lm_head' in lora_module_names:  # needed for 16-bit
        lora_module_names.remove('lm_head')
    return list(lora_module_names)


def print_trainable_parameters(model, use_4bit=False):
    """
    Prints the number of trainable parameters in the model.
    """
    trainable_params = 0
    all_param = 0
    for _, param in model.named_parameters():
        num_params = param.numel()
        # if using DS Zero 3 and the weights are initialized empty
        if num_params == 0 and hasattr(param, "ds_numel"):
            num_params = param.ds_numel

        all_param += num_params
        if param.requires_grad:
            trainable_params += num_params
    if use_4bit:
        trainable_params /= 2
    logger.info(
        f"all params: {all_param:,d} || trainable params: {trainable_params:,d} || trainable%: {100 * trainable_params / all_param}"
    )

# %%
def train(model, tokenizer, dataset, output_dir):
    # Apply preprocessing to the model to prepare it by
    # 1 - Enabling gradient checkpointing to reduce memory usage during fine-tuning
    model.gradient_checkpointing_enable()

    # 2 - Using the prepare_model_for_kbit_training method from PEFT
    model = prepare_model_for_kbit_training(model)

    # Get lora module names
    modules = find_all_linear_names(model)

    # Create PEFT config for these modules and wrap the model to PEFT
    peft_config = create_peft_config(modules)
    model = get_peft_model(model, peft_config)
    
    # Print information about the percentage of trainable parameters
    print_trainable_parameters(model)
    
    # Training parameters
    trainer = Trainer(
        model=model,
        train_dataset=dataset,
        args=TrainingArguments(
            per_device_train_batch_size=1,
            gradient_accumulation_steps=4,
            warmup_steps=2,
            max_steps=20,
            learning_rate=2e-4,
            fp16=True,
            logging_steps=1,
            output_dir="outputs",
            optim="paged_adamw_8bit",
        ),
        data_collator=DataCollatorForLanguageModeling(tokenizer, mlm=False)
    )
    
    model.config.use_cache = False  # re-enable for inference to speed up predictions for similar inputs
    
    ### SOURCE https://github.com/artidoro/qlora/blob/main/qlora.py
    # Verifying the datatypes before training
    
    dtypes = {}
    for _, p in model.named_parameters():
        dtype = p.dtype
        if dtype not in dtypes: dtypes[dtype] = 0
        dtypes[dtype] += p.numel()
    total = 0
    for k, v in dtypes.items(): total+= v
    for k, v in dtypes.items():
        print(k, v, v/total)
     
    do_train = True
    
    # Launch training
    logger.info("Training...")
    
    if do_train:
        train_result = trainer.train()
        metrics = train_result.metrics
        trainer.log_metrics("train", metrics)
        trainer.save_metrics("train", metrics)
        trainer.save_state()
        logger.info(metrics)    
    
    ###
    
    # Saving model
    logger.info("Saving last checkpoint of the model...")
    os.makedirs(output_dir, exist_ok=True)
    trainer.model.save_pretrained(output_dir)
    
    # Free memory for merging weights
    del model
    del trainer
    torch.cuda.empty_cache()

# %% [markdown]
# ## Load model

# %%
models_list = [
    "codellama/CodeLlama-7b-Instruct-hf",
    "codellama/CodeLlama-13b-Instruct-hf",
    "codellama/CodeLlama-34b-Instruct-hf",
    "codellama/CodeLlama-7b-Python-hf",
    "codellama/CodeLlama-13b-Python-hf",
    "codellama/CodeLlama-34b-Python-hf",
    "meta-llama/Llama-2-7b-hf",
    "meta-llama/Llama-2-13b-hf",
    "meta-llama/Llama-2-70b-hf",
    "lmsys/vicuna-7b-v1.5",
    "lmsys/vicuna-13b-v1.5",
    "lmsys/vicuna-33b-v1.3",
    "Phind/Phind-CodeLlama-34B-v2",
    "Phind/Phind-CodeLlama-34B-Python-v1",
    "WizardLM/WizardCoder-Python-7B-V1.0",
    "WizardLM/WizardCoder-Python-13B-V1.0",
    "WizardLM/WizardCoder-Python-34B-V1.0",
    "microsoft/Orca-2-7b",
    "microsoft/Orca-2-13b",
]

# top_10 = [
#     "codellama/CodeLlama-13b-Instruct-hf",
#     "codellama/CodeLlama-34b-Instruct-hf",
#     "codellama/CodeLlama-7b-Instruct-hf",
#     "Phind/Phind-CodeLlama-34B-v2",
#     "WizardLM/WizardCoder-Python-13B-V1.0",
#     "meta-llama/Llama-2-70b-hf",
#     "codellama/CodeLlama-13b-Python-hf",
#     "meta-llama/Llama-2-13b-hf",
# ]

# models_list = top_10
# models_list = [
#     "codellama/CodeLlama-7b-Instruct-hf",
# ]

# %%
# Load model from HF with user's token and with bitsandbytes config

ft_version = "ag_model_inst"

output_dir_str = "/scratch/hpc-prf-hdgen/ashwin/finetuned_models/{ft_version}_{model_name}"
output_dir_merged_str = "/scratch/hpc-prf-hdgen/ashwin/finetuned_models/{ft_version}_{model_name}_merged"
output_dir_ollama_str = "/scratch/hpc-prf-hdgen/ashwin/finetuned_models/ollama_models"
llama_cpp_convert_path = "/scratch/hpc-prf-hdgen/ashwin/llama.cpp/convert.py"

os.makedirs(output_dir_ollama_str, exist_ok=True)

start_time = time.time()
for model_name in models_list:
    try:
        logger.info(f"Processing Model: {model_name}")
        # model_name = "meta-llama/Llama-2-7b-hf" 
        bnb_config = create_bnb_config()
        model, tokenizer = load_model(model_name, bnb_config)
    
        # Preprocess dataset
        logger.info("Preprocess dataset")
        max_length = get_max_length(model)
        dataset = preprocess_dataset(tokenizer, max_length, 0, dataset)
    
        # Start training
        logger.info("Start training")
        output_dir = output_dir_str.format(model_name=model_name.split("/")[1], ft_version=ft_version)
        train(model, tokenizer, dataset, output_dir)
    
        # Save and Merge Model
        logger.info("Save and Merge Model")
        model = AutoPeftModelForCausalLM.from_pretrained(output_dir, device_map="auto", torch_dtype=torch.bfloat16)
        model = model.merge_and_unload()
    
        output_merged_dir = output_dir_merged_str.format(model_name=model_name.split("/")[1], ft_version=ft_version)
        os.makedirs(output_merged_dir, exist_ok=True)
        model.save_pretrained(output_merged_dir, safe_serialization=True)
    
        # save tokenizer for easy inference
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        tokenizer.save_pretrained(output_merged_dir)
    except Exception as e:
        logger.info(f"Error training: {model_name}")
        logger.info(e)


import subprocess

def run_system_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        return result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        return "", str(e)

for model_name in models_list:
    try:
        output_merged_dir = output_dir_merged_str.format(model_name=model_name.split("/")[1], ft_version=ft_version)
        output_dir_ollama_dir = f"{output_dir_ollama_str}/{ft_version}_{model_name.split('/')[1]}.gguf"
        output_dir_ollama_modelfile_str = f"{output_dir_ollama_str}/{ft_version}_{model_name.split('/')[1]}.modelfile"

        with open(output_dir_ollama_modelfile_str, 'w') as file:
            # Writing content to the file
            file.write(f"FROM ./{ft_version}_{model_name.split('/')[1]}.gguf\n")

            file.write(r'TEMPLATE """[INST] {{ if and .First .System }}<<SYS>>{{ .System }}<</SYS>>\n\n')
            file.write(r'{{ end }}{{ .Prompt }} [/INST] """\n')
            file.write(r'SYSTEM """"""\n')
            file.write(r'PARAMETER stop [INST]\n')
            file.write(r'PARAMETER stop [/INST]\n')
            file.write(r'PARAMETER stop <<SYS>>\n')
            file.write(r'PARAMETER stop <</SYS>>\n')

        logger.info(f"python3 {llama_cpp_convert_path} {output_merged_dir} --outfile {output_dir_ollama_dir}")
        output, error = run_system_command(f"python3 {llama_cpp_convert_path} {output_merged_dir} --outfile {output_dir_ollama_dir}")
        print("Output:", output)
        print("Error:", error)

        logger.info(f"ollama create example -f {output_dir_ollama_modelfile_str}")
        # This should work. But my setup is a bit hacky with slurm
        # output, error = run_system_command(f"ollama create example -f {output_dir_ollama_modelfile_str}")
        # print("Output:", output)
        # print("Error:", error)
    except Exception as e:
        logger.info(f"Error Model convert: {model_name}")
        logger.info(e)

logger.info("\n\nConvert the models by running the following.\n")
for model_name in models_list:
    output_dir_ollama_modelfile_str = f"{output_dir_ollama_str}/{ft_version}_{model_name.split('/')[1]}.modelfile"
    logger.info(f"ollama create {ft_version}_{model_name.split('/')[1]} -f {output_dir_ollama_modelfile_str}")

logger.info(f"DONE! Took{time.time()-start_time}")

