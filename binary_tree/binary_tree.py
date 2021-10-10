"""

Implementation of the data structure "Binary Tree"
"""


class Node:
    def __init__(self, value=None, right=None, left=None):
        self.value = value
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, element: int):
        if not self.root:
            self.root = Node(element)
        else:
            self._add(element, self.root)

    def _add(self, element, node):
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
        if self.find(element):
            if element == self.root.value:
                self.root = None
            else:
                self._remove(element, self.root)
        else:
            raise ValueError

    def _remove(self, element, node):
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
        if not self.root:
            raise ValueError
        return self._find(element, self.root)

    def _find(self, element, node):
        if element == node.value:
            return node.value
        elif element < node.value and node.left:
            return self._find(element, node.left)
        elif element > node.value and node.right:
            return self._find(element, node.right)
        else:
            raise ValueError

    def get_height(self):
        if not self.root:
            return 0
        return self._get_height(self.root)

    def _get_height(self, node):
        if node.left:
            left_height = self._get_height(node.left)
        else:
            left_height = 0
        if node.right:
            right_height = self._get_height(node.right)
        else:
            right_height = 0
        return 1 + max(left_height, right_height)
