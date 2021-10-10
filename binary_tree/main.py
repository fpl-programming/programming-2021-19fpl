"""
Programming for linguists

Implementation of the data structure "BinaryTree"
"""


class Node:
    """
    Node Data Structure
    """

    def __init__(self, root: int = None, left: 'Node' = None, right: 'Node' = None):
        self.root = root
        self.left = left
        self.right = right


class BinaryTree:
    """
    BinaryTree Data Structure
    """

    def __init__(self, root=None):
        self.name = str(root)
        self.node = Node(root)

    def _add_node_recursive(self, node, node_to_add):
        """
        Hidden function for recursive search
        :param node:
        :param added_node:
        :return:
        """
        if node_to_add < node.root and node.left:
            self._add_node_recursive(node.left, node_to_add)
        elif node_to_add > node.root and node.right:
            self._add_node_recursive(node.right, node_to_add)
        if node_to_add < node.root:
            node.left = Node(node_to_add)
        elif node_to_add > node.root:
            node.right = Node(node_to_add)
        return

    def add_node(self, node_to_add):
        """
        Add the new node by means of binary search algorithm
        :return:
        """
        if not self.node.root:
            self.node = Node(node_to_add)
        self._add_node_recursive(self.node, node_to_add)

    def delete_node(self, node_to_delete):
        """
        Delete the node by means of binary search algorithm
        :return:
        """
        current_root = self.node
        while True:
            if current_root and node_to_delete < current_root.root:
                current_root = current_root.left
            elif current_root and node_to_delete > current_root.root:
                current_root = current_root.right
            else:
                self.node = Node(None)
                break
        return

    def search_node(self, searched_node):
        """
        Search the node with the specified value of the key feature
        :return:
        """
        current_root = self.node
        while True:
            if current_root and searched_node < current_root.root:
                current_root = current_root.left
            elif current_root and searched_node > current_root.root:
                current_root = current_root.right
            else:
                return Node(None)
        return current_root

    def get_max_tree_height(self):
        """
        Get the maximum height of the tree
        :return:
        """
