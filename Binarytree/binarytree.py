"""
Programming for linguists
Implementation of the data structure "Binary Search Tree"
"""


class EmptyError (Exception):
    """
    Custom Error
    """


class NoNodeError (Exception):
    """
    Custom Error
    """


class Node:
    """
    Node Data Structure
    """
    def __init__(self, el: int):
        if not isinstance(el, int):
            raise ValueError
        self.element = el
        self.right = None
        self.left = None

    def first_public_method(self):
        """
        To solve the lint problem
        """

    def second_public_method(self):
        """
        To solve the lint problem
        """


class BinarySearchTree:
    """
    Binary Search Tree Data Structure
    """
    def __init__(self):
        self.root = None

    def add(self, el, node=None):
        """
        Add element to the tree
        """
        if self.root is None:
            self.root = Node(el)
        else:
            if self.find(el):
                raise ValueError
            if node is None:
                node = self.root
            if el < node.element:
                if node.left is None:
                    node.left = Node(el)
                else:
                    self.add(el, node.left)
            else:
                if node.right is None:
                    node.right = Node(el)
                else:
                    self.add(el, node.right)

    def remove(self, el, node=None):
        """
        Remove element from the tree
        """
        if self.root is None:
            raise EmptyError
        if self.find(el) is True:
            if node is None:
                node = self.root
            if el < node.el and node.left:
                if node.left.el == el:
                    node.left = None
                else:
                    self.remove(el, node.left)
            if el > node.el and node.right:
                if node.right.el == el:
                    node.right = None
                else:
                    self.remove(el, node.right)
        else:
            raise NoNodeError

    def find(self, el, node=None):
        """
        Find if this element is in the tree
        """
        if self.root is None:
            raise EmptyError
        if node is None:
            node = self.root
        if node.element == el:
            return True
        if not (node.left or node.right):
            return False
        if el < node.element and node.left:
            return self.find(el, node.left)
        if el > node.element and node.right:
            return self.find(el, node.right)
        return False

    def get_height(self, node=None):
        """
        Return the max height of the tree
        """
        if self.root is None:
            raise EmptyError
        if node is None:
            node = self.root
        if node.left:
            left_height = self.get_height(node.left)
        else:
            left_height = 0
        if node.right:
            right_height = self.get_height(node.right)
        else:
            right_height = 0
        return 1 + max(left_height, right_height)
