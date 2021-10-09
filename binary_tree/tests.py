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

    def test_raise_type_error(self):
        """
        Create a Node with no integer attribute
        Test that creation of Node raises Type error
        """
        parameters = ['123', [], (), {}, 2.5, True]
        for parameter in parameters:
            self.assertRaises(TypeError, Node, parameter)

    def test_saving_none_values(self):
        """
        Create a Node
        Test that left_node, right_node, value are None
        """
        node = Node(2)
        self.assertEqual(node.left_node, None)
        self.assertEqual(node.right_node, None)
        self.assertEqual(node.value, None)

    def test_root_attribute(self):
        """
        Create a Node with an integer parameter
        Test that root is equal to parameter
        """
        node = Node(1)
        self.assertEqual(node.root, 1)


class BinarySearchingTreeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Binary Searching Tree
    """

    def test_raise_creation_type_error(self):
        """
        Create a Binary Searching Tree with no integer or None attribute
        Test that creation of Tree raises Type error
        """
        parameters = ['123', [], (), {}, 2.5, True]
        for parameter in parameters:
            self.assertRaises(TypeError, BSTree, parameter)

    def test_tree_without_root_creation(self):
        """
        Create a Binary Searching Tree with None attribute
        Test that tree_root is None
        """
        tree = BSTree(None)
        self.assertEqual(tree.tree_root, None)

    def test_tree_with_root_creation(self):
        """
        Create a Binary Searching Tree with integer attribute
        Test that tree_root is Node object with integer attribute root
        """
        tree = BSTree(5)
        self.assertEqual(tree.tree_root.root, Node(5).root)

    def test_raise_adding_type_error(self):  # add
        """
        Add non integer attribute to Tree
        Test that adding raises Type error
        """
        tree = BSTree()
        parameters = ['123', [], (), {}, 2.5, True]
        for parameter in parameters:
            self.assertRaises(TypeError, tree.add, parameter)

    def test_add_node(self):   # add
        """
        Add a node to Tree
        Test that node is in Tree
        """
        tree = BSTree()
        tree.add(3)
        self.assertEqual(tree.find(3).root, Node(3).root)
        self.assertEqual(isinstance(tree.find(3), Node), isinstance(Node(3), Node))

    def test_root_equal_to_element(self):   # add
        """
        Add a node to empty Tree
        Test that tree_root is equal to node
        """
        tree = BSTree()
        tree.add(8)
        self.assertEqual(tree.tree_root.root, 8)

    def test_raise_removing_type_error(self):  # remove
        """
        Remove method gets non integer parameter
        Test that removing raises Type Error
        """
        tree = BSTree()
        parameters = ['123', [], (), {}, 2.5, True]
        for parameter in parameters:
            self.assertRaises(TypeError, tree.remove, parameter)

    def test_remove_node(self):  # remove
        """
        Remove node from Tree
        Test that Tree has no such node
        """
        tree = BSTree(3)
        tree.add(5)
        tree.remove(5)
        self.assertFalse(tree.find(5))

    def test_remove_not_existed_node(self):  # remove
        """
        Remove not existed node from Tree
        Test that remove method returns False
        """
        tree = BSTree(1)
        tree.add(5)
        tree.add(3)
        self.assertRaises(ValueError, tree.remove, 4)

    def test_raise_finding_type_error(self):  # find
        """
        Find method gets non integer parameter
        Test that finding raises Type Error
        """
        tree = BSTree()
        parameters = ['123', [], (), {}, 2.5, True]
        for parameter in parameters:
            self.assertRaises(TypeError, tree.find, parameter)

    def test_find_existing_node(self):  # find
        """
        Find existing node in Tree
        Test that method returns node
        """
        tree = BSTree(1)
        tree.add(5)
        self.assertEqual(tree.find(5).root, Node(5).root)
        self.assertEqual(isinstance(tree.find(5), Node), isinstance(Node(5), Node))

    def test_find_non_existing_node(self):  # find
        """
        Find non existing node in Tree
        Test that method returns False
        """
        tree = BSTree(8)
        tree.add(5)
        tree.add(3)
        tree.remove(5)
        self.assertFalse(tree.find(5))

    def test_raise_depth_type_error(self):  # depth
        """
        Depth method gets neither integer, nor None, nor Node parameter
        Test that method raises Type Error
        """
        tree = BSTree()
        parameters = ['123', [], (), {}, 2.5, True]
        for parameter in parameters:
            self.assertRaises(TypeError, tree.depth, parameter)

    def test_get_tree_depth(self):  # depth
        """
        Get depth of the Tree
        Test that method returns number of levels
        """
        tree = BSTree()
        tree.add(8)
        tree.add(4)
        tree.add(3)
        self.assertEqual(tree.depth(8), 3)

    def test_get_non_existing_tree(self):  # depth
        """
        Get depth of non-existing Tree
        Test that method returns Value Error
        """
        tree = BSTree()
        tree.add(8)
        tree.add(4)
        tree.add(3)
        self.assertRaises(ValueError, tree.depth, 1)
