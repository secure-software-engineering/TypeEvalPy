# result_translator.py
import ast
import json
from typing import List, Dict, Any

def parse_annotation(annotation_node: ast.AST) -> str:
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

def get_type_annotations_from_content(source: str, filename: str) -> List[Dict[str, Any]]:
    """Parse type annotations from source code content."""
    tree = ast.parse(source)
    annotations = []

    class TypeAnnotationVisitor(ast.NodeVisitor):
        def __init__(self, filename):
            self.filename = filename

        def visit_FunctionDef(self, node: ast.FunctionDef):
            current_function = node.name
            for arg in node.args.args:
                if arg.annotation:
                    annotations.append({
                        "file": self.filename,
                        "line_number": arg.lineno,
                        "col_offset": arg.col_offset,
                        "parameter": arg.arg,
                        "function": current_function,
                        "type": [parse_annotation(arg.annotation)]
                    })

            if node.returns:
                annotations.append({
                    "file": self.filename,
                    "line_number": node.lineno,
                    "col_offset": node.col_offset,
                    "function": current_function,
                    "type": [parse_annotation(node.returns)]
                })

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

        def visit_AnnAssign(self, node: ast.AnnAssign):
            if isinstance(node.target, ast.Name):
                annotations.append({
                    "file": self.filename,
                    "line_number": node.lineno,
                    "col_offset": node.col_offset,
                    "variable": node.target.id,
                    "type": [parse_annotation(node.annotation)]
                })
            self.generic_visit(node)
    
    visitor = TypeAnnotationVisitor(filename)
    visitor.visit(tree)

    return annotations

def format_annotations_for_ground_truth(annotations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Format annotations to match the ground truth JSON structure."""
    formatted_annotations = []
    for annotation in annotations:
        formatted_annotation = {
            "file": annotation["file"],
            "line_number": annotation["line_number"],
            "col_offset": annotation["col_offset"],
            "type": annotation["type"]
        }
        
        # Conditionally add fields based on their presence
        if "function" in annotation:
            formatted_annotation["function"] = annotation["function"]
        if "variable" in annotation:
            formatted_annotation["variable"] = annotation["variable"]
        if "parameter" in annotation:
            formatted_annotation["parameter"] = annotation["parameter"]
        
        formatted_annotations.append(formatted_annotation)
    
    return formatted_annotations

def translate_output_to_annotations(source: str, filename: str) -> str:
    """Translate source code output to JSON-formatted type annotations, matching ground truth format."""
    annotations = get_type_annotations_from_content(source, filename)
    formatted_annotations = format_annotations_for_ground_truth(annotations)
    return json.dumps(formatted_annotations, indent=4)