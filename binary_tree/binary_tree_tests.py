"""
Tests for BinaryTree
"""

import unittest

from binary_tree.main import BinaryTree, Node


class BinaryTreeTestCase(unittest.TestCase):
    """
    Tests for BinaryTree
    """

    def test_create_node(self):
        """
        Creates a node.
        Tests that correct root, left and right are returned.
        """
        node = Node(5)
        self.assertEqual(node.node, 5)
        self.assertEqual(node.right, None)
        self.assertEqual(node.left, None)

    def test_create_empty_tree(self):
        """
        Tests that tree is empty.
        """
        tree = BinaryTree()
        self.assertEqual(tree.root.node, None)

    def test_add_node_to_empty_tree(self):
        """
        Tests that node is added.
        """
        tree = BinaryTree()
        tree.add_node(8)
        self.assertEqual(tree.search_node(8).left, None)
        self.assertEqual(tree.search_node(8).right, None)

    def test_add_left_and_right(self):
        """
        Tests that nodes are added at right place.
        """
        tree = BinaryTree(8)
        tree.add_node(7)
        tree.add_node(9)
        self.assertEqual(tree.root.left.node, 7)
        self.assertEqual(tree.root.right.node, 9)

    def test_add_deep_nodes(self):
        """
        Tests that deep nodes are added at right place.
        """
        tree = BinaryTree(8)
        for node in [6, 10, 5, 7, 9, 11]:
            tree.add_node(node)
        self.assertEqual(tree.root.left.left.node, 5)
        self.assertEqual(tree.root.left.right.node, 7)
        self.assertEqual(tree.root.right.left.node, 9)
        self.assertEqual(tree.root.right.right.node, 11)

    def test_search_node(self):
        """
        Tests that particular node can be find.
        """
        tree = BinaryTree(8)
        tree.add_node(9)
        self.assertEqual(tree.search_node(8).node, 8)
        self.assertEqual(tree.search_node(9).node, 9)

    def test_search_in_empty_tree(self):
        """
        Tests that the program can handle a search in empty tree.
        """
        tree = BinaryTree()
        self.assertEqual(tree.search_node(10).node, None)

    def test_search_nonexistent_node(self):
        """
        Tests that the program can't find a nonexistent node.
        """
        tree = BinaryTree(8)
        self.assertEqual(tree.search_node(10).node, None)

    def test_delete_node(self):
        """
        Tests that particular node is deleted.
        """
        tree = BinaryTree(8)
        tree.add_node(9)
        self.assertEqual(tree.search_node(9).node, 9)
        tree.delete_node(9)
        self.assertEqual(tree.search_node(9).node, None)

    def test_delete_node_with_descendants(self):
        """
        Tests that descendant nodes are deleted.
        """
        tree = BinaryTree(8)
        for node in [10, 9, 11]:
            tree.add_node(node)
        for node in [10, 9, 11]:
            self.assertEqual(tree.search_node(node).node, node)
        tree.delete_node(10)
        self.assertEqual(tree.search_node(9).node, None)
        self.assertEqual(tree.search_node(11).node, None)

    def test_delete_nonexistent_node(self):
        """
        Tests that the error is raised when trying to delete a nonexistent node.
        """
        tree = BinaryTree(8)
        self.assertRaises(ValueError, tree.delete_node, 10)
