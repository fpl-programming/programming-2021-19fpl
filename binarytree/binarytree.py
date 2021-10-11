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
        self.dfs_nodes = []

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
        Find if a value is in the binary tree
        :param value: the value of the node to be found in the binary tree
        :return: the value of the sought node if the binary tree contains it
        """
        def find_recursive(value_to_find, current_node):
            if value_to_find == current_node.value:
                return current_node.value
            if value_to_find < current_node.value:
                if current_node.left is not None:
                    if value_to_find == current_node.left.value:
                        return current_node.left.value
                    return find_recursive(value_to_find, current_node.left)
            if value_to_find > current_node.value:
                if current_node.right is not None:
                    if value_to_find == current_node.right.value:
                        return current_node.right.value
                    return find_recursive(value_to_find, current_node.right)
            return None

        if self.root is not None and isinstance(value, int):
            return find_recursive(value, self.root)

    def remove(self, value: int):
        """
        Remove the node and its descendants from the binary tree and return the node value
        :param value: the value of the node to remove from the binary tree
        :return: the value of the node if it has been removed from the binary tree
        """
        def remove_recursive(value_to_remove, current_node):
            if current_node is not None and current_node.value is not None:
                if value_to_remove < current_node.value:
                    return remove_recursive(value_to_remove, current_node.left)
                if value_to_remove > current_node.value:
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

    def get_height(self, current_node: Node = None, current_height: int = 0):
        """
        Calculate the height of the binary tree
        :param current_node: the node in the current recursive iteration
        :param current_height: the height calculated in the current iteration
        :return: the number of levels in the tree
        """
        if self.root is None:
            return None
        if self.root is not None and current_node is None:
            current_node = self.root
        if current_node.left is not None:
            left_height = self.get_height(current_node.left, current_height + 1)
        else:
            left_height = current_height
        if current_node.right is not None:
            right_height = self.get_height(current_node.right, current_height + 1)
        else:
            right_height = current_height
        current_height = max(left_height, right_height)
        return current_height

    def get_dfs(self):
        """
        Print the sequence of nodes from DFS traversal through the binary tree
        """
        def get_dfs_recursive(node_to_traverse):
            if node_to_traverse is None:
                node_to_traverse = self.root
            else:
                self.dfs_nodes.append(node_to_traverse.value)
                if node_to_traverse.left is not None:
                    get_dfs_recursive(node_to_traverse.left)
                if node_to_traverse.right is not None:
                    get_dfs_recursive(node_to_traverse.right)

        if self.root is not None:
            self.dfs_nodes = []
            get_dfs_recursive(self.root)
        if self.dfs_nodes:
            for node in self.dfs_nodes:
                print(node, end=' ')
        else:
            print('-')


binary_tree = BinaryTree()
# node_values = [14, 7, 12, 11, 10, 6]
# node_values = [6, 5, 11, 12, 2, 7]
node_values = [15, 14, 13, 17, 25, 8]
for val in node_values:
    binary_tree.add(val)
binary_tree.get_dfs()
