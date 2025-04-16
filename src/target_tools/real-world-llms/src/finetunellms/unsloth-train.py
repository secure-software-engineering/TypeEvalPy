# # %%
# %%capture
# %pip install unsloth
# # Also get the latest nightly Unsloth!
# %pip install --force-reinstall --no-cache-dir --no-deps git+https://github.com/unslothai/unsloth.git

# # %%
# %pip uninstall torch torchaudio torchvision xformers vllm

# # %%
# %pip install torch==2.5.0 torchaudio==2.5.0 torchvision==0.20.0

# # %%
# %pip check

# %%
import torch
print(f"{torch.cuda.is_available()=}")
print(f"{torch.rand(6,9).to(torch.device('cuda'))=}")

# %%
from unsloth import FastLanguageModel
import torch
max_seq_length = 4000 # Choose any! We auto support RoPE Scaling internally!
dtype = None # None for auto detection. Float16 for Tesla T4, V100, Bfloat16 for Ampere+
load_in_4bit = True # Use 4bit quantization to reduce memory usage. Can be False.

# 4bit pre quantized models we support for 4x faster downloading + no OOMs.
fourbit_models = [
    "unsloth/Meta-Llama-3.1-8B-bnb-4bit",      # Llama-3.1 15 trillion tokens model 2x faster!
    "unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit",
    "unsloth/Meta-Llama-3.1-70B-bnb-4bit",
    "unsloth/Meta-Llama-3.1-405B-bnb-4bit",    # We also uploaded 4bit for 405b!
    "unsloth/Mistral-Nemo-Base-2407-bnb-4bit", # New Mistral 12b 2x faster!
    "unsloth/Mistral-Nemo-Instruct-2407-bnb-4bit",
    "unsloth/mistral-7b-v0.3-bnb-4bit",        # Mistral v3 2x faster!
    "unsloth/mistral-7b-instruct-v0.3-bnb-4bit",
    "unsloth/Phi-3.5-mini-instruct",           # Phi-3.5 2x faster!
    "unsloth/Phi-3-medium-4k-instruct",
    "unsloth/gemma-2-9b-bnb-4bit",
    "unsloth/gemma-2-27b-bnb-4bit",            # Gemma 2x faster!
] # More models at https://huggingface.co/unsloth

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/qwen2.5-coder-7b-instruct-bnb-4bit",  # Smaller model
    max_seq_length=max_seq_length,
    dtype=torch.bfloat16,
    load_in_4bit=load_in_4bit,
    token= "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"
)

# %%
model = FastLanguageModel.get_peft_model(
    model,
    r = 16, # Choose any number > 0 ! Suggested 8, 16, 32, 64, 128
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 16,
    lora_dropout = 0, # Supports any, but = 0 is optimized
    bias = "none",    # Supports any, but = "none" is optimized
    # [NEW] "unsloth" uses 30% less VRAM, fits 2x larger batch sizes!
    use_gradient_checkpointing = "unsloth", # True or "unsloth" for very long context
    random_state = 3407,
    use_rslora = False,  # We support rank stabilized LoRA
    loftq_config = None, # And LoftQ
)

# %%
#Load dataset
from datasets import load_dataset
dataset = load_dataset("/home/ssegpu/rashida/TypeEvalPy/src/target_tools/real-world-llms/src/finetunellms/dataset", split = "train")

# # %%
# %pip install xformers==0.0.28.post2

# %%
#train the model
from trl import SFTTrainer
from transformers import TrainingArguments
from unsloth import is_bfloat16_supported

trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset, dataset_text_field="messages",
    max_seq_length=max_seq_length,
    dataset_num_proc=2,
    packing=False,
    args=TrainingArguments(
        per_device_train_batch_size=2,
        gradient_accumulation_steps=4,
        warmup_steps=5,
        num_train_epochs=2,
        learning_rate=2e-4,
        fp16=not is_bfloat16_supported(),
        bf16=is_bfloat16_supported(),
        logging_steps=1,
        optim="adamw_8bit",
        weight_decay=0.01,
        lr_scheduler_type="linear",
        seed=3407,
        output_dir="outputs",
        report_to="none",
    ),
)

# %%
trainer_stats = trainer.train()

model.save_pretrained("finetuned_without_any_qwen2.5-Coder-7B-Instruct")  # Local saving
tokenizer.save_pretrained("finetuned_without_any_qwen2.5-Coder-7B-Instruct")
model.push_to_hub("rbharmal/finetuned_without_any_qwen2.5-Coder-7B-Instruct", token = "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") # Online saving
tokenizer.push_to_hub("rbharmal/finetuned_without_any_qwen2.5-Coder-7B-Instruct", token = "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") # Online saving

