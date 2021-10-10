"""
Programming for linguists

Implementation of the data Structure "Binary Search Tree"
"""


class Node:
    """
    Node Data Structure
    """

    def __init__(self, element: int, left_node: 'Node' = None, right_node: 'Node' = None):
        if not element:
            raise ValueError
        self.element = element
        self.left_node = left_node
        self.right_node = right_node

    def first_public_method(self):
        """
        Solve a lint problem
        """

    def second_public_method(self):
        """
        Solve a lint problem
        """


class BinarySearchTree:
    """
    Binary Search Tree data structure
    """

    def __init__(self, root: int = None):
        self.root = root

    def add(self, element, node=None):
        """
        Add the element 'element' at the current place of the Binary Search Tree
        """
        if self.root is None:
            self.root = Node(element)

        else:
            if self.find(element):
                raise ValueError
            if node is None:
                node = self.root
            if element < node.element:
                if node.left_node is None:
                    node.left_node = Node(element)
                else:
                    self.add(element, node.left_node)
            else:
                if node.right_node is None:
                    node.right_node = Node(element)
                else:
                    self.add(element, node.right_node)

    def remove(self, element, node=None):
        """
        Remove the required node from Binary Tree
        """
        if self.root is None:
            raise EmptyError

        if self.find(element) is True:
            if node is None:
                node = self.root
            if element < node.element and node.left_node:
                if node.left_node.element == element:
                    node.left_node = None
                else:
                    self.remove(element, node.left_node)
            if element > node.element and node.right_node:
                if node.right_node.element == element:
                    node.right_node = None
                else:
                    self.remove(element, node.right_node)
        else:
            raise NoNodeError

    def find(self, element, node=None):
        """
        Find if this element is in Binary Search Tree
        """
        if self.root is None:
            raise EmptyError

        if node is None:
            node = self.root
        if node.element == element:
            return True
        if not node.left_node or node.right_node:
            return False
        if element < node.element and node.left_node:
            return self.find(element, node.left_node)
        if element > node.element and node.right_node:
            return self.find(element, node.right_node)
        return False

    def get_height(self, root: 'Node' = None, current_max: int = 0):
        """
        Get a height of Binary Tree
        :return: number of levels in the tree
        """
        if root is None:
            raise EmptyError

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


class EmptyError(Exception):
    """
    Custom Error
    """


class NoNodeError(Exception):
    """
    Custom Error
    """
