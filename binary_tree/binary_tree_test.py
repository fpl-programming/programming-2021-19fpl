"""
Programming for linguists
Tests for BinarySearchTree class.
"""

import unittest

from binary_tree.binary_tree import BinarySearchTree


class TestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of BinarySearchTree
    """

    def test_add_one_element(self):
        """
        Add element to BinarySearchTree.
        Test that max height is 1.
        Check that tree is not empty.
        """
        tree = BinarySearchTree()
        tree.add(1)
        self.assertFalse(tree.empty())
        self.assertEqual(tree.height(), 1)

    def test_add_multiple_element(self):
        """
        Add element to BinarySearchTree.
        Test that max height is 1.
        Check that tree is not empty.
        """
        tree = BinarySearchTree()
        tree.add(1)
        tree.add(2)
        tree.add(5)
        self.assertFalse(tree.empty())
        self.assertNotEqual(tree.height(), 10)

    def test_add_incorrect_input(self):
        """
        Add incorrect element to BinarySearchTree.
        Check that ValueError is raised.
        """
        tree = BinarySearchTree()
        for element in (None, (), [], {}):
            self.assertRaises(ValueError, tree.add, element)

    def test_new_tree_is_empty(self):
        """
        Create an empty BinarySearchTree.
        Test that its max height is 0.
        """
        tree = BinarySearchTree()
        self.assertTrue(tree.empty())
        self.assertEqual(tree.height(), 0)

    def test_height_seq(self):
        """
        Add elements to BinarySearchTree.
        Test that its max height is correct.
        """
        tree = BinarySearchTree()
        tree.add(1)
        tree.add(2)
        tree.add(3)
        tree.add(4)
        self.assertEqual(tree.height(), 4)

    def test_height_nonseq(self):
        """
        Add elements to BinarySearchTree.
        Test that its max height is correct.
        """
        tree = BinarySearchTree()
        tree.add(42)
        tree.add(3301)
        tree.add(100)
        tree.add(1)
        self.assertEqual(tree.height(), 3)

    def test_find_elements(self):
        """
        Add elements to BinarySearchTree.
        Test that elements an be found.
        """
        tree = BinarySearchTree()
        for element in (1, 10, 12, 5, 8):
            tree.add(element)
            self.assertTrue(tree.find(element))

    def test_find_absent_elements(self):
        """
        Add elements to BinarySearchTree.
        Test that elements an be found.
        """
        tree = BinarySearchTree()
        for element in (1, 10, 12, 5, 8):
            tree.add(element)
            self.assertFalse(tree.find(element + 3))

    def test_find_incorrect_input(self):
        """
        Try to find incorrect element in BinarySearchTree.
        Check that ValueError is raised.
        """
        tree = BinarySearchTree()
        for element in (None, (), [], {}):
            self.assertRaises(ValueError, tree.find, element)

    def test_remove_element(self):
        """
        Add elements to BinarySearchTree.
        Test that elements can be removed.
        Check that after removal they cannot be found.
        """
        tree = BinarySearchTree()
        tree.add(6)
        tree.add(5)
        tree.remove(5)
        self.assertFalse(tree.find(5))

    def test_remove_root(self):
        """
        Add an element to BinarySearchTree.
        Test that root can be easily removed.
        Check that tree becomes empty after root removal.
        """
        tree = BinarySearchTree()
        tree.add(5)
        tree.remove(5)
        self.assertFalse(tree.find(5))
        self.assertTrue(tree.empty())

    def test_remove_branch(self):
        """
        Add elements to BinarySearchTree.
        Test that after not-final node removal all later nodes in the brunch are also removed.
        """
        tree = BinarySearchTree()
        tree.add(1)
        tree.add(2)
        tree.add(3)
        tree.remove(2)
        self.assertFalse(tree.find(2))
        self.assertFalse(tree.find(3))

    def test_remove_incorrect_input(self):
        """
        Try to remove incorrect element.
        Check that ValueError is raised.
        """
        tree = BinarySearchTree()
        for element in (None, (), [], {}):
            self.assertRaises(ValueError, tree.remove, element)

    def test_e2e(self):
        """
        Creates a binary tree and fills it with different values.
        Try to fill value that already exists.
        Adds 1000 to the tree and checks its new height.
        Removes absent values and checks that ValueError is raised.
        Removes small element and checks that all connected elements are also removed.
        Checks that there is only 1 element (and level) left.
        """
        tree = BinarySearchTree()
        self.assertTrue(tree.empty, BinarySearchTree())

        for element in (0, 2, 42, 330, 15, 10, 7):
            self.assertTrue(tree.add(element))

        self.assertFalse(tree.add(42))  # elements should be added only once
        self.assertTrue(tree.add(1000))

        self.assertEqual(tree.height(), 6)
        self.assertTrue(tree.find(330))

        for element in (25, 16, 90, 87):  # try to remove absent elements
            self.assertRaises(ValueError, tree.remove, element)

        tree.remove(2)  # removal of one of the smallest elements

        for element in (7, 10, 15, 42, 330):  # check for the cascaded removal of all larger elements
            self.assertFalse(tree.find(element))

        self.assertTrue(tree.height, 1)
