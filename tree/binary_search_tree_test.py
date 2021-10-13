"""
Tests for the Tree class.
"""

import unittest

from tree.binary_search_tree import BinarySearchTree
from tree.node import Node


class TreeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Tree
    """

    def test_tree_creation(self):
        """
        Test if a new tree is created correctly
        """
        root = Node(0)
        tree = BinarySearchTree(root)
        self.assertEqual(tree.root.value, 0)

    def test_tree_creation_incorrect_input(self):
        """
        Test that creation of a tree with incorrect input raises TypeError
        """
        for root in [0, True, '']:
            self.assertRaises(TypeError, BinarySearchTree, root)

    def test_add(self):
        """
        Test that nodes are added to the tree correctly
        """
        root = Node(0)
        right_child = Node(2)
        root.insert_right(right_child)
        new_node_value = 1

        tree = BinarySearchTree(root)
        tree.add(new_node_value)
        self.assertEqual(tree.root.right.left.value, 1)

    def test_add_existing_element(self):
        """
        Test that adding an existing value raises ValueError
        """
        root = Node(0)
        tree = BinarySearchTree(root)
        self.assertRaises(ValueError, tree.add, 0)

    def test_find(self):
        """
        Test that existing values are found, non-existing are not found
        """
        root = Node(0)
        tree = BinarySearchTree(root)
        tree.add(2)
        tree.add(1)
        for existing in [0, 1, 2]:
            self.assertTrue(tree.find(existing))
        for non_existing in [3, 4, 5]:
            self.assertFalse(tree.find(non_existing))

    def test_find_incorrect_input(self):
        """
        Test that searching for incorrect value raises TypeError
        """
        tree = BinarySearchTree(Node(0))
        for incorrect in [1.0, (), '']:
            self.assertRaises(TypeError, tree.find(incorrect))

    def test_remove(self):
        """
        Test that nodes are removed correctly
        """
        tree = BinarySearchTree(Node(0))
        for value in [2, 1, 3, 4, -2, -3, -1]:
            tree.add(value)
        tree.remove(2)
        for removed in [1, 2, 3, 4]:
            self.assertFalse(tree.find(removed))
        for left in [0, -2, -3, -1]:
            self.assertTrue(tree.find(left))

    def test_remove_root_raises_error(self):
        """
        Test that removal of root raises ValueError
        """
        tree = BinarySearchTree(Node(0))
        for value in [2, 1, 3, 4, -2, -3, -1]:
            tree.add(value)
        self.assertRaises(ValueError, tree.remove, 0)

    def test_get_height(self):
        """
        Test that height of a tree is calculated correcrly
        """
        tree = BinarySearchTree(Node(0))
        for value in [2, 1, 3, 4, -2, -3, -1]:
            tree.add(value)
        self.assertEqual(3, tree.get_height())

    def test_dfs(self):
        """
        Test that existing values are found, non-existing are not found
        """
        tree = BinarySearchTree(Node(0))
        values = [2, 1, 3, 4, -2, -3, -1]
        for value in values:
            tree.add(value)
        self.assertEqual([0, -2, -3, -1, 2, 1, 3, 4], tree.depth_first_search())

    def test_binary_tree_total(self):
        """
        Test that all methods work correctly altogether as a pipeline
        """
        root = Node(0)
        self.assertEqual(0, root.value)
        self.assertEqual(None, root.left)
        self.assertEqual(None, root.right)

        tree = BinarySearchTree(root)
        self.assertEqual(tree.get_height(), 0)
        self.assertFalse(tree.find(2))

        tree.add(2)
        self.assertTrue(tree.find(2))
        self.assertEqual(tree.get_height(), 1)
        self.assertEqual(tree.root.right.value, 2)
        self.assertEqual(tree.root.left, None)
        self.assertEqual([0, 2], tree.depth_first_search())

        tree.remove(2)
        self.assertEqual(tree.get_height(), 0)
        self.assertFalse(tree.find(2))
        self.assertEqual([0], tree.depth_first_search())
