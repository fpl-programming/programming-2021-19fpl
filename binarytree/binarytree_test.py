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
        integers = [3, 1, 2, 6, 7, 5]
        for val in integers:
            binary_tree.add(val)
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
        for val in non_integers:
            self.assertRaises(ValueError, binary_tree.add, val)

    def test_add_to_empty_binary_tree(self):
        """
            (end-to-end testing of add function)
        Create an empty binary tree.
        Add nodes from a generator to the binary tree.
        Test that all the nodes are placed correctly
        """
        binary_tree = BinaryTree()
        for val in range(1, 5):
            binary_tree.add(val)
        self.assertEqual(binary_tree.root.value, 1)
        self.assertEqual(binary_tree.root.right.value, 2)
        self.assertEqual(binary_tree.root.right.right.value, 3)
        self.assertEqual(binary_tree.root.right.right.right.value, 4)

    def test_find_1(self):
        """
            (positive testing of find function)
        Create an empty binary tree.
        Add nodes from list to the binary tree.
        Test that the nodes of the binary tree can be found by the value
        """
        binary_tree = BinaryTree()
        node_values = [10, 5, 15, 2, 12, 6, 20, 19]
        for val in node_values:
            binary_tree.add(val)
        for val in node_values:
            self.assertEqual(binary_tree.find(val), val)

    def test_find_2(self):
        """
            (negative testing of find function)
        Create an empty binary tree.
        Add nodes from list to the binary tree.
        Test that call of find with incorrect values returns None
        """
        binary_tree = BinaryTree()
        node_values = [10, 5, 15, 2, 12, 6, 20, 19]
        for val in node_values:
            binary_tree.add(val)
        wrong_values = [0, 1, 3, 4, 13, 100, 548150]
        for val in wrong_values:
            self.assertEqual(binary_tree.find(val), None)
        non_integers = [10.44465, 'two', None, {}, ['wow']]
        for val in non_integers:
            self.assertEqual(binary_tree.find(val), None)

    def test_find_3(self):
        """
            (end-to-end testing of find function)
        hiiiii there
        """
        self.assertEqual(True, True)

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
