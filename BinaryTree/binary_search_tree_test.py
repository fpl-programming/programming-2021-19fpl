"""
Programming for linguists

Tests for BinarySearchTree class.
"""

import io
import unittest
import unittest.mock

from BinaryTree.binary_search_tree import BinarySearchTree


class TestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of BinarySearchTree
    """

    def test_new_tree_is_empty(self):
        """
        Create an empty BinarySearchTree.
        Test that its max height is 0.
        """
        tree = BinarySearchTree()
        self.assertTrue(tree.is_empty())
        self.assertEqual(tree.get_max_height(), 0)

    def test_max_height(self):
        """
        Add elements to BinarySearchTree.
        Test that its max height is correct.
        """
        tree = BinarySearchTree()
        tree.add(1)
        tree.add(2)
        tree.add(3)
        tree.add(4)
        self.assertEqual(tree.get_max_height(), 4)

    def test_add_one_element(self):
        """
        Add element to BinarySearchTree.
        Test that max height is 1.
        Check that tree is not empty.
        """
        tree = BinarySearchTree()
        tree.add(1)
        self.assertFalse(tree.is_empty())
        self.assertEqual(tree.get_max_height(), 1)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_add_existing_element(self, mock_stdout):
        """
        Add element to BinarySearchTree that is already in.
        Check that max height did not change.
        Check that message is printed.
        """
        tree = BinarySearchTree()
        tree.add(1)
        tree.add(1)
        self.assertEqual(tree.get_max_height(), 1)
        self.assertEqual(mock_stdout.getvalue(), '1 is already in the tree\n')

    def test_add_not_number(self):
        """
        Add not numeric element to BinarySearchTree
        Check that ValueError is raised
        """
        tree = BinarySearchTree()
        for element in (None, 'n', (), []):
            self.assertRaises(ValueError, tree.add, element)

    def test_find_elements(self):
        """
        Add elements to BinarySearchTree.
        Test that elements an be found.
        """
        tree = BinarySearchTree()
        for element in (1, 10, 12, 5, 8):
            tree.add(element)
            self.assertEqual(tree.find(element).root, element)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_find_not_existing_elements(self, mock_stdout):
        """
        Add elements to BinarySearchTree.
        Test that not existing elements are not found.
        Check that message is printed.
        """
        tree = BinarySearchTree()
        tree.add(5)
        tree.add(6)
        tree.add(7)
        self.assertIsNone(tree.find(15))
        self.assertEqual(mock_stdout.getvalue(), 'Not found\n')

    def test_find_not_number(self):
        """
        Try to find not numeric element in BinarySearchTree
        Check that ValueError is raised
        """
        tree = BinarySearchTree()
        for element in (None, 'n', (), []):
            self.assertRaises(ValueError, tree.find, element)

    def test_remove_element(self):
        """
        Add elements to BinarySearchTree.
        Test that elements can be removed.
        Check that after removal they cannot be found.
        """
        tree = BinarySearchTree()
        tree.add(6)
        tree.add(5)
        tree.remove(5)
        self.assertIsNone(tree.find(5))

    def test_remove_root(self):
        """
        Add an element to BinarySearchTree.
        Test that root can be removed.
        Check that after root removal the tree is empty.
        """
        tree = BinarySearchTree()
        tree.add(5)
        tree.remove(5)
        self.assertIsNone(tree.find(5))
        self.assertTrue(tree.is_empty())

    def test_remove_whole_brunch(self):
        """
        Add elements to BinarySearchTree.
        Test that after not-final node removal all later nodes in the brunch are also removed.
        """
        tree = BinarySearchTree()
        tree.add(5)
        tree.add(6)
        tree.add(7)
        tree.remove(6)
        self.assertIsNone(tree.find(6))
        self.assertIsNone(tree.find(7))

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_remove_not_existing_element(self, mock_stdout):
        """
        Add elements to BinarySearchTree.
        Test that a message is printed when trying to remove not existing element.
        """
        tree = BinarySearchTree()
        tree.add(5)
        tree.add(6)
        self.assertIsNone(tree.remove(15))
        self.assertEqual(mock_stdout.getvalue(), '15 is not in the tree\n')

    def test_remove_not_number(self):
        """
        Try to remove not numeric element.
        Check that ValueError is raised.
        """
        tree = BinarySearchTree()
        for element in (None, 'n', (), []):
            self.assertRaises(ValueError, tree.remove, element)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_look_dfs(self, mock_stdout):
        """
        Add elements to BinarySearchTree.
        Test that looking_dfs prints found elements in right order.
        """
        tree = BinarySearchTree()
        tree.add(3)
        tree.add(2)
        tree.add(4)
        tree.add(6)
        tree.add(1)
        tree.look_dfs()
        self.assertEqual(mock_stdout.getvalue(), '3 2 1 4 6 \n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_look_dfs_empty_tree(self, mock_stdout):
        """
        Test that a message is printed when trying to look through empty tree.
        """
        tree = BinarySearchTree()
        tree.look_dfs()
        self.assertEqual(mock_stdout.getvalue(), 'The tree is empty\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_look_dfs_only_root(self, mock_stdout):
        """
        Test that a root is printed when trying to look through tree which contains only root.
        """
        tree = BinarySearchTree()
        tree.add(1)
        tree.look_dfs()
        self.assertEqual(mock_stdout.getvalue(), '1 \n')
