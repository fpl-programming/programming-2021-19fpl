"""
Programming for linguists
Implementation of the data structure "BinarySearchTree"
"""

# pylint: disable=too-few-public-methods


class Node:
    """
    Node Data Structure
    """

    def __init__(self, root: int or None, left_node: 'Node' = None, right_node: 'Node' = None):
        self.root = root
        self.left_node = left_node
        self.right_node = right_node


class BinarySearchTree:
    """
    BinarySearchTree Structure
    """
    def __init__(self, name: str = None, root: int = None):
        self.name = name
        self._root = Node(root)

    def add(self, element: int):
        """
        Add the element ‘element’ at the correct place of the tree
        :param element: element to add to the tree
        """
        if not self._root.root:
            self._root = Node(element)
            return
        if self.find(element).root:
            raise ValueError('Element Already In The Tree')
        self._add_node(self._root, element)

    def _add_node(self, root: 'Node', element: int):
        """
        Function to find the right place for the element in the Binary Tree
        :param root: current node to search a free place in
        :param element: element to add to the tree
        """
        if element < root.root and root.left_node:
            self._add_node(root.left_node, element)
        elif element > root.root and root.right_node:
            self._add_node(root.right_node, element)
        else:
            new_node = Node(element)
            if element < root.root:
                root.left_node = new_node
            elif element > root.root:
                root.right_node = new_node
            return

    def remove(self, element: int):
        """
        Remove the required node from Binary Tree
        :param element: element remove from the tree
        """
        if self.find(element).root is None:
            return 'Not found'
        if element == self._root.root:
            self._root = Node(None)
            return

    def find(self, element: int):
        """
        Find and return the required node
        :param element: element to find in the tree
        """
        current_node = self._root
        while current_node.root != element and current_node.root:
            if element < current_node.root and current_node.left_node:
                current_node = current_node.left_node
            elif element > current_node.root and current_node.right_node:
                current_node = current_node.right_node
            else:
                return Node(None)
        return current_node

    def get_root(self):
        """
        Return the current root of the tree
        """
        return self._root.root

    def get_height(self, root: 'Node' = None, current_max: int = 0):
        """
        Get a height of Binary Tree
        :return: number of levels in the tree
        """
        if root.left_node:
            left_max = self.get_height(root.left_node, current_max + 1)
        else:
            left_max = current_max
        if root.right_node:
            right_max = self.get_height(root.right_node, current_max + 1)
        else:
            right_max = current_max
        current_max = (max(left_max, right_max))
        return current_max
