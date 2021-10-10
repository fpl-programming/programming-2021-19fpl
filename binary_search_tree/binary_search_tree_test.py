"""
Programming for linguists

Tests for BinarySearchTree and Node classes.
"""

import unittest

from binary_search_tree.binary_search_tree import Node, BinarySearchTree, \
                    EmptyTreeError, DuplicateError, NonExistentNodeError


class NodeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Node class
    """

    def test_non_integer_node_raised_error(self):
        """
        Create a new node.
        Test that node of non integer values raises TypeError.
        """
        for value_to_check in [[1, 2], (3, 4, 5), None, 'value', 4.45, {'key': 3}]:
            self.assertRaises(TypeError, Node.__init__, value_to_check)

class BinarySearchTreeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of BinarySearchTree class
    """

    def test_empty_tree_values(self):
        """
        Create an empty Binary Search Tree.
        Test that its root is None and name is set by default.
        """
        empty_tree = BinarySearchTree()
        self.assertIsNone(empty_tree.root)
        self.assertEqual(empty_tree.name, "Binary_Search_Tree")

    def test_add_one_element(self):
        """
        Create an empty Binary Search Tree.
        Test that add method adds an element as a root.
        """
        tree = BinarySearchTree()
        tree.add(10)
        self.assertEqual(tree.find(10), tree.root)


    def test_add_many_elements(self):
        """
        Create an empty Binary Search Tree.
        Test that add method works correctly with many elements.
        """
        tree = BinarySearchTree()
        for value_to_add in [12, 2, 4, 6, 8, 34, 20]:
            tree.add(value_to_add)
            self.assertEqual(tree.find(value_to_add).root, value_to_add)

    def test_add_existing_element_raised_error(self):
        """
         Create an empty Binary Search Tree.
         Test that add method raises DuplicateError when adding an existing value.
        """
        tree = BinarySearchTree()
        tree.add(100)
        self.assertRaises(DuplicateError, tree.add, 100)

    def test_add_non_integer_raised_value(self):
        """
        Create an empty Binary Search Tree.
        Test that adding of non integer values raises TypeError.
        """
        tree = BinarySearchTree()
        for value_to_check in [[], (), None, 'value', 4.45, {'key': 3}]:
            self.assertRaises(TypeError, tree.add, value_to_check)

    def test_find_in_empty_tree_raised_error(self):
        """
        Create an empty Binary Search Tree.
        Test that find method raises EmptyTreeError.
        """
        tree = BinarySearchTree()
        self.assertRaises(EmptyTreeError, tree.find, 100)

    def test_find_non_existing_element(self):
        """
        Create an empty Binary Search Tree.
        Test that find method returns False when trying to find non-existing element in tree.
        """
        tree = BinarySearchTree()
        for value in [8, 4, 10, 2, 6, 3, 7]:
            tree.add(value)
        self.assertFalse(tree.find(100))

    def test_find_elements(self):
        """
        Create an empty Binary Search Tree.
        Test that find method returns correct values.
        """
        tree = BinarySearchTree()
        for value in [8, 4, 10, 2, 6, 3, 7]:
            tree.add(value)
        actual_output = []
        for value in [4, 6, 7]:
            actual_output.append(tree.find(value).root)
        for value in [100, 1000, 5]:
            actual_output.append(tree.find(value))
        self.assertEqual([4, 6, 7, False, False, False], actual_output)

    def test_remove_empty_tree_raised_error(self):
        """
        Create an empty Binary Search Tree.
        Test that remove_node method raises EmptyTreeError.
        """
        tree = BinarySearchTree()
        self.assertRaises(EmptyTreeError, tree.remove_node, 10)

    def test_remove_non_existing_node_raised_error(self):
        """
        Create an empty Binary Search Tree.
        Tst that remove_node method raises NonExistingNodeError when trying to delete non-existing node.
        """
        tree = BinarySearchTree()
        for value in [10, 23, 4, 35, 54, 67, 1, 98]:
            tree.add(value)
        self.assertRaises(NonExistentNodeError, tree.remove_node, 100)

    def test_get_height_of_empty_tree(self):
        """
        Create an empty Binary Search Tree.
        Test that length of empty tree equals 0.
        """
        tree = BinarySearchTree()
        self.assertEqual(tree.get_height(), 0)

    def test_get_height_of_same_length_nodes(self):
        """
        Create a Binary Search Tree with 5 elements.
        Test that get_height method works correctly when last nodes are at the same level.
        """
        tree = BinarySearchTree()
        for value in [10, 4, 5, 23, 40]:
            tree.add(value)
        self.assertEqual(tree.get_height(), 3)

    def test_get_height_of_different_length_nodes(self):
        """
        Create a Binary Search Tree with 6 elements.
        Test that get_height method returns the longest branch when last nodes are at the different levels.
        """
        tree = BinarySearchTree()
        for value in [8, 4, 10, 2, 6, 3]:
            tree.add(value)
        self.assertEqual(tree.get_height(), 4)

    def test_call_width_traverse(self):
        """
        Create a Binary Search Tree with 7 elements.
        Test that width_traverse method returns correct values
        """
        tree = BinarySearchTree()
        for value in [8, 4, 10, 2, 6, 3, 7]:
            tree.add(value)
        actual_output = tree.width_traverse()
        self.assertEqual(actual_output[1], 8)
        self.assertEqual(actual_output[2], (4, 10))
        self.assertEqual(actual_output[3], (2, 6))
        self.assertEqual(actual_output[4], (3, 7))

    def test_call_width_traverse_of_empty_tree_raised_error(self):
        """
        Create an empty Binary Search Tree.
        Test that width_traverse method raises EmptyTreeError.
        """
        tree = BinarySearchTree()
        self.assertRaises(EmptyTreeError, tree.width_traverse)

    def test_remove_node_with_no_children(self):
        """
        Create a Binary Search Tree with 7 elements.
        Test that remove_node method deletes node with no children
        """
        tree = BinarySearchTree()
        for value in [8, 4, 10, 2, 6, 3, 7]:
            tree.add(value)
        tree.remove_node(3)
        self.assertEqual(tree.find(3), False)

    def test_remove_node_with_one_child(self):
        """
        Create a Binary Search Tree with 7 elements.
        Test that remove_node method deletes node and replaces it with its child
        """
        tree = BinarySearchTree()
        for value in [8, 4, 10, 2, 6, 3, 7]:
            tree.add(value)
        tree.remove_node(2)
        self.assertEqual(tree.find(2), False)
        self.assertEqual(tree.width_traverse()[3], (3, 6))

    def test_remove_node_with_two_children(self):
        """
        Create a Binary Search Tree with 7 elements.
        Test that remove_node method deletes node with two children and replaces it with its biggest child
        """
        tree = BinarySearchTree()
        for value in [8, 4, 10, 2, 6, 3, 7]:
            tree.add(value)
        tree.remove_node(4)
        self.assertEqual(tree.find(4), False)
        self.assertEqual(tree.width_traverse()[2], (6, 10))
