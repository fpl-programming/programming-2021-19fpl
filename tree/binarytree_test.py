"""
Programming for linguists

Tests for BinaryTree classes.
"""

import unittest

from tree.binarytree import Node, BinarySearchTree, EmptyError, NoNodeError


class NodeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementations of Node.
    """
    def test_create_new_node(self):
        """
        Test that node is created correctly.
        """
        nodes = [20, 11, 33, 1, 31, 10, 30]
        for element in nodes:
            node = Node(element)
            self.assertEqual(node.element, element)

    def test_incorrect_element_create_node(self):
        """
        Test that incorrect element in creating new node raises ValueError.
        """
        incorrect_elements = ['a', 1.1, (), [], {}]
        for element in incorrect_elements:
            self.assertRaises(ValueError, Node, element)


class BinarySearchTreeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementations of BinarySearchTree.
    """

    def test_add_element(self):
        """
        Test that add function adds new element to tree.
        """
        tree = BinarySearchTree()
        tree.add(20)
        self.assertEqual(tree.find(20), True)

    def test_add_existing_element(self):
        """
        Test that add function raises ValueError when an element is already in the tree.
        """
        tree = BinarySearchTree()
        tree.add(20)
        self.assertRaises(ValueError, tree.add, 20)

    def test_add_multiple_elements(self):
        """
        Test that add function adds all elements.
        """
        tree = BinarySearchTree()
        nodes = [20, 33, 31, 30]
        for element in nodes:
            tree.add(element)
            self.assertEqual(tree.find(element), True)

    def test_remove(self):
        """
        Test that remove function removes element.
        """
        tree = BinarySearchTree()
        tree.add(10)
        self.assertEqual(tree.remove(10), None)

    def test_remove_element(self):
        """
        Test that remove function removes not only element, but also all his descendants.
        """
        tree = BinarySearchTree()
        nodes = [20, 11, 33, 1, 31, 10, 30]
        for element in nodes:
            tree.add(element)
        tree.remove(33)
        self.assertEqual(tree.find(30), False)

    def test_remove_not_existing_element(self):
        """
        Test that remove function raises NoNodeError when an element is not in the tree.
        """
        tree = BinarySearchTree()
        tree.add(10)
        self.assertRaises(NoNodeError, tree.remove, 11)

    def test_find_element(self):
        """
        Test that find function return True in case when element is found.
        """
        tree = BinarySearchTree()
        node, node_l, node_r = 5, 2, 6
        tree.add(node)
        tree.add(node_l)
        tree.add(node_r)
        self.assertEqual(tree.find(node_l), True)

    def test_find_not_existing_element(self):
        """
        Test that find function return False in case when element is not found.
        """
        tree = BinarySearchTree()
        nodes = [20, 11, 33, 1, 31, 10, 30]
        for element in nodes:
            tree.add(element)
        self.assertEqual(tree.find(25), False)

    def test_find_element_in_empty_tree(self):
        """
        Test that find function raises EmptyError when tree is empty.
        """
        tree = BinarySearchTree()
        self.assertRaises(EmptyError, tree.find, 10)

    def test_get_height(self):
        """
        Test that get_height function returns the max height of the tree.
        """
        tree = BinarySearchTree()
        nodes = [20, 11, 33, 1, 31, 10, 30]
        for element in nodes:
            tree.add(element)
        self.assertEqual(tree.get_height(), 4)

    def test_get_height_of_empty_tree(self):
        """
        Test that get_height function raises EmptyError when tree is empty.
        """
        tree = BinarySearchTree()
        self.assertRaises(EmptyError, tree.get_height)

    def test_get_height_after_remove(self):
        """
        Test that get_height function returns correct max height of the tree after removing element.
        """
        tree = BinarySearchTree()
        nodes = [20, 11, 33, 31, 30]
        for element in nodes:
            tree.add(element)
        tree.remove(33)
        self.assertEqual(tree.get_height(), 2)
