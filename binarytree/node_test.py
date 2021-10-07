"""
Test for Node class
"""

import unittest

from binarytree.node import Node
# from node import Node


class NodeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the Node implementation
    """

    def test_node_add_left_descendant(self):
        """
            (positive testing of add_left function)
        Create a Node.
        Add left descendant from a list of correct values.
        Test that the input value is equal to the left descendant of the Node
        """
        smaller_than_five = [0, Node(1), 2, Node(3), 4]
        for val in smaller_than_five:
            node = Node(5)
            node.add_left(val)
            self.assertEqual(val, node.left)

    def test_call_add_wrong_left_descendants_raised_error(self):
        """
            (negative testing of add_left function)
        Create a Node.
        Add left descendant from lists of incorrect values.
        Test that call of add_left function with incorrect inputs raises errors
        """
        greater_than_five = [Node(5), 6, Node(7), 1000, Node(100000000000)]
        for val in greater_than_five:
            node = Node(5)
            self.assertRaises(ValueError, node.add_left, val)
        non_integers = [2.4, 'three', None, {}, []]
        for val in non_integers:
            node = Node(5)
            self.assertRaises(TypeError, node.add_left, val)

    def test_node_add_multiple_left_descendants(self):
        """
            (end-to-end testing of add_left function)
        Create a Node with three left descendants.
        Test that the values are added correctly to the Node.
        """
        node = Node(10000000)
        node.add_left(Node(3))
        node.left.add_left(Node(2))
        node.left.left.add_left(Node(1))
        self.assertEqual(10000000, node.value)
        self.assertEqual(3, node.left.value)
        self.assertEqual(2, node.left.left.value)
        self.assertEqual(1, node.left.left.left.value)

    def test_node_add_right_descendant(self):
        """
            (positive testing of add_right function)
        Create a Node.
        Add right descendant from a list of correct values.
        Test that the input value is equal to the right descendant of the Node
        """
        greater_than_five = [6, Node(7), Node(8), 9, Node(10000000)]
        for val in greater_than_five:
            node = Node(5)
            node.add_right(val)
            self.assertEqual(val, node.right)

    def test_call_add_wrong_right_descendants_raised_error(self):
        """
            (negative testing of add_right function)
        Create a Node.
        Add right descendant from lists of incorrect values.
        Test that call of add_right function with incorrect inputs raises errors
        """
        smaller_than_five = [5, Node(4), 3, 2, Node(1), Node(0)]
        for val in smaller_than_five:
            node = Node(5)
            self.assertRaises(ValueError, node.add_right, val)
        non_integers = [10.44465, 'twelve', None, {}, []]
        for val in non_integers:
            node = Node(5)
            self.assertRaises(TypeError, node.add_right, val)

    def test_node_add_multiple_right_descendants(self):
        """
            (end-to-end testing of add_right function)
        Create a Node with three right descendants.
        Test that the values are added correctly to the Node.
        """
        node = Node(0)
        node.add_right(Node(1))
        node.right.add_right(Node(2))
        node.right.right.add_right(Node(3))
        self.assertEqual(0, node.value)
        self.assertEqual(1, node.right.value)
        self.assertEqual(2, node.right.right.value)
        self.assertEqual(3, node.right.right.right.value)
