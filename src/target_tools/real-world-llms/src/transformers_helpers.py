import transformers
import torch
from tqdm import tqdm
from torch.utils.data import Dataset


class ListDataset(Dataset):

    def __init__(self, original_list):
        self.original_list = original_list

    def __len__(self):
        return len(self.original_list)

    def __getitem__(self, i):
        return self.original_list[i]


DEFAULT_CHAT_TEMPLATE = (
    "{% if messages[0]['role'] == 'system' %}"
    "{% set loop_messages = messages[1:] %}"  # Extract system message if it's present
    "{% set system_message = messages[0]['content'] %}"
    "{% elif USE_DEFAULT_PROMPT == true and not '<<SYS>>' in messages[0]['content'] %}"
    "{% set loop_messages = messages %}"  # Or use the default system message if the flag is set
    "{% set system_message = 'DEFAULT_SYSTEM_MESSAGE' %}"
    "{% else %}"
    "{% set loop_messages = messages %}"
    "{% set system_message = false %}"
    "{% endif %}"
    "{% for message in loop_messages %}"  # Loop over all non-system messages
    "{% if (message['role'] == 'user') != (loop.index0 % 2 == 0) %}"
    "{{ raise_exception('Conversation roles must alternate user/assistant/user/assistant/...') }}"
    "{% endif %}"
    "{% if loop.index0 == 0 and system_message != false %}"  # Embed system message in first message
    "{% set content = '<<SYS>>\\n' + system_message + '\\n<</SYS>>\\n\\n' + message['content'] %}"
    "{% else %}"
    "{% set content = message['content'] %}"
    "{% endif %}"
    "{% if message['role'] == 'user' %}"  # After all of that, handle messages/roles in a fairly normal way
    "{{ bos_token + '[INST] ' + content.strip() + ' [/INST]' }}"
    "{% elif message['role'] == 'system' %}"
    "{{ '<<SYS>>\\n' + content.strip() + '\\n<</SYS>>\\n\\n' }}"
    "{% elif message['role'] == 'assistant' %}"
    "{{ ' '  + content.strip() + ' ' + eos_token }}"
    "{% endif %}"
    "{% endfor %}"
)


# Load model, tokenizer and create pipeline
def load_model_and_configurations(
    HF_TOKEN, model_name, use_quantized_model=True, temperature=0.001
):
    temperature = temperature

    bnb_config = transformers.BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
    )

    model = transformers.AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        quantization_config=bnb_config if use_quantized_model else None,
        token=HF_TOKEN,
        trust_remote_code=True,
        torch_dtype="bfloat16" if model_name.startswith("google") else "auto",
        attn_implementation=(
            "flash_attention_2" if model_name.startswith("microsoft") else None
        ),
    )

    tokenizer = transformers.AutoTokenizer.from_pretrained(
        model_name, token=HF_TOKEN, trust_remote_code=True, padding_side="left", truncation=True
    )
    # padding should be padding_side='left' for llama models

    if not tokenizer.chat_template:
        tokenizer.chat_template = DEFAULT_CHAT_TEMPLATE
        print("Default Chat template set")

    if not tokenizer.pad_token:
        tokenizer.pad_token = tokenizer.eos_token

    pipe = transformers.pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        pad_token_id=tokenizer.eos_token_id,
        # temperature=temperature,
    )

    return pipe


def process_requests(
    pipe,
    prompts,
    print_responses: bool = False,
    max_new_tokens: int = 128,
    batch_size: int = 1,
):
    """Continuously process a list of prompts and handle the outputs."""
    # dataset = ListDataset(prompts) # TODO: issues making this work, mainly to show progress bar
    # print(f"Processing {len(prompts)} prompts for model {pipe.model.name_or_path}")
    responses = [
        i for i in pipe(prompts, max_new_tokens=max_new_tokens, batch_size=batch_size)
    ]

    return responses
