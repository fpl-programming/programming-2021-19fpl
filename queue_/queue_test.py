# pylint: disable=duplicate-code
"""
Programming for linguists

Tests for Queue class.
"""

import unittest

from queue_.queue_ import Queue_, CapacityError


class QueueTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Queue
    """

    def test_new_queue_is_empty(self):
        """
        Create an empty Queue.
        Test that its size is 0.
        """
        queue = Queue_()
        self.assertTrue(queue.empty())
        self.assertEqual(queue.size(), 0)

    def test_get_element(self):
        """
        Get an element from a queue.
        Test that it is 1.
        """
        data = (1, 2, 3, 4)
        queue = Queue_(data)
        self.assertEqual(queue.get(), data[0])

    def test_new_queue_from_tuple(self):
        """
        Create a Queue from an iterable object.
        Check that the size of queue_ equals to the size of the given tuple.
        """
        data = (1, 2, 3, 4)
        queue = Queue_(data)
        self.assertFalse(queue.empty())
        self.assertEqual(queue.size(), len(data))
        for value in data:
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
        queue = Queue_(data)
        self.assertFalse(queue.empty())
        self.assertEqual(queue.size(), len(data))
        self.assertEqual(queue.top(), data[0])

    def test_new_queue_from_generator(self):
        """
        Create a Queue_ from a generator.
        Test that its size equals to the number provided in the generator.
        """
        queue = Queue_(range(10))
        self.assertFalse(queue.empty())
        self.assertEqual(queue.size(), 10)
        self.assertEqual(queue.top(), 0)

    def test_put_element(self):
        """
        Put an element in queue.
        Test that its size is 1.
        """
        queue = Queue_()
        queue.put(1)
        self.assertFalse(queue.empty())
        self.assertEqual(queue.size(), 1)
        self.assertEqual(queue.top(), 1)

    def test_call_get_of_empty_queue_raised_error(self):
        """
        Create an empty Queue.
        Test that call of get function raises Assertion error
        """
        queue = Queue_()
        self.assertRaises(IndexError, queue.get)

    def test_type_capacity_not_int_raised_error(self):
        """
        Test that initialisation of class Queue when capacity is not int raises Type error
        """
        for capacity in ['a', 3.15, {'a': 'a'}, [2]]:
            self.assertRaises(TypeError, Queue_().__init__, None, capacity)

    def test_put_element_in_full_queue_raised_error(self):
        """
        Test that call of put function when queue is full raises Capacity error
        """
        queue = Queue_(range(40), 40)
        self.assertRaises(CapacityError, queue.put, 8)

    def test_initialisation_of_class_queue_when_data_exceeded_capacity_raised_error(self):
        """
        Create a Queue.
        Test that initialisation of class Queue
        when length of data exceeds capacity raises Capacity error
        """
        self.assertRaises(CapacityError, Queue_().__init__, range(41), 40)

    def test_queue_is_full(self):
        """
        Test that call of full function returns False
        when queue is not full and then True when it is full
        """
        queue = Queue_(range(39), 40)
        self.assertFalse(queue.full())
        queue.put(2)
        self.assertTrue(queue.full())
        self.assertEqual(queue.size(), queue.capacity_n)

    def test_capacity(self):
        """
        Test that call of capacity function returns the max size of queue
        """
        queue = Queue_(range(40))
        self.assertEqual(0, queue.capacity())  # queue is infinite
        queue_2 = Queue_(range(40), 50)
        self.assertEqual(50, queue_2.capacity())
