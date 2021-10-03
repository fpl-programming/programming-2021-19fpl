"""
Implementation of the data structure "Binary Tree"
"""

from binarytree.node import Node


class BinaryTree:
    """
    Binary Tree Data structure
    """
    def __init__(self, root: int):
        self.nodes = []
        self.root = Node(root)
        pass

    def add(self, value):
        """
        Add the value to the certain place in the binary tree
        :param value: value to add to the binary tree
        """
        pass

    def remove(self, value):
        """
        Remove the value from the binary tree
        :param value: value to remove from the binary tree
        """
        pass

    def find(self, value) -> bool:
        """
        Return whether the value is in the binary tree or not
        :return: True if the binary tree contains the value.
                 False if the binary tree does not contain the value
        """
        pass

    def get_height(self):
        """
        Return the height of the binary tree
        """
        pass

    def get_dfs(self):
        """
        Return the DFS of the binary tree
        """
        pass
