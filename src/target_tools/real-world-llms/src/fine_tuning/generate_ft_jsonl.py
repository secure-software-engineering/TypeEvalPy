import sys
import os
import json
from pathlib import Path

# Add the parent directory to the system path to import utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import utils


def generate_ft_json(prompt_template, json_files, output_path, use_system_prompt=False):
    """
    Generates a fine-tuning JSONL file from a list of JSON files, sorted by prompt length.

    Args:
        prompt_template (str): Template name for generating prompts.
        json_files (List[Path]): List of JSON input file paths.
        output_path (Path): Output path for the resulting JSONL.
        use_system_prompt (bool): Whether to include system prompt formatting.
    """
    id_mapping = get_prompt_mapping(prompt_template, use_system_prompt, json_files)

    # Sort prompts by token count in descending order
    prompt_id_mapping_pairs = [(x["prompt"], x) for x in id_mapping.values()]
    sorted_prompt_id_mapping_pairs = sorted(
        prompt_id_mapping_pairs, key=lambda x: utils.get_token_count(x[0]), reverse=True
    )

    # Reconstruct the sorted mapping with new indices
    sorted_id_mapping = {
        i: pair[1] for i, pair in enumerate(sorted_prompt_id_mapping_pairs)
    }

    # Save as JSONL
    utils.dump_ft_jsonl(sorted_id_mapping, output_path)


def get_prompt_mapping(prompt_template, use_system_prompt, json_files):
    """
    Reads paired code and ground-truth files, generates prompts for fine-tuning.

    Args:
        prompt_template (str): Name of the prompt template to use.
        use_system_prompt (bool): Whether to include system-level prompts.
        json_files (List[Path]): List of all .json files in the dataset.

    Returns:
        dict: Mapping from integer IDs to prompt metadata.
    """
    id_mapping = {}
    idx = 0

    # Create pairs of source JSON and _gt.json files
    json_pairs = {}
    for code_json in json_files:
        if code_json.name.endswith("_gt.json"):
            continue
        gt_json = code_json.parent / f"{code_json.stem}_gt.json"
        if gt_json.exists():
            json_pairs[code_json] = gt_json

    for code_json, gt_json in json_pairs.items():
        with open(code_json, "r") as code_file:
            code_data = json.load(code_file)
        with open(gt_json, "r") as gt_file:
            gt_data = json.load(gt_file)

        # Build file-based lookup for GT entries
        gt_mapping = {}
        for entry in gt_data:
            file_path = entry["file"]
            gt_mapping.setdefault(file_path, []).append(entry)

        # Create prompts per source file
        for project_name, project_info in code_data.items():
            src_files = project_info.get("src_files", {})

            for file_path, file_info in src_files.items():
                source_code = file_info.get("source_code", "")
                if not source_code:
                    continue

                type_info_list = gt_mapping.get(file_path, [])
                if not type_info_list:
                    continue

                prompt = utils.get_prompt(
                    prompt_template,
                    source_code,
                    type_info_list,
                    use_system_prompt=use_system_prompt,
                    file_path=file_path,
                    token_limit=4000,
                )

                if prompt is None:
                    continue

                id_mapping[idx] = {
                    "project_name": project_name,
                    "file_path": file_path,
                    "json_filepath": str(gt_json),
                    "prompt": prompt,
                }
                idx += 1

    return id_mapping


def list_json_files(folder_path):
    """Recursively lists all .json files in the specified folder."""
    return sorted(Path(folder_path).rglob("*.json"))


def main():
    prompt_template = "prompt_template_questions_based_2"
    base_input_dir = Path(
        "/mnt/hf_cache/rashida_manytype4py/many-types-4-py-dataset/rw-benchmark"
    )
    base_output_dir = Path("./dataset")
    base_output_dir.mkdir(parents=True, exist_ok=True)

    # Run for each of train, test, valid
    for split in ["train", "test", "valid"]:
        split_input_dir = base_input_dir / split
        if not split_input_dir.exists():
            print(f"[warn] Skipping missing split: {split}")
            continue

        json_files = list_json_files(split_input_dir)
        output_path = base_output_dir / f"{split}.jsonl"
        print(f"Processing split '{split}' with {len(json_files)} files...")
        generate_ft_json(
            prompt_template, json_files, output_path, use_system_prompt=False
        )
        print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()
