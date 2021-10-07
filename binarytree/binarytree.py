"""
Implementation of the data structure "Binary Tree"
"""

from binarytree.node import Node
# from node import Node


class BinaryTree:
    """
    Binary Tree Data structure
    """
    def __init__(self, root: int = None):
        self.root = None
        if isinstance(root, int):
            self.root = Node(root)

    def add(self, value: int):
        """
        Add the value to the certain place in the binary tree
        :param value: value to add to the binary tree
        """
        def add_recursive(value_to_add, current_node):
            if value_to_add < current_node.value:
                if current_node.left is None:
                    current_node.add_left(Node(value_to_add))
                add_recursive(value_to_add, current_node.left)
            elif value_to_add > current_node.value:
                if current_node.right is None:
                    current_node.add_right(Node(value_to_add))
                add_recursive(value_to_add, current_node.right)

        if not isinstance(value, int):
            raise ValueError('Binary tree contains only integers')
        if self.root is not None:
            add_recursive(value, self.root)
        else:
            self.root = Node(value)

    def find(self, value) -> bool:
        """
        Return whether the value is in the binary tree or not
        :return: True if the binary tree contains the value.
                 False if the binary tree does not contain the value
        """
        if self.root is None:
            return False
        pass

    def remove(self, value):
        """
        Remove the value from the binary tree
        :param value: value to remove from the binary tree
        """
        if self.root is None:
            raise IndexError
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
