"""
Implementation of the data structure "Binary Tree"
"""

from binarytree.node import Node


class BinaryTree:
    """
    Binary Tree Data structure
    """
    def __init__(self, root=None):
        self.root = None
        if isinstance(root, Node):
            self.root = root
        elif isinstance(root, int):
            self.root = Node(root)
        self.dfs_nodes = []

    def add(self, node_to_add: Node, current_node: Node = None):
        """
        Add a node to the certain place in the binary tree
        :param node_to_add: node to add to the binary tree
        :param current_node: the node in the current recursive iteration
        """
        if not isinstance(node_to_add, Node):
            raise ValueError('Binary tree contains only Node instances')
        if self.root is None or self.root.value is None:
            self.root = node_to_add
        if not current_node:
            current_node = self.root
        if node_to_add.value < current_node.value:
            if current_node.left is None:
                current_node.add_left(node_to_add)
            self.add(node_to_add, current_node.left)
        elif node_to_add.value > current_node.value:
            if current_node.right is None:
                current_node.add_right(node_to_add)
            self.add(node_to_add, current_node.right)

    def find(self, node_to_find: Node, current_node: Node = None):
        """
        Find if a node is in the binary tree
        :param node_to_find: the node to be found in the binary tree
        :param current_node: the node in the current recursive iteration
        :return: the sought node if the binary tree contains it
        """
        if self.root is not None and isinstance(node_to_find, Node):
            if not current_node:
                current_node = self.root
            if node_to_find.value == current_node.value:
                return current_node
            if node_to_find.value < current_node.value:
                if current_node.left is not None:
                    if node_to_find.value == current_node.left.value:
                        return current_node.left
                    return self.find(node_to_find, current_node.left)
            if node_to_find.value > current_node.value:
                if current_node.right is not None:
                    if node_to_find.value == current_node.right.value:
                        return current_node.right
                    return self.find(node_to_find, current_node.right)
            return None

    def remove(self, node_to_remove: Node, current_node: Node = None):
        """
        Remove the node and its descendants from the binary tree and return the node value
        :param node_to_remove: the node to remove from the binary tree
        :param current_node: the node in the current recursive iteration
        :return: the removed node if it has been removed from the binary tree
        """
        if self.root is None:
            raise IndexError('Cannot remove nodes from empty binary tree')
        if isinstance(node_to_remove, Node):
            if not current_node:
                current_node = self.root
            if current_node is not None and current_node.value is not None:
                if node_to_remove.value < current_node.value:
                    if current_node.left is not None:
                        return self.remove(node_to_remove, current_node.left)
                if node_to_remove.value > current_node.value:
                    if current_node.right is not None:
                        return self.remove(node_to_remove, current_node.right)
                if current_node is not None and current_node.value == node_to_remove.value:
                    current_node.value = None
                    current_node.left = None
                    current_node.right = None
                    return node_to_remove
            return None

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
