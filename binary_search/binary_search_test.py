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
        """
        Create an empty BinarySearchTree and add an element.
        Test that the element becomes root.
        """
        tree = BinarySearchTree()
        tree.add(8)
        self.assertEqual(tree.get_root(), 8)
        self.assertEqual(tree.find(8).left_node, None)
        self.assertEqual(tree.find(8).right_node, None)

    def test_add_more(self):
        """
        Create a BinarySearchTree with root and add some elements.
        Test that all elements added.
        """
        tree = BinarySearchTree(root=8)
        for elem in [6, 9, 5, 7]:
            tree.add(elem)
            self.assertEqual(tree.find(elem).root, elem)

    def test_add_existing(self):
        """
        Create a BinarySearchTree with root and add an element twice.
        Test that it returns a message.
        """
        tree = BinarySearchTree(root=8)
        tree.add(6)
        self.assertRaises(ValueError, tree.add, 6)

    def test_binary_search_tree_find(self):
        """
        Create a BinarySearchTree with root and an element.
        Test that find function finds the element correctly.
        """
        tree = BinarySearchTree(root=8)
        tree.add(6)
        self.assertEqual(tree.find(6).root, 6)
        self.assertEqual(tree.find(8).left_node.root, 6)

    def test_find_all(self):
        """
        Create a BinarySearchTree with root and add many elements.
        Test that all are found correctly.
        """
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
        """
        Create a BinarySearchTree with root.
        Test that find a non-existing element returns Node with nones.
        """
        tree = BinarySearchTree(root=8)
        self.assertEqual(tree.find(6).root, None)

    def test_remove_leaf(self):
        """
        Create a BinarySearchTree with root, add and remove an element.
        Test that element is not found.
        """
        tree = BinarySearchTree(root=8)
        tree.add(10)
        tree.remove(10)
        self.assertEqual(tree.find(10).root, None)

    def test_remove_branch(self):
        """
        Create a BinarySearchTree with root, add elements and remove one.
        Test that you can`t find the other nodes.
        """
        tree = BinarySearchTree(root=8)
        for elem in [6, 9, 5, 7]:
            tree.add(elem)
        tree.remove(6)
        for element in [6, 5, 7]:
            self.assertEqual(tree.find(element).root, None)

    def test_remove_root(self):
        """
        Create a BinarySearchTree with root, add elements and remove root.
        Test that you can`t find any elements.
        """
        tree = BinarySearchTree(root=8)
        for elem in [6, 9, 5, 7]:
            tree.add(elem)
        tree.remove(8)
        for element in [6, 9, 5, 7]:
            self.assertEqual(tree.find(element).root, None)

    def test_remove_not_existing(self):
        """
        Create a BinarySearchTree with root and try to remove non-existing element.
        Test that it returns a message.
        """
        tree = BinarySearchTree(root=8)
        self.assertRaises(ValueError, tree.remove, 9)

    def test_get_root_no_initial(self):
        """
        Create an empty BinarySearchTree and add an element.
        Test that it becomes root.
        """
        tree = BinarySearchTree()
        tree.add(7)
        self.assertEqual(tree.get_root(), 7)

    def test_get_root_initial(self):
        """
        Create a BinarySearchTree with root.
        Test that root returns correctly.
        """
        tree = BinarySearchTree(root=8)
        self.assertEqual(tree.get_root(), 8)

    def test_get_root_after_removal(self):
        """
        Create a BinarySearchTree with root, remove the root and add an element.
        Test that the root is the new element.
        """
        tree = BinarySearchTree(root=7)
        tree.remove(7)
        tree.add(9)
        self.assertEqual(tree.get_root(), 9)

    def test_go_width_traversal(self):
        """
        Create a BinarySearchTree with root, add elements.
        Test that the function can go around tree correctly.
        """
        tree = BinarySearchTree(root=8)
        list_elements = [6, 9, 5, 7, 10, 12]
        for elem in list_elements:
            tree.add(elem)
        result = [element.root for element in tree.go_width_traversal()]
        self.assertEqual(len(result), len(list_elements)+1)

    def test_go_width_traversal_no_elements(self):
        """
        Create an empty BinarySearchTree.
        Test that the function rises error.
        """
        tree = BinarySearchTree()
        self.assertRaises(ValueError, tree.go_width_traversal)

    def test_print_tree(self):
        """
        Create a BinarySearchTree with root, add elements.
        Test that str method divides tree into levels.
        """
        tree = BinarySearchTree(root=8)
        for elem in [6, 9, 5, 7, 10, 12, 3]:
            tree.add(elem)
        result = [elem for elem in str(tree).split('\n') if elem.strip()]
        self.assertEqual(4, len(result))

    def test_end_to_end(self):
        """
        Create a BinarySearchTree with root and all the sequence.
        Test that all functions work fine together.
        """
