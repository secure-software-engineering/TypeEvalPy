import libcst as cst
import os

# Function to check if all annotations in a file are MASK
def check_annotations_with_mask(file_path):
    try:
        with open(file_path, "r") as modified_file:
            modified_code = modified_file.read()
    except Exception as e:
        print(f"Could not read file {file_path}: {e}")
        return False

    try:
        # Parse the code to check annotations
        modified_tree = cst.parse_module(modified_code)
    except cst.ParserSyntaxError as e:
        print(f"Skipping {file_path}: Syntax error detected at {e}.")
        return False  # Indicate failure to parse, treated as a failed check
    except Exception as e:
        print(f"Unexpected error while parsing {file_path}: {e}")
        return False

    # Define a visitor class to collect all annotations and assignments
    class AnnotationChecker(cst.CSTVisitor):
        def __init__(self):
            self.all_annotations_masked = True  # Default assumption: all are masked

        def visit_Param(self, node: cst.Param):
            # Check if the parameter annotation is MASK
            if not node.annotation or not isinstance(node.annotation.annotation, cst.Name) or node.annotation.annotation.value != "MASK":
                self.all_annotations_masked = False
                print(f"Annotation check failed in {file_path}: Parameter '{node.name.value}' is missing MASK annotation.")
        
        def visit_AnnAssign(self, node: cst.AnnAssign):
            # Check if the variable annotation is MASK (for variables with explicit annotations)
            if not isinstance(node.annotation.annotation, cst.Name) or node.annotation.annotation.value != "MASK":
                self.all_annotations_masked = False
                if isinstance(node.target, cst.Name):
                    print(f"Annotation check failed in {file_path}: Variable '{node.target.value}' is missing MASK annotation.")
        
        def visit_FunctionDef(self, node: cst.FunctionDef):
            # Check if the return type annotation is MASK, even if not explicitly present
            if node.returns:
                if not isinstance(node.returns.annotation, cst.Name) or node.returns.annotation.value != "MASK":
                    self.all_annotations_masked = False
                    print(f"Annotation check failed in {file_path}: Return type of function '{node.name.value}' not masked with MASK.")
            else:
                # Log an error if the function does not have a return type at all
                self.all_annotations_masked = False
                print(f"Annotation check failed in {file_path}: Function '{node.name.value}' is missing return type annotation with MASK.")
            
            # Check each parameter within the function
            for param in node.params.params:
                if not param.annotation or not isinstance(param.annotation.annotation, cst.Name) or param.annotation.annotation.value != "MASK":
                    self.all_annotations_masked = False
                    print(f"Annotation check failed in {file_path}: Parameter '{param.name.value}' in function '{node.name.value}' is missing MASK annotation.")
        
        def visit_Assign(self, node: cst.Assign):
            # Check unannotated variables, logging if an annotation is missing
            for target in node.targets:
                if isinstance(target.target, cst.Name):
                    # Only log if no annotation is present for standalone assignments
                    self.all_annotations_masked = False
                    print(f"Annotation check failed in {file_path}: Variable '{target.target.value}' is missing MASK annotation.")

    # Use the visitor to verify annotations
    checker = AnnotationChecker()
    modified_tree.visit(checker)

    # Return whether all annotations were masked
    if checker.all_annotations_masked:
        print(f"File {file_path} passed the annotation check.")
    return checker.all_annotations_masked

# Main function to test all .py files in a directory for MASK annotations
def main():
    root_directory = '/media/pysse/analysis/TypeEvalPy/micro-benchmark/python_features'
    all_files_passed = True

    for subdir, _, files in os.walk(root_directory):
        for file_name in files:
            if file_name.endswith('.py'):
                file_path = os.path.join(subdir, file_name)

                # Check if all annotations were masked with MASK
                if not check_annotations_with_mask(file_path):
                    print(f"Test failed or skipped: Not all annotations were replaced with MASK in {file_path}.")
                    all_files_passed = False
                else:
                    print(f"Test passed: All annotations were correctly replaced with MASK in {file_path}.")

    # Final result
    if all_files_passed:
        print("All files passed: All annotations were correctly replaced with MASK.")
    else:
        print("Some files failed or were skipped due to errors: Not all annotations were replaced with MASK.")

if __name__ == "__main__":
    main()