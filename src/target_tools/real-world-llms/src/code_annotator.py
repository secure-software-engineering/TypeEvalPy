import libcst as cst
import os

class TypeAnnotatorTransformer(cst.CSTTransformer):
    def leave_FunctionDef(
        self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
        # Force replace parameters and return type annotations with 'TP_MASK'
        new_params = [
            param.with_changes(annotation=cst.Annotation(cst.Name("TP_MASK")))
            for param in updated_node.params.params
        ]
        
        # Annotate *args with TP_MASK if it exists
        new_star_arg = updated_node.params.star_arg
        if isinstance(new_star_arg, cst.Param):
            new_star_arg = new_star_arg.with_changes(
                annotation=cst.Annotation(cst.Name("TP_MASK"))
            )

        # Annotate **kwargs with TP_MASK if it exists
        new_star_kwarg = updated_node.params.star_kwarg
        if isinstance(new_star_kwarg, cst.Param):
            new_star_kwarg = new_star_kwarg.with_changes(
                annotation=cst.Annotation(cst.Name("TP_MASK"))
            )
        
        # Annotate keyword-only arguments after * with TP_MASK if they exist
        new_kwonly_params = [
            kwonly_param.with_changes(annotation=cst.Annotation(cst.Name("TP_MASK")))
            if isinstance(kwonly_param, cst.Param) else kwonly_param
            for kwonly_param in updated_node.params.kwonly_params
        ]

        # Replace return type with TP_MASK
        new_returns = cst.Annotation(cst.Name("TP_MASK"))

        # Return the updated function definition
        return updated_node.with_changes(
            params=updated_node.params.with_changes(
                params=new_params,
                star_arg=new_star_arg,
                star_kwarg=new_star_kwarg,
                kwonly_params=new_kwonly_params
            ),
            returns=new_returns,
        )

    def leave_AnnAssign(
        self, original_node: cst.AnnAssign, updated_node: cst.AnnAssign
    ) -> cst.BaseStatement:
        # Force replace any existing annotation with 'TP_MASK'
        return updated_node.with_changes(
            annotation=cst.Annotation(cst.Name("TP_MASK"))
        )

    def _extract_names(self, target):
        """
        Recursively extract names from tuples or lists for individual annotation.
        """
        names = []
        if isinstance(target, (cst.Tuple, cst.List)):
            for element in target.elements:
                names.extend(self._extract_names(element.value))
        elif isinstance(target, cst.Name):
            names.append(target)
        return names

    def leave_Assign(
        self, original_node: cst.Assign, updated_node: cst.Assign
    ) -> cst.BaseStatement:
        annotations = []

        # Handle all types of unpacking and assignments by extracting individual names
        for target in updated_node.targets:
            extracted_names = self._extract_names(target.target)
            for name in extracted_names:
                annotations.append(
                    cst.AnnAssign(
                        target=name,
                        annotation=cst.Annotation(cst.Name("TP_MASK")),
                        value=None
                    )
                )

        # Add the original assignment after the annotations
        annotations.append(updated_node)

        # Flatten the list of annotated statements
        return cst.FlattenSentinel(annotations)

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