from pathlib import Path
import os
import utils
import json
from runner import create_result_json_file


def list_python_files(folder_path):
    python_files = sorted(Path(folder_path).rglob("main.py"))
    return python_files


models = [
    # {
    #     "name": "gpt-4o_hg_cs",
    #     "path": "/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_test/.scrapy/batch_prompts_results/gpt-4o_hg_cs-batch_1PSl4bmOdffJdyRraiOPbleP.jsonl",
    #     "bechmark_path": Path(
    #         "/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_test/autogen_typeevalpy_benchmark"
    #     ),
    # },
    # {
    #     "name": "gpt-4o_js",
    #     "path": "/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_test/.scrapy/batch_prompts_results/gpt-4o_js-batch_YE7JzcBsKLSeZ7CeoeGIkCdZ.jsonl",
    #     "bechmark_path": Path(
    #         "/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_test/autogen_typeevalpy_benchmark"
    #     ),
    # },
    # {
    #     "name": "gpt-4o_pycg",
    #     "path": "/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_test/.scrapy/batch_prompts_results/gpt-4o_pycg-batch_uGBHKpb5oeIHVaBNXUQCdipr.jsonl",
    #     "bechmark_path": Path(
    #         "/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_test/autogen_typeevalpy_benchmark"
    #     ),
    # },
    # {
    #     "name": "gpt-4o-mini_hg_cs",
    #     "path": "/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_test/.scrapy/batch_prompts_results/gpt-4o-mini_hg_cs-batch_3dK2KOYlkhovzS7Qmqbs0Cnc.jsonl",
    #     "bechmark_path": Path(
    #         "/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_test/autogen_typeevalpy_benchmark"
    #     ),
    # },
    # {
    #     "name": "gpt-4o-mini_js",
    #     "path": "/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_test/.scrapy/batch_prompts_results/gpt-4o-mini_js-batch_rbNCMtcZIUyzD9aZ4QQ2RsIu.jsonl",
    #     "bechmark_path": Path(
    #         "/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_test/autogen_typeevalpy_benchmark"
    #     ),
    # },
    # {
    #     "name": "gpt-4o-mini_pycg",
    #     "path": "/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_test/.scrapy/batch_prompts_results/gpt-4o-mini_pycg-batch_Nk9np2B9rhzD3AaDgMZEU7oB.jsonl",
    #     "bechmark_path": Path(
    #         "/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_test/autogen_typeevalpy_benchmark"
    #     ),
    # },
    # {
    #     "name": "gpt-4o_autogen",
    #     "path": "/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_test/.scrapy/batch_prompts_results/gpt-4o_autogen-batch_sjDtwbjl3IB6GRZg5XP4svqS.jsonl",
    #     "bechmark_path": Path(
    #         "/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_test/autogen_typeevalpy_benchmark"
    #     ),
    # },
    # {
    #     "name": "gpt-4o-mini_autogen",
    #     "path": "/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_test/.scrapy/batch_prompts_results/gpt-4o-mini_autogen-batch_glNBmyi30uDTH0EuG3c6jTov.jsonl",
    #     "bechmark_path": Path(
    #         "/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_test/autogen_typeevalpy_benchmark"
    #     ),
    # },
    {
        "name": "gpt-4o_micro",
        "path": "/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_test/.scrapy/batch_prompts_results/gpt-4o_micro-batch_GL3PSRMWW25MNowx8ERWCDhD.jsonl",
        "bechmark_path": Path(
            "/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_test/micro-benchmark"
        ),
    },
    {
        "name": "gpt-4o-mini_micro",
        "path": "/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_test/.scrapy/batch_prompts_results/gpt-4o-mini_micro-batch_zz7O1DOR6r7eVpvuvn8g6GgZ.jsonl",
        "bechmark_path": Path(
            "/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_test/micro-benchmark"
        ),
    },
]


def get_prompt_mapping(prompt_template, python_files, use_system_prompt=False):
    id_mapping = {
        idx: {
            "file_path": file_path,
            "json_filepath": str(file_path).replace(".py", "_gt.json"),
            "result_filepath": str(file_path).replace(".py", f"_result.json"),
            "result_dump_filepath": str(file_path).replace(".py", f"_result_dump.txt"),
            "prompt": utils.get_prompt(
                prompt_template, file_path, use_system_prompt=use_system_prompt
            ),
        }
        for idx, file_path in enumerate(python_files)
    }

    return id_mapping


prompt_template = "prompt_template_questions_based_2"
results_dir = Path(
    "/mnt/Projects/PhD/Research/TypeEvalPy/git_sources/TypeEvalPy_test/.scrapy/batch_results_micro"
)

for model in models:
    results_dst = Path(results_dir) / model["name"] / "micro-benchmark"
    os.makedirs(results_dst, exist_ok=True)

    utils.copy_folder(model["bechmark_path"], results_dst)

    python_files = list_python_files(results_dst)

    id_mapping = get_prompt_mapping(
        prompt_template, python_files, use_system_prompt=True
    )

    # read jsonl file and iterate over each line as json object
    with open(model["path"], "r") as f:
        for line in f:
            fact_json = json.loads(line)
            output_raw = fact_json["response"]["body"]["choices"][0]["message"][
                "content"
            ]
            r_id = int(fact_json["custom_id"].split("-")[-1])
            file_info = id_mapping[r_id]
            print(id_mapping[r_id]["file_path"])
            print(fact_json["custom_id"])

            create_result_json_file(file_info, output_raw, prompt_template)
