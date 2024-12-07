import libcst as cst
import os

class TypeAnnotatorTransformer(cst.CSTTransformer):
    def leave_FunctionDef(
        self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
        # Replace parameters and return type annotations with [MASK]
        mask_annotation = cst.Annotation(cst.parse_expression("[MASK]"))
        
        new_params = [
            param.with_changes(annotation=mask_annotation)
            for param in updated_node.params.params
        ]
        
        # Annotate *args with [MASK] if it exists
        new_star_arg = updated_node.params.star_arg
        if isinstance(new_star_arg, cst.Param):
            new_star_arg = new_star_arg.with_changes(annotation=mask_annotation)

        # Annotate **kwargs with [MASK] if it exists
        new_star_kwarg = updated_node.params.star_kwarg
        if isinstance(new_star_kwarg, cst.Param):
            new_star_kwarg = new_star_kwarg.with_changes(annotation=mask_annotation)
        
        # Annotate keyword-only arguments after * with [MASK] if they exist
        new_kwonly_params = [
            kwonly_param.with_changes(annotation=mask_annotation)
            if isinstance(kwonly_param, cst.Param) else kwonly_param
            for kwonly_param in updated_node.params.kwonly_params
        ]

        # Replace return type with [MASK]
        new_returns = mask_annotation

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
        # Replace any existing annotation with [MASK]
        return updated_node.with_changes(
            annotation=cst.Annotation(cst.parse_expression("[MASK]"))
        )

    def _extract_names(self, target):
        """
        Recursively extract names from tuples, lists, and generator expressions for individual annotation.
        """
        names = []
        if isinstance(target, (cst.Tuple, cst.List)):
            # Handle tuple and list unpacking
            for element in target.elements:
                names.extend(self._extract_names(element.value))
        elif isinstance(target, cst.Name):
            # Direct variable name
            names.append(target)
        elif isinstance(target, cst.Attribute):
            # Handle attribute names like self.width
            names.append(target)
        elif isinstance(target, cst.GeneratorExp):
            # Handle generator expressions by treating each target as a separate variable
            for comprehension in target.for_in:
                names.extend(self._extract_names(comprehension.target))
        return names

    def leave_Assign(
        self, original_node: cst.Assign, updated_node: cst.Assign
    ) -> cst.BaseStatement:
        annotations = []
        mask_annotation = cst.Annotation(cst.parse_expression("[MASK]"))

        # Process each target in the assignment, including complex unpacking
        for target in updated_node.targets:
            extracted_names = self._extract_names(target.target)
            for name in extracted_names:
                # Add annotation for each extracted variable
                annotations.append(
                    cst.AnnAssign(
                        target=name,
                        annotation=mask_annotation,
                        value=None  # Set value to None for individual annotations
                    )
                )
        
        # Add the original assignment after the individual annotations
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
    root_directory = '/home/ssegpu/rashida/TypeEvalPy/autogen_typeevalpy_benchmark'
    for subdir, _, files in os.walk(root_directory):
        for file_name in files:
            if file_name.endswith('.py'):
                file_path = os.path.join(subdir, file_name)
                process_file(file_path)

if __name__ == "__main__":
    main()