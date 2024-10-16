#datastrucutres
# ast_engine.py

class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type  # "operator" (AND/OR) or "operand" (condition)
        self.value = value      # For operands (like age, department)
        self.left = left        # Left child node
        self.right = right      # Right child node

    def __repr__(self):
        return f"Node(type={self.type}, value={self.value})"
