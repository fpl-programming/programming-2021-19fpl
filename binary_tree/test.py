# pylint: disable=W1401
"""
Programming for linguists

Tests for Binary Tree and Node classes.
Tree in tests:
        5
      /   \
     2     7
   /  \   / \
  0   4  6  10
"""

import unittest

from binary_tree import BinaryTree, Node


class BinaryTreeTestCase(unittest.TestCase):
    "This Case of tests checks the functionality of the implementation of Binary tree"

    def test_create_node(self):
        """
        Creates a node.
        Tests that the correct val is returned.
        """
        node = Node(5)
        self.assertEqual(node.value, 5)

    def test_insert_node(self):
        """
        Creates a binary tree.
        Tests that the tree can insert new values.
        """
        tree = BinaryTree()
        for elem in (5, 2, 7, 0, 4, 6, 10):
            self.assertTrue(tree.insert(elem))

    def test_insert_exists_node(self):
        """
        Creates a binary tree.
        Tests that the tree doesn't insert values that already exists in the tree.
        """
        tree = BinaryTree()
        for elem in (5, 2, 7, 0, 4, 6, 10):
            self.assertTrue(tree.insert(elem))
        for elem in (5, 2, 7, 0, 4, 6, 10):
            self.assertFalse(tree.insert(elem))

    def test_insert_non_integer(self):
        """
        Creates a binary tree.
        Tests that the tree can't insert non-integer values.
        """
        tree = BinaryTree()
        for elem in ([], (), None, {}, '', 2.5):
            self.assertRaises(ValueError, tree.insert, elem)

    def test_find_node(self):
        """
        Creates a binary tree.
        Tests that the tree can find inserted value.
        """
        tree = BinaryTree()
        tree.insert(5)
        tree.insert(2)
        self.assertTrue(tree.find(2))

    def test_find_not_exists_node(self):
        """
        Creates a binary tree.
        Tests that the tree can't find value that is not inserted.
        """
        tree = BinaryTree()
        tree.insert(5)
        tree.insert(2)
        self.assertFalse(tree.find(7))

    def test_find_non_integer(self):
        """
        Creates a binary tree.
        Tests that the tree can't find non-integer values.
        """
        tree = BinaryTree()
        for elem in ([], (), None, {}, '', 2.5):
            self.assertRaises(ValueError, tree.find, elem)

    def test_get_height_empty_tree(self):
        """
        Creates a binary tree.
        Tests that height of empty tree equals 0.
        """
        tree = BinaryTree()
        self.assertEqual(tree.get_height(), 0)

    def test_get_height(self):
        """
        Creates a binary tree.
        Tests that height gets properly.
                5
              /   \
             2     7
           /  \   / \
          0   4  6  10
             /
            3
        """
        tree = BinaryTree()
        tree.insert(5)
        self.assertEqual(tree.get_height(), 1)
        tree.insert(2)
        tree.insert(7)
        self.assertEqual(tree.get_height(), 2)
        tree.insert(0)
        tree.insert(4)
        self.assertEqual(tree.get_height(), 3)
        tree.insert(6)
        tree.insert(10)
        self.assertEqual(tree.get_height(), 3)
        tree.insert(3)
        self.assertEqual(tree.get_height(), 4)

    def test_remove_empty(self):
        """
        Creates a binary tree.
        Tests that tree can't remove value from empty tree.
        """
        tree = BinaryTree()
        self.assertFalse(tree.remove(5))

    def test_remove_not_exists(self):
        """
        Creates a binary tree.
        Tests that tree can't remove value that is not in the tree.
        """
        tree = BinaryTree()
        tree.insert(5)
        self.assertFalse(tree.remove(2))

    def test_remove_root(self):
        """
        Creates a binary tree.
        Tests that tree can remove root and new root equals the min value from right child.
        """
        tree = BinaryTree()
        for elem in (5, 2, 7, 0, 4, 6, 10):
            tree.insert(elem)
        tree.remove(5)
        self.assertFalse(tree.find(5))
        self.assertEqual(tree.root.value, 6)

    def test_remove_no_children(self):
        """
        Creates a binary tree.
        Tests that tree can remove node without children.
        """
        tree = BinaryTree()
        for elem in (5, 2, 7, 0, 4, 6, 10):
            tree.insert(elem)
        tree.remove(0)
        self.assertFalse(tree.find(0))

    def test_remove_left_child(self):
        """
        Creates a binary tree.
        Tests that tree can remove node with left child only and new value equals left child.
                5
              /   \
             2     7
           /
          0
        """
        tree = BinaryTree()
        for elem in (5, 2, 7, 0):
            tree.insert(elem)
        tree.remove(2)
        self.assertFalse(tree.find(2))
        self.assertEqual(tree.root.left_child.value, 0)

    def test_remove_right_child(self):
        """
        Creates a binary tree.
        Tests that tree can remove node with right child only and new value equals right child.
                5
              /   \
             2     7
                    \
                    10
        """
        tree = BinaryTree()
        for elem in (5, 2, 7, 10):
            tree.insert(elem)
        tree.remove(7)
        self.assertFalse(tree.find(7))
        self.assertEqual(tree.root.right_child.value, 10)

    def test_remove_two_children(self):
        """
        Creates a binary tree.
        Tests that tree can remove node with two children
        and new node equals the min value from right node's child.
                5
              /   \
             2     7
           /  \   / \
          0   4  6  10
                   /
                  8
        """
        tree = BinaryTree()
        for elem in (5, 2, 7, 0, 4, 6, 10, 8):
            tree.insert(elem)
        tree.remove(7)
        self.assertFalse(tree.find(7))
        self.assertEqual(tree.root.right_child.value, 8)

    def end_to_end_test(self):
        """
        Creates a binary tree.
        Fill tree with values.
        Try to fill value that already exists.
        Get heiht of the tree.
        Find 7. Remove 7. Try to find removed 7.
        Remove nodes one by one. Check that tree equals empty tree.
        """
        tree = BinaryTree()
        for elem in (5, 2, 7, 0, 4, 6, 10):
            self.assertTrue(tree.insert(elem))
        self.assertFalse(tree.insert(elem))

        self.assertEqual(tree.get_height(), 3)

        self.assertTrue(tree.find(7))
        self.assertTrue(tree.remove(7))
        self.assertFalse(tree.find(7))

        for elem in (5, 2, 0, 4, 6, 10):
            self.assertTrue(tree.remove(elem))
        self.assertEqual(tree, BinaryTree())
