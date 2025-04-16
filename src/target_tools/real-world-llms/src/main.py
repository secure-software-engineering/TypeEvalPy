import ast
from graphviz import Digraph
import os

class ASTVisualizer:
    def __init__(self):
        self.graph = Digraph()
        self.node_count = 0

    def _new_node(self, label):
        node_id = f'node{self.node_count}'
        self.graph.node(node_id, label)
        self.node_count += 1
        return node_id

    def _visit(self, node):
        if isinstance(node, ast.AST):
            node_id = self._new_node(type(node).__name__)
            for field, value in ast.iter_fields(node):
                if isinstance(value, list):
                    for item in value:
                        child_id = self._visit(item)
                        if child_id:
                            self.graph.edge(node_id, child_id)
                elif isinstance(value, ast.AST):
                    child_id = self._visit(value)
                    if child_id:
                        self.graph.edge(node_id, child_id)
                elif value is not None:
                    # Skip None values
                    leaf_id = self._new_node(str(value))
                    self.graph.edge(node_id, leaf_id)
            return node_id
        return None

    def generate(self, source_code, output_file="ast_tree"):
        tree = ast.parse(source_code)
        self._visit(tree)

        # Save in same directory as the script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(script_dir, f"{output_file}.png")
        self.graph.render(filename=output_file, directory=script_dir, format='png', cleanup=True)
        print(f" AST tree saved to: {output_path}")

# Example usage
code = """
def add(a:[MASK], b: [MASK]) -> [MASK]:
    return a + b

result: [MASK] = add(5, 10)
"""

ASTVisualizer().generate(code)