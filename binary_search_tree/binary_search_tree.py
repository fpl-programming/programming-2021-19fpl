# pylint: disable=too-few-public-methods
"""
Implementation of the data structure 'Binary Search Tree'
"""


class NoTreeError(Exception):
    """
    Custom error
    """


class NoNodeError(Exception):
    """
    Custom error
    """


class NodeExistsError(Exception):
    """
    Custom error
    """


class Node:
    """
    A class for nodes
    """
    def __init__(self, root: int,  left=None, right=None):
        if not isinstance(root, int) or isinstance(root, bool):
            raise TypeError
        self.root = root
        self.left = left
        self.right = right


class BinarySearchTree:
    """
    Binary Search Tree data structure
    """
    def __init__(self):
        self.root = None

    def add(self, number: int, node=None):
        """
        Adds 'number' to the tree
        :param number: element to add to the tree
        :param node: tree's node
        """
        if not isinstance(number, int) or isinstance(number, bool):
            raise TypeError
        if self.root is None:
            self.root = Node(number)
        elif self.find(number) is not None:
            raise NodeExistsError
        else:
            if node:
                if number < node.root:
                    if node.left:
                        self.add(number, node.left)
                    else:
                        node.left = Node(number)
                else:
                    if node.right:
                        self.add(number, node.right)
                    else:
                        node.right = Node(number)
            else:
                self.add(number, self.root)

    def find(self, number: int, node=None):
        """
        Returns the node with root equal to number if exists
        :param number: element to find in the tree
        :param node: tree's node
        """
        if not isinstance(number, int) or isinstance(number, bool):
            raise TypeError
        if self.root is None:
            raise NoTreeError
        if node is None:
            return self.find(number, self.root)

        if number < node.root:
            if node.left is not None:
                return self.find(number, node.left)
            return None
        if number > node.root:
            if node.right is not None:
                return self.find(number, node.right)
            return None
        return node

    def remove(self, number: int, node=None):
        """
        Removes number and all its children from the tree
        :param number: element to remove from the tree
        :param node: tree's node
        """
        if not isinstance(number, int) or isinstance(number, bool):
            raise TypeError
        if self.root is None:
            raise NoTreeError
        if not self.find(number):
            raise NoNodeError
        if node is None:
            return self.remove(number, self.root)
        if number == self.root.root:
            self.root = None
        elif number < node.root:
            if number == node.left.root:
                node.left = None
            else:
                self.remove(number, node.left)
        else:
            if number == node.right.root:
                node.right = None
            else:
                self.remove(number, node.right)

    def get_height(self, node=None):
        """
        Returns number of levels in the tree
        :param node: tree's node
        """
        if self.root is None:
            return 0
        if node is None:
            return self.get_height(self.root)
        left_height = self.get_height(node.left) if node.left else 0
        right_height = self.get_height(node.right) if node.right else 0
        return max(left_height, right_height) + 1

    def __str__(self):
        return self._print_tree(self.root)

    def _print_tree(self, node=None, level=0):
        """
        Returns a string which represents the structure of the tree
        :param node: tree's node
        :param level: tree's level
        """
        visual_tree = ''
        if node is not None:
            visual_tree += self._print_tree(node.right, level + 1)
            visual_tree += '|  ' * level + str(node.root) + '\n'
            visual_tree += self._print_tree(node.left, level + 1)
        return visual_tree
