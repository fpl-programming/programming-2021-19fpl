"""
Programming for linguists

Tests for QueueStack class.
"""

import unittest

from queue_.queue_stack import QueueStack


class QueueTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Queue
    """

    def test_new_queue_is_empty(self):
        """
        Create an empty QueueStack.
        Test that its size is 0.
        """
        queue = QueueStack()
        self.assertTrue(queue.empty())
        self.assertEqual(queue.size(), 0)

    def test_get_element(self):
        """
        Get an element from a queue_stack.
        Test that it is 1.
        """
        data = (1, 2, 3, 4)
        queue = QueueStack(data)
        self.assertEqual(queue.get(), data[0])

    def test_new_queue_stack_from_tuple(self):
        """
        Create a QueueStack from an iterable object.
        Check that the size of queue_stack equals to the size of the given tuple.
        """
        data = (1, 2, 3, 4)
        queue = QueueStack(data)
        self.assertEqual(queue.size(), len(data))
        self.assertFalse(queue.empty())
        for value in data:
            test_value = queue.get()
            self.assertEqual(test_value, value)
        self.assertEqual(queue.size(), 0)
        self.assertTrue(queue.empty())

    def test_new_queue_stack_from_list(self):
        """
        Create a QueueStack from a list.
        Check that the size of queue_stack equals to the size of the queue.
        Check that the top element of queue_stack equals to the latest element of the list.
        """
        data = [1, 3, 5, 7, 2, 4]
        queue = QueueStack(data)
        self.assertFalse(queue.empty())
        self.assertEqual(queue.size(), len(data))
        self.assertEqual(queue.top(), data[0])

    def test_new_queue_from_generator(self):
        """
        Create a QueueStack from a generator.
        Test that its size equals to the number provided in the generator.
        """
        queue = QueueStack(range(10))
        self.assertFalse(queue.empty())
        self.assertEqual(queue.size(), 10)
        self.assertEqual(queue.top(), 0)

    def test_put_element(self):
        """
        Put an element in queue_stack.
        Test that its size is 1.
        """
        queue = QueueStack()
        queue.put(1)
        self.assertFalse(queue.empty())
        self.assertEqual(queue.size(), 1)
        self.assertEqual(queue.top(), 1)

    def test_call_get_of_empty_queue_stack_raised_error(self):
        """
        Create an empty QueueStack.
        Test that call of get function raises Assertion error
        """
        queue = QueueStack()
        self.assertRaises(IndexError, queue.get)

    def test_put_out_of_the_size(self):
        """
        Create a QueueStack of certain size. Put more than allowed.
        Test that the ValueError is raised.
        """
        queue = QueueStack([1, 2, 3], 3)
        self.assertRaises(ValueError, queue.put, 4)

    def test_unpassed_size(self):
        """
        Create a QueueStack with a not passed size.
        Test that the ValueError is raised.
        """
        queue = QueueStack([1, 2, 3])
        self.assertEqual(queue.size(), 3)

    def test_put_out_of_the_unpassed_size(self):
        """
        Create a QueueStack with a not passed size. Put more than allowed.
        Test that the ValueError is raised.
        """
        queue = QueueStack([1, 2, 3])
        self.assertRaises(ValueError, queue.put, 4)
