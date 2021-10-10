"""
Tests for BinarySearchTree class.
"""


import unittest

from binarytree.binarytree import BinarySearchTree, Node


class BinarySearchTreeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Queue
    """

    def test_add_root(self):
        """
        Create an empty BinarySearchTree and add an element.
        Test that the element becomes root
        """
        tree = BinarySearchTree()
        tree.add(9)
        self.assertEqual(tree.get_root(), 9)
        self.assertEqual(tree.find(9).left_node, None)
        self.assertEqual(tree.find(9).right_node, None)

    def test_find_existing_node(self):
        """
        Find existing node in Tree
        Test that method returns node
        """
        tree = BinarySearchTree(1)
        tree.add(5)
        self.assertEqual(tree.find(5).root, Node(5).root)
        self.assertEqual(isinstance(tree.find(5), Node), isinstance(Node(5), Node))
