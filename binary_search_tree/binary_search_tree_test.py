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

    def test_1(self):
        pass

    def test_2(self):
        pass

    def test_3(self):
        pass

    def test_4(self):
        pass

    def test_5(self):
        pass

    def test_6(self):
        pass

    def test_7(self):
        pass

    def test_8(self):
        pass

    def test_9(self):
        pass

    def test_10(self):
        pass

    def test_11(self):
        pass

    def test_12(self):
        pass

    def test_13(self):
        pass

