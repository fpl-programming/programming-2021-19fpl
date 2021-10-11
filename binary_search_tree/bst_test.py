"""
Programming for linguists

Tests for BinarySearchTree class.
"""

import unittest
import random

from binary_search_tree.binary_search_tree import BinarySearchTree, AlreadyInTree, CannotRemoveRoot


class BSTreeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of BinarySearchTree
    """

    def test_create_tree_add_nodes(self):
        """
        Test that when tree is created and nodes are added all fields are filled correctly
        """
        bs_tree = BinarySearchTree(10)
        self.assertEqual(bs_tree.root.value, 10)

        bs_tree.add(8)
        self.assertEqual(bs_tree.root.left.value, 8)
        self.assertEqual(bs_tree.root.left.parent.value, 10)

        bs_tree.add(7)
        self.assertEqual(bs_tree.root.left.left.value, 7)

        bs_tree.add(9)
        self.assertEqual(bs_tree.root.left.right.value, 9)
        self.assertEqual(bs_tree.root.left.right.parent.value, 8)

        bs_tree.add(12)
        self.assertEqual(bs_tree.root.right.value, 12)

        bs_tree.add(11)
        self.assertEqual(bs_tree.root.right.left.value, 11)

        bs_tree.add(13)
        self.assertEqual(bs_tree.root.right.right.value, 13)

    def test_create_tree_with_bool_root(self):
        """
        Test that when tree is created with root whose type is bool it iis converted to 0 or 1
        """
        bs_tree = BinarySearchTree(True)
        self.assertEqual(bs_tree.root.value, 1)
        bs_tree = BinarySearchTree(False)
        self.assertEqual(bs_tree.root.value, 0)

    def test_add_existing_element(self):
        """
        Test that function raises custom exception when trying to add existing element to tree
        """
        bs_tree = BinarySearchTree(10)
        bs_tree.add(8)
        with self.assertRaises(AlreadyInTree):
            bs_tree.add(8)

    def test_add_random_elements(self):
        """
        Test that all random elements are added correctly
        """
        bs_tree = BinarySearchTree(5)
        elements = random.sample([1, 2, 3, 4, 6, 7, 8, 9], 4)
        for element in elements:
            bs_tree.add(element)
            self.assertTrue(bs_tree.find(element))

    def test_remove_element(self):
        """
        Test that element is removed correctly
        """
        bs_tree = BinarySearchTree(10)
        bs_tree.add(8)
        bs_tree.add(7)
        bs_tree.add(9)
        bs_tree.remove(8)
        self.assertEqual(bs_tree.root.left.value, 9)
        self.assertEqual(bs_tree.root.left.parent.value, 10)
        self.assertEqual(bs_tree.root.left.left.value, 7)
        self.assertEqual(bs_tree.root.left.left.parent.value, 9)
        self.assertEqual(bs_tree.root.left.right, None)

    def test_remove_root(self):
        """
        Test that function raises custom exception when trying to remove tree root
        """
        bs_tree = BinarySearchTree(10)
        bs_tree.add(12)
        bs_tree.add(11)
        bs_tree.add(13)
        with self.assertRaises(CannotRemoveRoot):
            bs_tree.remove(10)

    def test_remove_random_elements(self):
        """
        Test that all random elements are removed correctly
        """
        bs_tree = BinarySearchTree(10)
        elements = random.sample(range(1, 20, 2), 6)
        for element in elements:
            bs_tree.add(element)
        for element in elements:
            if bs_tree.find(element):
                bs_tree.remove(element)
                self.assertFalse(bs_tree.find(element))

    def test_remove_non_existent_element(self):
        """
        Test that function raises ValueError when trying to remove non existent element from tree
        """
        bs_tree = BinarySearchTree(10)
        bs_tree.add(8)
        bs_tree.add(12)
        with self.assertRaises(ValueError):
            bs_tree.remove(13)

    def test_find_element(self):
        """
        Test that find method returns True when element is in tree
        """
        bs_tree = BinarySearchTree(10)
        bs_tree.add(12)
        bs_tree.add(11)
        bs_tree.add(13)
        self.assertTrue(bs_tree.find(13))

    def test_find_non_existent_element(self):
        """
        Test that find method returns False when element is not in tree
        """
        bs_tree = BinarySearchTree(10)
        bs_tree.add(8)
        bs_tree.add(7)
        self.assertFalse(bs_tree.find(9))

    def test_get_tree_height(self):
        """
        Test that tree height is calculated correctly
        """
        bs_tree = BinarySearchTree(10)
        bs_tree.add(8)
        bs_tree.add(9)
        bs_tree.add(7)
        bs_tree.add(6)
        bs_tree.add(12)
        self.assertEqual(bs_tree.get_height(), 3)

    def test_get_tree_height_with_root_only(self):
        """
        Test that height of tree with root only equals 0
        """
        bs_tree = BinarySearchTree(10)
        self.assertEqual(bs_tree.get_height(), 0)
