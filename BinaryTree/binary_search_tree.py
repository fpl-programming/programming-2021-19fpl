"""

Implementation of the data structure "BinarySearchTree"
"""


class Node:   # pylint: disable=too-few-public-methods
    """
    Node Structure
    """
    def __init__(self, root, left_node=None, right_node=None):
        self.root = root
        self.left_node = left_node
        self.right_node = right_node


class BinarySearchTree:
    """
    Binary search tree Structure
    """
    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        """
        Return whether tree is empty or not
        :return: True if tree does not contain any elements
                 False if tree contains elements
        """
        return self.root is None

    def _add_node_recursive(self, element, node):
        """
        Add elements applying recursion
        :return: created node
        """
        if element == node.root:
            print(f'{element} is already in the tree')
            return node
        if element < node.root:
            if node.left_node is None:
                node.left_node = Node(element)
                return node.left_node
            return self._add_node_recursive(element, node.left_node)

        if node.right_node is None:
            node.right_node = Node(element)
            return node.right_node
        return self._add_node_recursive(element, node.right_node)

    def add(self, element):
        """
        Check whether elements is numeric, whether tree is empty
        and call _add_node_recursive function
        """
        if not isinstance(element, (int, float)):
            raise ValueError

        if self.is_empty():
            self.root = Node(element)
            return

        self._add_node_recursive(element, self.root)

    def _find_element_in_root_recursive(self, element, node):
        """
        Find element recursively
        :return: found node
        """
        if node is None or node.root == element:
            return node

        if element < node.root:
            return self._find_element_in_root_recursive(element, node.left_node)

        return self._find_element_in_root_recursive(element, node.right_node)

    def find(self, element):
        """
        Check whether elements is numeric, whether tree is empty,
         call _find_element_in_root_recursive function and prints message
         :return: found node
        """
        if not isinstance(element, (int, float)):
            raise ValueError

        if self.is_empty():
            print('The tree is empty')
        else:
            node = self._find_element_in_root_recursive(element, self.root)
            if node is None:
                print('Not found')
            return node

    def _find_element_in_left_right_nodes_recursive(self, element, node):
        """
        Find node whose nodes contain element recursively
        :return: found node
        """
        if element < node.root:
            if node.left_node is None or node.left_node.root == element:
                return node
            return self._find_element_in_left_right_nodes_recursive(element, node.left_node)

        if node.right_node is None or node.right_node.root == element:
            return node
        return self._find_element_in_left_right_nodes_recursive(element, node.right_node)

    def remove(self, element):
        """
        Check whether elements is numeric, whether tree is empty,
         call _find_element_in_left_right_nodes_recursive function and prints message
        """
        if not isinstance(element, (int, float)):
            raise ValueError
        if self.is_empty():
            print('The tree is empty')
        else:
            if element == self.root.root:
                self.root = None
                return
            node = self._find_element_in_left_right_nodes_recursive(element, self.root)
            if node is None:
                print(f'{element} is not in the tree')
            elif node.left_node is not None and node.left_node.root == element:
                node.left_node = None
            else:
                node.right_node = None

    def _get_height_rec(self, node):
        """
        Count number of levels recursively
        :return: max height of the tree
        """
        return 1 + max(self._get_height_rec(node.left_node) if node.left_node is not None else 0,
                       self._get_height_rec(node.right_node) if node.right_node is not None else 0)

    def get_max_height(self):
        """
        Check whether tree is empty and prints message,
        call _get_height_rec function.
        :return: max height
        """
        if self.is_empty():
            print('The tree is empty')
            return 0

        return self._get_height_rec(self.root)

    def _dfs_recursive(self, node):
        """
        Visit all nodes recursively
        """
        if node:
            print(node.root, end=' ')
            self._dfs_recursive(node.left_node)
            self._dfs_recursive(node.right_node)

    def look_dfs(self):
        """
        Check whether tree is empty,
         call _dfs_recursive
        """
        if self.is_empty():
            print('The tree is empty')
            return
        self._dfs_recursive(self.root)
        print('')
