import ast
import symtable
from pathlib import Path


class NodeVisitor(ast.NodeVisitor):
    def visit_FunctionDef(self, node):
        print(
            f"Function: {node.name} -> Line: {node.lineno}, Column:"
            f" {node.col_offset + 5}"
        )
        for arg in node.args.args:
            if arg.arg == "self":
                continue
            print(
                f"Parameter: {arg.arg} -> Line: {arg.lineno}, Column:"
                f" {arg.col_offset + 1}"
            )

        self.generic_visit(node)

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                print(
                    f"Local variable: {target.id} -> Line: {target.lineno}, Column:"
                    f" {target.col_offset + 1}"
                )
        self.generic_visit(node)

    def visit_Lambda(self, node):
        print(f"Lambda function -> Line: {node.lineno}, Column: {node.col_offset + 1}")
        for arg in node.args.args:
            print(
                f"Parameter: {arg.arg} -> Line: {arg.lineno}, Column:"
                f" {arg.col_offset+1}"
            )
        self.generic_visit(node)


def parse_python_code(code):
    tree = ast.parse(code)
    NodeVisitor().visit(tree)


def describe_symtable(st, recursive=True, indent=0):
    def print_d(s, *args):
        prefix = " " * indent
        print(prefix + s, *args)

    assert isinstance(st, symtable.SymbolTable)
    print_d("Symtable: type=%s, name=%s" % (st.get_type(), st.get_name()))
    print_d("  identifiers:", list(st.get_identifiers()))

    if recursive:
        for child_st in st.get_children():
            describe_symtable(child_st, recursive, indent + 5)


in_py_path = "../micro-benchmark/python_features"
for _file in sorted(Path(in_py_path).rglob("*.py")):
    # Create a dictionary to store line numbers for identifiers
    # identifiers = {}
    print(_file.parts[-4:])
    # describe_symtable(
    #     symtable.symtable(_file.read_text(), _file.name, compile_type="exec")
    # )

    # # Parse the code into an AST (Abstract Syntax Tree)
    # tree = ast.parse(_file.read_text())

    # # Traverse the AST and extract line numbers for identifiers
    # for node in ast.walk(tree):
    #     if isinstance(node, ast.Name):
    #         identifier = node.id
    #         lineno = node.lineno
    #         if identifier in identifiers:
    #             identifiers[identifier].append(lineno)
    #         else:
    #             identifiers[identifier] = [lineno]

    print("\n")
    parse_python_code(_file.read_text())
    # print(identifiers)
    print("\n\n###########################\n\n")
