import json
from pathlib import Path


# Function to modify the JSON data
def modify_data(data):
    # Example modification: add a new key-value pair
    new_data = {
        "replacement_mode": "Imports",
        "imports": ["to_import.py"],
        "type_replacements": ["int", "float", "str", "bool", "list", "dict", "tuple"],
        "ground_truth": data,
    }
    return new_data


# Function to process each JSON file
def process_json_file(file_path):
    # Read the JSON file
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Modify the data
    modified_data = modify_data(data)

    # Write the modified data back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(modified_data, file, indent=4)


# Main function to find and process all JSON files in subdirectories
def main(directory_path):
    # Create a Path object for the directory
    path = Path(directory_path)

    # Recursively find all JSON files
    for json_file in path.rglob("*.json"):
        process_json_file(json_file)


# Example usage
if __name__ == "__main__":
    main(
        "/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_AutoBench/.scrapy/micro-benchmark-autogen-templates"
    )  # Change this
