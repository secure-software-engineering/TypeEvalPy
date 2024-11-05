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

    # Define a visitor class to collect all annotations
    class AnnotationChecker(cst.CSTVisitor):
        def __init__(self):
            self.all_annotations_masked = True  # Default assumption: all are masked
        
        def visit_Param(self, node: cst.Param):
            # Check if the parameter annotation is MASK
            if node.annotation and (not isinstance(node.annotation.annotation, cst.Name) or node.annotation.annotation.value != "MASK"):
                self.all_annotations_masked = False
                print(f"Annotation check failed in {file_path}: Parameter not masked with MASK.")
        
        def visit_AnnAssign(self, node: cst.AnnAssign):
            # Check if the variable annotation is MASK
            if not isinstance(node.annotation.annotation, cst.Name) or node.annotation.annotation.value != "MASK":
                self.all_annotations_masked = False
                print(f"Annotation check failed in {file_path}: Variable not masked with MASK")
        
        def visit_FunctionDef(self, node: cst.FunctionDef):
            # Check if the return type annotation is MASK
            if node.returns and (not isinstance(node.returns.annotation, cst.Name) or node.returns.annotation.value != "MASK"):
                self.all_annotations_masked = False
                print(f"Annotation check failed in {file_path}: Return type not masked with MASK")

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
        print("All files passed: All annotations were correctly replaced with MASK")
    else:
        print("Some files failed or were skipped due to errors: Not all annotations were replaced with MASK.")

if __name__ == "__main__":
    main()