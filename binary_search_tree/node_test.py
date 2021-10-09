"""
Programming for linguists

Tests for Node class.
"""

import unittest
from binary_search_tree.binary_search_tree import Node


class NodeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Node
    """
    def test_node_is_created(self):
        """
        Create a node with root only.
        Test that node is created.
        """
        node = Node(10)
        self.assertEqual(10, node.root)

    def test_node_is_created_with_children(self):
        """
        Create a node with children.
        Test that node is created.
        """
        node = Node(10, 8, 12)
        self.assertEqual(10, node.root)
        self.assertEqual(8, node.left)
        self.assertEqual(12, node.right)

    def test_node_creation_raises_error(self):
        """
        Create a node with incorrect root.
        Test that creation of node raises error.
        """
        self.assertRaises(TypeError, Node, None)
