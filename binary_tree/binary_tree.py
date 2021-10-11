"""
Programming for linguists
Implementation of the data structure Binary Search Tree
"""



class Node:
    """
    A class for nodes
    """

    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None

    def first_method(self):
        """
        lint problem
        """

    def second_method(self):
        """
        lint problem
        """

class BinarySearchTree:
    """
    Binary Search Tree data structure
    """

    def __init__(self, root: int = None):
        self.root = root

    def add(self, element, node=None):
        """
        Add the element to the Binary Search Tree
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
        Remove the required node from Binary Search Tree
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
        Find if this element is in the Binary Search Tree
        """
        if self.root is None:
            raise EmptyError

        if node is None:
            node = self.root
        if node.element == element:
            return True
        if not node.left_element or node.right_element:
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