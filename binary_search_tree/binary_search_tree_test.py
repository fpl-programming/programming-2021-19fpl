"""
Programming for linguists

Tests for BinarySearchTree class.
"""

import unittest
from binary_search_tree.binary_search_tree import Node, BinarySearchTree, NoTreeError, NoNodeError, NodeExistsError


class BinarySearchTreeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of BinarySearchTree
    """
    def test_empty_tree_is_created(self):
        """
        Create an empty tree.
        Test that tree is empty.
        """
        tree = BinarySearchTree()
        self.assertEqual(tree.root, None)
        self.assertEqual(tree.get_height(), 0)

    def test_tree_is_created(self):
        """
        Add three elements to the tree.
        Test that tree is created.
        """
        tree = BinarySearchTree()
        elements = [10, 8, 12]
        for element in elements:
            tree.add(element)
        self.assertEqual(tree.root.root, 10)
        self.assertEqual(tree.root.left.root, 8)
        self.assertEqual(tree.root.right.root, 12)

    def test_tree_creation_raised_error(self):
        """
        Try to add an element that is already in the tree or not integer.
        Test that adding an element raises error.
        """
        tree = BinarySearchTree()
        correct_elements = [10, 8, 12, 6, 7]
        incorrect_elements = [True, 'str', [2, 4], {'a': 1}, None]
        for element in correct_elements:
            tree.add(element)
            self.assertRaises(NodeExistsError, tree.add, element)
        for element in incorrect_elements:
            self.assertRaises(TypeError, tree.add, element)

    def test_find_element_in_the_tree(self):
        """
        Try to find an element in the tree.
        Test that a call of the function returns a Node class of an element.
        """
        tree = BinarySearchTree()
        elements = [10, 8, 12, 6, 7]
        for element in elements:
            tree.add(element)
            node_isolated = Node(element)
            node_from_tree = tree.find(element)
            self.assertEqual(node_isolated.root, node_from_tree.root)

    def test_find_nonexistent_element(self):
        """
        Try to find element that is not in the tree.
        Test that a call of the function returns None.
        """
        tree = BinarySearchTree()
        tree.add(9)
        not_nodes = [10, 8, 12, 6, 7]
        for element in not_nodes:
            self.assertEqual(None, tree.find(element))

    def test_find_element_raised_error(self):
        """
        Try to find an element in the empty tree.
        Try to find an element that is not integer.
        Test that a call of the function raises error.
        """
        tree = BinarySearchTree()
        correct_elements = [10, 8, 12, 6, 7]
        incorrect_elements = [True, 'str', [2, 4], {'a': 1}, None]
        for element in correct_elements:
            self.assertRaises(NoTreeError, tree.find, element)
        for element in incorrect_elements:
            self.assertRaises(TypeError, tree.find, element)

    def test_remove_element_from_the_tree(self):
        """
        Try to remove an element from the tree.
        Test that after a call of the function an element is removed from the tree.
        """
        tree = BinarySearchTree()
        elements = [10, 8, 12, 6, 7]
        for element in elements:
            tree.add(element)
        for element in elements[:0:-1]:
            tree.remove(element)
            self.assertEqual(None, tree.find(element))

    def test_children_after_removing(self):
        """
        Try to remove an element from the tree.
        Test that after a call of the function a parent of an element has no children.
        """
        tree = BinarySearchTree()
        elements = [10, 8, 12]
        for element in elements:
            tree.add(element)
        tree.remove(8)
        tree.remove(12)
        self.assertEqual(None, tree.root.left)
        self.assertEqual(None, tree.root.right)

    def test_remove_nonexistent_element(self):
        """
        Try to remove element that is not in the tree.
        Test that a call of the function raises error.
        """
        tree = BinarySearchTree()
        tree.add(9)
        not_nodes = [10, 8, 12, 6, 7]
        for element in not_nodes:
            self.assertRaises(NoNodeError, tree.remove, element)

    def test_get_height(self):
        """
        Test that a call of the function returns a number of levels in the tree.
        """
        tree = BinarySearchTree()
        elements = [10, 8, 12, 6, 7]
        for element in elements:
            tree.add(element)
        self.assertEqual(4, tree.get_height())

    def test_get_height_after_removing(self):
        """
        Test that a call of the function returns a correct number of levels in the tree after removing some elements.
        """
        tree = BinarySearchTree()
        elements = [10, 8, 12, 6, 7]
        for element in elements:
            tree.add(element)
        self.assertEqual(4, tree.get_height())
        tree.remove(12)
        self.assertEqual(4, tree.get_height())
        tree.remove(8)
        self.assertEqual(1, tree.get_height())

    def test_get_height_of_an_empty_tree(self):
        """
        Test that a call of the function returns 0.
        """
        tree = BinarySearchTree()
        self.assertEqual(0, tree.get_height())

    def test_all_class_implementation(self):
        """
        Test the whole realisation of the class.
        """
        tree = BinarySearchTree()
        elements = [10, 8, 12, 6, 7]
        for element in elements:
            tree.add(element)
            node_from_tree = tree.find(element)
            self.assertEqual(element, node_from_tree.root)
        tree.remove(8)
        self.assertEqual(None, tree.find(8))
        self.assertEqual(None, tree.find(6))
        self.assertEqual(2, tree.get_height())
