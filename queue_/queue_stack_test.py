# pylint: disable=duplicate-code
"""
Programming for linguists

Tests for Queue class.
"""

import unittest

from queue_.queue_stack import QueueStack_


class QueueTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Queue
    """

    def test_new_queue_is_empty(self):
        """
        Create an empty Queue.
        Test that its size is 0.
        """
        queue = QueueStack_()
        self.assertTrue(queue.empty())
        self.assertEqual(queue.size(), 0)

    def test_get_element(self):
        """
        Get an element from a queue.
        Test that it is 1.
        """
        data = (1, 2, 3, 4)
        queue = QueueStack_(data)
        self.assertEqual(queue.get(), data[-1])

    def test_new_queue_from_tuple(self):
        """
        Create a Queue from an iterable object.
        Check that the size of queue_ equals to the size of the given tuple.
        """
        data = (1, 2, 3, 4)
        queue = QueueStack_(data)
        self.assertFalse(queue.empty())
        self.assertEqual(queue.size(), len(data))
        for value in data[::-1]:
            test_value = queue.get()
            self.assertEqual(test_value, value)
        self.assertTrue(queue.empty())
        self.assertEqual(queue.size(), 0)

    def test_new_queue_from_list(self):
        """
        Create a Queue from a list.
        Check that the size of queue equals to the size of the queue.
        Check that the top element of queue equals to the latest element of the list.
        """
        data = [1, 3, 5, 7, 2, 4]
        queue = QueueStack_(data)
        self.assertFalse(queue.empty())
        self.assertEqual(queue.size(), len(data))
        self.assertEqual(queue.top(), data[-1])

    def test_new_queue_from_generator(self):
        """
        Create a Queue_ from a generator.
        Test that its size equals to the number provided in the generator.
        """
        queue = QueueStack_(range(10))
        self.assertFalse(queue.empty())
        self.assertEqual(queue.size(), 10)
        self.assertEqual(queue.top(), 9)

    def test_put_element(self):
        """
        Put an element in queue.
        Test that its size is 1.
        """
        queue = QueueStack_()
        queue.put(1)
        self.assertFalse(queue.empty())
        self.assertEqual(queue.size(), 1)
        self.assertEqual(queue.top(), 1)

    def test_call_get_of_empty_queue_raised_error(self):
        """
        Create an empty Queue.
        Test that call of get function raises Assertion error
        """
        queue = QueueStack_()
        self.assertRaises(IndexError, queue.get)

    def test_capacity(self):
        """
        Create an empty Queue, then Queue with another capacity.
        Test that function capacity returns correct data.
        """
        queue = QueueStack_()
        self.assertEqual(50, queue.capacity())
        queue_new = QueueStack_(capacity=10)
        self.assertEqual(10, queue_new.capacity())

    def test_capacity_wrong_type(self):
        """
        Create an empty Queue, then Queue with another capacity.
        Test that function capacity returns correct data.
        """
        bad_inputs = ['1', 0.5, [], False]
        for inp in bad_inputs:
            self.assertRaises(TypeError, QueueStack_.__init__, data=[], capacity=inp)

    def test_full_ideal(self):
        """
        Create Queue and fill the capacity.
        Test that at first the full function returns False, then True.
        """
        queue = QueueStack_(capacity=4)
        self.assertFalse(queue.full())
        for element in [4, 3, 2, 1]:
            queue.put(element)
        self.assertTrue(queue.full())

    def test_put_more_than_capacity(self):
        """
        Create a full Queue and put one more element.
        Test that call of put function raises Assertion error
        """
        queue = QueueStack_([1, 2, 3, 4, 5], 5)
        self.assertRaises(IndexError, queue.put, 0)
