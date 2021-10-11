"""

Implementation of the data structure "Binary Tree"
"""


class Node:
    """
    Root Data Structure
    """

    def __init__(self, root: int):  # pylint: disable=too-few-public-methods
        self.root = root
        self.left = None
        self.right = None


class BinaryTree:
    """
    Binary Tree Data Structure
    """

    def __init__(self, root: Node):  # always not empty BT
        self.root = root

    def add(self, root: Node, node: Node):
        """
        Add the node ‘node’ to Binary Tree
        :param node: node to add to Binary Tree
        @type node: Node
        @type root: Node
        """
        if root is None:
            self.root.root = node
        else:
            if node.root < root.root:
                root.left = self.add(root.left, node)
            elif node.root > root.root:
                root.right = self.add(root.right, node)
            else:
                raise ValueError('not able to put the node in Binary Tree')

        return True

    def remove(self, root: Node, node: Node):
        """
        Delete the node from Binary Tree
        """
        if root == node:
            self.root.root = None
        else:
            if node.root < root.root:
                root.left = self.add(root.left, node)
            elif node.root > root.root:
                root.right = self.add(root.right, node)

        return True

    def find(self, node: Node):
        """
        Finds a node in Binary Tree
        """
        if self.root.root > node.root:
            if self.root.left:
                return self.root.left.find(node)
        if self.root.right:
            return self.root.right.find(node)

        return True

    def get_height(self):
        """
        Gets height of Binary Tree
        """
        if self.root.left and self.root.right:
            return 1 + max(self.root.left.get_height(), self.root.right.get_height())
        if self.root.left:
            return 1 + self.root.left.get_height()
        if self.root.right:
            return 1 + self.root.right.get_height()

        return True
