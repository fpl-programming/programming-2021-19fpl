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
        return root

    def erase(self, value):
        if self.find(value):
            self.root = self._erase(self.root, value)
            self.size -= 1
        else:
            raise IndexError

    def _erase(self,):
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
        return self._find(self.root, value)

    def _find(self, node, value):
        if node is None:
            return False
        if node.get_value() == value:
            return True
        if node.get_value() > value:
            return self._find(node.get_left(), value)
        else:
            return self._find(node.get_right(), value)

    def get_size(self):
        return self.size

    def height(self):
        pass

    def width(self):
        pass
