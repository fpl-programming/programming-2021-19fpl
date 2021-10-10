"""
Tests for BinarySearchTree class.
"""


import unittest

from binarytree.binarytree import BinarySearchTree, Node


class BinarySearchTreeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Queue
    """

    def test_add_root(self):   # add
        """
        Create an empty BinarySearchTree and add an element.
        Test that the element becomes root
        """
        tree = BinarySearchTree()
        tree.add(9)
        self.assertEqual(tree.get_root(), 9)
        self.assertEqual(tree.find(9).left_node, None)
        self.assertEqual(tree.find(9).right_node, None)

    def test_remove_node(self):   # remove
        """
        Remove node from Tree
        Test that Tree has no such node
        """
        tree = BinarySearchTree(3)
        tree.add(5)
        tree.remove(5)
        self.assertFalse(tree.find(5))

    def test_find_existing_node(self):  # find
        """
        Find existing node in Tree
        Test that method returns node
        """
        tree = BinarySearchTree(1)
        tree.add(5)
        self.assertEqual(tree.find(5).root, Node(5).root)
        self.assertEqual(isinstance(tree.find(5), Node), isinstance(Node(5), Node))

    def test_get_root_initial(self):  # get_root
        """
        Create a BinarySearchTree with root.
        Test that root returns correctly.
        """
        tree = BinarySearchTree(root=8)
        self.assertEqual(tree.get_root(), 8)

    def test_get_height(self):  # get_height
        """
        Test that get_height function returns the max height of the tree.
        """
        tree = BinarySearchTree()
        nodes = [70, 31, 93, 94, 14, 23, 73]
        for element in nodes:
            tree.add(element)
        self.assertEqual(tree.get_height(), 4)
