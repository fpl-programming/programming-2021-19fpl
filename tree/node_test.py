"""
Tests for the Node class.
"""

import unittest

from tree.node import Node


class NodeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Node
    """

    def test_new_node(self):
        """
        Test if a new node is created correctly
        """
        for value in [0, 5, 10, 5]:
            node = Node(value)
            self.assertEqual(node.value, value)

    def test_new_node_incorrect_input(self):
        """
        Test that creating a node with incorrect value raises ValueError
        """
        for value in [0.1, (), 'abc']:
            self.assertRaises(ValueError, Node, value)

    def test_node_insertion(self):
        """
        Test that children are created correctly
        """
        node = Node(0)
        node_left = Node(-1)
        node_right = Node(1)

        node.insert_left(node_left)
        node.insert_right(node_right)

        self.assertEqual(node.left.value, -1)
        self.assertEqual(node.right.value, 1)

    def test_insert_node_incorrect(self):
        """
        Test that creating children with incorrect values raises ValueError
        """
        node = Node(0)
        node_left = Node(-1)
        node_right = Node(1)

        self.assertRaises(ValueError, node.insert_left, node_right)
        self.assertRaises(ValueError, node.insert_right, node_left)
