# Environment setup (commented out for context)
# These commands were likely used in a Jupyter notebook to install required packages.
# You can uncomment and use them if running interactively.

# %%capture
# %pip install unsloth
# %pip install --force-reinstall --no-cache-dir --no-deps git+https://github.com/unslothai/unsloth.git

# %pip uninstall torch torchaudio torchvision xformers vllm
# %pip install torch==2.5.0 torchaudio==2.5.0 torchvision==0.20.0
# %pip check

import torch

# -------------------------------------------------------------
# 🚀 Load model using Unsloth's FastLanguageModel wrapper
# -------------------------------------------------------------
from unsloth import FastLanguageModel

# Define model loading parameters
max_seq_length = 4000  # Maximum sequence length supported
dtype = None  # Auto-detect (Float16 for V100/T4, BFloat16 for A100 etc.)
load_in_4bit = True  # Use 4-bit quantized model for memory efficiency

# List of compatible 4-bit models for faster loading/training (optional reference)
fourbit_models = [
    "unsloth/Meta-Llama-3.1-8B-bnb-4bit",
    "unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit",
    "unsloth/Meta-Llama-3.1-70B-bnb-4bit",
    "unsloth/Meta-Llama-3.1-405B-bnb-4bit",
    "unsloth/Mistral-Nemo-Base-2407-bnb-4bit",
    "unsloth/Mistral-Nemo-Instruct-2407-bnb-4bit",
    "unsloth/mistral-7b-v0.3-bnb-4bit",
    "unsloth/mistral-7b-instruct-v0.3-bnb-4bit",
    "unsloth/Phi-3.5-mini-instruct",
    "unsloth/Phi-3-medium-4k-instruct",
    "unsloth/gemma-2-9b-bnb-4bit",
    "unsloth/gemma-2-27b-bnb-4bit",
]

# Load the pretrained model and tokenizer
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="mistralai/Codestral-22B-v0.1",  # Original 22B Codestral model
    max_seq_length=max_seq_length,
    dtype=torch.bfloat16,
    load_in_4bit=load_in_4bit,
    # token="",
)

# -------------------------------------------------------------
# 🔧 Convert the model to a PEFT (LoRA) model
# -------------------------------------------------------------
model = FastLanguageModel.get_peft_model(
    model,
    r=16,  # LoRA rank (8-128 recommended depending on memory/batch size)
    target_modules=[
        "q_proj",
        "k_proj",
        "v_proj",
        "o_proj",
        "gate_proj",
        "up_proj",
        "down_proj",
    ],
    lora_alpha=16,  # LoRA scaling factor
    lora_dropout=0,  # Dropout (0 is best optimized)
    bias="none",  # Bias handling (recommended "none" for efficiency)
    use_gradient_checkpointing="unsloth",  # Saves VRAM using Unsloth's efficient implementation
    random_state=3407,  # Reproducibility
    use_rslora=False,  # Optionally enable rank-stabilized LoRA
    loftq_config=None,  # Optional quantization-aware training
)

# -------------------------------------------------------------
# 📦 Load dataset for training
# -------------------------------------------------------------
from datasets import load_dataset

# Assumes a preprocessed HuggingFace-compatible dataset in the given folder
dataset = load_dataset(
    "/home/ssegpu/rashida/TypeEvalPy/src/target_tools/real-world-llms/src/finetunellms/dataset",
    split="train",
)

# -------------------------------------------------------------
# 🧠 Train the LoRA fine-tuned model using TRL's SFTTrainer
# -------------------------------------------------------------
from trl import SFTTrainer
from transformers import TrainingArguments
from unsloth import is_bfloat16_supported  # Check for BF16 support (Ampere+ GPUs)

trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset,
    dataset_text_field="messages",  # Field name containing the text (JSON format)
    max_seq_length=max_seq_length,
    dataset_num_proc=2,  # Parallel processing threads
    packing=False,  # Enable if packing multiple examples per input
    args=TrainingArguments(
        per_device_train_batch_size=10,  # Adjust depending on GPU RAM
        gradient_accumulation_steps=4,  # Effective batch size = 40
        warmup_steps=5,  # LR warmup
        num_train_epochs=2,  # Train for 2 epochs
        learning_rate=2e-4,  # Typical learning rate
        fp16=not is_bfloat16_supported(),  # Use FP16 if BF16 unsupported
        bf16=is_bfloat16_supported(),  # Use BF16 if supported
        logging_steps=1,  # Log every step
        optim="adamw_8bit",  # 8-bit optimizer for memory efficiency
        weight_decay=0.01,  # Regularization
        lr_scheduler_type="linear",  # Linear decay LR scheduler
        seed=3407,  # Reproducibility
        output_dir="outputs",  # Output folder for logs/checkpoints
        report_to="none",  # Disable W&B or other logging tools
    ),
)

# -------------------------------------------------------------
# 🚀 Start training and capture stats
# -------------------------------------------------------------
trainer_stats = trainer.train()

# -------------------------------------------------------------
# 💾 Save the fine-tuned model and tokenizer locally
# -------------------------------------------------------------
model.save_pretrained("finetuned_Codestral-22B-v0.1")
tokenizer.save_pretrained("finetuned_Codestral-22B-v0.1")
