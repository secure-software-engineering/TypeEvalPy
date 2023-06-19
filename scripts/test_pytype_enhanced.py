import ast
import json
from pytype import config
from pytype.tools.annotate_ast import annotate_ast

source = open("test.py").read()


def _get_node_key(node):
    base = (node.lineno, node.__class__.__name__)

    if isinstance(node, ast.Name):
        # print(base)
        # print(node.id)
        return base + (node.id,)
    elif isinstance(node, ast.Attribute):
        print(base)
        print(node.name)
        print(node.attr)
        return base + (node.attr,)
    elif isinstance(node, ast.FunctionDef):
        return base + (node.name,)
    else:
        return base


"""
def get_annotations_dict(module):
    return {
        _get_node_key(node): node.resolved_annotation
        for node in ast.walk(module)
        if hasattr(node, "resolved_type")
    }


pytype_options = config.Options.create(python_version=(3, 10))
module = annotate_ast.annotate_source(source, ast, pytype_options)

types_dict = get_annotations_dict(module)
print(types_dict)
"""


def parse_type_hint(node):
    if isinstance(node, ast.Name):
        return node.id
    elif isinstance(node, ast.Subscript):
        return parse_type_hint(node.value)
    elif isinstance(node, ast.Attribute):
        return parse_type_hint(node.value) + "." + node.attr
    elif isinstance(node, ast.Call):
        return parse_type_hint(node.func)
    elif isinstance(node, ast.Constant):
        return node.value
    return None


def get_annotations_list(module):
    results = []
    current_class = None
    for node in ast.walk(module):
        if hasattr(node, "resolved_type"):
            if isinstance(node, ast.ClassDef):
                current_class = node.name
            if isinstance(node, ast.FunctionDef):
                function = {
                    "file": "test.py",
                    "line_number": node.lineno,
                    "function": node.name,
                    "type": [node.resolved_annotation],
                }
                results.append(function)

                if current_class:
                    function["function"] = f"{current_class}.{node.name}"

                for param in node.args.args:
                    parameter = {
                        "file": "test.py",
                        "line_number": param.lineno,
                        "parameter": param.arg,
                        "function": node.name,
                        "type": [node.resolved_annotation],
                    }
                    if current_class:
                        function["function"] = f"{current_class}.{node.name}"
                    results.append(parameter)

            elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                variable = {
                    "file": "test.py",
                    "line_number": node.lineno,
                    "variable": node.id,
                    "type": [node.resolved_annotation],
                }
                results.append(variable)

    return results


pytype_options = config.Options.create(python_version=(3, 10))
module = annotate_ast.annotate_source(source, ast, pytype_options)

annotations_list = get_annotations_list(module)
json_output = json.dumps(annotations_list, indent=4)
print(json_output)


""" members = dir(node)
                for member in members:
                    value = getattr(node, member)
                    print(f"{member}: {value}")"""
