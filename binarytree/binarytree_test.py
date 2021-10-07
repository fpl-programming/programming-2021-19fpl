"""
Test for BinaryTree class
"""

import unittest

from binarytree.binarytree import BinaryTree
# from binarytree import BinaryTree


class BinaryTreeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Binary Tree
    """

    def test_add_nodes_from_list(self):
        """
            (positive testing of add function)
        Create a binary tree.
        Add nodes from list to the binary tree.
        Test that all the nodes are placed correctly
        """
        binary_tree = BinaryTree(4)
        elements = [3, 1, 2, 6, 7, 5]
        for element in elements:
            binary_tree.add(element)
        self.assertEqual(binary_tree.root.value, 4)
        self.assertEqual(binary_tree.root.left.value, 3)
        self.assertEqual(binary_tree.root.right.value, 6)

    def test_call_add_non_integers_raised_error(self):
        """
            (negative testing of add function)
        Create a binary tree.
        Test that call of add method with incorrect inputs raises Value error
        """
        binary_tree = BinaryTree(4)
        non_integers = [10.44465, 'two', None, {}, ['wow']]
        for element in non_integers:
            self.assertRaises(ValueError, binary_tree.add, element)

    def test_add_to_empty_binary_tree(self):
        """
            (end-to-end testing of add function)
        Create an empty binary tree.
        Add nodes from a generator to the binary tree.
        Test that all the nodes are placed correctly
        """
        binary_tree = BinaryTree()
        for num in range(1, 5):
            binary_tree.add(num)
        self.assertEqual(binary_tree.root.value, 1)
        self.assertEqual(binary_tree.root.right.value, 2)
        self.assertEqual(binary_tree.root.right.right.value, 3)
        self.assertEqual(binary_tree.root.right.right.right.value, 4)

    def test_remove_1(self):
        """
            (positive testing of remove function)
        hiiiii there
        """
        self.assertEqual(True, True)

    def test_remove_2(self):
        """
            (negative testing of remove function)
        hiiiii there
        """
        self.assertEqual(True, True)

    def test_remove_3(self):
        """
            (end-to-end testing of remove function)
        hiiiii there
        """
        self.assertEqual(True, True)

    def test_find_1(self):
        """
            (positive testing of find function)
        hiiiii there
        """
        self.assertEqual(True, True)

    def test_find_2(self):
        """
            (negative testing of find function)
        hiiiii there
        """
        self.assertEqual(True, True)

    def test_find_3(self):
        """
            (end-to-end testing of find function)
        hiiiii there
        """
        self.assertEqual(True, True)

    def test_get_height_1(self):
        """
            (positive testing of get_height function)
        hiiiii there
        """
        self.assertEqual(True, True)

    def test_get_height_2(self):
        """
            (negative testing of get_height function)
        hiiiii there
        """
        self.assertEqual(True, True)

    def test_get_height_3(self):
        """
            (end-to-end testing of get_height function)
        hiiiii there
        """
        self.assertEqual(True, True)

    def test_get_dfs_1(self):
        """
            (positive testing of get_dfs function)
        hiiiii there
        """
        self.assertEqual(True, True)

    def test_get_dfs_2(self):
        """
            (negative testing of get_dfs function)
        hiiiii there
        """
        self.assertEqual(True, True)

    def test_get_dfs_3(self):
        """
            (end-to-end testing of get_dfs function)
        hiiiii there
        """
        self.assertEqual(True, True)
