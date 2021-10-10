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
        for element in elements:
            self.assertRaises(ValueError, Node, element)

    class BinaryTreeTestCase(unittest.TestCase):
        """
        Tests for BinaryTree  class
        """
        def test_add_element(self):
            """
            Tests if the new element is added to the tree
            """
            tree = BinaryTree()
            tree.add(4, 10)
            self.assertEqual(tree.find(4, 10), True)

        def test_remove_root(self):
            """
            Remove the root element
            """
            tree = BinaryTree()
            tree.add(None, 3)
            tree.remove(None, 3)
            self.assertEqual(tree.root, None)

        def test_find_element(self):
            """
            Find the element
            """

            tree = BinaryTree()
            tree.add(None,3)
            tree.add(None,2)
            tree.add(None,8)
            self.assertEqual(tree.find(None,6), True)

        def test_get_height(self):
            """
            Get the height of the  binary tree
            """
            tree = BinaryTree()
            tree.add(None,7)
            tree.add(None,10)
            tree.add(None,6)
            self.assertEqual(tree.get_height(None), 2)
