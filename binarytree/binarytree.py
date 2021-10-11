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

    def find(self, value: int):
        """
        Return the value if the binary tree contains it
        """
        def find_recursive(value_to_find, current_node):
            if value_to_find == current_node.value:
                return current_node.value
            elif value_to_find < current_node.value:
                if current_node.left is not None:
                    if value_to_find == current_node.left.value:
                        return current_node.left.value
                    return find_recursive(value_to_find, current_node.left)
            elif value_to_find > current_node.value:
                if current_node.right is not None:
                    if value_to_find == current_node.right.value:
                        return current_node.right.value
                    return find_recursive(value_to_find, current_node.right)

        if self.root is not None and isinstance(value, int):
            return find_recursive(value, self.root)

    def remove(self, value):
        """
        Remove the node and its descendants from the binary tree and return the node value
        :param value: value of the node that has been removed from the binary tree
        """
        def remove_recursive(value_to_remove, current_node):
            if current_node is not None and current_node.value is not None:
                if value_to_remove < current_node.value:
                    return remove_recursive(value_to_remove, current_node.left)
                elif value_to_remove > current_node.value:
                    return remove_recursive(value_to_remove, current_node.right)
                else:
                    if current_node is not None and current_node.value == value_to_remove:
                        current_node.value = None
                        return value_to_remove
            return None

        if self.root is None:
            raise IndexError('Cannot remove nodes from empty binary tree')
        if isinstance(value, int):
            return remove_recursive(value, self.root)

    def get_dfs(self):
        """
        Return the DFS of the binary tree
        """
        pass

    def get_height(self):
        """
        Return the height of the binary tree
        """
        pass
