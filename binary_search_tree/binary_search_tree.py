"""
Programming for linguists

Implementation of the data structure "Binary Search Tree"
"""


class EmptyTreeError(Exception):
    """
    Custom Error
    Error is raised when BinarySearchTree is empty
    """
    def __str__(self):
        return 'Binary Search Tree is empty'

class DuplicateError(Exception):
    """
    Custom Error
    Error is raised when the value is already exists as a root of a node
    """
    def __str__(self):
        return 'Value is already in the tree'

class NonexistentNodeError(Exception):
    """
    Custom Error
    Error is raised when there is no such node in the tree
    """
    def __str__(self):
        return 'There is no such node in the tree'

# pylint: disable=too-few-public-methods
class Node:
    """
    Node Data Structure
    """

    def __init__(self, root: int):
        if not isinstance(root, int):
            raise TypeError

        self.root = root
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree:
    """
    Binary Search Tree Data Structure
    """

    def __init__(self, name="Binary_Search_Tree"):
        self.name = name
        self.root = None

    def add(self, value_to_add):
        """
        Add the element 'value_to_add' as a node to the tree
        """
        if self.root is None:
            self.root = Node(value_to_add)
        else:
            self._add(value_to_add, self.root)

    def _add(self, value_to_add, cur_node):
        """
        Recursively search the position in the tree for the element 'value_to_add'
        """
        if value_to_add < cur_node.root:
            if cur_node.left is None:
                cur_node.left = Node(value_to_add)
                cur_node.left.parent = cur_node
            else:
                self._add(value_to_add, cur_node.left)

        elif value_to_add > cur_node.root:
            if cur_node.right is None:
                cur_node.right = Node(value_to_add)
                cur_node.right.parent = cur_node
            else:
                self._add(value_to_add, cur_node.right)

        else:
            raise DuplicateError

    def find(self, value_to_find):
        """
        Check that the element 'value_to_find' is in the tree
        :return: False if tree does not contain element 'value_to_find'
                 Value of type <class '__main__.Node'> if tree contains element 'value_to_find'
        """
        if not self.root:
            raise EmptyTreeError
        return self._find(value_to_find, self.root)


    def _find(self, value_to_find, cur_node):
        """
        Recursively search the position in the tree for the element 'value_to_find'
        """
        if value_to_find > cur_node.root and cur_node.right:
            return self._find(value_to_find, cur_node.right)

        if value_to_find < cur_node.root and cur_node.left:
            return self._find(value_to_find, cur_node.left)

        if value_to_find == cur_node.root:
            return cur_node

        else:
            return False

    def remove_node(self, value_to_delete):
        """
        Delete the element 'value_to_delete' from the tree
        """
        if not self.find(value_to_delete):
            raise NonexistentNodeError
        self._remove_node(self.find(value_to_delete))

    def _remove_node(self, value_to_delete):
        """
        Recursively delete the element 'value_to_delete'
        """
        parent_node = value_to_delete.parent

        if value_to_delete.left and value_to_delete.right:
            num_of_children = 2
        elif value_to_delete.left is None and value_to_delete.right is None:
            num_of_children = 0
        else:
            num_of_children = 1

        def get_min_child(node):
            cur_value = node
            while cur_value.left is not None:
                cur_value = cur_value.left
            return cur_value

        # No children
        if num_of_children == 0:
            if parent_node is not None:
                if parent_node.left == value_to_delete:
                    parent_node.left = None
                else:
                    parent_node.right = None
            else:
                self.root = None

        # 1 child
        elif num_of_children == 1:
            if value_to_delete.left is not None:
                child = value_to_delete.left
            else:
                child = value_to_delete.right

            if parent_node is not None:
                if parent_node.left == value_to_delete:
                    parent_node.left = child
                else:
                    parent_node.right = child
            else:
                self.root = child

            child.parent = parent_node

        # 2 children
        else:
            heir = get_min_child(value_to_delete.right)
            value_to_delete.root = heir.root
            self._remove_node(heir)

    def get_height(self):
        """
        Get the height of the tree including root
        """
        if self.root is None:
            return 0
        return self._get_height(self.root, cur_height=0)

    def _get_height(self, cur_node, cur_height):
        """
        Recursively search the longest branch in the tree
        """
        if cur_node is None:
            return cur_height

        right_h = self._get_height(cur_node.right, cur_height + 1)
        left_h = self._get_height(cur_node.left, cur_height + 1)
        return max(right_h, left_h)

    def width_traverse(self):
        """
        Print nodes of the tree by levels
        """
        height = self.get_height()
        level_values = {}
        for level in range(1, height + 1):
            level_values[level] = self._width_traverse(self.root, level)

        for key, values in level_values.items():
            print(f'Level({key}) values: {values}')

    def _width_traverse(self, cur_node, cur_level):
        """
        Recursively get nodes of the tree by level
        """
        if cur_node is None:
            return

        if cur_level == 1:
            return cur_node.root

        if cur_level > 1:
            left = self._width_traverse(cur_node.left, cur_level - 1)
            right = self._width_traverse(cur_node.right, cur_level - 1)

            if left is None:
                return right

            if right is None:
                return left

            if left is None and right is None:
                return

            return left, right
