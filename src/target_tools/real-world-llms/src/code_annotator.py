import libcst as cst
import os

class TypeAnnotatorTransformer(cst.CSTTransformer):
    def leave_FunctionDef(
        self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
        # Force replace parameters and return type annotations with 'MASK'
        new_params = [
            param.with_changes(annotation=cst.Annotation(cst.Name("MASK")))
            for param in updated_node.params.params
        ]
        
        # Annotate *args with MASK if it exists
        new_star_arg = updated_node.params.star_arg
        if isinstance(new_star_arg, cst.Param):
            new_star_arg = new_star_arg.with_changes(
                annotation=cst.Annotation(cst.Name("MASK"))
            )

        # Annotate **kwargs with MASK if it exists
        new_star_kwarg = updated_node.params.star_kwarg
        if isinstance(new_star_kwarg, cst.Param):
            new_star_kwarg = new_star_kwarg.with_changes(
                annotation=cst.Annotation(cst.Name("MASK"))
            )
        
        # Replace return type with MASK
        new_returns = cst.Annotation(cst.Name("MASK"))

        # Return the updated function definition
        return updated_node.with_changes(
            params=updated_node.params.with_changes(
                params=new_params,
                star_arg=new_star_arg,
                star_kwarg=new_star_kwarg
            ),
            returns=new_returns,
        )

    def leave_AnnAssign(
        self, original_node: cst.AnnAssign, updated_node: cst.AnnAssign
    ) -> cst.BaseStatement:
        # Force replace any existing annotation with 'MASK'
        return updated_node.with_changes(
            annotation=cst.Annotation(cst.Name("MASK"))
        )

    def leave_Assign(
        self, original_node: cst.Assign, updated_node: cst.Assign
    ) -> cst.BaseStatement:
        annotations = []

        # Handle standalone variable assignments, attributes, dictionary keys, etc.
        for target in updated_node.targets:
            target = target.target
            if isinstance(target, (cst.Name, cst.Attribute, cst.Subscript)):
                annotations.append(
                    cst.AnnAssign(
                        target=target,
                        annotation=cst.Annotation(cst.Name("MASK")),
                        value=updated_node.value
                    )
                )

        # Place the updated assignments before the original assignment
        return cst.FlattenSentinel(annotations) if annotations else updated_node

def process_file(file_path):
    with open(file_path, "r") as source_code:
        code = source_code.read()

    # Parse the file into a concrete syntax tree (CST)
    tree = cst.parse_module(code)

    # Apply the type annotation transformer
    transformer = TypeAnnotatorTransformer()
    modified_tree = tree.visit(transformer)

    # Write the modified code back to the original file
    with open(file_path, "w") as original_file:
        original_file.write(modified_tree.code)

    print(f"Processed and saved: {file_path}")

# Process all .py files in a specified directory
def main():
    root_directory = '/media/pysse/analysis/TypeEvalPy/micro-benchmark/python_features'
    for subdir, _, files in os.walk(root_directory):
        for file_name in files:
            if file_name.endswith('.py'):
                file_path = os.path.join(subdir, file_name)
                process_file(file_path)

if __name__ == "__main__":
    main()