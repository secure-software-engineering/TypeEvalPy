import argparse
import json
import os
from pathlib import Path


def parse_type_prediction(pred: list[list], id_type=None) -> str:
    if pred:
        return [pred[0][0]]
    else:
        return ["Unknown"]


def translate_content(data):
    if not data:
        return []

    functions = data["response"]["funcs"]
    variables = data["response"]["variables_p"]
    mod_var_ln = data["response"]["mod_var_ln"]
    output = []
    for func in functions:
        name = func["name"]
        fn_lc = func["fn_lc"]

        # Function entry
        output.append(
            {
                "file": "main.py",
                "line_number": fn_lc[0][0],
                "function": name,
                "type": parse_type_prediction(func.get("ret_type_p")),
                "all_type_preds": func.get("ret_type_p"),
            }
        )
        # Function parameters
        params_p = func["params_p"]
        # params_p.pop("args")
        # params_p.pop("kwargs")
        for param, param_type in params_p.items():
            output.append(
                {
                    "file": "main.py",
                    "line_number": fn_lc[0][0],
                    "parameter": param,
                    "function": name,
                    "type": parse_type_prediction(param_type),
                    "all_type_preds": param_type,
                }
            )

    for var, var_type in variables.items():
        var_ln = mod_var_ln.get(var)
        if var_ln:
            # Variable declaration
            output.append(
                {
                    "file": "main.py",
                    "line_number": var_ln[0][0],
                    "variable": var,
                    "type": parse_type_prediction(var_type),
                    "all_type_preds": var_type,
                }
            )

    inferred_serializable = [
        {k: list(v) if isinstance(v, set) else v for k, v in d.items()} for d in output
    ]

    return inferred_serializable


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--bechmark_path",
        help="Specify the benchmark path",
        default="/tmp/micro-benchmark",
    )

    args = parser.parse_args()
    # main_translator(args)
