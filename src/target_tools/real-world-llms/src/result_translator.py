import ast
import json
import os
from typing import List, Dict, Any

def parse_annotation(annotation_node: ast.AST) -> str:
    """
    Convert an AST annotation node into its original source code string.

    Args:
        annotation_node (ast.AST): The AST node representing a type annotation.

    Returns:
        str: The string representation of the type annotation, or "None" if missing.
    """
    if annotation_node is None:
        return "None"
    return ast.unparse(annotation_node)  # Converts AST back to source code.


def get_type_annotations_from_content(source: str, filename: str) -> List[Dict[str, Any]]:
    """
    Extract all type annotations from a Python source code string.

    Args:
        source (str): The source code content as a string.
        filename (str): The filename of the source file (used for metadata).

    Returns:
        List[Dict[str, Any]]: A list of annotation metadata including file, line number, column, 
                              function or variable name, and type string.
    """
    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        print(f"File-level SyntaxError in {filename}: {e}")
        return []  # Skip file if it contains a top-level syntax error

    annotations = []
    source_lines = source.splitlines()

    class TypeAnnotationVisitor(ast.NodeVisitor):
        """
        AST visitor that extracts function parameter types, return types,
        and annotated variable types.
        """
        def __init__(self, filename):
            self.filename = os.path.basename(filename).replace("_gt.json", ".py")
            self.current_class = None
            self.current_function = None
            self.processed_variables = set()  # Track already extracted variables to prevent duplicates

        def visit_ClassDef(self, node: ast.ClassDef):
            self.current_class = node.name
            self.generic_visit(node)
            self.current_class = None

        def visit_FunctionDef(self, node: ast.FunctionDef):
            self.current_function = node.name
            function_name = f"{self.current_class}.{self.current_function}" if self.current_class else self.current_function

            try:
                line = source_lines[node.lineno - 1]
                name_col_offset = line.index(node.name) + 1

                # Parameters: normal + keyword-only
                for arg in node.args.args + node.args.kwonlyargs:
                    if arg.annotation:
                        param_id = (node.lineno, arg.arg)
                        if param_id not in self.processed_variables:
                            annotations.append({
                                "file": self.filename,
                                "line_number": arg.lineno,
                                "col_offset": arg.col_offset + 1,
                                "parameter": arg.arg,
                                "function": function_name,
                                "type": [parse_annotation(arg.annotation)]
                            })
                            self.processed_variables.add(param_id)

                # *args
                if node.args.vararg and node.args.vararg.annotation:
                    vararg_id = (node.args.vararg.lineno, node.args.vararg.arg)
                    if vararg_id not in self.processed_variables:
                        annotations.append({
                            "file": self.filename,
                            "line_number": node.args.vararg.lineno,
                            "col_offset": node.args.vararg.col_offset + 1,
                            "parameter": f"*{node.args.vararg.arg}",
                            "function": function_name,
                            "type": [parse_annotation(node.args.vararg.annotation)]
                        })
                        self.processed_variables.add(vararg_id)

                # **kwargs
                if node.args.kwarg and node.args.kwarg.annotation:
                    kwarg_id = (node.args.kwarg.lineno, node.args.kwarg.arg)
                    if kwarg_id not in self.processed_variables:
                        annotations.append({
                            "file": self.filename,
                            "line_number": node.args.kwarg.lineno,
                            "col_offset": node.args.kwarg.col_offset + 1,
                            "parameter": f"**{node.args.kwarg.arg}",
                            "function": function_name,
                            "type": [parse_annotation(node.args.kwarg.annotation)]
                        })
                        self.processed_variables.add(kwarg_id)

                # Return type
                if node.returns:
                    func_id = (node.lineno, function_name)
                    if func_id not in self.processed_variables:
                        annotations.append({
                            "file": self.filename,
                            "line_number": node.lineno,
                            "col_offset": name_col_offset,
                            "function": function_name,
                            "type": [parse_annotation(node.returns)]
                        })
                        self.processed_variables.add(func_id)

                self.generic_visit(node)

            except Exception as e:
                print(f"Error in function '{function_name}' in {filename}: {e}")

            self.current_function = None

        def visit_AnnAssign(self, node: ast.AnnAssign):
            """
            Visit annotated assignments (e.g., x: int = 5) and extract variable type annotations.
            """
            try:
                if isinstance(node.target, ast.Name):
                    variable_name = node.target.id
                    function_name = self.current_function if self.current_function else None
                    var_id = (node.lineno, variable_name)

                    if var_id not in self.processed_variables:
                        # If it's a class variable (not in a function), prepend class name
                        if self.current_class and not function_name:
                            variable_name = f"{self.current_class}.{variable_name}"

                        annotation_entry = {
                            "file": self.filename,
                            "line_number": node.lineno,
                            "col_offset": node.col_offset + 1,
                            "variable": variable_name,
                            "type": [parse_annotation(node.annotation)]
                        }

                        if function_name:
                            annotation_entry["function"] = function_name

                        annotations.append(annotation_entry)
                        self.processed_variables.add(var_id)

            except Exception as e:
                print(f"Error processing annotated assignment in {self.filename}: {e}")

    visitor = TypeAnnotationVisitor(filename)
    visitor.visit(tree)
    return annotations


def format_annotations_for_ground_truth(annotations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Format raw annotation records into a simplified structure for ground truth comparisons.

    Args:
        annotations (List[Dict[str, Any]]): Raw extracted annotation dictionaries.

    Returns:
        List[Dict[str, Any]]: Formatted annotation dictionaries with only necessary keys.
    """
    formatted_annotations = []
    for annotation in annotations:
        formatted_annotation = {
            "file": annotation["file"],
            "line_number": annotation["line_number"],
            "col_offset": annotation["col_offset"],
            "type": annotation["type"],
        }

        # Add relevant identifier fields
        if "function" in annotation:
            formatted_annotation["function"] = annotation["function"]
        if "variable" in annotation:
            formatted_annotation["variable"] = annotation["variable"]
        if "parameter" in annotation:
            formatted_annotation["parameter"] = annotation["parameter"]

        formatted_annotations.append(formatted_annotation)

    return formatted_annotations


def translate_output_to_annotations(source: str, filename: str) -> str:
    """
    Convert source code into a JSON-formatted list of type annotations.

    Args:
        source (str): Python source code as a string.
        filename (str): Path to the file (used for metadata).

    Returns:
        str: JSON string representing extracted and formatted type annotations.
    """
    annotations = get_type_annotations_from_content(source, filename)
    formatted_annotations = format_annotations_for_ground_truth(annotations)
    return json.dumps(formatted_annotations, indent=4)


def main():
    """
    Entry point for testing the annotation extraction tool.
    Reads a Python file and prints extracted annotations in JSON format.
    """
    test_file = "/home/ssegpu/rashida/TypeEvalPy/src/target_tools/real-world-llms/src/.scrapy/main.py"  # Replace with your test file path

    with open(test_file, "r") as f:
        source_code = f.read()

    output_json = translate_output_to_annotations(source_code, test_file)
    print(output_json)


if __name__ == "__main__":
    main()