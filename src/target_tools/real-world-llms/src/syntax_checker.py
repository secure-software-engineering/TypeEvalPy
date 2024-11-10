import os
import ast

def check_syntax(file_path):
    """
    Check the syntax of a Python file.
    Returns None if the file is syntactically correct, otherwise returns the error message.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            source_code = file.read()
        ast.parse(source_code, filename=file_path)
        return None  # No syntax errors
    except SyntaxError as e:
        return f"SyntaxError in {file_path}: {e}"

def find_files_with_syntax_errors(root_directory):
    """
    Recursively walk through all .py files in a directory and check for syntax errors.
    Prints out the files with syntax errors.
    """
    files_with_errors = []
    
    for subdir, _, files in os.walk(root_directory):
        for file_name in files:
            if file_name.endswith('.py'):
                file_path = os.path.join(subdir, file_name)
                error_message = check_syntax(file_path)
                if error_message:
                    files_with_errors.append(error_message)
    
    if files_with_errors:
        print("Files with syntax errors:")
        for error in files_with_errors:
            print(error)
    else:
        print("No syntax errors found in any files.")

if __name__ == "__main__":
    root_directory = "/media/pysse/analysis/TypeEvalPy/src/target_tools/real-world-llms/src/.scrapy"
    find_files_with_syntax_errors(root_directory)