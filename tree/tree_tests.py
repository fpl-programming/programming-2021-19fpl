"""

Tests for BinarySearchTree class
"""


import unittest

from tree.tree import BinarySearchTree


class BinarySearchTreeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of BinarySearchTree
    """

    def test_tree_creation(self):
        """
        Test if a new tree is created correctly
        """
        tree = BinarySearchTree(0)
        self.assertEqual(tree.root, 0)

    def test_binary_search_tree_add_root(self):
        """
        Create an empty BinarySearchTree and add an element.
        Test that the element becomes root
        """
        tree = BinarySearchTree()
        tree.add(5)
        self.assertEqual(tree.get_root(), 5)
        self.assertEqual(tree.find(5).left_node, None)
        self.assertEqual(tree.find(5).right_node, None)

    def test_add_more(self):
        """
        Create a BinarySearchTree with root and add elements
        Test that all elements added
        """
        tree = BinarySearchTree(root=5)
        for element in [1, 6, 2, 8]:
            tree.add(element)
            self.assertEqual(tree.find(element).root, element)

    def test_find(self):
        """
        Create a BinarySearchTree.
        Test that exiting values are found
        """
        tree = BinarySearchTree(0)
        tree.add(3)
        tree.add(1)
        for exiting in [0, 1, 3]:
            self.assertTrue(tree.find(exiting))
        for non_exiting in [4, 5, 6]:
            self.assertFalse(tree.find(non_exiting))
