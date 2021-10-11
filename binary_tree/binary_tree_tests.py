"""
Tests for BinaryTree
"""

import unittest

from binary_tree.main import BinaryTree, Node


class BinaryTreeTestCase(unittest.TestCase):
    """
    Tests for BinaryTree
    """

    def test_create_node(self):
        """
        Creates a node.
        Tests that correct root, left and right are returned.
        """
        node = Node(5)
        self.assertEqual(node.node, 5)
        self.assertEqual(node.right, None)
        self.assertEqual(node.left, None)

    def test_binary_search_tree_add_node(self):
        """
        Tests that node is added.
        """
        tree = BinaryTree()
        tree.add_node(8)
        self.assertEqual(tree.search_node(8).left, None)
        self.assertEqual(tree.search_node(8).right, None)
