"""
Programming for linguists

Implementation of the data structure "BinaryTree"
"""


# pylint: disable=too-few-public-methods
class Node:
    """
    Node Data Structure
    """

    def __init__(self, root: int = None, left: 'Node' = None, right: 'Node' = None):
        self.node = root
        self.left = left
        self.right = right


class BinaryTree:
    """
    BinaryTree Data Structure
    """

    def __init__(self, root=None):
        self.root = Node(root)

    def _add_node_recursive(self, node, node_to_add):
        """
        Hidden function for recursive search
        """
        if node.node:
            if node_to_add < node.node and node.left:
                self._add_node_recursive(node.left, node_to_add)
            elif node_to_add > node.node and node.right:
                self._add_node_recursive(node.right, node_to_add)
            else:
                if node_to_add < node.node:
                    node.left = Node(node_to_add)
                elif node_to_add > node.node:
                    node.right = Node(node_to_add)

    def add_node(self, node_to_add):
        """
        Add the new node by means of binary search algorithm
        """
        if not self.root.node:
            self.root= Node(node_to_add)
        self._add_node_recursive(self.root, node_to_add)

    def delete_node(self, node_to_delete, node=None):
        """
        Delete the node by means of binary search algorithm
        """
        current_node = node
        if not current_node:
            current_node = self.root
        if current_node.node:
            if node_to_delete < current_node.node and current_node.left:
                self.delete_node(node_to_delete, current_node.left)
            elif node_to_delete > current_node.node and current_node.right:
                self.delete_node(node_to_delete, current_node.right)
            elif (node_to_delete < current_node.node and not current_node.left) or \
                    (node_to_delete > current_node.node and not current_node.right):
                raise ValueError("There is no such node in the tree")
            else:
                current_node.node = None
                current_node.right = None
                current_node.left = None

    def search_node(self, searched_node):
        """
        Search the node with the specified value of the key feature
        """
        current_root = self.root
        while current_root and current_root.node:
            if current_root and searched_node < current_root.node:
                current_root = current_root.left
            elif current_root and searched_node > current_root.node:
                current_root = current_root.right
            elif current_root:
                return Node(current_root.node)
        return Node(None)

    def get_max_tree_height(self, node=None):
        """
        Get the maximum height of the tree
        """
        h_left = 0
        h_right = 0
        if not node:
            if self.root.node:
                h_left += 1
                h_right += 1
            current_node = self.root
        else:
            current_node = node
        if current_node.left:
            h_left += self.get_max_tree_height(current_node.left)
            h_left += 1
        if current_node.right:
            h_right += self.get_max_tree_height(current_node.right)
            h_right += 1
        if h_right <= h_left:
            return h_left
        return h_right

    def go_wide(self):
        """
        Go through the tree in width.
        """
        if not self.root.node:
            raise ValueError("The tree is empty. Can't go threw the tree.")
        if not self.root.right and not self.root.left:
            return [self.root]
        nodes_of_level = [self.root]
        all_nodes = []
        while nodes_of_level:
            for node in nodes_of_level:
                if node.left:
                    nodes_of_level.append(node.left)
                if node.right:
                    nodes_of_level.append(node.right)
            for node in nodes_of_level:
                if node.node:
                    all_nodes.append(node)
            nodes_of_level = []
        return all_nodes
