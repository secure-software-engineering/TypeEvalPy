import json
import logging
import re
import uuid
from typing import Optional

import litellm

from prompts import SYSTEM_PROMPT
from tools import TOOL_DISPATCH, TOOL_SCHEMAS
import translator

logger = logging.getLogger("agent")

# Suppress verbose litellm logging
litellm.suppress_debug_info = True


class AgenticTypeInferrer:
    def __init__(
        self,
        model: str,
        api_key: Optional[str],
        api_base: Optional[str],
        max_iterations: int,
        temperature: float,
    ):
        self.model = model
        self.api_key = api_key or None
        self.api_base = api_base or None
        self.max_iterations = max_iterations
        self.temperature = temperature

    def infer_types(self, file_path: str, benchmark_dir: str) -> tuple[list, list]:
        """
        Run the agentic tool-calling loop for a single benchmark file.
        Returns (annotations, trajectory) where:
          - annotations: final type annotation list in TypeEvalPy format ([] on failure)
          - trajectory: list of step dicts recording the full agent interaction
        """
        messages = self._build_initial_messages(file_path, benchmark_dir)
        trajectory = [
            {
                "step": 0,
                "role": "user",
                "content": messages[-1]["content"],
            }
        ]

        for iteration in range(self.max_iterations):
            logger.debug(f"Iteration {iteration + 1}/{self.max_iterations} for {file_path}")

            try:
                response = self._call_llm(messages)
            except Exception as e:
                logger.error(f"LLM call failed on iteration {iteration + 1}: {e}")
                trajectory.append({
                    "step": iteration + 1,
                    "role": "error",
                    "content": str(e),
                })
                raise

            assistant_msg = response.choices[0].message

            # Hermes/Qwen models embed tool calls in content as <tool_call>...</tool_call>
            # instead of using the OpenAI tool_calls field — parse them as a fallback.
            effective_tool_calls = assistant_msg.tool_calls or self._parse_hermes_tool_calls(
                assistant_msg.content or ""
            )

            # Build assistant dict for message history
            assistant_dict = {"role": "assistant", "content": assistant_msg.content or ""}
            if effective_tool_calls:
                assistant_dict["tool_calls"] = [
                    {
                        "id": tc.id,
                        "type": "function",
                        "function": {
                            "name": tc.function.name,
                            "arguments": tc.function.arguments,
                        },
                    }
                    for tc in effective_tool_calls
                ]
            messages.append(assistant_dict)

            # Record assistant step in trajectory
            traj_step = {
                "step": iteration + 1,
                "role": "assistant",
                "thought": assistant_msg.content or "",
                "tool_calls": [],
            }

            if not effective_tool_calls:
                logger.warning(
                    f"LLM returned plain text on iteration {iteration + 1}, nudging."
                )
                nudge = (
                    "You must call `submit_type_answers` (or `submit_type_annotations`) "
                    "to provide your final answer. Do not respond with plain text only."
                )
                traj_step["tool_calls"] = []
                trajectory.append(traj_step)
                trajectory.append({"step": iteration + 1, "role": "nudge", "content": nudge})
                messages.append({"role": "user", "content": nudge})
                continue

            # Process all tool calls in this turn
            tool_result_messages = []
            submit_result = None

            for tool_call in effective_tool_calls:
                tool_name = tool_call.function.name
                try:
                    tool_args = json.loads(tool_call.function.arguments)
                except json.JSONDecodeError as e:
                    tool_result = f"ERROR: Could not parse tool arguments: {e}"
                    tool_args = None

                if tool_args is not None:
                    if tool_name in ("submit_type_answers", "submit_type_annotations"):
                        try:
                            tool_result = TOOL_DISPATCH[tool_name](tool_args)
                            if tool_name == "submit_type_answers":
                                result_data = json.loads(tool_result)
                                submit_result = result_data.get("annotations", [])
                            else:
                                submit_result = tool_args.get("annotations", [])
                        except (ValueError, KeyError) as e:
                            tool_result = f"ERROR: {e}. Please fix and resubmit."
                            traj_step["tool_calls"].append({
                                "name": tool_name,
                                "arguments": tool_args,
                                "response": tool_result,
                            })
                            tool_result_messages.append({
                                "role": "tool",
                                "tool_call_id": tool_call.id,
                                "name": tool_name,
                                "content": tool_result,
                            })
                            submit_result = None
                            continue

                        traj_step["tool_calls"].append({
                            "name": tool_name,
                            "arguments": tool_args,
                            "response": tool_result,
                        })
                        tool_result_messages.append({
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "name": tool_name,
                            "content": tool_result,
                        })
                        trajectory.append(traj_step)
                        messages.extend(tool_result_messages)
                        return self._parse_final_result(submit_result), trajectory
                    else:
                        tool_result = self._execute_tool_call(tool_name, tool_args)
                else:
                    tool_result = "ERROR: Could not parse tool arguments"

                traj_step["tool_calls"].append({
                    "name": tool_name,
                    "arguments": tool_args if tool_args is not None else {},
                    "response": tool_result,
                })
                tool_result_messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_name,
                    "content": tool_result,
                })

            trajectory.append(traj_step)
            messages.extend(tool_result_messages)

        logger.warning(f"Max iterations ({self.max_iterations}) reached for {file_path}")
        trajectory.append({
            "step": self.max_iterations + 1,
            "role": "system",
            "content": f"Terminated: max_iterations ({self.max_iterations}) reached without submission.",
        })
        return [], trajectory

    def _build_initial_messages(self, file_path: str, benchmark_dir: str) -> list:
        return [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": (
                    f"Please infer all types for the Python file: `{file_path}`\n"
                    f"The benchmark directory containing this test case is: `{benchmark_dir}`\n\n"
                    "Workflow: call list_directory, then read_file on main.py (and any helper "
                    "modules it imports), then generate_type_questions on main.py, write your "
                    "answers, and finally call submit_type_answers."
                ),
            },
        ]

    def _parse_hermes_tool_calls(self, content: str) -> list:
        """
        Parse <tool_call>...</tool_call> blocks from assistant content.
        Used as a fallback for Hermes/Qwen-style vLLM servers that embed tool
        calls in message content instead of the OpenAI tool_calls field.
        """
        pattern = re.compile(r"<tool_call>\s*(.*?)\s*</tool_call>", re.DOTALL)
        tool_calls = []
        for match in pattern.finditer(content):
            try:
                data = json.loads(match.group(1))
            except json.JSONDecodeError as e:
                logger.warning(f"Failed to parse hermes tool_call JSON: {e}")
                continue

            tc_id = f"call_{uuid.uuid4().hex[:8]}"
            arguments = data.get("arguments", {})
            # Build a lightweight object matching the litellm tool_call interface
            tc = type("ToolCall", (), {
                "id": tc_id,
                "function": type("Function", (), {
                    "name": data.get("name", ""),
                    "arguments": json.dumps(arguments) if not isinstance(arguments, str) else arguments,
                })(),
            })()
            tool_calls.append(tc)

        if tool_calls:
            logger.debug(f"Parsed {len(tool_calls)} hermes tool call(s) from content")
        return tool_calls

    def _call_llm(self, messages: list):
        kwargs = dict(
            model=self.model,
            messages=messages,
            tools=TOOL_SCHEMAS,
            tool_choice="auto",
            # temperature=self.temperature,
        )
        if self.api_key:
            kwargs["api_key"] = self.api_key
        if self.api_base:
            kwargs["api_base"] = self.api_base

        return litellm.completion(**kwargs)

    def _execute_tool_call(self, tool_name: str, tool_args: dict) -> str:
        if tool_name not in TOOL_DISPATCH:
            return f"ERROR: Unknown tool '{tool_name}'"
        try:
            result = TOOL_DISPATCH[tool_name](tool_args)
            return result if isinstance(result, str) else json.dumps(result)
        except PermissionError as e:
            return f"ERROR: {e}"
        except FileNotFoundError as e:
            return f"ERROR: {e}"
        except NotADirectoryError as e:
            return f"ERROR: {e}"
        except Exception as e:
            logger.warning(f"Tool '{tool_name}' raised unexpected error: {e}")
            return f"ERROR: {e}"

    def _parse_final_result(self, annotations: list) -> list:
        """Run translator normalization over submitted annotations."""
        try:
            return translator.translate_content(annotations)
        except Exception as e:
            logger.warning(f"Translator failed: {e}, returning raw annotations")
            return annotations
