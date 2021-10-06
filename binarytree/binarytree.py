"""
Programming for linguists

Implementation of the data structure "Binarytree"
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left_element = None
        self.right_element = None


class BinaryTree(Node):
    def __init__(self, tree, root):
        self.root = None

    def add(self, element):
        pass

    def find_recurs(self, node, key):

        if self.node.data == self.key or self.node is None:
            return self.root
        elif self.key < self.node.data:
            return self.find_recurs(node.left_element,key)
        else:
            return self.find_recurs(node.right_element, key)

    def remove_recurs(self):
        pass

    def get_height(self):
        pass
