"""
Programming for linguists

Tests for BinarySearchTree class.
"""

import unittest

from binary_search.binary_search import BinarySearchTree


class BinarySearchTreeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Queue
    """

    def test_binary_search_tree_add_root(self):
        tree = BinarySearchTree()
        tree.add(8)
        self.assertEqual(tree.get_root(), 8)
        self.assertEqual(tree.find(8).left_node, None)
        self.assertEqual(tree.find(8).right_node, None)

    def test_add_more(self):
        tree = BinarySearchTree(root=8)
        for elem in [6, 9, 5, 7]:
            tree.add(elem)
            self.assertEqual(tree.find(elem).root, elem)

    def test_add_existing(self):
        tree = BinarySearchTree(root=8)
        tree.add(6)
        self.assertIsInstance(tree.add(6), str)

    def test_binary_search_tree_find(self):
        tree = BinarySearchTree(root=8)
        tree.add(6)
        self.assertEqual(tree.find(6).root, 6)
        self.assertEqual(tree.find(8).left_node.root, 6)

    def test_find_all(self):
        tree = BinarySearchTree(root=8)
        for elem in [4, 2, 3, 6, 1, 10, 7]:
            tree.add(elem)
        node_four = tree.find(4)
        self.assertEqual(node_four.left_node.root, 2)
        self.assertEqual(node_four.right_node.root, 6)
        node_two = tree.find(2)
        self.assertEqual(node_two.left_node.root, 1)
        self.assertEqual(node_two.right_node.root, 3)
        self.assertEqual(tree.find(8).right_node.root, 10)

    def test_find_not_existing(self):
        tree = BinarySearchTree(root=8)
        tree.add(4)
        self.assertEqual(tree.find(6).root, None)

    def test_remove_leaf(self):
        tree = BinarySearchTree(root=8)
        tree.add(10)
        tree.remove(10)
        self.assertEqual(tree.find(10).root, None)

    def test_remove_branch(self):
        tree = BinarySearchTree(root=8)
        for elem in [6, 9, 5, 7]:
            tree.add(elem)
        tree.remove(6)
        for el in [6, 5, 7]:
            self.assertEqual(tree.find(el).root, None)
        self.assertEqual(tree.find(9).root, 9)

    def test_remove_root(self):
        tree = BinarySearchTree(root=8)
        for elem in [6, 9, 5, 7]:
            tree.add(elem)
        tree.remove(8)
        for el in [6, 9, 7]:
            self.assertEqual(tree.find(el).root, None)

    def test_remove_not_existing(self):
        tree = BinarySearchTree(root=8)
        tree.add(10)
        self.assertIsInstance(tree.remove(9), str)

    def test_get_root_no_initial(self):
        tree = BinarySearchTree()
        tree.add(7)
        self.assertEqual(tree.get_root(), 7)

    def test_get_root_initial(self):
        tree = BinarySearchTree(root=8)
        self.assertEqual(tree.get_root(), 8)

    def test_get_root_after_removal(self):
        tree = BinarySearchTree(root=7)
        tree.remove(7)
        tree.add(9)
        self.assertEqual(tree.get_root(), 9)

    def test_end_to_end(self):
        pass

    '''
    def test_binary_search_tree_print(self):
        tree = BinarySearchTree(root=8)
        tree.add(6)
        self.assertEqual(tree.__str__(), '8 6')
    '''
