import os
from pathlib import Path

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))


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
        f" {results_dir.name.split('_')[1]})</sub>*"
    )

    table_text = table + auto_gen_info

    # Read the content of the input markdown file
    with open(input_md_file, "r") as file:
        content = file.read()

    # Replace the placeholder text with the table
    content = content.replace(placeholder_text, table_text)

    # Write the updated content to the output markdown file
    with open(f"{ROOT_DIR}/{output_md_file}", "w") as file:
        file.write(content)

    print(f"{output_md_file} has been created successfully!")


results_dir = None
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
    "README_template.md",
    "[INSERT_TABLE_HERE]",
    csv_str,
    tool_mapping,
    header_mapping,
    results_dir,
)
