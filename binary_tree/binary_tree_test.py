"""
Tests for BinaryTree class
"""


import unittest

from binary_tree.binary_tree import BinaryTree


class QueueTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Queue
    """

    def test_add_the_root_element(self):
        element = 3
        binary_tree = BinaryTree()
        binary_tree.add(element)
        self.assertEqual(binary_tree.root.value, 3)

    def test_add_three_elements(self):
        element1 = 3
        element2 = 5
        element3 = 6
        binary_tree = BinaryTree()
        binary_tree.add(element1)
        binary_tree.add(element2)
        binary_tree.add(element3)
        self.assertEqual(binary_tree.root.value, element1)
        self.assertEqual(binary_tree.root.right.value, element2)
        self.assertEqual(binary_tree.root.right.right.value, element3)

    def test_add_three_diff_elements(self):
        element1 = 3
        element2 = 5
        element3 = 2
        binary_tree = BinaryTree()
        binary_tree.add(element1)
        binary_tree.add(element2)
        binary_tree.add(element3)
        self.assertEqual(binary_tree.root.value, element1)
        self.assertEqual(binary_tree.root.right.value, element2)
        self.assertEqual(binary_tree.root.left.value, element3)

    def test_find_element_root(self):
        element = 3
        binary_tree = BinaryTree()
        binary_tree.add(element)
        self.assertEqual(binary_tree.find(element), 3)

    def test_find_third_elements(self):
        element1 = 3
        element2 = 5
        element3 = 6
        binary_tree = BinaryTree()
        binary_tree.add(element1)
        binary_tree.add(element2)
        binary_tree.add(element3)
        self.assertEqual(binary_tree.find(5), 5)

    def test_find_not_existing_element(self):
        element1 = 3
        element2 = 5
        element3 = 6
        binary_tree = BinaryTree()
        binary_tree.add(element1)
        binary_tree.add(element2)
        binary_tree.add(element3)
        self.assertRaises(ValueError, binary_tree.find, 7)

    def test_remove_root(self):
        element = 3
        binary_tree = BinaryTree()
        binary_tree.add(element)
        binary_tree.remove(element)
        self.assertEqual(binary_tree.root, None)

    def test_remove_third_element(self):
        element1 = 3
        element2 = 2
        element3 = 1
        binary_tree = BinaryTree()
        binary_tree.add(element1)
        binary_tree.add(element2)
        binary_tree.add(element3)
        binary_tree.remove(element3)
        self.assertEqual(binary_tree.root.left.value, element2)
        self.assertEqual(binary_tree.root.left.left, None)

    def test_remove_not_existing_element(self):
        element1 = 3
        element2 = 2
        element3 = 1
        binary_tree = BinaryTree()
        binary_tree.add(element1)
        binary_tree.add(element2)
        binary_tree.add(element3)
        self.assertRaises(ValueError, binary_tree.remove, 5)

    def test_get_height_empty(self):
        binary_tree = BinaryTree()
        self.assertEqual(binary_tree.get_height(), 0)

    def test_get_height_easy(self):
        element1 = 3
        element2 = 2
        element3 = 1
        binary_tree = BinaryTree()
        binary_tree.add(element1)
        binary_tree.add(element2)
        binary_tree.add(element3)
        self.assertEqual(binary_tree.get_height(),3)

    def test_get_height_hard(self):
        element1 = 3
        element2 = 5
        element3 = 2
        element4 = 11
        binary_tree = BinaryTree()
        binary_tree.add(element1)
        binary_tree.add(element2)
        binary_tree.add(element3)
        binary_tree.add(element4)
        self.assertEqual(binary_tree.get_height(), 3)

    def test_all_tree(self):
        element1 = 8
        element2 = 10
        element3 = 3
        element4 = 1
        element5 = 6
        element6 = 14
        element7 = 4
        element8 = 7
        list_of_elements = [8,10,3,1,6,14,4,7]
        binary_tree = BinaryTree()
        for element in list_of_elements:
            binary_tree.add(element)
        self.assertEqual(binary_tree.root.value, element1)
        self.assertEqual(binary_tree.root.right.value, element2)
        self.assertEqual(binary_tree.root.left.value, element3)
        self.assertEqual(binary_tree.root.left.left.value, element4)
        self.assertEqual(binary_tree.root.left.right.value, element5)
        self.assertEqual(binary_tree.root.right.right.value, element6)
        self.assertEqual(binary_tree.root.left.right.left.value, element7)
        self.assertEqual(binary_tree.root.left.right.right.value, element8)
        for element in list_of_elements:
            self.assertEqual(binary_tree.find(element), element)
        self.assertEqual(binary_tree.get_height(), 4)
        binary_tree.remove(element5)
        self.assertEqual(binary_tree.root.left.right, None)
        self.assertEqual(binary_tree.get_height(), 3)
