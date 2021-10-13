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
        nodes = [20, 12, 32, 10, 1, 34, 97]
        for value in nodes:
            node = TreeNode(value)
            self.assertEqual(node.value, value)

    def test_type_of_node(self):
        """
        Checks if the type of the node is correct
        """
        error_elements = ['Hello', 1.2]
        for element in error_elements:
            self.assertRaises(ValueError, TreeNode, element)


class BinarySearchTreeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementations of BinarySearchTree
    """

    def test_add_element(self):
        """
        Tests if the new element is added to the tree
        """
        element = 3
        binary_tree = BinarySearchTree()
        binary_tree.add(element)
        self.assertEqual(binary_tree.root.value, 3)

    def test_find_element(self):
        """
        Create a BinarySearchTree.
        Test that find function return True in case when element is found
        """
        binary_tree = BinarySearchTree()
        binary_tree.add(2)
        binary_tree.add(3)
        binary_tree.add(4)
        self.assertTrue(binary_tree.find(3))

    def test_remove_element(self):
        """
        Checks if element is removed
        """
        tree = BinarySearchTree()
        tree.add(2)
        self.assertEqual(tree.remove(2), None)
