"""
Programming for linguists

Tests for SQueue class.
"""

import unittest

from queue_.squeue import SQueue


class SQueueTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the stack-based implementation of Queue
    """

    def test_new_queue_stack_is_empty(self):
        """
        Create an empty SQueue.
        Test that its size is 0.
        """
        queue = SQueue()

        self.assertTrue(queue.empty())
        self.assertEqual(queue.size(), 0)

    def test_get_queue_stack_element(self):
        """
        Get an element from a SQueue.
        Test that it is 1.
        """
        data = (1, 2, 3, 4)
        queue = SQueue(data)

        self.assertEqual(queue.get(), data[-1])

    def test_new_queue_stack_from_tuple(self):
        """
        Create a SQueue from an iterable object.
        Check that the size of queue_ equals to the size of the given tuple.
        """
        data = (1, 2, 3, 4)
        queue = SQueue(data)

        self.assertFalse(queue.empty())
        self.assertEqual(queue.size(), len(data))

        for value in data[::-1]:
            test_value = queue.get()
            self.assertEqual(test_value, value)

        self.assertEqual(queue.size(), 0)
        self.assertTrue(queue.empty())

    def test_new_queue_stack_from_list(self):
        """
        Create a SQueue from a list.
        Check that the size of queue equals to the size of the queue.
        Check that the top element of queue equals to the latest element of the list.
        """
        data = [1, 3, 5, 7, 2, 4]
        queue = SQueue(data)

        self.assertFalse(queue.empty())
        self.assertEqual(queue.size(), len(data))
        self.assertEqual(queue.top(), data[-1])

    def test_new_queue_stack_from_generator(self):
        """
        Create a SQueue from a generator.
        Test that its size equals to the number provided in the generator.
        """
        queue = SQueue(range(10))

        self.assertFalse(queue.empty())
        self.assertEqual(queue.size(), 10)
        self.assertEqual(queue.top(), 9)

    def test_put_queue_stack_element(self):
        """
        Put an element in SQueue.
        Test that its size is 1.
        """
        queue = SQueue()
        queue.put(1)

        self.assertFalse(queue.empty())
        self.assertEqual(queue.size(), 1)
        self.assertEqual(queue.top(), 1)

    def test_call_get_of_empty_queue_stack_raised_error(self):
        """
        Create an empty SQueue.
        Test that call of get function raises Assertion error
        """
        queue = SQueue()
        self.assertRaises(IndexError, queue.get)

    def test_queue_stack_capacity(self):
        """
        Create an empty SQueue and SQueue with another capacity.
        Test that function capacity returns correct data.
        """
        queue = SQueue()
        self.assertEqual(50, queue.capacity())

        queue_new = SQueue(capacity=25)
        self.assertEqual(25, queue_new.capacity())

    def test_queue_stack_capacity_wrong_type(self):
        """
        Create an empty SQueue, then SQueue with another capacity.
        Test that function capacity returns correct data.
        """
        bad_inputs = [4, '100', {}, float("inf")]

        for item in bad_inputs:
            self.assertRaises(TypeError, SQueue.__init__, data=[], capacity=item)

    def test_queue_stack_full_ideal(self):
        """
        Create SQueue and fill the capacity.
        Test that at first the full function returns False, then True.
        """
        queue = SQueue(capacity=100)
        self.assertFalse(queue.full())

        for element in range(100, 0, -1):
            queue.put(element)

        self.assertTrue(queue.full())

    def test_put_overcapacity(self):
        """
        Create a full SQueue and put one more element.
        Test that call of put function raises Assertion error
        """
        queue = SQueue([2, 3, 4, 5, 6, 7], 6)

        self.assertRaises(IndexError, queue.put, 1)
