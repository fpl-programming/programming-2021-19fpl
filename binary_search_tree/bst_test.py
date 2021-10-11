"""
Tests for BinarySearchTree class.
"""


import unittest

from binary_search_tree.bst import BinarySearchTree, Node, NoNodeError, EmptyError


class NodeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementations of Node.
    """

    def test_create_node(self):
        """
        Test of creation node
        """
        nodes = [89, 23, 98, 95, 10, 29, 77]
        for element in nodes:
            node = Node(element)
            self.assertEqual(node.element, element)

    '''def test_raise_type_error(self):
        """
        Raising Type error in Node
        """
        elements = ['123', [], (), {}, 2.5]
        for element in elements:
            self.assertRaises(ValueError, Node, element)'''

    class BinarySearchTreeTestCase(unittest.TestCase):
        """
        This Case of tests checks the functionality of the implementation of Queue
        """

    def test_add_element(self):
        """
        Test of adding new element to tree.
        """
        tree = BinarySearchTree()
        tree.add(46)
        self.assertEqual(tree.find(46), True)

    def test_add_existing_element(self):
        """
        Test of adding existing element
        """
        tree = BinarySearchTree()
        tree.add(11)
        self.assertRaises(ValueError, tree.add, 11)

    def test_add_multiple_elements(self):
        """
        Test of adding all elements
        """
        tree = BinarySearchTree()
        nodes = [89, 23, 98, 95]
        for element in nodes:
            tree.add(element)
            self.assertEqual(tree.find(element), True)

    def test_remove(self):
        """
        Test of removing element
        """
        tree = BinarySearchTree()
        tree.add(16)
        self.assertEqual(tree.remove(16), None)

    def test_remove_element(self):
        """
        Test of removing not only element, but also all his descendants
        """
        tree = BinarySearchTree()
        nodes = [89, 23, 98, 95, 10, 29, 77]
        for element in nodes:
            tree.add(element)
        tree.remove(95)
        self.assertEqual(tree.find(28), False)

    def test_remove_not_existing_element(self):
        """
        Test of removing an element that is not in the tree
        """
        tree = BinarySearchTree()
        tree.add(16)
        self.assertRaises(NoNodeError, tree.remove, 24)

    def test_find_element(self):
        """
        Test of finding element
        """
        tree = BinarySearchTree()
        node, node_left, node_right = 4, 1, 7
        tree.add(node)
        tree.add(node_left)
        tree.add(node_right)
        self.assertEqual(tree.find(node_left), True)

    def test_find_not_existing_element(self):
        """
        Test of finding not existing element
        """
        tree = BinarySearchTree()
        nodes = [89, 23, 98, 95, 10, 29, 77]
        for element in nodes:
            tree.add(element)
        self.assertEqual(tree.find(61), False)

    def test_find_element_in_empty_tree(self):
        """
        Test of finding empty tree
        """
        tree = BinarySearchTree()
        self.assertRaises(EmptyError, tree.find, 16)

    def test_get_height(self):
        """
        Test of getting height of the tree
        """
        tree = BinarySearchTree()
        nodes = [89, 23, 98, 95, 10, 29, 77]
        for element in nodes:
            tree.add(element)
        self.assertEqual(tree.get_height(), 4)

    def test_get_height_of_empty_tree(self):
        """
        Test of getting height of the empty tree
        """
        tree = BinarySearchTree()
        self.assertRaises(EmptyError, tree.get_height)

    def test_get_height_after_remove(self):
        """
        Test of getting height of the tree after removing element
        """
        tree = BinarySearchTree()
        nodes = [89, 23, 98, 95, 10, 29, 77]
        for element in nodes:
            tree.add(element)
        tree.remove(29)
        self.assertEqual(tree.get_height(), 3)
