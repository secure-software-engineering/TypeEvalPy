import json


def translate_content(data):
    type_mapping = {
        "integer": "int",
        "string": "str",
        "function": "callable",
        "none": "Nonetype",
    }

    for entry in data:
        translated_types = [
            type_mapping[t.lower()] if t.lower() in type_mapping else t
            for t in entry["type"]
        ]
        entry["type"] = translated_types

    return data
