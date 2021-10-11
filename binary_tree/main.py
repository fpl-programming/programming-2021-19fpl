"""
Binary tree implementation
"""


class Node:
    """
    node structure
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.dfs = []

    def get_value(self):
        """
        get value
        """
        return self.value

    def set_value(self, value):
        """
        sets new value
        """
        self.value = value

    def get_left(self):
        """
        goes to the left column if the previous node is smaller
        """
        return self.left

    def set_left(self, left):
        """
        places new node in the left column
        """
        self.left = left

    def get_right(self):
        """
        goes to the left column if the previous node is bigger
        """
        return self.right

    def set_right(self, right):
        """
        places new node in the right column
        """
        self.right = right


class Tree:
    """
    Binary search tree structure
    """
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        """
        adds new value to the tree
        increases tree's size
        """
        self.root = self._insert(self.root, value)
        self.size += 1

    def _insert(self, root, value):
        """
        method which chooses where to place next node
        """
        if not isinstance(value, int):
            raise ValueError

        if root is None:
            return Node(value)
        if root.get_value() > value:
            root.set_left(self._insert(root.get_left(), value))
        else:
            root.set_right(self._insert(root.get_right(), value))
        return root

    def erase(self, value):
        """
        removes tree's value
        reduces tree's size
        """
        if self.find(value):
            self.root = self._erase(self.root, value)
            self.size -= 1
        else:
            raise IndexError

    def _erase(self, node, value):
        """
        recursive erasing node method
        """
        if node.get_value() == value:
            if node.get_right() is None:
                return node.get_left()
            node.get_right().set_left(node.get_left())
            return node.get_right()
        if node.get_value() > value:
            node.set_left(self._erase(node.get_left(), value))
        else:
            node.set_right(self._erase(node.get_right(), value))
        return node

    def find(self, value):
        """
        returns the value if the tree contains it
        """
        return self._find(self.root, value)

    def _find(self, node, value):
        """
        recursive finding value method
        """
        if node is None:
            return False
        if node.get_value() == value:
            return True
        if node.get_value() > value:
            return self._find(node.get_left(), value)

        return self._find(node.get_right(), value)

    def get_size(self):
        """
        returns tree's size
        """
        return self.size

    def height(self):
        """
        returns tree's height
        """
        return self._height(self.root)

    def _height(self, root):
        """
        height finding recursive method
        """
        if root is None:
            return 0
        return 1 + max(self._height(root.get_left()), self._height(root.get_right()))

    def width(self):
        """
        returns tree's width
        """
        list_now_level = []
        if self.root is not None:
            list_now_level.append(self.root)
        list_next_level = []
        result = 0
        while len(list_now_level) != 0:
            result = max(result, len(list_now_level))
            for node in list_now_level:
                if not node.get_left() is None:
                    list_next_level.append(node.get_left())
                if not node.get_right() is None:
                    list_next_level.append(node.get_right())
            list_now_level = list_next_level
            list_next_level = []
        return result

    def get_dfs(self):
        pass