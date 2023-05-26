import ast
import symtable
from pathlib import Path


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


in_py_path = "../micro-benchmark"
for _file in sorted(Path(in_py_path).rglob("*.py")):
    # Create a dictionary to store line numbers for identifiers
    identifiers = {}
    print(_file.parts[-4:])
    describe_symtable(
        symtable.symtable(_file.read_text(), _file.name, compile_type="exec")
    )

    # Parse the code into an AST (Abstract Syntax Tree)
    tree = ast.parse(_file.read_text())

    # Traverse the AST and extract line numbers for identifiers
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            identifier = node.id
            lineno = node.lineno
            if identifier in identifiers:
                identifiers[identifier].append(lineno)
            else:
                identifiers[identifier] = [lineno]

    print("\n")
    print(identifiers)
    print("\n\n###########################\n\n")
