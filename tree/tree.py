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

    def __init__(self, root: Node):
        self.root = root

    def add(self, node: Node):
        """
        Add the node ‘node’ to Binary Tree
        :param node: node to add to Binary Tree
        """
        tem_root = self.root
        while tem_root.right and tem_root.left:
            if node < tem_root.root:
                tem_root = tem_root.left

            elif node > tem_root.root:
                tem_root = tem_root.right


        if node < self.root:        # 10
            self.root.left = node   # 2

        elif node > self.root:
            self.root.right = node  # 11

    def remove(self):
        """
        Delete the node from Binary Tree
        """
        pass

    def find(self):
        """
        Finds a node in Binary Tree
        """
        pass

    def get_height(self):
        """
        Gets height of Binary Tree
        """
        pass
