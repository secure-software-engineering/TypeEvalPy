import libcst as cst
import os

class TypeAnnotatorTransformer(cst.CSTTransformer):
    def leave_FunctionDef(
        self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
        # Annotate parameters with 'MASK' if they are not annotated or replace with 'MASK'
        new_params = []
        for param in updated_node.params.params:
            if param.annotation is None or param.annotation.annotation.value != "MASK":
                annotated_param = param.with_changes(
                    annotation=cst.Annotation(cst.Name("MASK"))
                )
                new_params.append(annotated_param)
            else:
                new_params.append(param)
        
        # Annotate or replace return type with 'MASK'
        new_returns = (
            updated_node.returns
            if updated_node.returns and updated_node.returns.annotation.value == "MASK"
            else cst.Annotation(cst.Name("MASK"))
        )

        # Return the updated function definition
        return updated_node.with_changes(
            params=updated_node.params.with_changes(params=new_params),
            returns=new_returns,
        )

    def leave_Assign(
        self, original_node: cst.Assign, updated_node: cst.Assign
    ) -> cst.BaseStatement:
        annotations = []

        # Check for multiple targets (chained assignments)
        if len(updated_node.targets) > 1:
            # Generate individual annotations for each target, handling chained and nested tuples
            for assign_target in updated_node.targets:
                target = assign_target.target
                annotations.extend(self._generate_annotations_from_target(target, updated_node.value))
            # Add the original assignment after the annotations
            return cst.FlattenSentinel(annotations + [updated_node])

        # Handle standalone assignment or dictionary items
        target = updated_node.targets[0].target

        # If target is a complex structure (e.g., nested tuple unpacking)
        if isinstance(target, cst.Tuple):
            # Extract all individual names in the tuple unpacking and create annotations
            unpacked_annotations = [
                cst.AnnAssign(
                    target=cst.Name(value=name),
                    annotation=cst.Annotation(cst.Name("MASK")),
                    value=None
                )
                for name in self._extract_names_from_tuple(target)
            ]
            return cst.FlattenSentinel(unpacked_annotations + [updated_node])

        # Annotate standalone variables, attributes, and other compatible targets
        annotations.extend(self._generate_annotations_from_target(target, updated_node.value))

        # If we generated any annotations, add them before the original assignment
        return cst.FlattenSentinel(annotations + [updated_node]) if annotations else updated_node

    def _generate_annotations_from_target(self, target, value):
        """
        Generates `AnnAssign` nodes with `MASK` for each standalone target or tuple unpacking.
        If the target already has the annotation `MASK`, it skips re-annotation.
        """
        annotations = []
        if isinstance(target, cst.Name):
            # Add new AnnAssign if this target is unannotated
            annotations.append(
                cst.AnnAssign(
                    target=target,
                    annotation=cst.Annotation(cst.Name("MASK")),
                    value=None
                )
            )
        elif isinstance(target, cst.AnnAssign):
            # If the target is already an AnnAssign, replace the annotation with MASK
            if target.annotation.annotation.value != "MASK":
                annotations.append(
                    target.with_changes(annotation=cst.Annotation(cst.Name("MASK")))
                )
        elif isinstance(target, cst.Tuple):
            # Recursive extraction for nested tuples
            for name in self._extract_names_from_tuple(target):
                annotations.append(
                    cst.AnnAssign(
                        target=cst.Name(value=name),
                        annotation=cst.Annotation(cst.Name("MASK")),
                        value=None  # Keep original value only in the main assignment
                    )
                )
        elif isinstance(target, cst.Attribute):
            # For attribute assignments (e.g., resp.status), skip if already annotated with MASK
            if (
                not isinstance(target, cst.AnnAssign)
                or target.annotation.annotation.value != "MASK"
            ):
                annotations.append(
                    cst.AnnAssign(
                        target=target,
                        annotation=cst.Annotation(cst.Name("MASK")),
                        value=value
                    )
                )
        elif isinstance(target, cst.Subscript):
            # Dictionary item (e.g., d["key"] = value)
            annotations.append(
                cst.AnnAssign(
                    target=target,
                    annotation=cst.Annotation(cst.Name("MASK")),
                    value=None
                )
            )
        return annotations

    def _extract_names_from_tuple(self, tuple_node):
        """
        Recursively extract names from nested tuples for unpacking assignments.
        """
        names = []
        for element in tuple_node.elements:
            if isinstance(element.value, cst.Name):
                names.append(element.value.value)
            elif isinstance(element.value, cst.Tuple):
                # Recursive call for nested tuples
                names.extend(self._extract_names_from_tuple(element.value))
        return names

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

# Set the root directory for the Python files based on the structure
root_directory = '/media/pysse/analysis/TypeEvalPy/src/target_tools/real-world-llms/src/many-types-4-py-dataset/repos/ABitMoreDepth'

# Loop through all .py files in the directory tree
for subdir, _, files in os.walk(root_directory):
    for file_name in files:
        if file_name.endswith('.py'):
            file_path = os.path.join(subdir, file_name)
            process_file(file_path)