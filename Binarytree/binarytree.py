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

    def __init__(self, data):
        self.data = data
        self.left_element = None
        self.right_element = None

    def method_1(self):
        """
        To solve the lint problem
        """

    def method_2(self):
        """
        To solve the lint problem
        """


class BinarySearchTree:
    """
    Binary Search Tree Data Structure
    """
    def __init__(self):
        self.root = None

    def add(self, element, node=None):
        """
        Add element to the tree
        """
        if self.root is None:
            self.root = Node(element)
        else:
            if self.find(element):
                raise ValueError
            if node is None:
                node = self.root
            if element > node.element:
                if node.right_element is None:
                    node.right_element = Node(element)
                self.add(node.right_element, element)
            else:
                if node.left.element is None:
                    node.left_element = Node(element)
                self.add(node.left_element, element)

    def remove(self, element, node=None):
        """
        Remove element from the tree
        """
        if self.find(element) is True:
            if node is None:
                node = self.root
            if element < node.element and node.left_element:
                if node.left.element == element:
                    node.left_element = None
                else:
                    self.remove(element, node.leftelement)
            if element > node.element and node.right_element:
                if node.right_element == element:
                    node.right_element = None
                else:
                    self.remove(element, node.right_element)
        else:
            raise NoNodeError

    def find(self, element, node=None):
        """
        Find if this element is in the tree
        """
        if self.root is None:
            raise EmptyError

        if node is None:
            node = self.root
        if node.element == element or node.left_element or node.right_element:
            return True
        if element < node.element and node.left_element:
            return self.find(element, node.left_element)
        if element > node.element and node.right_element:
            return self.find(element, node.right_element)
        return False

    def get_height(self, node=None):
        """
        Return the max height of the tree
        """
        if self.root is None:
            raise EmptyError
        if node is None:
            node = self.root
        if node.left_element:
            left_height = self.get_height(node.left)
        else:
            left_height = 0
        if node.right_element:
            right_height = self.get_height(node.right)
        else:
            right_height = 0
        return 1 + max(left_height, right_height)
