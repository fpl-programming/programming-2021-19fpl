"""
Programming for linguists

Implementation of the data structure "Binary Search Tree"
"""

from binary_search_tree.node import Node


class BinarySearchTree:
    """
    Binary Tree Search Data Structure
    """
    def __init__(self, root: int):
        self.root = Node(root)

    def add(self, element: int, current_node: Node = None, in_tree_check: bool = True):
        """
        Add the element ‘element’ to the tree
        :param element: element to add to the tree
        :param current_node: node that we are working with at the moment
        :param in_tree_check: if True then check if the element is already in the tree
        """
        if in_tree_check and self.find(element, current_node):
            raise AlreadyInTree
        current_node = current_node if current_node else self.root
        if element < current_node.value and not current_node.left:
            current_node.left = Node(element)
            current_node.left.parent = current_node
        elif element > current_node.value and not current_node.right:
            current_node.right = Node(element)
            current_node.right.parent = current_node
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
        current_node = current_node if current_node else self.root
        if element == current_node.value:
            while current_node.right or current_node.left:
                current_node.value = (current_node.right.value if current_node.right
                                      else current_node.left.value)
                current_node = current_node.right if current_node.right else current_node.left
            if current_node.parent and current_node.value == current_node.parent.left.value:
                current_node.parent.left = None
            elif current_node.parent and current_node.value == current_node.parent.right.value:
                current_node.parent.right = None
            return
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
        current_node = current_node if current_node else self.root
        if element == current_node.value:
            return True
        if (element < current_node.value and not current_node.left) \
                or (element > current_node.value and not current_node.right):
            return False
        current_node = current_node.left if element < current_node.value else current_node.right
        return self.find(element, current_node)

    def get_height(self, current_node: Node = None):
        """
        Get the height of the tree
        :param current_node: node that we are working with at the moment
        :return: height of the tree
        """
        current_node = current_node if current_node else self.root
        ltree_height = self.get_height(current_node.left)
        rtree_height = self.get_height(current_node.right)
        return max(ltree_height, rtree_height) + 1


class AlreadyInTree(Exception):
    """
    Raised when trying to add an element that is already in the tree
    """
