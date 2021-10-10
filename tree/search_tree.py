"""
Programming for linguists

Implementation of the data structure "Binary Search Tree"
"""
from tree.custom_exceptions import Existed, NotExisted


class Node:
    """
    Implementation of a recursive tree structure.
    """
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        """
        Add the element ‘data' in the tree
        :param data: element to add in a tree
        """
        if data > self.data:
            if self.right is None:
                self.right = Node(data)
                return
            self.right.insert(data)
        elif data < self.data:
            if self.left is None:
                self.left = Node(data)
                return
            self.left.insert(data)
        raise Existed(data)

    def find(self, data):
        """
        Find the element ‘data' in the tree
        :param data: element to find in a tree
        """
        if self.data == data:
            return f'data {data} is found', self
        if data > self.data and self.right is not None:
            return self.right.find(data)
        if data < self.data and self.left is not None:
            return self.left.find(data)
        raise NotExisted(data)

    def find_height(self, node):
        """
        Find the hight from node
        :param node: node from which to find the height
        """
        if node is None:
            return 0
        left_height = self.find_height(node.left)
        right_height = self.find_height(node.right)
        return max(left_height, right_height) + 1

    @staticmethod
    def find_min_deep(node):
        """
        Find the deepest element in a subtree node
        :param node: subtree in which to search
        """
        current_node = node
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def delete_node(self, node, data):
        """
        Delete the node with data
        :param node: node from which to start deleting
        :param data: data of the node to be deleted
        """
        # 0 - node is a leaf
        if node is None:
            return node

        # recursively go to the left side
        if data < node.data:
            node.left = self.delete_node(node.left, data)
        # recursively got to the right side
        if data > node.data:
            node.right = self.delete_node(node.right, data)

        # the node to be deleted is found
        if data == node.data:
            # node with one child - just take the value of this child
            if node.left is None:
                temp = node.right
                return temp
            if node.right is None:
                temp = node.left
                return temp
            # two children - find the smallest in the right subtree
            temp = self.find_min_deep(node.right)
            node.data = temp.data
            # delete the successor
            node.right = self.delete_node(node.right, temp.data)

        return node

    def in_width(self):
        """
        Go in a tree in width
        """
        whole_tree, current_level = [self], [self]

        def make_step(level):
            level = [node.left for node in level] + [node.right for node in level]
            level = [node for node in level if node is not None]
            return level

        while current_level:
            current_level = make_step(current_level)
            whole_tree.extend(current_level)
        return [node.data for node in whole_tree]

    def __str__(self):
        return f'Node with data {self.data}'
