import requests
import json


def parse_type_prediction(pred: list[list]) -> str:
    if pred:
        return pred[0][0]
    else:
        return "Unknown"


# Replace 'main.py' with the path to your Python source file
with open("../functions/default/main.py") as f:
    code = f.read()

response = requests.post("https://type4py.com/api/predict?tc=0", code, verify=False)
data = response.json()

if data.get("error") is not None:
    print("Error:", data["error"])
else:
    output = []

    functions = data["response"]["funcs"]
    # print(functions)
    variables = data["response"]["variables_p"]
    # print(variables)
    mod_var_ln = data["response"]["mod_var_ln"]
    # print(mod_var_ln)

    for func in functions:
        name = func["name"]
        fn_lc = func["fn_lc"]

        # Function entry
        output.append(
            {
                "file": "main.py",
                "line_number": fn_lc[0][0],
                "function": name,
                "type": [parse_type_prediction(func["ret_type_p"])],
            }
        )
        # Function parameters
        params_p = func["params_p"]
        params_p.pop("args")
        params_p.pop("kwargs")
        for param, param_type in params_p.items():
            output.append(
                {
                    "file": "main.py",
                    "line_number": fn_lc[0][0],
                    "parameter": param,
                    "function": name,
                    "type": [parse_type_prediction(param_type)],
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
                    "type": [parse_type_prediction(var_type)],
                }
            )

    # print(output)
    print(json.dumps(output, indent=4))
