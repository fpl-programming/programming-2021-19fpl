"""

Tests for the Stack class.
"""

import unittest

from stack.stack import Stack


class StackTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Stack
    """

    def test_new_stack_is_empty(self):
        """
        Create an empty Stack.
        Test that its size is 0.
        """
        stack = Stack()
        self.assertTrue(stack.empty())
        self.assertEqual(stack.size(), 0)

    def test_new_stack_from_list(self):
        """
        Create a Stack from a list.
        Check that the size of stack equals to the size of the list.
        Check that the top element of stack equals to the latest element of the list.
        """
        data_to_stack = [1, 3, 5, 7, 2, 4]
        stack = Stack(data_to_stack)
        self.assertFalse(stack.empty())
        self.assertEqual(stack.size(), len(data_to_stack))
        self.assertEqual(stack.top(), data_to_stack[-1])

    def test_new_stack_from_generator(self):
        """
        Create a Stack from a generator.
        Test that its size equals to the number provided in the generator.
        """
        stack = Stack(range(10))
        self.assertFalse(stack.empty())
        self.assertEqual(stack.size(), 10)
        self.assertEqual(stack.top(), 9)

    def test_push_element(self):
        """
        Push an element in stack.
        Test that its size is 1.
        """
        stack = Stack()
        stack.push(None)
        self.assertFalse(stack.empty())
        self.assertEqual(stack.size(), 1)

    def test_push_sequence_of_elements(self):
        """
        Push a sequence of elements in stack.
        Test that its size equals to the length of the given sequence.
        Pop all elements from stack and check reversed order.
        """
        stack = Stack()
        elements = (1, 2, "string", None, 0, Stack())
        for element in elements:
            stack.push(element)
        self.assertEqual(stack.size(), len(elements))
        for index, element in enumerate(reversed(elements)):
            top = stack.top()
            self.assertEqual(top, element)
            stack.pop()
            self.assertEqual(stack.size(), len(elements) - index - 1)
        self.assertTrue(stack.empty())

    def test_call_top_of_empty_stack_raised_error(self):
        """
        Create an empty Stack.
        Test that call of top function raises Value error
        """
        stack = Stack()
        self.assertRaises(ValueError, stack.top)

    def test_call_pop_of_empty_stack_raised_error(self):
        """
        Create an empty Stack.
        Test that call of pop function raises Value error
        """
        stack = Stack()
        self.assertRaises(ValueError, stack.pop)

    def test_push_and_pop_elements(self):
        """
        Create an empty Stack.
        Push elements from the list sequentially in the stack.
        Pop the element and test that the size of stack is 0
        """
        stack = Stack()
        elements = [1, 2.0, "string", None, TypeError, False, Stack()]
        for element in elements:
            stack.push(element)
            stack.pop()
            self.assertEqual(stack.size(), 0)

    def test_new_stack_from_string_and_pop(self):
        """
        Create Stack from a string.
        Pop an element from the stack.
        Test if the penultimate symbol of the string equals to the top element of the stack.
        """
        data_to_stack = "stack"
        stack = Stack(data_to_stack)
        stack.pop()
        self.assertEqual(stack.top(), data_to_stack[-2])

    def test_push_empty_data_types(self):
        """
        Create an empty Stack.
        Push empty data types sequentially in the stack.
        Test that the stack is not empty
        """
        empty_data_types = [[], (), {}, '', ""]
        stack = Stack()
        for element in empty_data_types:
            stack.push(element)
            self.assertFalse(stack.empty())
            stack.pop()

    def test_new_stack_from_empty_data_types(self):
        """
        Create Stacks from empty data types.
        Test that all the stacks are empty
        """
        empty_data_types = [[], (), {}, '', ""]
        for element in empty_data_types:
            stack = Stack(element)
            self.assertTrue(stack.empty())
