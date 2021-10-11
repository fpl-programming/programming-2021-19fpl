"""
Programming for linguists

Implementation of the data structure "Binary Search Tree"
"""

from node import Node


class BinarySearchTree:
    """
    Binary Tree Search Data Structure
    """
    def __init__(self, root: int):
        if isinstance(root, bool):
            root = 1 if root else 0
        self.root = Node(root)

    def add(self, element: int, current_node: Node = None, in_tree_check: bool = True):
        """
        Add the element ‘element’ to the tree
        :param element: element to add to the tree
        :param current_node: node that we are working with at the moment
        :param in_tree_check: if True then check if the element is already in the tree
        """
        if isinstance(element, bool):
            element = 1 if element else 0
        if in_tree_check and self.find(element, current_node):
            raise AlreadyInTree
        current_node = current_node if current_node else self.root
        if element < current_node.value and not current_node.left:
            current_node.left = Node(element)
            current_node.left.parent = current_node
            return None
        if element > current_node.value and not current_node.right:
            current_node.right = Node(element)
            current_node.right.parent = current_node
            return None
        else:
            current_node = (current_node.left if element < current_node.value
                            else current_node.right)
            return self.add(element, current_node, False)

    def remove(self, element: int, current_node: Node = None):
        """
        Remove the element from the tree
        :param element: element to remove from the tree
        :param current_node: node that we are working with at the moment
        """
        if isinstance(element, bool):
            element = 1 if element else 0
        if element == self.root.value:
            raise CannotRemoveRoot
        current_node = current_node if current_node else self.root
        if element == current_node.value:
            while current_node.right or current_node.left:
                current_node.value = (current_node.right.value if current_node.right
                                      else current_node.left.value)
                current_node = current_node.right if current_node.right else current_node.left
            if current_node.value == current_node.parent.left.value:
                current_node.parent.left = None
            elif current_node.value == current_node.parent.right.value:
                current_node.parent.right = None
            return None
        if not current_node.right and not current_node.left:
            raise ValueError
        current_node = current_node.left if element < current_node.value else current_node.right
        return self.remove(element, current_node)

    def find(self, element: int, current_node: Node = None):
        """
        Search for the element and check if it is in the tree
        :param element: element to find
        :param current_node: node that we are working with at the moment
        :return: True if element is in the tree.
                 False if element is not in the tree
        """
        if isinstance(element, bool):
            element = 1 if element else 0
        current_node = current_node if current_node else self.root
        if element == current_node.value:
            return True
        if (element < current_node.value and not current_node.left) \
                or (element > current_node.value and not current_node.right):
            return False
        current_node = current_node.left if element < current_node.value else current_node.right
        return self.find(element, current_node)

    def get_height(self, current_node: Node = None, current_height: int = 0):
        """
        Get the height of the tree
        :param current_node: node that we are working with at the moment
        :param current_height: height of the tree that we are working with at the moment
        :return: height of the tree
        """
        current_node = current_node if current_node else self.root
        left_height = (self.get_height(current_node.left, current_height + 1) if current_node.left
                       else current_height)
        right_height = (self.get_height(current_node.right, current_height + 1)
                        if current_node.right else current_height)
        return max(left_height, right_height)


class AlreadyInTree(Exception):
    """
    Raised when trying to add an element that is already in the tree
    """


class CannotRemoveRoot(Exception):
    """
    Raised when trying to remove the tree root
    """
