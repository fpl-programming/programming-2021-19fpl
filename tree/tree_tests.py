"""
Programming for linguists

Tests for BinarySearchTree class
"""


import unittest

from tree.tree import Node, BinarySearchTree, EmptyError, NoNodeError


class NodeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementations of Node
    """
    def test_create_new_node(self):
        """
        Test that node is created correctly
        """
        nodes = [15, 10, 20, 7, 18, 9, 19]
        for element in nodes:
            node = Node(element)
            self.assertEqual(node.element, element)

    def test_incorrect_element_create_node(self):
        """
        Test that incorrect element in creating new node raises ValueError
        """
        incorrect_element = ['a', 1.5, (), []]
        for element in incorrect_element:
            self.assertRaises(ValueError, Node, element)


class BinarySearchTreeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementations of BinarySearchTree
    """
    def test_tree_creation(self):
        """
        Test if a new tree is created correctly
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

    def test_add_existing_element(self):
        """
        Create a BinarySearchTree.
        Test that add function raises ValueError when an element is already in the tree
        """
        tree = BinarySearchTree()
        tree.add(20)
        self.assertRaises(ValueError, tree.add, 20)

    def test_add_more(self):
        """
        Create a BinarySearchTree and add elements
        Test that all elements added
        """
        tree = BinarySearchTree()
        for element in [1, 6, 2, 8]:
            tree.add(element)
            self.assertEqual(tree.find(element), element)

    def test_remove(self):
        """
        Create a BinarySearchTree.
        Test that remove function removes element
        """
        tree = BinarySearchTree()
        tree.add(11)
        self.assertEqual(tree.remove(10), None)

    def test_remove_element(self):
        """
        Test that remove function removes not only element, but also all his descendants
        """
        tree = BinarySearchTree()
        nodes = [15, 10, 20, 7, 18, 9, 19]
        for element in nodes:
            tree.add(element)
        tree.remove(20)
        self.assertEqual(tree.find(19), False)

    def test_remove_not_exiting_element(self):
        """
        Create a BinarySearchTree.
        Test that remove function raises NoNodeError when an element is not in the tree
        """
        tree = BinarySearchTree()
        tree.add(10)
        self.assertRaises(NoNodeError, tree.remove, 11)

    def test_find(self):
        """
        Create a BinarySearchTree.
        Test that find function return True in case when element is found
        """
        tree = BinarySearchTree()
        node = 5
        node_left = 3
        node_right = 7
        tree.add(node)
        tree.add(node_left)
        tree.add(node_right)
        self.assertEqual(tree.find(node_right), True)

    def test_find_not_existing_element(self):
        """
        Create a BinarySearchTree.
        Test that find function return False in case when element is not found
        """
        tree = BinarySearchTree()
        nodes = [15, 10, 20, 7, 18, 9, 19]
        for element in nodes:
            tree.add(element)
        self.assertEqual(tree.find(16), False)

    def test_find_element_in_empty_tree(self):
        """
        Test that find function raises EmptyError when tree is empty
        """
        tree = BinarySearchTree()
        self.assertRaises(EmptyError, tree.find, 10)

    def test_get_height(self):
        """
        Create a BinarySearchTree.
        Test that get_height function returns the max height of the tree
        """
        tree = BinarySearchTree()
        nodes = [15, 10, 20, 7, 18, 9, 19]
        for element in nodes:
            tree.add(element)
        self.assertEqual(tree.get_height(), 4)

    def test_get_height_of_empty_tree(self):
        """
        Test that get_height function raises EmptyError when tree is empty
        """
        tree = BinarySearchTree()
        self.assertRaises(EmptyError, tree.get_height)

    def test_get_height_after_remove(self):
        """
        Create a BinarySearchTree.
        Test that get_height function returns correct max height of the tree after removing element
        """
        tree = BinarySearchTree()
        nodes = [15, 10, 20, 18, 19]
        for element in nodes:
            tree.add(element)
        tree.remove(20)
        self.assertEqual(tree.get_height(), 2)
