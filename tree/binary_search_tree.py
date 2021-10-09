"""

Implementation of the data structure "Binary Search Tree"
"""

from tree.node import Node


class Tree:
    """
    Binary Search Tree Data Structure
    """

    def __init__(self, root: Node):
        if not isinstance(root, Node):
            raise TypeError
        self.root = root

    def add(self, value: int, node: Node = None):
        """
        Add the value to the appropriate node in a tree
        :param value: value of the new node
        :param node: current node in a given recursive iteration
        """
        if not node:
            node = self.root
        if node.value > value:
            if node.left:
                self.add(value, node.left)
            else:
                node.insert_left(Node(value))
        elif node.value < value:
            if node.right:
                self.add(value, node.right)
            else:
                node.insert_right(Node(value))
        else:
            raise ValueError

    def find(self, value: int, node: Node = None):
        """
        Find if a value is present in a tree using binary search algorithm
        :param value: sought value
        :param node: current node in a given recursive iteration
        :return: True if value is present, False otherwise
        """
        if not isinstance(value, int) and isinstance(node, Node):
            raise TypeError
        if not node:
            node = self.root
        if node.value == value:
            return True
        if not (node.right or node.left):
            return False
        if value > node.value and node.right:
            return bool(self.find(value, node.right))
        if value < node.value and node.left:
            return bool(self.find(value, node.left))

    def remove(self, value: int, node: Node = None):
        """
        Delete a node with a given value, as well as all its children
        :param value: value to remove
        :param node: current node in a given recursive iteration
        """
        if self.root.value == value:
            raise ValueError
        if not node:
            node = self.root
        if value < node.value and node.left:
            if node.left.value == value:
                node.left = None
            else:
                self.remove(value, node.left)
        if value > node.value and node.right:
            if node.right.value == value:
                node.right = None
            else:
                self.remove(value, node.right)

    def get_height(self, node: Node = None, current_max: int = 0):
        """
        Find how many levels there are in the tree
        :return: number of levels in the tree
        """
        if not node:
            node = self.root
        if node.left:
            left_max = self.get_height(node.left, current_max + 1)
        else:
            left_max = current_max
        if node.right:
            right_max = self.get_height(node.right, current_max + 1)
        else:
            right_max = current_max
        current_max = max(left_max, right_max)
        return current_max

    def depth_first_search(self, value: int, node: Node = None):
        """
        Find if a value is present in a tree using dfs algorithm
        :param value: sought value
        :param node: current node in a given recursive iteration
        :return: True if value is present, False otherwise
        """
        if not isinstance(value, int):
            raise TypeError
        if not node:
            node = self.root
        if node.value == value:
            return True
        if node.left:
            if self.depth_first_search(value, node.left):
                return True
        if node.right:
            if self.depth_first_search(value, node.right):
                return True
        return False
