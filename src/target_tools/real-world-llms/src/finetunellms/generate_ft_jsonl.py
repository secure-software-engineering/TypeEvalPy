import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import utils
from pathlib import Path
import json

def generate_ft_json(prompt_template, json_files, use_system_prompt=False):
    id_mapping = get_prompt_mapping(prompt_template, use_system_prompt)

    # Create a list of tuples containing both the prompt and its corresponding id_mapping entry
    prompt_id_mapping_pairs = [(x["prompt"], x) for x in id_mapping.values()]

    # Sort the list of tuples based on the token count of the prompts
    sorted_prompt_id_mapping_pairs = sorted(
        prompt_id_mapping_pairs, key=lambda x: utils.get_token_count(x[0]), reverse=True
    )

    # Get the file paths of the top 5 largest prompts
    top_5_largest_prompts_file_paths = [pair[1]["file_path"] for pair in sorted_prompt_id_mapping_pairs[:5]]
    print("Top 5 largest prompts file paths:", top_5_largest_prompts_file_paths)

    # Separate the sorted prompts and id_mapping entries back into individual lists
    # sorted_prompts = [pair[0] for pair in sorted_prompt_id_mapping_pairs]
    # sorted_id_mapping = {i: pair[1] for i, pair in enumerate(sorted_prompt_id_mapping_pairs)}

    # utils.dump_ft_jsonl(sorted_id_mapping, f"/home/ssegpu/rashida/TypeEvalPy/src/target_tools/real-world-llms/src/finetunellms/dataset/valid.jsonl")

def get_prompt_mapping(
    prompt_template, use_system_prompt=False, token_limit=4000
):
    """
    Traverse the directory structure, pair .json and _gt.json files,
    and generate a combined id_mapping using get_prompt_mapping logic.
    """
    base_path = Path("/mnt/hf_cache/rashida_manytype4py/many-types-4-py-dataset/rw-benchmark")
    id_mapping = {}
    idx = 0
    # Walk through train, test, valid folders
    for subfolder in ["test"]:
        folder_path = base_path / subfolder
        if not folder_path.exists():
            continue

        # Get .json and _gt.json files
        code_json_files = sorted(folder_path.glob("*.json"))
        gt_json_files = sorted(folder_path.glob("*_gt.json"))

        # Ensure files are paired correctly
        json_pairs = {}
        for code_json in code_json_files:
            # Find the corresponding _gt.json
            gt_json = folder_path / f"{code_json.stem}_gt.json"
            if gt_json.exists():
                json_pairs[code_json] = gt_json

        # Process each pair
        for code_json, gt_json in json_pairs.items():

            with open(code_json, "r") as code_file:
                code_data = json.load(code_file)

            with open(gt_json, "r") as gt_file:
                gt_data = json.load(gt_file)

            # Create gt_mapping
            gt_mapping = {}
            for entry in gt_data:
                file_path = entry["file"]
                if file_path not in gt_mapping:
                    gt_mapping[file_path] = []
                gt_mapping[file_path].append(entry)

            # Process the code and generate prompts
            for project_name, project_info in code_data.items():
                src_files = project_info.get("src_files", {})

                for file_path, file_info in src_files.items():
                    source_code = file_info.get("source_code", "")

                    if source_code == "":
                        continue

                    # Fetch the typing information for the file from gt_mapping
                    type_info_list = gt_mapping.get(file_path, [])
                    if len(type_info_list) == 0:
                        continue

                    # Generate the prompt
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

                    # Store the result in id_mapping
                    id_mapping[idx] = {
                        "project_name": project_name,
                        "file_path": file_path,
                        "json_filepath": str(gt_json),
                        "prompt": prompt,
                    }
                    idx += 1

    return id_mapping

def list_json_files(folder_path):
    json_files = sorted(Path(folder_path).rglob("*.json"))
    return json_files

def main():
    prompt_template = "prompt_template_questions_based_2"
    json_files = list_json_files("/mnt/hf_cache/rashida_manytype4py/many-types-4-py-dataset/rw-benchmark")
    generate_ft_json(prompt_template, json_files, use_system_prompt=False)    

if __name__ == "__main__":
    main()