import libcst as cst
import os

class TypeAnnotatorTransformer(cst.CSTTransformer):
    def leave_FunctionDef(
        self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
        # Annotate parameters with 'MASK' if they are not annotated
        new_params = []
        for param in updated_node.params.params:
            if param.annotation is None:
                annotated_param = param.with_changes(
                    annotation=cst.Annotation(cst.Name("MASK"))
                )
                new_params.append(annotated_param)
            else:
                new_params.append(param)
        
        # Annotate return type with 'MASK' if not annotated
        new_returns = updated_node.returns
        if updated_node.returns is None:
            new_returns = cst.Annotation(cst.Name("MASK"))

        # Return the updated function definition
        return updated_node.with_changes(
            params=updated_node.params.with_changes(params=new_params),
            returns=new_returns,
        )

    def leave_Assign(
        self, original_node: cst.Assign, updated_node: cst.Assign
    ) -> cst.BaseStatement:
        # Convert Assign to AnnAssign with 'MASK' annotation
        if isinstance(updated_node.targets[0].target, cst.Name):
            # Create AnnAssign with 'MASK' annotation
            annotated_node = cst.AnnAssign(
                target=updated_node.targets[0].target,
                annotation=cst.Annotation(cst.Name("MASK")),
                value=updated_node.value,
            )
            return annotated_node
        return updated_node

def process_file(file_path):
    with open(file_path, "r") as source_code:
        code = source_code.read()

    # Parse the file into a concrete syntax tree (CST)
    tree = cst.parse_module(code)

    # Apply the type annotation transformer
    transformer = TypeAnnotatorTransformer()
    modified_tree = tree.visit(transformer)

    # Save the modified code to a new file
    new_file_path = file_path.replace(".py", "_annotated.py")
    with open(new_file_path, "w") as new_file:
        new_file.write(modified_tree.code)

    print(f"Processed and saved: {new_file_path}")

# Set the root directory for the Python files based on the structure
root_directory = '/media/pysse/analysis/TypeEvalPy/micro-benchmark/python_features'

# Loop through all .py files in the directory tree
for subdir, _, files in os.walk(root_directory):
    for file_name in files:
        if file_name.endswith('.py'):
            file_path = os.path.join(subdir, file_name)
            process_file(file_path)