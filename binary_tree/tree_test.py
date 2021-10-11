"""
Binary tree testing module
"""

import unittest
from binary_tree.main import Tree


class TreeUnitTestCase(unittest.TestCase):
    """
    Binary tree test case
    """

    def test_insert_increase_sequence(self):
        """
        inserting increasing values
        """
        tree = Tree()
        for i in range(100):
            tree.insert(i)

        self.assertEqual(tree.height(), 100)

    def test_insert_decrease_sequence(self):
        """
        inserting decreasing test
        """
        tree = Tree()
        data = list(range(100))
        data.reverse()
        for i in data:
            tree.insert(i)

        self.assertEqual(tree.height(), 100)

    def test_insert_negative(self):
        """
        inserting negative test
        """
        tree = Tree()
        for i in range(100):
            tree.insert(i)
        self.assertRaises(IndexError, tree.erase, 1000)

    def test_erase(self):
        """
        positive erase test
        """
        tree = Tree()
        tree.insert(100)
        tree.insert(150)
        tree.insert(50)
        tree.erase(50)
        self.assertEqual(tree.width(), 1)

    def test_erase_negative(self):
        """
        negative erase test
        """
        tree = Tree()
        for i in range(100):
            tree.insert(i)
        tree.erase(10)
        self.assertRaises(IndexError, tree.erase, 10)

    def test_find(self):
        """
        find ent-to-end test
        """
        tree = Tree()
        data = list(range(100))
        for i in range(1, 100):
            tree.insert(i)
        data.reverse()
        for i in data:
            tree.insert(i)
        self.assertTrue(tree.find(1))

    def test_width_greater_one(self):
        """
        width end-to-end test
        """
        tree = Tree()
        tree.insert(100)
        tree.insert(150)
        tree.insert(50)
        tree.insert(25)
        tree.insert(75)
        tree.insert(125)
        tree.insert(175)
        self.assertEqual(tree.width(), 4)

    def test_width_eight(self):
        """
        another width test
        """
        tree = Tree()
        for element in [100, 150, 50, 25, 75, 125, 175, 10, 30, 60, 80, 120, 130, 170, 180]:
            tree.insert(element)
        self.assertEqual(tree.width(), 8)

    def test_lot_insert_erase(self):
        """
        erase stress test
        """
        tree = Tree()
        for i in range(100):
            tree.insert(i)
        for i in range(100):
            tree.erase(i)
        self.assertEqual(0, tree.get_size())

    def test_wrong_input(self):
        """
        incorrect value input test
        """
        tree = Tree()
        bad_input = ["None", 1.2345, [], {}, None]
        for val in bad_input:
            self.assertRaises(ValueError, tree.insert, val)

    def test_sort_array(self):
        """
        creates unsorted array
        traverses its elements for dfs
        gets unsorted array
        compares two unsorted arrays
        """
        tree = Tree()
        tree_list = [1, 15, 12, 57, -13, 0]
        four_list = []
        for element in tree_list:
            tree.insert(element)
        tree.dfs(four_list.append)
        tree_list.sort()
        self.assertEqual(tree_list, four_list)

    def test_sum_with_traversal(self):
        """
        tests sum with dfs
        """
        tree = Tree()
        tree_list = [1, 3, 5, -1, -5]
        summary = 0

        def sum_elements(elementis):
            nonlocal summary
            summary += elementis
        for element in tree_list:
            tree.insert(element)
        tree.dfs(sum_elements)
        self.assertEqual(summary, 3)

    def test_factorial_with_traversal(self):
        """
        tests factorial via dfs
        """
        tree = Tree()
        factorial = 1
        for i in range(1, 6):
            tree.insert(i)

        def multiply(elementus):
            nonlocal factorial
            factorial *= elementus
        tree.dfs(multiply)
        self.assertEqual(factorial, 120)
