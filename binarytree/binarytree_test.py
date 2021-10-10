"""
Programming for linguists
Tests for Binarytree class.
"""

import unittest
from binarytree.binarytree import BinaryTree, Node


class NodeTestCase(unittest.TestCase):
    """
    Tests for Node class
    """

    def test_create_node(self):
        """
        Create a node with data 5 and tests
        if it is correct
        """
        node = Node(8)
        self.assertEqual(node.data, 8)

    def test_create_node_with_not_int_element(self):
        """
        Test if there would be a error
        when the element's type  is not int
        """
        elements = ['fjf', 0.45, {'a': 'node'}, []]
        for el in elements:
            self.assertRaises(ValueError, Node, el)

    class BinaryTreeTestCase(unittest.TestCase):
        """
        Tests for BinaryTree  class
        """
        def test_add_element(self):
            """
            Tests if the new element is added to the tree
            """
            tree = BinaryTree
            tree.add(10)
            self.assertEqual(tree.find(10), True)


