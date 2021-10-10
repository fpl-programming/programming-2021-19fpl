"""
Programming for linguists
Tests for BinarySearchTree class
"""


import unittest

from bintree.binarytree import Node, BinarySearchTree, NoNodeError, EmptyError


class NodeTestCase(unittest.TestCase):
    """
        This Case of tests checks the functionality of the implementations of Node.
        """

    def test_create_node(self):
        """
        Test that node is created correctly.
        """
        node = Node(8)
        self.assertEqual(node.data, 8)

    def test_create_node_with_not_int_element(self):
        """
         Test that incorrect element in creating new node raises ValueError.
        """
        elements = [15, [], 0.45, "fdgd", {'num': 'node'}]
        for element in elements:
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
            Create a BinarySearchTree.
            Test that add function raises ValueError when an element is already in the tree
            """
            tree = BinarySearchTree()
            tree.add(15)
            self.assertRaises(ValueError, tree.add, 15)

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
            tree.add(15)
            self.assertEqual(tree.remove(15), None)

        def test_remove_element(self):
            """
            Test that remove function removes not only element, but also all his descendants.
            """
            tree = BinarySearchTree()
            nodes = [2, 15, 3, 31, 74]
            for element in nodes:
                tree.add(element)
            tree.remove(15)
            self.assertEqual(tree.find(31), False)

        def test_remove_not_existing_element(self):
            """
            Test that remove function raises NoNodeError when an element is not in the tree.
            """
            tree = BinarySearchTree()
            tree.add(15)
            self.assertRaises(NoNodeError, tree.remove, 3)

        def test_find(self):
            """
            Create a BinarySearchTree.
            Test that find function return True in case when element is found
            """
            tree = BinarySearchTree()
            node = 9
            node_left_element = 4
            node_right_element = 2
            tree.add(node)
            tree.add(node_left_element)
            tree.add(node_right_element)
            self.assertEqual(tree.find(node_right_element), True)

        def test_find_not_existing_element(self):
            """
            Create a BinarySearchTree.
            Test that find function return False in case when element is not found
            """
            tree = BinarySearchTree()
            nodes = [5, 14, 27, 19]
            for element in nodes:
                tree.add(element)
            self.assertEqual(tree.find(26), False)

        def test_find_element_in_empty_tree(self):
            """
            Test that find function raises EmptyError when tree is empty
            """
            tree = BinarySearchTree()
            self.assertRaises(EmptyError, tree.find, 14)

        def test_get_height(self):
            """
            Test that get_height function returns the max height of the tree.
            """
            tree = BinarySearchTree()
            nodes = [25, 31, 33, 12, 14, 10, 40]
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
            nodes = [23, 19, 76, 41, 14]
            for element in nodes:
                tree.add(element)
            tree.remove(20)
            self.assertEqual(tree.get_height(), 2)
