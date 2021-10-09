# pylint: disable=too-few-public-methods
"""
Programming for linguists
Implementation of the class BinarySearchTree
"""


class NodeExistsError(Exception):
    """
    Custom error
    Error is raised when an element that is trying to be added is already in the tree
    """
    def __str__(self):
        return "The element is already in the tree"


class NodeNotFoundError(Exception):
    """
    Custom error
    Error is raised when an element that is trying to be removed is not in the tree
    """
    def __str__(self):
        return "The element is not in the tree"


class Node:
    """
    A class for nodes of the tree
    """
    def __init__(self, num):
        if not isinstance(num, int):
            raise TypeError('The element is not integer')
        self.root = num
        self.left_node = None
        self.right_node = None


class BinarySearchTree:
    """
    A class for binary search trees
    """
    def __init__(self, name: str):
        if not isinstance(name, str):
            raise TypeError('The name of the tree is not a string')
        self.name = name
        self._root = None

    def add(self, element):
        """
        Add an element in the tree, creating a new tree node.
        :param element: an element need to be added
        """
        if not isinstance(element, int):
            raise TypeError('The element that is trying to be added is not int')

        def recursive_add_node(tree_node):
            """
            Recursion for adding an element
            :param tree_node: a node of the tree
            """
            if element < tree_node.root:
                if tree_node.left_node is None:
                    tree_node.left_node = Node(element)
                else:
                    recursive_add_node(tree_node.left_node)
            elif element > tree_node.root:
                if tree_node.right_node is None:
                    tree_node.right_node = Node(element)
                else:
                    recursive_add_node(tree_node.right_node)
            else:
                raise NodeExistsError

        if self._root is None:
            self._root = Node(element)
        else:
            recursive_add_node(self._root)

    def remove(self, element):
        """
        Remove an element in the tree, deleting all its children.
        :param element: an element need to be deleted
        """
        if not isinstance(element, int):
            raise TypeError('The element that is trying to be removed is not int')

        def recursive_remove_node(tree_node):
            """
            Recursion for removing an element
            :param tree_node: a node of the tree
            """
            if element < tree_node.root:
                if element == tree_node.left_node.root:
                    tree_node.left_node = None
                else:
                    recursive_remove_node(tree_node.left_node)
            elif element > tree_node.root:
                if element == tree_node.right_node.root:
                    tree_node.right_node = None
                else:
                    recursive_remove_node(tree_node.right_node)
            else:
                self._root = None
                # tree_node.root = None
                # tree_node.left_node = None
                # tree_node.right_node = None

        if not self.find(element):
            raise NodeNotFoundError
        recursive_remove_node(self._root)

    def find(self, element):
        """
        Find an element in the tree and return the node or
        None if the the element is not found.
        :param element: an element need to be found
        :return Node class instance if the element is found
                None if the element is not found
        """
        if not isinstance(element, int):
            raise TypeError('The element that is trying to be found is not int')

        def recursive_find_node(tree_node):
            """
            Recursion for finding an element
            :param tree_node: a node of the tree
            """
            if tree_node is None:
                return None
            elif element == tree_node.root:
                return tree_node
            elif element < tree_node.root:
                return recursive_find_node(tree_node.left_node)
            else:
                return recursive_find_node(tree_node.right_node)

        return recursive_find_node(self._root)

    @property
    def max_height(self):
        """
        Return the max height for the tree.
        :return: max tree height
        """
        def recursive_get_height(tree_node):
            """
            Recursion for counting the max height
            :param tree_node: a node of the tree
            """
            if tree_node is None:
                return 0

            return 1 + max(recursive_get_height(tree_node.left_node),
                           recursive_get_height(tree_node.right_node))

        return recursive_get_height(self._root)

    def get_tree_traversal(self):
        """
        Lengthwise tree traversal (from the left to the right side) and
        return the list of numbers according to their order in the tree
        :return: list of numbers of the tree in order from left to right
        """

        numbers_list = list()

        def recursive_traversal(tree_node):
            """
            Recursion for lengthwise traversal
            :param tree_node: a node of the tree
            """
            if tree_node is not None:
                numbers_list.append(tree_node.root)
                recursive_traversal(tree_node.left_node)
                recursive_traversal(tree_node.right_node)

        recursive_traversal(self._root)

        return numbers_list

    def __str__(self):
        """
        Returns a string representation of the tree.
        :return: string with the tree
        """

        def recursive_print_tree(tree_node, level=0):
            """
            Recursion for printing the tree
            :param tree_node: a node of the tree
            :param level: the level of the node (starting with 0)
            """
            strings_list = []
            if tree_node is not None:
                strings_list.append(recursive_print_tree(tree_node.right_node, level + 1))
                strings_list.append(' ' * 5 * level + '--> ' + str(tree_node.root) + '\n')
                strings_list.append(recursive_print_tree(tree_node.left_node, level + 1))
            return ''.join(strings_list)

        return recursive_print_tree(self._root)
