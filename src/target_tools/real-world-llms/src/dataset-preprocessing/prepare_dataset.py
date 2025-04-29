import json
import os
from translate import translate_content
import libcst as cst
from typehint_clean import typing_clean

# Get the absolute path of the current script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define paths to the dataset, base, and output directories
json_directory = os.path.join(
    script_directory,
    "../downloaded-dataset/ManyTypes4PyDataset-v0.7/processed_projects_clean",
)
base_directory = os.path.join(script_directory, "../")

# Convert relative paths to absolute paths
json_directory = os.path.abspath(json_directory)
base_directory = os.path.abspath(base_directory)

# Dictionary to organize the dataset by split: train, test, valid
output_data = {"train": {}, "test": {}, "valid": {}}

# Track the number of JSON files that were successfully processed (not deleted)
non_deleted_json_count = 0


def read_file_content(file_path):
    """
    Reads and returns the content of a source file.
    Returns an empty string on error.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return ""
    except Exception as e:
        print(f"An error occurred while reading {file_path}: {e}")
        return ""


def update_json(json_path, base_dir, avoid_files=[]):
    """
    Updates a single JSON file by:
    - Attaching 'source_code' to each source file
    - Applying LibCST-safe type hint stripping
    - Classifying data into train/test/valid splits
    - Removing JSON file if all files are missing
    """
    global non_deleted_json_count
    global libcst_fail_count

    # Load the JSON data
    try:
        with open(json_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading {json_path}: {e}")
        return

    all_files_missing = True
    libcst_fail_count = 0

    # Iterate through each project in the JSON
    for project_name, project_data in data.items():
        if "src_files" in project_data:
            for file_name, attributes in project_data["src_files"].items():
                # Skip blacklisted files
                if file_name in avoid_files.get("file_paths", []):
                    continue

                # Read and clean the file content
                full_path = os.path.join(base_dir, file_name)
                file_content = read_file_content(full_path)

                if file_content != "":
                    all_files_missing = False

                # Remove incompatible type hints
                file_content, used_fallback = typing_clean.strip(file_content)

                if used_fallback:
                    libcst_fail_count += 1

                # Attach source code to attributes
                attributes["source_code"] = file_content

                if file_content == "":
                    continue

                # Save by split type (train/test/valid)
                split_type = attributes.get("set")
                if split_type in ["train", "test", "valid"]:
                    if project_name not in output_data[split_type]:
                        output_data[split_type][project_name] = {"src_files": {}}
                    output_data[split_type][project_name]["src_files"][
                        file_name
                    ] = attributes

    if all_files_missing:
        # Delete the file if all sources are missing
        try:
            os.remove(json_path)
        except Exception as e:
            print(f"Error deleting {json_path}: {e}")
    else:
        # Save the updated JSON
        try:
            with open(json_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
            non_deleted_json_count += 1
            print(f"File failed to parse with LibCST: {libcst_fail_count}")
        except Exception as e:
            print(f"Error writing {json_path}: {e}")


def process_json_files_in_directory(directory, base_dir):
    """
    Processes all JSON files in a directory:
    - Loads avoid-list for oversized files
    - Updates each JSON file with source code
    - Categorizes data into splits
    - Saves split datasets to new JSON files
    """
    # Load the list of files to avoid processing (too large or token-limit exceeded)
    try:
        with open(
            "/mnt/hf_cache/rashida_manytype4py/many-types-4-py-dataset/scripts/.scrapy/exceeded_token_limit_files.json",
            "r",
            encoding="utf-8",
        ) as avoid_file:
            avoid_files = json.load(avoid_file)
    except Exception as e:
        print(f"Error loading avoid list: {e}")
        avoid_files = []

    # Process each JSON file in the directory
    for file_name in os.listdir(directory):
        if file_name.endswith(".json"):
            json_path = os.path.join(directory, file_name)
            update_json(json_path, base_dir, avoid_files)

    # Organize split output files into rw-benchmark/train|test|valid
    split_dataset_dir = os.path.join(base_dir, "rw-benchmark")
    os.makedirs(split_dataset_dir, exist_ok=True)

    for split_type in ["train", "test", "valid"]:
        split_dir = os.path.join(split_dataset_dir, split_type)
        os.makedirs(split_dir, exist_ok=True)

        output_file_path = os.path.join(split_dir, f"{split_type}.json")
        try:
            with open(output_file_path, "w", encoding="utf-8") as output_file:
                json.dump(output_data[split_type], output_file, indent=4)
            print(
                f"{split_type}.json file created successfully in {split_type} folder."
            )
        except Exception as e:
            print(f"Error writing {split_type}.json: {e}")


def translate_and_save_json_files(split_data_directory):
    """
    Translates the JSON data (e.g., source code) in each split file and
    saves a corresponding _gt.json (ground truth) file.
    """
    splits = ["train", "test", "valid"]
    for split in splits:
        input_file_path = os.path.join(split_data_directory, split, f"{split}.json")
        output_file_path = os.path.join(split_data_directory, split, f"{split}_gt.json")

        try:
            with open(input_file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            translated_data = translate_content(data)

            with open(output_file_path, "w", encoding="utf-8") as file:
                json.dump(translated_data, file, indent=4)
            print(f"Translated {split}.json file saved to {output_file_path}")
        except Exception as e:
            print(f"Error translating {input_file_path}: {e}")


# === Script Execution ===

# Step 1: Process and clean all project JSON files
process_json_files_in_directory(json_directory, base_directory)

# Step 2: Translate source code content in each split and save ground-truth versions
translate_and_save_json_files(os.path.join(base_directory, "rw-benchmark"))
