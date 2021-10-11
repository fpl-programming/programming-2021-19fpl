"""
Node class
"""


class Node:
    """
    Node class
    """
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return f'Node: {self.value}'

    def __repr__(self):
        pass
