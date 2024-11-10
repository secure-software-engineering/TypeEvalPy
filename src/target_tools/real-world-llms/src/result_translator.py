import ast
import json
import os
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
    """Parse type annotations from source code content with syntax error handling."""
    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        print(f"File-level SyntaxError in {filename}: {e}")
        return []  # Skip the whole file if file-level syntax is invalid

    annotations = []
    source_lines = source.splitlines()

    class TypeAnnotationVisitor(ast.NodeVisitor):
        def __init__(self, filename):
            self.filename = os.path.basename(filename).replace("_gt.json", ".py")  # Standardize filename

        def visit_FunctionDef(self, node: ast.FunctionDef):
            current_function = node.name
            try:
                # Adjust col_offset for the function name
                line = source_lines[node.lineno - 1]
                name_col_offset = line.index(current_function) + 1  # 1-based col offset for function name
                
                # Process function parameters
                for arg in node.args.args:
                    if arg.annotation:
                        annotations.append({
                            "file": self.filename,
                            "line_number": arg.lineno - 1,  # Adjust for filename line
                            "col_offset": arg.col_offset + 1,  # Convert to 1-based
                            "parameter": arg.arg,
                            "function": current_function,
                            "type": [parse_annotation(arg.annotation)]
                        })

                # Process function return type
                if node.returns:
                    annotations.append({
                        "file": self.filename,
                        "line_number": node.lineno - 1,  # Adjust for filename line
                        "col_offset": name_col_offset,  # Corrected col_offset for function name
                        "function": current_function,
                        "type": [parse_annotation(node.returns)]
                    })

                # Process annotated variables within the function
                for stmt in node.body:
                    if isinstance(stmt, ast.AnnAssign) and stmt.annotation:
                        annotations.append({
                            "file": self.filename,
                            "line_number": stmt.lineno - 1,  # Adjust for filename line
                            "col_offset": stmt.col_offset + 1,  # Convert to 1-based
                            "variable": stmt.target.id if isinstance(stmt.target, ast.Name) else None,
                            "function": current_function,
                            "type": [parse_annotation(stmt.annotation)]
                        })

            except (SyntaxError, AttributeError, IndexError) as e:
                print(f"Error in function '{current_function}' in {filename}: {e}")

        def visit_AnnAssign(self, node: ast.AnnAssign):
            try:
                # Process global or class-level annotated variables
                if isinstance(node.target, ast.Name):
                    annotations.append({
                        "file": self.filename,
                        "line_number": node.lineno - 1,  # Adjust for filename line
                        "col_offset": node.col_offset + 1,  # Convert to 1-based
                        "variable": node.target.id,
                        "type": [parse_annotation(node.annotation)]
                    })
            except (SyntaxError, AttributeError) as e:
                print(f"Error processing annotated assignment in {self.filename}: {e}")
    
    visitor = TypeAnnotationVisitor(filename)
    visitor.visit(tree)

    return annotations

def format_annotations_for_ground_truth(annotations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Format annotations to match the ground truth JSON structure."""
    formatted_annotations = []
    for annotation in annotations:
        # Order fields to match ground truth exactly
        formatted_annotation = {
            "file": annotation["file"],
            "line_number": annotation["line_number"],
            "col_offset": annotation["col_offset"],
        }
        
        # Conditionally add fields based on their presence
        if "function" in annotation:
            formatted_annotation["function"] = annotation["function"]
        if "variable" in annotation:
            formatted_annotation["variable"] = annotation["variable"]
        if "parameter" in annotation:
            formatted_annotation["parameter"] = annotation["parameter"]
        
        # Place "type" at the end as in ground truth
        formatted_annotation["type"] = annotation["type"]

        formatted_annotations.append(formatted_annotation)
    
    return formatted_annotations

def translate_output_to_annotations(source: str, filename: str) -> str:
    """Translate source code output to JSON-formatted type annotations, matching ground truth format."""
    annotations = get_type_annotations_from_content(source, filename)
    formatted_annotations = format_annotations_for_ground_truth(annotations)
    return json.dumps(formatted_annotations, indent=4)

# Main function for testing
def main():
    test_file = "/media/pysse/analysis/TypeEvalPy/src/target_tools/real-world-llms/src/.scrapy/test.py"  # Update this path as necessary
    
    # Read the test file content
    with open(test_file, "r") as f:
        source_code = f.read()

    # Run the translator on the test file
    output_json = translate_output_to_annotations(source_code, test_file)

    # Print the output to verify
    print("Translated Annotations Output:")
    print(output_json)

if __name__ == "__main__":
    main()