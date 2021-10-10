"""
Implementation of the data structure "Binary Tree"
"""


class Node:
    """
    Node data structure
    """
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None

    def some_method(self):
        """
        empty
        """
        pass

    def some_method_again(self):
        """
        empty
        """
        pass


class BinaryTree:
    """
    Node data structure
    """
    def __init__(self):
        self.root = None

    def add(self, element: int):
        """
        Add the element to the binary tree
        """
        if not self.root:
            self.root = Node(element)
        else:
            self._add(element, self.root)

    def _add(self, element, node):
        """
        Recursive method add
        """
        if element < node.value:
            if node.left:
                self._add(element, node.left)
            else:
                node.left = Node(element)
        elif element > node.value:
            if node.right:
                self._add(element, node.right)
            else:
                node.right = Node(element)

    def remove(self, element):
        """
        Remove the element from the binary tree
        """
        if self.find(element):
            if element == self.root.value:
                self.root = None
            else:
                self._remove(element, self.root)
        else:
            raise ValueError

    def _remove(self, element, node):
        """
        Recursive method remove
        """
        if element < node.value and node.left:
            if element == node.left.value:
                node.left = None
            else:
                self._remove(element, node.left)
        elif element > node.value and node.right:
            if element == node.right.value:
                node.right = None
            else:
                self._remove(element, node.right)

    def find(self, element):
        """
        Find the element in the binary tree
        return: the element
        """
        if not self.root:
            raise ValueError
        return self._find(element, self.root)

    def _find(self, element, node):
        """
        Recursive method find
        """
        if element == node.value:
            return node.value
        if element < node.value and node.left:
            return self._find(element, node.left)
        elif element > node.value and node.right:
            return self._find(element, node.right)
        else:
            raise ValueError

    def get_height(self):
        """
        Get the height of the binary tree
        return: the height
        """
        if not self.root:
            return 0
        return self._get_height(self.root)

    def _get_height(self, node):
        """
        Recursive method get_height
        """
        if node.left:
            left_height = self._get_height(node.left)
        else:
            left_height = 0
        if node.right:
            right_height = self._get_height(node.right)
        else:
            right_height = 0
        return 1 + max(left_height, right_height)
