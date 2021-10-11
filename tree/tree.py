"""

Implementation of the data structure "Binary Tree"
"""


class Node:
    """
    Root Data Structure
    """

    def __init__(self, root: int):
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
        """
        # recursion
        if root is None:
            root = node
        else:
            if node < root.root:
                root.left = self.add(root.left, node)
            elif node > root.root:
                root.right = self.add(root.right, node)
            else:
                raise ValueError('not able to put the node in Binary Tree')

        # no recursion
        """tem_root = self.root
        while tem_root.right and tem_root.left:
            if node < tem_root.root:
                tem_root = tem_root.left
            elif node > tem_root.root:
                tem_root = tem_root.right
            else:
                raise ValueError ('not able to put the node in Binary Tree')

        if node < tem_root.root:
            tem_root.left = node
        elif node > tem_root.root:
            tem_root.right = tem_root.right
        else:
            raise ValueError('not able to put the node in Binary Tree')"""

    def remove(self, root: Node, node: Node):
        """
        Delete the node from Binary Tree
        """
        if root == node:
            root = None
        else:
            if node < root.root:
                root.left = self.add(root.left, node)
            elif node > root.root:
                root.right = self.add(root.right, node)

    def find(self, node: Node):
        """
        Finds a node in Binary Tree
        """
        if self.root > node:
            if self.left:
                return self.left.find(node)
        if self.right:
            return self.right.find(node)

    def get_height(self, root: Node, counter=1):
        """
        Gets height of Binary Tree
        """
        if self.left and self.right:
            return 1 + max(self.left.get_height(), self.right.get_height())
        if self.left:
            return 1 + self.left.get_height()
        if self.right:
            return 1 + self.right.get_height()

        """if root is None:
            return max(left_h, right_h)
        else:
            if root.left and root.right:
                counter += 1
                left_h = self.get_height(root.left, counter)
                right_h = self.get_height(root.right, counter)
            elif root.left:
                counter += 1
                left_h = self.get_height(root.left, counter)
            elif root.right:
                counter += 1
                right_h = self.get_height(root.right, counter)"""
