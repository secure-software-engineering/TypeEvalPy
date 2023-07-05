import requests
import json
import os


def list_python_files(folder_path):
    python_files = []
    for root, Readme, files in os.walk(os.path.abspath(folder_path)):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files


def parse_type_prediction(pred: list[list]) -> str:
    if pred:
        return pred[0][0]
    else:
        return "Unknown"


def type4py(file):
    output = []
    with open(file) as f:
        code = f.read()

    response = requests.post("https://type4py.com/api/predict?tc=0", code, verify=False)
    data = response.json()

    def variables_analysis(variables, function=None, class_name=None):
        for var, var_type in variables.items():
            var_ln = mod_var_ln.get(var)
            if var_ln:
                # Variable declaration
                output_data = {
                    "file": "main.py",
                    "line_number": var_ln[0][0],
                    "variable": var,
                    "type": [parse_type_prediction(var_type)],
                }
                if function:
                    if class_name:
                        output_data["function"] = f"{class_name}.{function}"
                    else:
                        output_data["function"] = f"{function}"
                elif class_name:
                    output_data["variable"] = f"{class_name}.{var}"
                output.append(output_data)

    def functions_analysis(functions, class_name=None):
        for func in functions:
            name = func["name"]
            fn_lc = func["fn_lc"]

            # Function entry
            output_data = {
                "file": "main.py",
                "line_number": fn_lc[0][0],
                "function": name,
                "type": [parse_type_prediction(func["ret_type_p"])],
            }
            if class_name:
                output_data["function"] = f"{class_name}.{name}"
            output.append(output_data)

            # Function parameters
            params_p = func["params_p"]
            params_p.pop("args")
            params_p.pop("kwargs")
            params_p.pop("self")
            for param, param_type in params_p.items():
                output_data = {
                    "file": "main.py",
                    "line_number": fn_lc[0][0],
                    "parameter": param,
                    "function": name,
                    "type": [parse_type_prediction(param_type)],
                }
                if class_name:
                    func["function"] = f"{class_name}.{name}"
                output.append(output_data)
            # Function variables
            variables = func["variables_p"]
            variables_analysis(variables, func, class_name)

    if data.get("error") is not None:
        print("Error:", data["error"])
    else:
        classes = data["response"]["classes"]
        # For class data
        for class_obj in classes:
            functions = class_obj["funcs"]
            variables = class_obj["variables_p"]
            class_name = class_obj["name"]
            # mod_var_ln = data["response"]["mod_var_ln"]
            functions_analysis(functions, class_name)  # class functions
            variables_analysis(variables, None, class_name)  # class variables

        # For global data
        functions = data["response"]["funcs"]
        variables = data["response"]["variables_p"]
        mod_var_ln = data["response"]["mod_var_ln"]
        variables_analysis(variables)

        return output


folder_path = "/tmp/micro-benchmark/python_features"

python_files = list_python_files(folder_path)

for file in python_files:
    try:
        print(file)
        output = type4py(file)
        json_file_path = file.replace(".py", "_type4py.json")

        with open(json_file_path, "w") as json_file:
            inferred_serializable = [
                {k: list(v) if isinstance(v, set) else v for k, v in d.items()}
                for d in output
            ]
            json.dump(inferred_serializable, json_file, indent=4)

            # print(json.dumps(output, indent=4))
    except Exception as e:
        print(e)
