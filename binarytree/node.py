"""
Implementation of the structure "Node" of data structure "Binary Tree"
"""


class Node:
    """
    Node of the Binary Tree Structure (auxiliary)
    """
    def __init__(self, value: int):
        if not isinstance(value, int):
            raise ValueError('Nodes can only contain integers')
        self.value = value
        self.left = None
        self.right = None

    def add_left(self, node_to_add):
        """
        Add left descendant of the node
        :param node_to_add: a node with value smaller than that of the current node
        """
        if self.left is not None:
            raise IndexError('Left descendant is already added to this node')
        if not isinstance(node_to_add, Node):
            raise TypeError('Binary tree contains only Node instances')
        if node_to_add.value >= self.value:
            raise ValueError('Left descendant must have a value smaller than current node')
        self.left = node_to_add

    def add_right(self, node_to_add):
        """
        Add right descendant of the node
        :param node_to_add: a node with value smaller than that of the current node
        """
        if self.right is not None:
            raise IndexError('Right descendant is already added to this node')
        if not isinstance(node_to_add, Node):
            raise TypeError('Binary tree contains only Node instances')
        if node_to_add.value <= self.value:
            raise ValueError('Right descendant must have a value greater than current node')
        self.right = node_to_add
