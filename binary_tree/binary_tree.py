"""
Programming for linguists

Implementation of the data structure "Binary Search Tree"
"""


class TreeNode:
    """
    Node Structure
    """
    def __init__(self, value: int):
        if not isinstance(value, int):
            raise ValueError
        self.value = value
        self.left = None
        self.right = None

    def first_method(self):
        """
        Fix error
        """

    def second_method(self):
        """
        Fix error
        """


class BinarySearchTree:
    """
    Binary Search Tree Structure
    """

    def __init__(self):
        self.root = None

    def add(self, value):
        """
        Add element to the tree
        """
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.add_(value, self.root)

    def add_(self, value, node):
        """
        Add element to the tree (recursive method)
        """
        if value < node.value:
            if node.left is not None:
                self.add_(value, node.left)
            else:
                node.left = TreeNode(value)
        else:
            if node.right is not None:
                self.add_(value, node.right)
            else:
                node.right = TreeNode(value)

    def find(self, value):
        """
        Find element in the tree
        """
        if self.root is not None:
            return self.find_(value, self.root)
        return None

    def find_(self, value, node):
        """
        Find element in the tree (recursive method)
        """
        if value == node.value:
            return node
        elif value < node.value and node.left is not None:
            return self.find_(value, node.left)
        elif value > node.value and node.right is not None:
            return self.find_(value, node.right)

    def get_height(self, node=None):
        """
        Find the top of the tree
        """
        if self.root is None:
            print('Root is empty')
        if node.left_element:
            left_h = self.get_height(node.left_element)
        else:
            left_h = 0
        if node.right_element:
            right_h = self.get_height(node.right_element)
        else:
            right_h = 0
        return 1 + max(left_h, right_h)

    def remove(self, element):
        """
        Remove the element from BinarySearchTree
        """
        if self.find(element):
            if element == self.root.value:
                self.root = None
            else:
                self.remove_(element, self.root)
        else:
            raise ValueError

    def remove_(self, element, node):
        """
        Remove the element from BinarySearchTree (recursive method)
        """
        if element < node.value and node.left:
            if element == node.left.value:
                node.left = None
            else:
                self.remove_(element, node.left)
        elif element > node.value and node.right:
            if element == node.right.value:
                node.right = None
            else:
                self.remove_(element, node.right)
