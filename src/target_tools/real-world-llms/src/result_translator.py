import ast
import json
from typing import List, Dict


def parse_annotation(annotation_node):
    """Convert AST annotation node into a readable type string."""
    if isinstance(annotation_node, ast.Name):
        return annotation_node.id
    elif isinstance(annotation_node, ast.Subscript):
        value = parse_annotation(annotation_node.value)
        slice_value = parse_annotation(annotation_node.slice)
        return f"{value}[{slice_value}]"
    elif isinstance(annotation_node, ast.Tuple):
        return f"tuple[{', '.join(parse_annotation(elt) for elt in annotation_node.elts)}]"
    elif isinstance(annotation_node, ast.Constant):
        return repr(annotation_node.value)
    return ast.dump(annotation_node)  # Fallback to raw AST dump if unrecognized


def get_type_annotations(filename: str) -> List[Dict]:
    with open(filename, "r") as file:
        source = file.read()
    tree = ast.parse(source)
    
    annotations = []

    class TypeAnnotationVisitor(ast.NodeVisitor):
        def __init__(self, filename):
            self.filename = filename

        def visit_FunctionDef(self, node):
            # Record function name for scope
            current_function = node.name

            # Capture parameter types
            for arg in node.args.args:
                if arg.annotation:
                    annotations.append({
                        "file": self.filename,
                        "line_number": arg.lineno,
                        "col_offset": arg.col_offset,
                        "variable": arg.arg,
                        "function": current_function,
                        "type": [parse_annotation(arg.annotation)]
                    })

            # Capture return type
            if node.returns:
                annotations.append({
                    "file": self.filename,
                    "line_number": node.lineno,
                    "col_offset": node.col_offset,
                    "variable": "return",
                    "function": current_function,
                    "type": [parse_annotation(node.returns)]
                })

            # Capture local variables with type annotations
            for stmt in node.body:
                if isinstance(stmt, ast.AnnAssign) and stmt.annotation:
                    annotations.append({
                        "file": self.filename,
                        "line_number": stmt.lineno,
                        "col_offset": stmt.col_offset,
                        "variable": stmt.target.id if isinstance(stmt.target, ast.Name) else None,
                        "function": current_function,
                        "type": [parse_annotation(stmt.annotation)]
                    })
            self.generic_visit(node)

        def visit_AnnAssign(self, node):
            # Capture global variables with type annotations
            if isinstance(node.target, ast.Name):
                annotations.append({
                    "file": self.filename,
                    "line_number": node.lineno,
                    "col_offset": node.col_offset,
                    "variable": node.target.id,
                    "function": None,
                    "type": [parse_annotation(node.annotation)]
                })
            self.generic_visit(node)
    
    visitor = TypeAnnotationVisitor(filename)
    visitor.visit(tree)

    return annotations


# Path to the source file
source_file = "/media/pysse/analysis/TypeEvalPy/src/target_tools/real-world-llms/src/test-repo/BBVA/apicheck/build_docker_images.py"

# Get the annotations
annotations = get_type_annotations(source_file)

# Print the result in JSON format
print(json.dumps(annotations, indent=4))