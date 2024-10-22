import os
from pathlib import Path

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
EXPERIMENT_RUN_ON = "14 Jan 2024"


def csv_to_markdown_table_ranked(csv_str, tool_mapping, header_mapping):
    # Split the csv string into lines
    lines = csv_str.strip().split("\n")

    # Extract headers and data
    headers = ["Rank"] + lines[0].split(",")
    data = [line.split(",") for line in lines[1:]]

    # Map headers
    headers_display = [header_mapping.get(header, header) for header in headers]

    # Group data by tool
    grouped_data = {}
    for row in data:
        tool = row[0]
        if tool not in grouped_data:
            grouped_data[tool] = []
        grouped_data[tool].append(row)

    # Create the markdown table
    table = []
    table.append("| " + " | ".join(headers_display) + " |")
    table.append("|" + "----|" * len(headers_display))

    rank = 1
    for tool, rows in grouped_data.items():
        # Map tool name and hyperlink
        tool_display = tool_mapping.get(tool, {}).get("name", tool)
        tool_url = tool_mapping.get(tool, {}).get("url", None)
        if tool_url:
            tool_display = f"**[{tool_display}]({tool_url})**"

        multiline_rows = list(zip(*[row[1:] for row in rows]))
        multiline_rows_display = [
            "<br>".join(map(str, column)) for column in multiline_rows
        ]

        table.append(
            f"| {rank} | "
            + tool_display
            + " | "
            + " | ".join(multiline_rows_display)
            + " |"
        )
        rank += 1

    return "\n".join(table)


def create_readme_with_table(
    input_md_file,
    placeholder_text,
    csv_str,
    tool_mapping,
    header_mapping,
    results_dir,
    output_md_file="README.md",
):
    # Generate the table from the CSV string
    table = csv_to_markdown_table_ranked(csv_str, tool_mapping, header_mapping)

    auto_gen_info = (
        "\n\n*<sub>(Auto-generated based on the the analysis run on"
        f" {EXPERIMENT_RUN_ON})</sub>*"
    )

    table_text = table + auto_gen_info

    # Read the content of the input markdown file
    with open(input_md_file, "r") as file:
        content = file.read()

    # Replace the placeholder text with the table
    content = content.replace(placeholder_text, table_text)

    # Write the updated content to the output markdown file
    with open(f"{SCRIPT_DIR}/{output_md_file}", "w") as file:
        file.write(content)

    print(f"{output_md_file} has been created successfully!")


results_dir = "/mnt/Projects/PhD/Research/EMSE_FORGE/results/types/autogen"
# results_dir = Path("../results/results_<>")
if results_dir is None:
    dir_path = Path(ROOT_DIR) / "results"
    directories = [
        f for f in dir_path.iterdir() if f.is_dir() and f.name.startswith("results_")
    ]
    directories.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    # Get the latest directory
    results_dir = directories[0] if directories else None

with open(
    f"{str(results_dir)}/analysis_results/paper_tables/paper_table_5.csv", "r"
) as f:
    csv_str = f.read()


tool_mapping = {
    "headergen": {
        "name": "HeaderGen",
        "url": "https://github.com/ashwinprasadme/headergen",
    },
    "jedi": {"name": "Jedi", "url": "https://github.com/davidhalter/jedi"},
    "pyright": {"name": "Pyright", "url": "https://github.com/microsoft/pyright"},
    "hityperdl": {"name": "HiTyper", "url": "https://github.com/JohnnyPeng18/HiTyper"},
    "hityper": {
        "name": "HiTyper (static)",
        "url": "https://github.com/JohnnyPeng18/HiTyper",
    },
    "scalpel": {"name": "Scalpel", "url": "https://github.com/SMAT-Lab/Scalpel/issues"},
    "type4py": {"name": "Type4Py", "url": "https://github.com/saltudelft/type4py"},
    "gpt-4o": {"name": "GPT-4o", "url": "https://openai.com/index/hello-gpt-4o/"},
    "gpt-4o-mini": {
        "name": "GPT 4o Mini",
        "url": "https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/",
    },
    "qwen2-it-7b": {
        "name": "qwen2-it-7b",
        "url": "https://huggingface.co/Qwen/Qwen2-7B-Instruct",
    },
    "qwen2-it-72b": {
        "name": "qwen2-it-72b",
        "url": "https://huggingface.co/Qwen/Qwen2-72B-Instruct",
    },
    "gemma2-it-9b": {
        "name": "gemma2-it-9b",
        "url": "https://huggingface.co/google/gemma-2-9b-it",
    },
    "gemma2-it-27b": {
        "name": "gemma2-it-27b",
        "url": "https://huggingface.co/google/gemma-2-27b-it",
    },
    "gemma2-it-2b": {
        "name": "gemma2-it-2b",
        "url": "https://huggingface.co/google/gemma-2-2b-it",
    },
    "codellama-it-7b": {
        "name": "codellama-it-7b",
        "url": "https://huggingface.co/meta-llama/CodeLlama-7b-Instruct-hf",
    },
    "codellama-it-13b": {
        "name": "codellama-it-13b",
        "url": "https://huggingface.co/meta-llama/CodeLlama-13b-Instruct-hf",
    },
    "codellama-it-34b": {
        "name": "codellama-it-34b",
        "url": "https://huggingface.co/meta-llama/CodeLlama-34b-Instruct-hf",
    },
    "llama3.1-it-8b": {
        "name": "llama3.1-it-8b",
        "url": "https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct",
    },
    "llama3.1-it-70b": {
        "name": "llama3.1-it-70b",
        "url": "https://huggingface.co/meta-llama/Meta-Llama-3.1-70B-Instruct",
    },
    "tinyllama-1.1b": {
        "name": "tinyllama-1.1b",
        "url": "https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    },
    "phi3-small-it-7.3b": {
        "name": "phi3-small-it-7.3b",
        "url": "https://huggingface.co/microsoft/Phi-3-small-128k-instruct",
    },
    "phi3-medium-it-14b": {
        "name": "phi3-medium-it-14b",
        "url": "https://huggingface.co/microsoft/Phi-3-medium-128k-instruct",
    },
    "phi3-mini-it-3.8b": {
        "name": "phi3-mini-it-3.8b",
        "url": "https://huggingface.co/microsoft/Phi-3-mini-128k-instruct",
    },
    "phi3.5-mini-it-3.8b": {
        "name": "phi3.5-mini-it-3.8b",
        "url": "https://huggingface.co/microsoft/Phi-3.5-mini-instruct",
    },
    "phi3.5-moe-it-41.9b": {
        "name": "phi3.5-moe-it-41.9b",
        "url": "https://huggingface.co/microsoft/Phi-3.5-MoE-instruct",
    },
    "mixtral-v0.1-it-8x22b": {
        "name": "mixtral-v0.1-it-8x22b",
        "url": "https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1",
    },
    "mixtral-v0.1-it-8x7b": {
        "name": "mixtral-v0.1-it-8x7b",
        "url": "https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1",
    },
    "mistral-v0.3-it-7b": {
        "name": "mistral-v0.3-it-7b",
        "url": "https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3",
    },
    "mistral-nemo-it-2407-12.2b": {
        "name": "mistral-nemo-it-2407-12.2b",
        "url": "https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407",
    },
    "mistral-large-it-2407-123b": {
        "name": "mistral-large-it-2407-123b",
        "url": "https://huggingface.co/mistralai/Mistral-Large-Instruct-2407",
    },
    "codestral-v0.1-22b": {
        "name": "codestral-v0.1-22b",
        "url": "https://huggingface.co/mistralai/Codestral-22B-v0.1",
    },
    "codellama-python-7b": {
        "name": "codellama-python-7b",
        "url": "https://huggingface.co/meta-llama/CodeLlama-7b-Python-hf",
    },
    "codellama-python-13b": {
        "name": "codellama-python-13b",
        "url": "https://huggingface.co/meta-llama/CodeLlama-13b-Python-hf",
    },
    "codellama-python-34b": {
        "name": "codellama-python-34b",
        "url": "https://huggingface.co/meta-llama/CodeLlama-34b-Python-hf",
    },
}

header_mapping = {
    "Tool": "🛠️ Tool",
    "Top_n": "Top-n",
    "function_returns": "Function Return Type",
    "function_parameters": "Function Parameter Type",
    "local_variables": "Local Variable Type",
    "Total": "Total",
}


create_readme_with_table(
    f"{SCRIPT_DIR}/README_template.md",
    "[INSERT_TABLE_HERE]",
    csv_str,
    tool_mapping,
    header_mapping,
    results_dir,
)
