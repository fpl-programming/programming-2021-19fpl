"""
Implementation of the data structure "Binary Search Tree"
"""
from typing import Optional, Union
from dataclasses import dataclass


@dataclass
class SuccessfulStatus:
    message: str

    @staticmethod
    def code():
        return True


@dataclass
class FailureStatus:
    message: str

    @staticmethod
    def code():
        return False


class Node:
    """
    Node Implementation
    """

    # TODO: implement better status monitoring (not True/False)

    def __init__(self, root, left_node=None, right_node=None):
        self.root: Union[int, float] = root
        self.left_node: Optional[Node] = left_node
        self.right_node: Optional[Node] = right_node

    def add(self, element: Union[int, float]):
        """
        Add element as a child of the node
        """
        if self.root == element:
            return FailureStatus.code()

        if self.root > element:
            if self.left_node:
                return self.left_node.add(element)

            self.left_node = Node(element)
            return SuccessfulStatus.code()

        if self.right_node:
            return self.right_node.add(element)

        self.right_node = Node(element)
        return SuccessfulStatus.code()

    def find(self, element: Union[int, float]):
        """
        Find element in the node
        """
        if self.root == element:
            return SuccessfulStatus.code()

        if self.root > element:
            if self.left_node:
                return self.left_node.find(element)

        if self.right_node:
            return self.right_node.find(element)

        return FailureStatus.code()

    def height(self):
        """
        Get height of the node.
        """
        if self.left_node and self.right_node:
            return 1 + max(self.left_node.height(), self.right_node.height())

        if self.left_node:
            return 1 + self.left_node.height()

        if self.right_node:
            return 1 + self.right_node.height()

        return 1

    def __bool__(self):
        """
        Return whether Tree is empty or not
        """

        return self.root is not None


class BinarySearchTree:
    """
    Binary Search Tree implementation
    """

    def __init__(self, root: Optional[Node] = None):
        self.root = root

    def add(self, element: Union[int, float]):
        """
        Check whether elements are numeric, tree is empty and add element to it
        """
        if not isinstance(element, (int, float)):
            raise ValueError

        if not self.empty():
            return self.root.add(element)

        self.root = Node(element)
        return SuccessfulStatus.code()

    def find(self, element: Union[int, float]):
        """
        Return an element if it is in the Tree
        """
        if not isinstance(element, (int, float)):
            raise ValueError

        if not self.empty():
            return self.root.find(element)

        return FailureStatus.code()

    def remove(self, element: Union[int, float]):
        """
        Remove the required node from the tree
        """
        if not self.find(element):
            raise ValueError

        if element == self.root.root:
            self.root = Node(None)
            return

        self._remove_child(self.root, element)

    def df_search(self):
        """
        Conduct Depth-first search in the given Binary Search Tree
        """
        self._dfs(self.root)

    def empty(self):
        """
        Return whether Tree is empty or not
        """
        return not bool(self.root)

    def height(self):
        """
        Get height of the tree.
        """
        if not self.root:
            return 0

        return self.root.height()

    def _remove_child(self, node: Node, element: Union[int, float]):
        """
        Auxiliary recursive function to find the right node for removal
        """
        if node.left_node and node.left_node.root == element:
            node.left_node = None
            return SuccessfulStatus.code()

        if node.right_node and node.right_node.root == element:
            node.right_node = None
            return SuccessfulStatus.code()

        if element < node.root:
            self._remove_child(node.left_node, element)

        elif element > node.root:
            self._remove_child(node.right_node, element)

        return FailureStatus.code()

    def _dfs(self, node):
        """
        Visit all nodes recursively
        """
        if node:
            self._dfs(node.left_node)
            print(str(node.root), end=' ')
            self._dfs(node.right_node)
