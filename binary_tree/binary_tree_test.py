"""
Programming for linguists

Tests for BinarySearchTree class.
"""

import unittest
from binary_tree.binary_tree import BinarySearchTree, TreeNode


class NodeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementations of Node.
    """

    def test_create_node(self):
        """
        Creates a node and checks
        if it is correct
        """
        node = TreeNode(22)
        self.assertEqual(node.value, 22)

    def test_type_of_node(self):
        """
        Checks if the type of the node is correct
        """
        error = ['Hello', 1]
        for element in error:
            self.assertRaises(ValueError, TreeNode, element)


class BinarySearchTreeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementations of BinarySearchTree
    """

    def test_tree_creation(self):
        """
        Tests if binary tree is correct
        """
        tree = BinarySearchTree(0)
        self.assertEqual(tree.root, 0)

    def test_binary_search_tree_add_element(self):
        """
        Create an empty BinarySearchTree and add an element.
        Test that add function adds new element to tree
        """
        tree = BinarySearchTree()
        tree.add(5)
        self.assertEqual(tree.find(5), True)

    def test_add_element(self):
        """
        Tests if the new element is added to the tree
        """
        tree = BinarySearchTree()
        tree.add(4)
        self.assertEqual(tree.find(4), True)

    def test_find(self):
        """
        Create a BinarySearchTree.
        Test that find function return True in case when element is found
        """
        tree = BinarySearchTree()
        one = 6
        two = 3
        three = 10
        tree.add(one)
        tree.add(two)
        tree.add(three)
        self.assertEqual(tree.find(three), True)

    def test_remove_element(self):
        """
        Checks if element is removed
        """
        pass
