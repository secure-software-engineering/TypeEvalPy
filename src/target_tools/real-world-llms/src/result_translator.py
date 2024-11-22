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
            self.current_class = None  # Track the current class name
            self.current_function = None  # Track the current function name
            self.processed_variables = set()  # Track processed variables to avoid duplicates

        def visit_ClassDef(self, node: ast.ClassDef):
            """Visit a class definition and track its name."""
            self.current_class = node.name
            self.generic_visit(node)  # Visit all child nodes within the class
            self.current_class = None  # Reset after leaving the class

        def visit_FunctionDef(self, node: ast.FunctionDef):
            self.current_function = node.name
            function_name = f"{self.current_class}.{self.current_function}" if self.current_class else self.current_function

            try:
                line = source_lines[node.lineno - 1]
                name_col_offset = line.index(node.name) + 1  # 1-based col offset for function name

                # Process function parameters, including *args and **kwargs
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

                # Process *args
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

                # Process **kwargs
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

                # Process function return type
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

                # Visit each statement in the function body
                self.generic_visit(node)

            except (SyntaxError, AttributeError, IndexError) as e:
                print(f"Error in function '{function_name}' in {filename}: {e}")

            self.current_function = None

        def visit_AnnAssign(self, node: ast.AnnAssign):
            try:
                # Determine if it's a class or function variable
                if isinstance(node.target, ast.Name):
                    variable_name = node.target.id
                    function_name = self.current_function if self.current_function else None
                    var_id = (node.lineno, variable_name)
                    
                    if var_id not in self.processed_variables:
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

                elif isinstance(node.target, ast.Attribute) and isinstance(node.target.value, ast.Name) and node.target.value.id == "self":
                    variable_name = f"{self.current_class}.{node.target.attr}" if self.current_class else node.target.attr
                    var_id = (node.lineno, variable_name)
                    
                    if var_id not in self.processed_variables:
                        self.processed_variables.add(var_id)
                        annotations.append({
                            "file": self.filename,
                            "line_number": node.lineno,
                            "col_offset": node.col_offset + 1,
                            "variable": variable_name,
                            "function": f"{self.current_class}.{self.current_function}",
                            "type": [parse_annotation(node.annotation)]
                        })

            except (SyntaxError, AttributeError) as e:
                print(f"Error processing annotated assignment in {self.filename}: {e}")

        def visit_Assign(self, node: ast.Assign):
            # Handle assignments in functions (e.g., words, word_count in count_words)
            function_name = self.current_function if self.current_function else None
            for target in node.targets:
                if isinstance(target, ast.Name):
                    variable_name = target.id
                    var_id = (node.lineno, variable_name)
                    
                    if var_id not in self.processed_variables:
                        annotation_entry = {
                            "file": self.filename,
                            "line_number": node.lineno,
                            "col_offset": node.col_offset + 1,
                            "variable": variable_name,
                            "type": ["int"]  # Placeholder; adapt as needed
                        }
                        if function_name:
                            annotation_entry["function"] = function_name
                        annotations.append(annotation_entry)
                        self.processed_variables.add(var_id)

                elif isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and target.value.id == "self":
                    variable_name = f"{self.current_class}.{target.attr}" if self.current_class else target.attr
                    var_id = (node.lineno, variable_name)
                    
                    if var_id not in self.processed_variables:
                        self.processed_variables.add(var_id)
                        annotations.append({
                            "file": self.filename,
                            "line_number": node.lineno,
                            "col_offset": node.col_offset + 1,
                            "variable": variable_name,
                            "function": f"{self.current_class}.{self.current_function}",
                            "type": ["int"]  # Placeholder; adapt as needed
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
        }
        
        if "function" in annotation:
            formatted_annotation["function"] = annotation["function"]
        if "variable" in annotation:
            formatted_annotation["variable"] = annotation["variable"]
        if "parameter" in annotation:
            formatted_annotation["parameter"] = annotation["parameter"]
        
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
    test_file = "/home/ssegpu/rashida/TypeEvalPy/src/target_tools/real-world-llms/src/.scrapy/test.py"  # Update this path as necessary
    
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