# pylint: skip-file
"""
Tests for the Tree class.
"""

import unittest

from tree.search_tree import Node
from tree.custom_exceptions import Existed, NotExisted

class TreeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Binary Search Tree
    """

    def test_create_tree(self):
        """
        Create a Tree with one start node.
        Test that its value is zero.
        """
        tree = Node(0)
        self.assertEqual(tree.data, 0)

    def test_create_type(self):
        """
        Create a Tree with different types of data.
        Test that it is possible to make node with any type of data.
        """
        data_types = ["tree", [], 8, {}, (), 9.0]
        for data_type in data_types:
            tree = Node(data_type)
            self.assertEqual(tree.data, data_type)

    def test_insert_right(self):
        """
        Insert a number bigger than a root.
        Test that this number is right child.
        """
        tree = Node(12)
        tree.insert(16)
        self.assertEqual(tree.right.data, 16)

    def test_insert_left(self):
        """
        Insert a number smaller than a root.
        Test that this number is left child.
        """
        tree = Node(12)
        tree.insert(10)
        self.assertEqual(tree.left.data, 10)

    def test_insert_existed(self):
        """
        Insert a number that is already in a tree.
        Test that it is obedient.
        """
        tree = Node(12)
        self.assertRaises(Existed, tree.insert, 12)

    def test_find_node_less(self):
        """
        Insert a number less than a root and find it.
        Test that the same node is found.
        """
        tree = Node(12)
        tree.insert(10)
        _, found_node = tree.find(10)
        self.assertEqual(tree.left, found_node)

    def test_find_node_more(self):
        """
        Insert a number less than a root and find it.
        Test that the same node is found.
        """
        tree = Node(12)
        tree.insert(18)
        _, found_node = tree.find(18)
        self.assertEqual(tree.right, found_node)

    def test_find_not_existed(self):
        """
        Find a node that is node in a tree.
        Test that it is obedient.
        """
        tree = Node(12)
        self.assertRaises(NotExisted, tree.find, 10)

    def test_height(self):
        """
        Create a tree.
        Test the height of a tree.
        """
        tree = Node(12)
        for element in [5, 16, 14, 19, 15, 20]:
            tree.insert(element)
        height = tree.find_height(tree)
        self.assertEqual(height, 4)

    def test_height_from_any_node(self):
        """
        Create a tree.
        Test the height of a tree.
        """
        tree = Node(12)
        for element in [5, 16, 14, 19, 15, 20]:
            tree.insert(element)
        height = tree.find_height(tree.right)
        self.assertEqual(3, height)

    def test_zero_height(self):
        """
        Create a tree and try to find a height from None node.
        Test that the height is zero.
        """
        tree = Node(12)
        height = tree.find_height(tree.right)
        self.assertEqual(0, height)

    def test_the_width_order(self):
        """
        Create a tree.
        Test the width order of a new tree.
        """
        tree = Node(12)
        for element in [5, 16, 14, 19, 15, 20, 6, 1]:
            tree.insert(element)
        tree_order = tree.in_width()
        self.assertEqual(tree_order, [12, 5, 16, 1, 14, 6, 19, 15, 20])

    def test_the_width_zero_level(self):
        """
        Create a tree.
        Test the width order of a zero level.
        """
        tree = Node(12)
        tree_order = tree.in_width()
        self.assertEqual(tree_order, [12])

    def test_the_width_elements(self):
        """
        Create a tree.
        Test the width order of a new tree.
        """
        tree = Node(12)
        elements = [5, 16, 14, 19, 15, 20, 6, 1]
        for element in elements:
            tree.insert(element)
        tree_order_length = len(tree.in_width())
        self.assertEqual(tree_order_length, len(elements) + 1)

    def test_delete_node_without_leaves(self):
        """
        Delete a node without leaves.
        Test that a new tree is None.
        """
        tree = Node(12)
        new_tree = tree.delete_node(tree, 12)
        self.assertEqual(None, new_tree)

    def test_delete_node_with_leaf(self):
        """
        Delete node with a leaf.
        Test that a node is changed with the lowest left node.
        """
        tree = Node(12)
        elements = [5, 16, 14, 19, 20]
        for element in elements:
            tree.insert(element)
        new_tree = tree.delete_node(tree, 16)
        new_tree_elements = new_tree.in_width()
        self.assertEqual([12, 5, 19, 14, 20], new_tree_elements)

    def test_delete_node_with_many_leaves(self):
        """
        Delete node with a few leaves.
        Test that a new node is changed with the lowest and the order is the same.
        """
        tree = Node(12)
        elements = [5, 16, 14, 19, 4, 8, 2, 6]
        for element in elements:
            tree.insert(element)
        new_tree = tree.delete_node(tree, 5)
        new_tree_elements = new_tree.in_width()
        self.assertEqual([12, 6, 16, 4, 14, 8, 19, 2], new_tree_elements)

