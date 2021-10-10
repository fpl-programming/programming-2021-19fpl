"""
Tests for the Binary search tree class.
"""

import unittest

from binary_tree import BinarySearchTree, Node


class BinaryTreeTestCase(unittest.TestCase):
    """
        This Case of tests checks the functionality of the implementation of Binarysearchtree
    """

    def test_create_node(self):
        """
        Creates a node.
        Tests that the correct val is returned.
        """
        node = Node(7)
        self.assertEqual(node.value, 7)

    def test_add_node(self):
        """
        Creates a binary tree.
        Tests that the tree can insert new values.
        """
        tree = BinarySearchTree()
        for elem in (6, 1, 0, 8, 2, 7, 15):
            self.assertTrue(tree.add(elem))

    def test_add_exists_node(self):
        """
        Creates a binary tree.
        Tests that the tree doesn't insert values that already exists in the tree.
        """
        tree = BinarySearchTree()
        for elem in (6, 1, 0, 8, 2, 7, 15):
            self.assertTrue(tree.add(elem))
        for elem in (6, 1, 0, 8, 2, 7, 15):
            self.assertFalse(tree.add(elem))

    def test_add_non_integer(self):
        """
        Creates a binary tree.
        Tests that the tree can't insert non-integer values.
        """
        tree = BinarySearchTree()
        for element in ([], (), None, {}, '', 3.5):
            self.assertRaises(ValueError, tree.add, element)

    def test_find_node(self):
        """
        Creates a binary tree.
        Tests that the tree can find inserted value.
        """
        tree = BinarySearchTree()
        tree.add(6)
        tree.add(1)
        self.assertTrue(tree.find(1))

    def test_find_not_exists_node(self):
        """
        Creates a binary tree.
        Tests that the tree can't find value that is not inserted.
        """
        tree = BinarySearchTree()
        tree.add(6)
        tree.add(1)
        self.assertFalse(tree.find(9))

    def test_find_non_integer(self):
        """
        Creates a binary tree.
        Tests that the tree can't find non-integer values.
        """
        tree = BinarySearchTree()
        for element in ([], (), None, {}, '', 3.5):
            self.assertRaises(ValueError, tree.find, element)

    def test_get_height_empty_tree(self):
        """
        Creates a binary tree.
        Tests that height of empty tree equals 0.
        """
        tree = BinarySearchTree()
        self.assertEqual(tree.get_height(), 0)

    def end_to_end_test(self):
        """
        Creates a binary tree.
        Fill tree with values.
        Try to fill value that already exists.
        Get height of the tree.
        Find 7. Remove 7. Try to find removed 7.
        Remove nodes one by one. Check that tree equals empty tree.
        """
        tree = BinarySearchTree()
        for elem in (6, 1, 0, 8, 2, 7, 15):
            self.assertTrue(tree.add(elem))
        self.assertFalse(tree.add(elem))

        self.assertEqual(tree.get_height(), 3)

        self.assertTrue(tree.find(1))
        self.assertTrue(tree.remove(1))
        self.assertFalse(tree.find(1))

        for elem in (6, 1, 0, 8, 2, 7, 15):
            self.assertTrue(tree.remove(elem))
        self.assertEqual(tree, BinarySearchTree())
