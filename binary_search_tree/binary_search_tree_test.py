"""
Programming for linguists

Tests for BinarySearchTree and Node classes.
"""

import unittest

from binary_search_tree.binary_search_tree import Node, BinarySearchTree, \
                    EmptyTreeError, DuplicateError, NonexistentNodeError


class NodeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Node class
    """

    def test_non_integer_node_raised_error(self):
        """
        Create a new node.
        Test that node of non integer values raises TypeError
        """
        for value_to_check in [[1, 2], (3, 4, 5), None, 'value', 4.45, {'key': 3}]:
            self.assertRaises(TypeError, Node.__init__, value_to_check)

class BinarySearchTreeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of BinarySearchTree class
    """

    def test_empty_tree_values(self):
        """
        Create an empty Binary Search tree.
        Test that its root is None and name is set by default.
        """
        empty_tree = BinarySearchTree()
        self.assertIsNone(empty_tree.root)
        self.assertEqual(empty_tree.name, "Binary_Search_Tree")
