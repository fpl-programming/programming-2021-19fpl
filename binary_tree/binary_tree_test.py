"""
Programming for linguists
Tests for BinarySearchTree class
"""


import unittest

from binary_tree.binary_tree import Node, BinarySearchTree

class BinarySearchTreeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of BinarySearchTree
    """

    def test_create_node(self):
        """
        Test that node is created correctly.
        """
        node = Node(9)
        self.assertEqual(node.data, 9)

    def test_create_node_with_not_int_element(self):
        """
        Test that incorrect element in creating new node raises ValueError
        """
        elements = [20, 0.55, (), []]
        for element in elements:
            self.assertRaises(ValueError, Node, element)

    class BinarySearchTreeTestCase(unittest.TestCase):
        """
        This Case of tests checks the functionality of the implementations of BinarySearchTree.
        """

        def test_add_existing_element(self):
            """
            Test that add function adds new element to tree
            """
            tree = BinarySearchTree()
            tree.add(10)
            self.assertEqual(tree.find(10), True)

        def test_remove(self):
            """
            Test that remove function removes element
            """
            tree = BinarySearchTree()
            tree.add(13)
            self.assertEqual(tree.remove(13), None)

        def test_find(self):
            """
            Create a BinarySearchTree
            Test that find function return True in case when element is found
            """
            tree = BinarySearchTree()
            node = 6
            node_left_element = 3
            node_right_element = 7
            tree.add(node)
            tree.add(node_left_element)
            tree.add(node_right_element)
            self.assertEqual(tree.find(node_right_element), True)

        def test_get_height(self):
            """
            Test that get_height function returns the max of the tree
            """
            tree = BinarySearchTree()
            nodes = [19, 35, 28, 10, 12, 22, 48]
            for element in nodes:
                tree.add(element)
            self.assertEqual(tree.get_height(), 4)