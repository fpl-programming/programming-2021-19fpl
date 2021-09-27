"""
Programming for linguists

Tests for QueueFromStack class.
"""

import unittest

from queue_.queue_from_stack import QueueFromStack


class QueueFromStackTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of QueueFromStack class
    """

    def test_queue_to_stack(self):
        """
        Create a Queue.
        Turn it into a stack back.
        Test that call this function again raises Type error
        """
        queue = QueueFromStack([1, 2, 3])
        queue.queue_to_stack()
        self.assertFalse(queue.is_queue)
        self.assertRaises(TypeError, queue.queue_to_stack)

    def test_queue_and_stack_empty(self):
        """
        Create two empty queues.
        Turn one queue into stack back.
        Test that the queue and the stack are empty
        """
        queue_1 = QueueFromStack([])
        queue_2 = QueueFromStack([])
        queue_2.queue_to_stack()
        self.assertTrue(queue_1.empty())
        self.assertTrue(queue_2.empty())

    def test_queue_and_stack_not_empty(self):
        """
        Create two queues from list.
        Turn one queue into stack back.
        Test that the queue and the stack are not empty
        """
        data = [1, 2, 3]
        queue_1 = QueueFromStack(data)
        queue_2 = QueueFromStack(data)
        queue_2.queue_to_stack()
        self.assertFalse(queue_1.empty())
        self.assertFalse(queue_2.empty())

    def test_call_top_of_queue_and_stack(self):
        """
        Create two queues from list.
        Turn one queue into stack back.
        Test that call top function of the queue returns the first element
        and call top function of the stack returns the last element
        """
        data = [1, 2, 3]
        queue_1 = QueueFromStack(data)
        queue_2 = QueueFromStack(data)
        queue_2.queue_to_stack()
        self.assertFalse(queue_2.is_queue)
        self.assertEqual(queue_1.top(), data[0])
        self.assertEqual(queue_2.top(), data[-1])

    def test_call_get_of_empty_queue_and_stack(self):
        """
        Create two empty queues.
        Turn one queue into stack back.
        Test that call get function of empty stack and queue raises Index error
        """
        queue_1 = QueueFromStack([])
        queue_2 = QueueFromStack([])
        queue_2.queue_to_stack()
        self.assertFalse(queue_2.is_queue)
        self.assertRaises(IndexError, queue_1.get)
        self.assertRaises(IndexError, queue_2.get)

    def test_put_element_into_queue_and_stack(self):
        """
        Create two empty queues.
        Turn one queue into stack back.
        Put an element in the stack and in the queue.
        Test that call of top function of both stack and queue returns the element.
        """
        queue_1 = QueueFromStack([])
        queue_2 = QueueFromStack([])
        queue_2.queue_to_stack()
        queue_1.put('a')
        queue_2.put('a')
        self.assertEqual(queue_1.top(), 'a')
        self.assertEqual(queue_2.top(), 'a')
