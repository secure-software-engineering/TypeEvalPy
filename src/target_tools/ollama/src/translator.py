import json

import utils


def translate_content(data):
    type_mapping = {
        "integer": "int",
        "string": "str",
        "function": "callable",
        "none": "Nonetype",
    }

    try:
        if isinstance(data, str):
            data = json.loads(data)
    except Exception as e:
        print(f"Not a valid JSON: {e}")
        raise utils.JsonException

    for entry in data:
        if "type" in entry:
            translated_types = [
                type_mapping[t.lower()] if t.lower() in type_mapping else t
                for t in entry["type"]
            ]
            entry["type"] = translated_types
        else:
            entry["type"] = []

    return data
