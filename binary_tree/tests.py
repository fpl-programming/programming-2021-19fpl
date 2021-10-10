"""
Programming for linguists

Tests for BinarySearchTree class.
"""

import unittest

from binary_tree.start import TreeNode
from binary_tree.start import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of BinarySearchTree
    """


    def set_up_2(self):
        """
        Put elements in the tree
        """
        binary_tree = BinarySearchTree()
        binary_tree.put(20)
        binary_tree.put(10)
        binary_tree.put(8)
        binary_tree.put(18)
        binary_tree.put(25)
        binary_tree.put(100)
        binary_tree.put(5)
        return binary_tree

    def test_create_node(self):
        """
        Check the node is created
        """
        tree_node = TreeNode(25)
        self.assertEqual(tree_node.val, 25)

    def test_create_tree(self):
        """
        Check the tree is created
        """
        binary_tree = BinarySearchTree()
        binary_tree.put(20)
        self.assertEqual(binary_tree.root.val, 20)

    def test_has_nodes(self):
        """
        Check the tree has nodes
        """
        binary_tree = self.set_up_2()

        self.assertEqual(binary_tree.root.val, 20)
        self.assertEqual(binary_tree.root.left.val, 10)
        self.assertEqual(binary_tree.root.left.left.val, 8)
        self.assertEqual(binary_tree.root.left.left.left.val, 5)
        self.assertEqual(binary_tree.root.left.right.val, 18)
        self.assertEqual(binary_tree.root.right.val, 25)
        self.assertEqual(binary_tree.root.right.right.val, 100)

    def test_delete_leaves(self):
        """
        Check if a node is deleted in the tree
        Case 1: delete a leaf
        """
        binary_tree = self.set_up_2()

        binary_tree.delete(5)
        self.assertTrue(binary_tree.contains(20))
        self.assertTrue(binary_tree.contains(10))
        self.assertTrue(binary_tree.contains(8))
        self.assertTrue(binary_tree.contains(18))
        self.assertTrue(binary_tree.contains(25))
        self.assertTrue(binary_tree.contains(100))

        self.assertTrue(not binary_tree.contains(5))
        self.assertFalse(binary_tree.contains(5))

    def test_delete_one_child(self):
        """
        Check if a node is deleted in the tree
        Case 2: delete one child
        """
        binary_tree = self.set_up_2()

        binary_tree.delete(10)
        self.assertTrue(binary_tree.contains(20))
        self.assertTrue(binary_tree.contains(25))
        self.assertTrue(binary_tree.contains(8))
        self.assertTrue(binary_tree.contains(18))
        self.assertTrue(binary_tree.contains(5))
        self.assertTrue(binary_tree.contains(100))

        self.assertTrue(not binary_tree.contains(10))
        self.assertFalse(binary_tree.contains(10))

    def test_delete_two_children(self):
        """
        Check if a node is deleted in the tree
        Case 3: delete two children
        """
        binary_tree = self.set_up_2()

        binary_tree.delete(8)
        self.assertTrue(binary_tree.contains(20))
        self.assertTrue(binary_tree.contains(10))
        self.assertTrue(binary_tree.contains(25))
        self.assertTrue(binary_tree.contains(18))
        self.assertTrue(binary_tree.contains(5))
        self.assertTrue(binary_tree.contains(100))

        self.assertTrue(not binary_tree.contains(8))
        self.assertFalse(binary_tree.contains(8))

    def test_find_node(self):
        """
        Check if we get node that we want to get
        """
        binary_tree = self.set_up_2()
        self.assertEqual(binary_tree.get(5), 5)
        self.assertEqual(binary_tree.get(1), None)
        self.assertEqual(binary_tree.get(100), 100)
        self.assertEqual(binary_tree.get(20), 20)

    def test_check_height(self):
        """
        Check height
        """
        binary_tree = self.set_up_2()
        height = binary_tree.height()
        self.assertNotEqual(height, 3)
        self.assertEqual(height, 4)
        self.assertNotEqual(height, 5)


if __name__ == "__main__":
    unittest.main()
