"""
Implementation of the data Structure "Binary Tree"
"""


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
    Binary Tree data structure
    """

    def __init__(self, root: int = None):
        self.root = Node(root)

    def add(self, element: int):
        """
        Add the element 'element' at the current place of the Binary Tree
        :param element: element to add to the Binary Tree
        """
        if not self.root.root:
            self.root = Node(element)
            return

        if self.find(element).root:
            return ValueError

        self.add_node(self.root, element)

    def add_node(self, root: 'Node', element: int):
        """
        Function to find the right place for the element in the Binary Tree
        :param root: current node to search a free place in
        :param element: element to add to the Binary tree
        """
        if element < root.root and root.left_node:
            self.add_node(root.left_node, element)
        elif element > root.root and root.right_node:
            self.add_node(root.right_node, element)
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
        if element == self.root.root:
            self.root = Node(None)
            return

    def find(self, element: int):
        """
        Find and return the required node in Binary Tree
        :param element: element to find in the tree
        """
        current_node = self.root
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
        return self.root.root

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
