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
    )

    tokenizer = transformers.AutoTokenizer.from_pretrained(
        model_name,
        token=HF_TOKEN,
    )

    pipe = transformers.pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        pad_token_id=tokenizer.eos_token_id,
        temperature=temperature,
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
    dataset = ListDataset(prompts)

    responses = [
        i
        for i in tqdm(
            pipe(dataset, max_new_tokens=max_new_tokens, batch_size=batch_size)
        )
    ]

    return responses
