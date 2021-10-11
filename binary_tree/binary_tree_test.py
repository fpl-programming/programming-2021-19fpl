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
        Create a BinarySearchTree.
        Tests that the tree can insert new values.
        """
        tree = BinarySearchTree()
        for elem in (6, 1, 0, 8, 2, 7, 15):
            self.assertTrue(tree.add(elem))

    def test_add_exists_node(self):
        """
        Create a BinarySearchTree.
        Tests that the tree doesn't insert values that already exists in the tree.
        """
        tree = BinarySearchTree()
        for elem in (6, 1, 0, 8, 2, 7, 15):
            self.assertTrue(tree.add(elem))
        for elem in (6, 1, 0, 8, 2, 7, 15):
            self.assertFalse(tree.add(elem))

    def test_add_non_integer(self):
        """
        Create a BinarySearchTree.
        Tests that the tree can't insert non-integer values.
        """
        tree = BinarySearchTree()
        for element in ([], (), None, {}, '', 3.5):
            self.assertRaises(ValueError, tree.add, element)

    def test_find_node(self):
        """
        Create a BinarySearchTree.
        Tests that the tree can find inserted value.
        """
        tree = BinarySearchTree()
        tree.add(6)
        tree.add(1)
        self.assertTrue(tree.find(1))

    def test_find_not_exists_node(self):
        """
        Create a BinarySearchTree.
        Tests that the tree can't find value that is not inserted.
        """
        tree = BinarySearchTree()
        tree.add(6)
        tree.add(1)
        self.assertFalse(tree.find(9))

    def test_find_non_integer(self):
        """
        Create a BinarySearchTree.
        Tests that the tree can't find non-integer values.
        """
        tree = BinarySearchTree()
        for element in ([], (), None, {}, '', 3.5):
            self.assertRaises(ValueError, tree.find, element)

    def test_get_height_empty_tree(self):
        """
        Create a BinarySearchTree
        Tests that height of empty tree equals 0.
        """
        tree = BinarySearchTree()
        self.assertEqual(tree.get_height(), 0)

    def test_remove_root(self):
        """
        Create a BinarySearchTree and remove the root element.
        Tests that there is no root.
        """
        binary_tree = BinarySearchTree()
        binary_tree.add(3)
        binary_tree.remove(3)
        self.assertEqual(binary_tree.root, None)

    def test_remove_third_element(self):
        """
        Create a BinarySearchTree and remove the element at the last level.
        Tests that the element is None.
        """
        binary_tree = BinarySearchTree()
        binary_tree.add(5)
        binary_tree.add(3)
        binary_tree.add(1)
        binary_tree.remove(1)
        self.assertEqual(binary_tree.root.left.value, 3)
        self.assertEqual(binary_tree.root.left.left, None)

    def test_remove_not_existing(self):
        """
        Create a BinarySearchTree and try to remove non-existing element.
        Test that it returns a message.
        """
        tree = BinarySearchTree()
        self.assertRaises(ValueError, tree.remove, 3)

    def end_to_end_test(self):
        """
        Creates a binary tree and fill tree with values.
        Try to fill value that already exists and get height of the tree.
        Find 1, remove 1 and try to find removed 1.
        Remove nodes one by one.
        Tests that tree equals empty tree.
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
