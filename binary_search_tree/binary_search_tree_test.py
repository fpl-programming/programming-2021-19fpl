"""
Programming for linguists

Tests for Node, BinarySearchTree classes.
"""

import unittest

from binary_search_tree.binary_search_tree import Node, BinarySearchTree,\
    EmptyError, DuplicateError, NodeNotFoundError


class NodeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of Node
    """
    def test_new_node_root(self):
        """
        Create a Node.
        Test that its root is given number, left_node and right_node are None.
        """
        node = Node(8)
        self.assertEqual(node.root, 8)
        self.assertIsNone(node.left_node, node.right_node)

    def _test_node_from_not_int_raises_error(self):
        """
        Test that initialisation of class Node when root is not int raises Type error
        """
        data_to_test = [3.75, 'and', [3], {1: 2}, True, None, input, dict]
        for item in data_to_test:
            self.assertRaises(TypeError, Node.__init__, item)


class BinarySearchTreeTestCase(unittest.TestCase):
    """
    This Case of tests checks the functionality of the implementation of BinarySearchTree
    """
    def test_new_tree_is_empty(self):
        """
        Create an empty BinarySearchTree.
        Test that its root is None.
        """
        tree = BinarySearchTree()
        self.assertIsNone(tree.root)

    def test_add_node_as_root(self):
        """
        Create an empty BinarySearchTree.
        Check that add function adds new Node and sets it as root
        """
        tree = BinarySearchTree()
        node = Node(5)
        tree.add(node)
        self.assertEqual(tree.root, node)

    def test_add_node_to_tree(self):
        """
        Create an empty BinarySearchTree.
        Check that add function adds new Node to root as right_node
        """
        tree = BinarySearchTree()
        node_root, node_right = Node(5), Node(7)
        tree.add(node_root)
        tree.add(node_right)
        self.assertEqual(tree.root.right_node, node_right)
        self.assertIsNone(tree.root.left_node)

    def test_add_node_to_tree_with_several_nodes(self):
        """
        Create an empty BinarySearchTree.
        Check that add function adds new Node correctly when there already several Nodes
        """
        tree = BinarySearchTree()
        node_root, node_left, node_left_2, node_right = Node(8), Node(4), Node(2), Node(3)
        tree.add(node_root)
        tree.add(node_left)
        tree.add(node_left_2)
        tree.add(node_right)
        self.assertEqual(tree.root.left_node.left_node.right_node, node_right)
        self.assertIsNone(tree.root.right_node)

    def _test_add_duplicate_node_raises_error(self):
        """
        Create an empty BinarySearchTree.
        Check that addition of a duplicate Node raises Duplicate Error
        """
        tree = BinarySearchTree()
        node_root, node_right = Node(5), Node(7)
        tree.add(node_root)
        tree.add(node_right)
        self.assertRaises(DuplicateError, tree.add, node_right)

    def test_remove_root_node(self):
        """
        Check that remove function removes root node and root turns None
        """
        tree = BinarySearchTree()
        node_root = Node(5)
        tree.add(node_root)
        tree.remove(node_root)
        self.assertIsNone(tree.root)

    def test_remove_node_in_tree_with_several_nodes(self):
        """
        Check that remove function removes node and connections with it
        """
        tree = BinarySearchTree()
        node_root, node_left, node_left_2, node_right = Node(8), Node(4), Node(2), Node(3)
        tree.add(node_root)
        tree.add(node_left)
        tree.add(node_left_2)
        tree.add(node_right)
        tree.remove(node_left_2)
        self.assertFalse(tree.contains(node_left_2))
        self.assertIsNone(tree.root.left_node.left_node)

    def _test_remove_from_empty_tree_raises_error(self):
        """
        Check that removal from an empty BinarySearchTree raises Empty Error
        """
        tree = BinarySearchTree()
        self.assertRaises(EmptyError, tree.remove, Node(5))

    def _test_remove_non_existent_node_raises_error(self):
        """
        Check that removal from an empty BinarySearchTree raises NodeNotFound Error
        """
        tree = BinarySearchTree()
        tree.add(Node(6))
        self.assertRaises(NodeNotFoundError, tree.remove, Node(5))

    def _test_contains_node_empty_tree_raises_error(self):
        """
        Check that contains function raises Empty Error when BinarySearchTree is empty
        """
        tree = BinarySearchTree()
        self.assertRaises(EmptyError, tree.contains, Node(5))

    def test_contains_node(self):
        """
        Check that contains function returns True when Node in BinarySearchTree
         and False otherwise
        """
        tree = BinarySearchTree()
        node_root = Node(5)
        tree.add(node_root)
        self.assertTrue(tree.contains(node_root))
        self.assertFalse(tree.contains(Node(6)))

    def test_contains_node_in_tree_with_several_nodes(self):
        """
        Check that contains function returns True when Node in BinarySearchTree
         and False otherwise when there are several Nodes
        """
        tree = BinarySearchTree()
        node_root, node_left, node_left_2, node_right = Node(8), Node(4), Node(2), Node(3)
        tree.add(node_root)
        tree.add(node_left)
        tree.add(node_left_2)
        tree.add(node_right)
        self.assertTrue(tree.contains(node_right))
        self.assertFalse(tree.contains(Node(1)))

    def _test_find_not_existent_node_raises_error(self):
        """
        Check that contains function raises NodeNotFound Error when Node is not found
        """
        tree = BinarySearchTree()
        tree.add(Node(6))
        self.assertRaises(NodeNotFoundError, tree.find, Node(5))

    def test_find_node(self):
        """
        Check that find function returns Node when Node in BinarySearchTree
        """
        tree = BinarySearchTree()
        node_root = Node(5)
        tree.add(node_root)
        self.assertIsInstance(tree.find(node_root), Node)
        self.assertEqual(tree.find(node_root).root, 5)

    def test_find_node_in_tree_with_several_nodes(self):
        """
        Check that find function returns Node in BinarySearchTree when there are several Nodes
        """
        tree = BinarySearchTree()
        node_root, node_left, node_left_2, node_right = Node(8), Node(4), Node(2), Node(3)
        tree.add(node_root)
        tree.add(node_left)
        tree.add(node_left_2)
        tree.add(node_right)
        self.assertIsInstance(tree.find(node_left_2), Node)
        self.assertEqual(tree.find(node_left_2).root, 2)

    def test_get_size(self):
        """
        Check that get_size function returns number of Nodes
        """
        tree = BinarySearchTree()
        node_root, node_left, node_left_2, node_right = Node(8), Node(4), Node(2), Node(3)
        tree.add(node_root)
        tree.add(node_left)
        tree.add(node_left_2)
        tree.add(node_right)
        self.assertEqual(tree.get_size(), 4)

    def test_get_size_return(self):
        """
        Check that get_size function returns int number of Nodes
        """
        tree = BinarySearchTree()
        node_root, node_left = Node(8), Node(4)
        tree.add(node_root)
        tree.add(node_left)
        self.assertEqual(type(tree.get_size()), int)

    def test_get_size_of_empty_tree(self):
        """
        Check that get_size function returns 0 when tree is empty
        """
        tree = BinarySearchTree()
        self.assertEqual(tree.get_size(), 0)

    def _test_get_max_height_of_empty_tree_raises_error(self):
        """
        Check that getting max height of an empty BinarySearchTree raises Empty Error
        """
        tree = BinarySearchTree()
        self.assertRaises(EmptyError, tree.get_max_height)

    def test_get_max_height_of_tree_with_only_root(self):
        """
        Check that get_max_height function returns 1
        """
        tree = BinarySearchTree()
        node_root = Node(5)
        tree.add(node_root)
        self.assertEqual(tree.get_max_height(), 1)

    def test_get_max_height_of_tree_with_several_nodes(self):
        """
        Check that get_max_height function returns the correct length of max branch
        """
        tree = BinarySearchTree()
        nodes_to_add = [Node(8), Node(4), Node(2), Node(3), Node(10),
                        Node(16), Node(13), Node(12), Node(11)]
        for node in nodes_to_add:
            tree.add(node)
        self.assertEqual(tree.get_max_height(), 6)

    def _test_traverse_breadth_tree_when_tree_is_empty_raises_error(self):
        """
        Check that getting breath_tree of an empty BinarySearchTree raises Empty Error
        """
        tree = BinarySearchTree()
        self.assertRaises(EmptyError, tree.traverse_breadth_tree)

    def test_traverse_breadth_tree_when_tree_has_only_root(self):
        """
        Check that traverse_breadth_tree function returns a list 1 number
        """
        tree = BinarySearchTree()
        node_root = Node(5)
        tree.add(node_root)
        self.assertEqual(tree.traverse_breadth_tree()[0].root, 5)

    def test_traverse_breadth_tree_when_tree_has_several_nodes(self):
        """
        Check that traverse_breadth_tree function returns a list with numbers according to breadth
        Tests that first number in list is the root and
         the last is on the last level of tree on the right
        """
        tree = BinarySearchTree()
        nodes_to_add = [Node(8), Node(4), Node(2), Node(3), Node(10),
                        Node(16), Node(13), Node(12), Node(11)]
        for node in nodes_to_add:
            tree.add(node)
        output = tree.traverse_breadth_tree()
        self.assertEqual(output[0].root, 8)
        self.assertEqual(output[-1].root, 11)
