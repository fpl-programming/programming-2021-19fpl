"""
Tests for BinarySearchTree class.
"""


import unittest

from binarytree.binarytree import BinarySearchTree, Node


class NodeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementations of Node.
    """

    def test_create_new_node(self):
        """
        Test that node is created correctly.
        """
        nodes = [70, 31, 93, 94, 14, 23, 73]
        for element in nodes:
            node = Node(element)
            self.assertEqual(node.element, element)

    def test_raise_type_error(self):
        """
        Create a Node with no integer attribute
        Test that creation of Node raises Type error
        """
        parameters = ['123', [], (), {}, 2.5, True]
        for parameter in parameters:
            self.assertRaises(TypeError, Node, parameter)

    class BinarySearchTreeTestCase(unittest.TestCase):
        """
        This Case of tests checks the functionality of the implementation of Queue
        """

    def test_add_element(self):  # add
        """
        Test that add function adds new element to tree.
        """
        tree = BinarySearchTree()
        tree.add(59)
        self.assertEqual(tree.find(59), True)

    def test_remove_node(self):   # remove
        """
        Remove node from Tree
        Test that Tree has no such node
        """
        tree = BinarySearchTree(3)
        tree.add(5)
        tree.remove(5)
        self.assertFalse(tree.find(5))

    def test_find_non_existing_node(self):  # find
        """
        Find non existing node in Tree
        Test that method returns False
        """
        tree = BinarySearchTree(8)
        tree.add(25)
        tree.add(35)
        tree.remove(25)
        self.assertFalse(tree.find(25))

    def test_get_height(self):  # get_height
        """
        Test that get_height function returns the max height of the tree.
        """
        tree = BinarySearchTree()
        nodes = [70, 31, 93, 94, 14, 23, 73]
        for element in nodes:
            tree.add(element)
        self.assertEqual(tree.get_height(), 3)
