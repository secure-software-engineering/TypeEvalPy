import ast

from pytype import config
from pytype.tools.annotate_ast import annotate_ast

source = open("test.py").read()


def _get_node_key(node):
    base = (node.lineno, node.__class__.__name__)

    if isinstance(node, ast.Name):
        return base + (node.id,)
    elif isinstance(node, ast.Attribute):
        return base + (node.attr,)
    elif isinstance(node, ast.FunctionDef):
        return base + (node.name,)
    else:
        return base


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
