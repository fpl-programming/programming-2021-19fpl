"""
Implementation of the data structure "Node"
"""


class Node:
    """
    Node of a Binary Search Tree Data Structure
    """

    def __init__(self, value: int):
        if not isinstance(value, int):
            raise ValueError
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, node: 'Node'):
        """
        Create left child for a node
        :param node: node to turn into left child
        """
        if not node.value < self.value:
            raise ValueError
        self.left = node

    def insert_right(self, node: 'Node'):
        """
        Create right child for a node
        :param node: node to turn into right child
        """
        if not node.value > self.value:
            raise ValueError
        self.right = node
