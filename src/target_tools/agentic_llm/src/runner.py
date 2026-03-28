import argparse
import json
import logging
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from tqdm import tqdm

import utils
from agent import AgenticTypeInferrer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger("runner")

# Suppress noisy third-party loggers
for _noisy in ("LiteLLM", "litellm", "httpx", "httpcore", "openai", "urllib3"):
    logging.getLogger(_noisy).setLevel(logging.WARNING)


def trajectory_to_markdown(trajectory: list, file_path: str) -> str:
    """Convert a trajectory list to a human-readable markdown string."""
    lines = []
    lines.append(f"# Agent Trajectory\n")
    lines.append(f"**File:** `{file_path}`\n")
    lines.append(f"**Steps:** {len([s for s in trajectory if s['role'] == 'assistant'])}\n")
    lines.append("---\n")

    for step in trajectory:
        role = step["role"]

        if role == "user":
            lines.append("## 🧑 Task\n")
            lines.append(f"{step['content']}\n")
            lines.append("---\n")

        elif role == "assistant":
            lines.append(f"## 🤖 Step {step['step']}\n")

            if step.get("thought"):
                lines.append("### Thought\n")
                lines.append(f"{step['thought']}\n")

            for tc in step.get("tool_calls", []):
                name = tc["name"]
                args = tc["arguments"]
                response = tc["response"]

                lines.append(f"### Tool: `{name}`\n")

                # Arguments block — pick language hint per tool
                if name == "read_file":
                    lines.append("**Arguments:**\n")
                    lines.append(f"```\n{args.get('path', '')}\n```\n")
                    lines.append("**Response:**\n")
                    lines.append(f"```python\n{response}\n```\n")

                elif name == "list_directory":
                    lines.append("**Arguments:**\n")
                    lines.append(f"```\n{args.get('path', '')}\n```\n")
                    lines.append("**Response:**\n")
                    lines.append(f"```\n{response}\n```\n")

                elif name == "get_ast_summary":
                    lines.append("**Arguments:**\n")
                    lines.append(f"```\n{args.get('path', '')}\n```\n")
                    lines.append("**Response:**\n")
                    # response is a JSON string — pretty-print it
                    try:
                        parsed = json.loads(response)
                        pretty = json.dumps(parsed, indent=2)
                    except (json.JSONDecodeError, TypeError):
                        pretty = response
                    lines.append(f"```json\n{pretty}\n```\n")

                elif name == "submit_type_annotations":
                    lines.append("**Annotations submitted:**\n")
                    try:
                        annotations = args.get("annotations", [])
                        pretty = json.dumps(annotations, indent=2)
                    except (TypeError, ValueError):
                        pretty = str(args)
                    lines.append(f"```json\n{pretty}\n```\n")
                    try:
                        resp = json.loads(response)
                        status = resp.get("status", "?")
                        count = resp.get("count", "?")
                        lines.append(f"**Result:** {status} — {count} annotation(s)\n")
                    except (json.JSONDecodeError, TypeError):
                        lines.append(f"**Result:** {response}\n")

                else:
                    lines.append(f"**Arguments:**\n```json\n{json.dumps(args, indent=2)}\n```\n")
                    lines.append(f"**Response:**\n```\n{response}\n```\n")

            lines.append("---\n")

        elif role == "nudge":
            lines.append(f"### ⚠️ Nudge\n")
            lines.append(f"> {step['content']}\n")

        elif role == "error":
            lines.append(f"### ❌ Error (step {step['step']})\n")
            lines.append(f"```\n{step['content']}\n```\n")
            lines.append("---\n")

        elif role == "system":
            lines.append(f"## 🛑 Terminated\n")
            lines.append(f"{step['content']}\n")

    return "\n".join(lines)


def list_python_files(folder_path: str) -> list:
    """Return all main.py files recursively — one agent run per test case directory."""
    return sorted(Path(folder_path).rglob("main.py"))


def process_file(agent, file_path) -> tuple[bool, str]:
    """Process a single test case. Returns (success, short_label)."""
    result_path = str(file_path).replace(".py", "_result.json")
    trajectory_path = str(file_path).replace(".py", "_trajectory.json")
    label = file_path.parent.name  # e.g. "assign_1"
    try:
        logger.debug(f"Processing: {file_path}")
        annotations, trajectory = agent.infer_types(
            file_path=str(file_path),
            benchmark_dir=str(file_path.parent),
        )
        with open(result_path, "w") as f:
            json.dump(annotations, f, indent=4, sort_keys=True)
        with open(trajectory_path, "w") as f:
            json.dump(trajectory, f, indent=4, ensure_ascii=False)
        md_path = str(file_path).replace(".py", "_trajectory.md")
        with open(md_path, "w") as f:
            f.write(trajectory_to_markdown(trajectory, str(file_path)))
        logger.debug(f"Saved {len(annotations)} annotations to {result_path}")
        return True, label
    except Exception as e:
        logger.error(f"Failed on {file_path}: {e}")
        with open(result_path, "w") as f:
            json.dump([], f)
        return False, label


def main_runner(args):
    agent = AgenticTypeInferrer(
        model=args.model,
        api_key=args.api_key if args.api_key else None,
        api_base=args.api_base if args.api_base and args.api_base != "null" else None,
        max_iterations=args.max_iterations,
        temperature=args.temperature,
    )

    python_files = list_python_files(args.bechmark_path)
    logger.info(f"Found {len(python_files)} test cases | workers={args.workers} | model={args.model}")

    error_count = 0
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(process_file, agent, fp): fp for fp in python_files}
        with tqdm(total=len(python_files), desc="Inferring types", unit="file", dynamic_ncols=True) as pbar:
            for future in as_completed(futures):
                success, label = future.result()
                if not success:
                    error_count += 1
                pbar.set_postfix(errors=error_count, last=label, refresh=False)
                pbar.update(1)

    logger.info(f"Done. {len(python_files)} files processed, {error_count} errors.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Agentic LLM type inference runner")
    parser.add_argument(
        "--bechmark_path",  # intentional typo to match TypeEvalPy convention
        default="/tmp/micro-benchmark",
        help="Path to the benchmark directory",
    )
    parser.add_argument(
        "--model",
        required=True,
        help="LiteLLM model string (e.g. gpt-4o, ollama/llama3, anthropic/claude-sonnet-4-5)",
    )
    parser.add_argument(
        "--api_key",
        default="",
        help="API key for the LLM provider (empty for Ollama or env-var-based auth)",
    )
    parser.add_argument(
        "--api_base",
        default="null",
        help="Custom API base URL (e.g. http://localhost:11434 for Ollama)",
    )
    parser.add_argument(
        "--max_iterations",
        type=int,
        default=10,
        help="Maximum tool-calling iterations per file before giving up",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.1,
        help="LLM sampling temperature",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        help="Number of parallel workers for concurrent file processing (default: 1 = sequential)",
    )

    args = parser.parse_args()

    # Allow env vars to fill in unset args (convenient for local dev / VSCode launch configs)
    # Priority: CLI arg > env var > default
    if not args.api_key:
        args.api_key = os.environ.get("OPENAI_API_KEY", "")
    if args.api_base == "null":
        env_base = os.environ.get("OPENAI_BASE_URL", "") or os.environ.get("OPENAI_API_BASE", "")
        if env_base:
            args.api_base = env_base

    main_runner(args)
