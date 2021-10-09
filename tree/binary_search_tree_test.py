"""
Tests for the Tree class.
"""

import unittest

from binary_search_tree import Tree
from node import Node


class TreeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Tree
    """

    def test_tree_creation(self):
        root = Node(0)
        tree = Tree(root)
        self.assertEqual(tree.root.value, 0)

    def test_tree_creation_incorrect_input(self):
        for root in [0, True, '']:
            self.assertRaises(TypeError, Tree, root)

    def test_add(self):
        root = Node(0)
        right_child = Node(2)
        root.insert_right(right_child)
        new_node_value = 1

        tree = Tree(root)
        tree.add(new_node_value)
        self.assertEqual(tree.root.right.left.value, 1)

    def test_add_existing_element(self):
        root = Node(0)
        tree = Tree(root)
        self.assertRaises(ValueError, tree.add, 0)

    def test_find(self):
        root = Node(0)
        tree = Tree(root)
        tree.add(2)
        tree.add(1)
        for existing in [0, 1, 2]:
            self.assertTrue(tree.find(existing))
        for non_existing in [3, 4, 5]:
            self.assertFalse(tree.find(non_existing))

    def test_find_incorrect_input(self):
        tree = Tree(Node(0))
        for incorrect in [1.0, (), '']:
            self.assertRaises(TypeError, tree.find(incorrect))

    def test_remove(self):
        tree = Tree(Node(0))
        for value in [2, 1, 3, 4, -2, -3, -1]:
            tree.add(value)
        tree.remove(2)
        for removed in [1, 2, 3, 4]:
            self.assertFalse(tree.find(removed))
        for left in [0, -2, -3, -1]:
            self.assertTrue(tree.find(left))

    def test_remove_root_raises_error(self):
        tree = Tree(Node(0))
        for value in [2, 1, 3, 4, -2, -3, -1]:
            tree.add(value)
        self.assertRaises(ValueError, tree.remove, 0)

    def test_get_height(self):
        tree = Tree(Node(0))
        for value in [2, 1, 3, 4, -2, -3, -1]:
            tree.add(value)
        self.assertEqual(3, tree.get_height())

    def test_dfs(self):
        tree = Tree(Node(0))
        values = [2, 1, 3, 4, -2, -3, -1]
        for value in values:
            tree.add(value)
        for value in values:
            self.assertTrue(tree.depth_first_search(value))
            self.assertFalse(tree.depth_first_search(value + 100))

    def test_dfs_incorrect_value(self):
        tree = Tree(Node(0))
        for incorrect_value in ['', None, 10.0, []]:
            self.assertRaises(TypeError, tree.depth_first_search, incorrect_value)

    def test_binary_tree_total(self):

        root = Node(0)
        self.assertEqual(0, root.value)
        self.assertEquals(None, root.left, root.right)

        tree = Tree(root)
        self.assertEqual(tree.get_height(), 0)
        self.assertFalse(all((tree.find(2), tree.depth_first_search(2))))

        tree.add(2)
        self.assertTrue(all((tree.find(2), tree.depth_first_search(2))))
        self.assertEqual(tree.get_height(), 1)
        self.assertEqual(tree.root.right.value, 2)
        self.assertEqual(tree.root.left, None)

        tree.remove(2)
        self.assertEqual(tree.get_height(), 0)
        self.assertFalse(all((tree.find(2), tree.depth_first_search(2))))
