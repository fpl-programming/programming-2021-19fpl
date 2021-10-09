"""
Programming for linguists
Tests for Queue class.
"""


import unittest
from binary_search_tree import BinarySearchTree, Node, NodeExistsError, NodeNotFoundError


class MyTestCase(unittest.TestCase):
    def test_create_node_ideal(self):
        """
        Create a node with 5 as a parameter.
        Test that node's root is 5.
        """
        node = Node(5)
        self.assertEqual(node.root, 5)

    def test_create_node_with_not_int_element(self):
        """
        Test that call of instantiation of class Node with
        not integer parameter raises the type error
        """
        elements = ['1', 0.11, print, {'name': 'tree'}, [1, 2, 3]]
        for element in elements:
            self.assertRaises(TypeError, Node.__init__, element)

    def test_new_BST_is_empty(self):
        """
        Create a binary search tree.
        Test that its root is None and its name is "Binary tree".
        """
        tree = BinarySearchTree('Binary search tree')
        self.assertEqual(tree.name, 'Binary search tree')
        self.assertEqual(tree._root, None)

    def test_new_BST_with_wrong_name_raised_error(self):
        """
        Test that call of instantiation of class BinarySearchTree with
        the not string name raises the type error
        """
        names = [1, 0.11, print, {'name': 'tree'}, [1, 2, 3]]
        for name in names:
            self.assertRaises(TypeError, BinarySearchTree.__init__, name)

    def test_add_not_integer_element(self):
        """
        Create an empty binary search tree and add elements.
        Test that adding an non-integer element raised type error.
        """
        tree = BinarySearchTree('Binary search tree')
        tree.add(10)
        tree.add(2)
        self.assertRaises(TypeError, tree.add, '11')

    def test_add_first_element(self):
        """
        Create an empty binary search tree and add an element.
        Test that the element which is added as the first one is root of the tree.
        """
        tree = BinarySearchTree('Binary search tree')
        self.assertEqual(tree._root, None)
        tree.add(10)
        self.assertEqual(tree._root.root, 10)

    def test_add_existing_element(self):
        """
        Create an empty binary search tree and add elements.
        Test that adding an element that is already in the tree
        raised NodeExists error.
        """
        tree = BinarySearchTree('Binary search tree')
        tree.add(10)
        tree.add(2)
        tree.add(11)
        self.assertRaises(NodeExistsError, tree.add, 11)

    def test_remove_element_ideal(self):
        """
        Create an empty binary search tree and add elements.
        Test that after removing the element its parent does not have it anymore
        """
        tree = BinarySearchTree('Binary search tree')
        tree.add(10)
        tree.add(2)
        tree.add(11)
        tree.remove(2)
        self.assertEqual(tree._root.left_node, None)

    def test_remove_not_existing_element(self):
        """
        Create an empty binary search tree and add elements.
        Test that call of remove function with the element that is
        ot in the tree raised NodeNotFoundError
        """
        tree = BinarySearchTree('Binary search tree')
        tree.add(10)
        tree.add(4)
        tree.add(11)
        self.assertRaises(NodeNotFoundError, tree.remove, 3)

    def test_remove_root_of_tree(self):
        """
        Create an empty binary search tree and add elements.
        Test that after removing the element that is the root of the tree
        the tree's _root is None (tree is empty)
        """
        tree = BinarySearchTree('Binary search tree')
        tree.add(10)
        tree.add(4)
        tree.add(11)
        tree.remove(10)
        self.assertEqual(tree._root, None)
        # self.assertEqual(tree._root.root, None)
        # self.assertEqual(tree._root.left_node, None)
        # self.assertEqual(tree._root.right_node, None)

    def test_find_element_ideal(self):
        """
        Create an empty binary search tree and add elements.
        Test that call of find function return the node
        where the root is the element
        Check that the root is 4 and node's left children is 2
        """
        tree = BinarySearchTree('Binary search tree')
        tree.add(10)
        tree.add(4)
        tree.add(2)
        tree.add(11)
        found_element = tree.find(4)
        self.assertEqual(found_element.root, 4)
        self.assertEqual(found_element.left_node.root, 2)

    def test_find_not_existing_element(self):
        """
        Create an empty binary search tree and add elements.
        Test that call of find function with the element that is not
        in the tree return None
        """
        tree = BinarySearchTree('Binary search tree')
        tree.add(10)
        tree.add(4)
        tree.add(2)
        tree.add(11)
        found_element = tree.find(5)
        self.assertEqual(found_element, None)

    def test_find_element_in_long_tree(self):
        """
        Create a tree with a lot of nodes.
        Test that call of find function for the last element in tree
        returns the node with that element
        """
        tree = BinarySearchTree('Binary search tree')
        for element in range(900):  # not more 977 because maximum recursion depth exceeded
            tree.add(element)
        found_element = tree.find(899)
        self.assertEqual(found_element.root, 899)

    def test_get_max_height_ideal(self):
        """
        Create a tree with 4 levels of nodes.
        Test that call of max_height getter return 4
        """
        tree = BinarySearchTree('Binary search tree')
        tree.add(10)
        tree.add(4)
        tree.add(2)
        tree.add(11)
        tree.add(3)
        self.assertEqual(tree.max_height, 4)

    def test_get_height_empty_and_only_root(self):
        """
        Create an empty tree.
        Test that call of max_height getter return 0
        Add a root.
        Test that call of max_height getter return 1
        """
        tree = BinarySearchTree('Binary search tree')
        self.assertEqual(tree.max_height, 0)

        tree.add(10)
        self.assertEqual(tree.max_height, 1)

    def test_get_height_only_one_branch(self):
        """
        Create a tree with one branch with 100 elements
        Test that call of of max_height getter return 100
        """
        tree = BinarySearchTree('Binary search tree')
        for element in range(100, 200):
            tree.add(element)
        self.assertEqual(tree.max_height, 100)

    def test_all_functions(self):
        """
        Create an empty tree.
        Test calls of add, remove, find, get max height functions
        """
        tree = BinarySearchTree('Binary search tree')
        elements = [10, 4, 12, 6, 2, 8, 11, 15, 3, 5, 7]
        for element in elements:
            tree.add(element)
        found_element = tree.find(6)
        self.assertEqual(found_element.root, 6)
        self.assertEqual(found_element.left_node.root, 5)
        self.assertEqual(found_element.right_node.root, 8)
        self.assertEqual(tree.max_height, 5)
        tree.remove(6)
        self.assertEqual(tree.find(8), None)
        self.assertEqual(tree.max_height, 4)

    def test_tree_traversal_ideal(self):
        """
        Create a tree and add elements.
        Test that call of tree traversal function
        returns the ordered list of elements
        """
        elements = [10, 4, 12, 6, 2, 8, 11]
        tree = BinarySearchTree('Binary search tree')
        for element in elements:
            tree.add(element)
        self.assertTrue(isinstance(tree.get_tree_traversal(), list))
        self.assertEqual(tree.get_tree_traversal(), [10, 4, 2, 6, 8, 12, 11])

    def test_tree_traversal_only_root(self):
        """
        Create a tree and add only root.
        Test that call of tree traversal function
        returns the value of the root
        """
        tree = BinarySearchTree('Binary search tree')
        tree.add(10)
        self.assertEqual(tree.get_tree_traversal(), [10])

    def test_tree_traversal_one_branch(self):
        """
        Create a tree with only one branch.
        Test that return of tree traversal function
        is equal to the list of elements were added
        """
        tree = BinarySearchTree('Binary search tree')
        elements = [element for element in range(900)]  # not more 977 because maximum recursion depth exceeded
        for element in elements:
            tree.add(element)
        self.assertEqual(tree.get_tree_traversal(), elements)
