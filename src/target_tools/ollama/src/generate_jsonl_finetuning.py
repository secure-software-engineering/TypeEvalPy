import json
import os
from pathlib import Path

import fine_tuning
import prompts
import utils
from runner import get_prompt


def process_file(file_path):
    with open(file_path, "r") as f:
        return f.read()


def generate_jsonl_gpt(folder_path, output_file, prompt_id):
    messages_list = []
    system_prompt = eval(f"prompts.{prompt_id}_system")

    system_message = {
        "role": "system",
        "content": system_prompt,
    }

    # Find all subdirectories in the root folder
    subdirectories = [
        os.path.join(folder_path, d)
        for d in os.listdir(folder_path)
        if os.path.isdir(os.path.join(folder_path, d))
    ]

    # Traverse all files in each sample
    for finetuning_sample in sorted(subdirectories):
        message = []
        message.append(system_message)

        print(f"Processing {finetuning_sample}...")
        for root, _, files in os.walk(finetuning_sample):
            code_file = os.path.join(root, files[0])
            gt_file = os.path.join(root, files[1])

            # User message
            user_message = {
                "role": "user",
                "content": get_prompt(prompt_id, code_file, gt_file),
            }
            message.append(user_message)

            # Assistant message
            assistant_message = {
                "role": "assistant",
                "content": utils.generate_answers_for_fine_tuning(gt_file),
            }
            message.append(assistant_message)

        messages_list.append(json.dumps({"messages": message}, separators=(",", ":")))

    # Write messages to the output file
    with open(output_file, "w") as output:
        for _m in messages_list:
            output.write(_m)
            output.write("\n")


def generate_jsonl_llama(folder_path, output_file, prompt_id):
    messages_list = []

    # Find all subdirectories in the root folder
    subdirectories = [
        os.path.join(folder_path, d)
        for d in os.listdir(folder_path)
        if os.path.isdir(os.path.join(folder_path, d))
    ]

    # Traverse all files in each sample
    for finetuning_sample in sorted(subdirectories):
        print(f"Processing {finetuning_sample}...")
        for root, _, files in os.walk(finetuning_sample):
            code_file = os.path.join(root, files[0])
            gt_file = os.path.join(root, files[1])

            full_text = get_prompt(
                prompt_id, code_file, gt_file, answers_placeholders=True
            ) + utils.generate_answers_for_fine_tuning(gt_file)

            full_message = {
                "text": full_text,
            }

            messages_list.append(json.dumps(full_message, separators=(",", ":")))

    # Write messages to the output file
    with open(output_file, "w") as output:
        for _m in messages_list:
            output.write(_m)
            output.write("\n")


# fine_tuning.generate_jsonl(folder_path, output_file, system_prompt, main_prompt)
if __name__ == "__main__":
    SCRIPT_DIR = Path(os.path.abspath(os.path.dirname(__file__)))

    # Create fine tuning dataset
    folder_path = SCRIPT_DIR / "fine_tuning" / "training_set"
    output_file_gpt = SCRIPT_DIR / "fine_tuning" / "finetuning_autoset_gpt_v1.5.jsonl"
    output_file_llama = (
        SCRIPT_DIR / "fine_tuning" / "finetuning_autoset_llama_v1.5.jsonl"
    )

    # Prepare prompts
    prompt_id_gpt = "questions_based_2"
    prompt_id_llama = "questions_based_2_ft"

    generate_jsonl_gpt(folder_path, output_file_gpt, prompt_id_gpt)
    generate_jsonl_llama(folder_path, output_file_llama, prompt_id_llama)
