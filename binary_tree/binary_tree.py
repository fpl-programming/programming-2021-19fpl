"""
Programming for linguists

Implementation of the data structure "Binary search tree"
"""


class Node:
    """
    Class for nodes of the tree
    """
    def __init__(self, value: int or None):
        self.value = value
        self.left = None
        self.right = None

    def add(self, element: int):
        """
        Add element data as node's child
        """
        if self.value == element:
            return False

        if self.value > element:
            if self.left:
                return self.left.add(element)

            self.left = Node(element)
            return True

        if self.right:
            return self.right.add(element)

        self.right = Node(element)
        return True

    def find(self, element: int):
        """
        Find element in the node.
        """
        if self.value == element:
            return True

        if self.value > element:
            if self.left:
                return self.left.find(element)
            return False

        if self.right:
            return self.right.find(element)

        return False

    def get_height(self):
        """
        Get height of the node.
        """
        if self.left and self.right:
            return 1 + max(self.left.get_height(), self.right.get_height())

        if self.left:
            return 1 + self.left.get_height()

        if self.right:
            return 1 + self.right.get_height()

        return True

    def depth_in_order(self):
        """
        Go to depth and print values.
        """
        if self:
            if self.left:
                self.left.depth_in_order()

            print(str(self.value), end=' ')

            if self.right:
                self.right.depth_in_order()


class BinarySearchTree:
    """
    Binary search tree data structure
    """
    def __init__(self):
        self.root = None

    def add(self, element: int):
        """
        Add the element ‘element’ to BinarySearchTree
        :param element: element to add to BinarySearchTree
        """
        if not isinstance(element, int):
            raise ValueError('Element is not integer.')

        if self.root:
            return self.root.add(element)

        self.root = Node(element)
        return True

    def remove(self, element: int):
        """
        Remove the element from the binary tree
        """
        if self.find(element):
            if element == self.root.value:
                self.root = None

            else:
                self._remove(element, self.root)

            return True
        else:
            raise ValueError

    def _remove(self, element: int, node):
        """
        Recursive method remove
        """
        if element < node.value and node.left:
            if element == node.left.value:
                node.left = None
            else:
                self._remove(element, node.left)
        elif element > node.value and node.right:
            if element == node.right.value:
                node.right = None
            else:
                self._remove(element, node.right)

    def find(self, element: int):
        """
        Return whether there is element in BinarySearchTree or not
        :return: True if there is element in BinarySearchTree
                 False if there is not element in BinarySearchTree
        """
        if not isinstance(element, int):
            raise ValueError('Element is not integer.')

        if self.root:
            return self.root.find(element)

        return False

    def get_height(self):
        """
        Get height of the tree.
        """
        if self.root:
            return self.root.get_height()

        return 0

    def depth_in_order(self):
        """
        Go to depth and print values.
        """
        if self.root is not None:
            self.root.depth_in_order()
        print('', end='\n')
