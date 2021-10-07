"""
Programming for linguists

Tests for Binary Searching Tree class.
"""

import unittest

from binary_tree.main import Node, BSTree


class NodeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Node
    """

    def test_new_queue_is_empty(self): # 1. вводят не число (-) 2. записывается число в root (+) 3. проверка что остальные значения None (+)
        """
        Create an empty Queue.
        Test that its size is 0.
        """
        queue = Queue_()
        self.assertTrue(queue.empty())
        self.assertEqual(queue.size(), 0)

