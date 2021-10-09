class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_left(self):
        return self.left

    def set_left(self, left):
        self.left = left

    def get_right(self):
        return self.right

    def set_right(self, right):
        self.right = right


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        self.root = self._insert(self.root, value)
        self.size += 1

    def _insert(self, root, value):
        if root is None:
            return Node(value)
        if root.get_value() > value:
            root.set_left(self._insert(root.get_left(), value))
        else:
            root.set_right(self._insert(root.get_right(), value))
        

    def erase(self, value):
        pass

    def find(self, value):
        pass

    def get_size(self):
        pass

    def height(self):
        pass

    def width(self):
        pass
