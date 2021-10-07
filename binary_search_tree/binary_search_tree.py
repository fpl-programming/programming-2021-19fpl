# pylint: skip-file
"""
Skip due to disable R0903 (about public methods) and
 R1710 (does not like return in traverse) does not work
Programming for linguists

Implementation of the data structure "Binary Search Tree"
"""


class DuplicateError(Exception):
    """
    Custom Error
    Raises when root of node is already in BinarySearchTree
    """


class NodeNotFoundError(Exception):
    """
    Custom Error
    Raises when root of node is not in BinarySearchTree while removing the node
    """


class EmptyError(Exception):
    """
    Custom Error
    Raises when BinarySearchTree is empty
    """


class Node:
    """
    Node Data Structure
    """
    def __init__(self, root: int, value='random info'):
        if not isinstance(root, int):
            raise TypeError('Node is not int')
        self.root = root
        self.right_node = None
        self.left_node = None
        self.value = value


class BinarySearchTree:
    """
    BinarySearchTree Data Structure
    """
    def __init__(self, name='tree'):
        self.name = name
        self.root = None
        self.size = 0

    def add(self, node: Node, root=None):
        """
        Add the node to the tree
        """
        if self.root is None:
            self.root = node
            self.size += 1
        else:
            if root is None:
                if self.contains(node):
                    raise DuplicateError('Node is already in BinarySearchTree')
                root = self.root
            if root.root > node.root:
                if root.left_node is None:
                    root.left_node = node
                    self.size += 1
                else:
                    self.add(node, root.left_node)
            else:
                if root.right_node is None:
                    root.right_node = node
                    self.size += 1
                else:
                    self.add(node, root.right_node)

    def remove(self, node: Node, root=None):
        """
        Remove the node from the tree
        """
        if root is None:
            if not self.contains(node):
                raise NodeNotFoundError('Can not remove non-existent node')
            root = self.root
        if root.root == node.root:
            self.root = None
            self.size -= 1
        else:
            if root.root > node.root:
                if root.left_node.root == node.root:
                    root.left_node = None
                    self.size -= 1
                else:
                    self.remove(node, root.left_node)
            else:
                if root.right_node.root == node.root:
                    root.right_node = None
                    self.size -= 1
                else:
                    self.remove(node, root.right_node)

    def find(self, node: Node, root=None) -> Node:
        """
        Return the found node in the tree
        :return: the node that was specified in find function
        """
        if root is None:
            if not self.contains(node):
                raise NodeNotFoundError('Node is not found')
            root = self.root
        if node.root == root.root:
            return root
        if node.root < root.root:
            return self.find(node, root.left_node)
        return self.find(node, root.right_node)

    def get_max_height(self, root=None) -> int:
        """
        Return the length of the longest branch in the tree
        :return: the length of the longest branch in the tree
        """
        if self.root is None:
            raise EmptyError('BinarySearchTree is empty')
        if root is None:
            root = self.root
        if root.left_node:
            i_left = self.get_max_height(root.left_node)
        else:
            i_left = 0
        if root.right_node:
            i_right = self.get_max_height(root.right_node)
        else:
            i_right = 0
        return 1 + max(i_left, i_right)

    def get_size(self) -> int:
        """
        Return the number of nodes in tree
        :return: Number of elements in tree
        """
        return self.size

    def traverse_breadth_tree(self):
        """
        Return the nodes according to breadth
        :return: Ordered list of nodes
        """
        if self.root is None:
            raise EmptyError('BinarySearchTree is empty')
        breadth_tree = []

        def traverse(node, number):
            nonlocal breadth_tree
            if node.left_node is not None:
                breadth_tree.append(node.left_node)
            if node.right_node is not None:
                breadth_tree.append(node.right_node)
            if number == (len(breadth_tree) - 1):
                return breadth_tree
            traverse(breadth_tree[number + 1], number + 1)

        breadth_tree.append(self.root)
        traverse(self.root, 0)
        return breadth_tree

    def contains(self, node: Node, root=None) -> bool:
        """
        Return whether node in tree or not
        :return: True if tree contains a node.
                 False if tree does not contain a node
        """
        if self.root is None:
            raise EmptyError('BinarySearchTree is empty')
        if root is None:
            root = self.root
        if node.root == root.root:
            return True
        if node.root < root.root:
            if root.left_node is None:
                return False
            return self.contains(node, root.left_node)
        if root.right_node is None:
            return False
        return self.contains(node, root.right_node)
