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

    def add(self, element):
        """
        Add element data as node's child
        """
        if self.value == element:
            return 0

        if self.value > element:
            if self.left:
                return self.left.add(element)
            self.left = Node(element)
            return 1

        if self.right:
            return self.right.add(element)

        self.right = Node(element)
        return 1

    def find(self, element):
        """
        Find element in the node.
        """
        if self.value == element:
            return 1

        if self.value > element:
            if self.left:
                return self.left.find(element)
            return 0

        if self.right:
            return self.right.find(element)
        return 0

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

        return 1

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
        return 1

    def remove(self, element: int):
        """
        Remove the required node from the tree
        :param element: element to remove from the tree
        """
        if self.find(element).root is None:
            raise ValueError('No node found to remove')
        if element == self.root.value:
            self.root = Node(None)
            return
        self._remove_side_node(self.root, element)

    def _remove_side_node(self, root: 'Node', element: int):
        """
        Auxiliary recursive function to find the right node for removal
        :param root: current node to search the element in
        :param element: element to remove from the tree
        """
        if root.left_node and root.left_node.root == element:
            root.left_node = None
            return
        if root.right_node and root.right_node.root == element:
            root.right_node = None
            return
        if element < root.value:
            self._remove_side_node(root.left_node, element)
        elif element > root.value:
            self._remove_side_node(root.right_node, element)

    def find(self, element):
        """
        Return whether there is element in BinarySearchTree or not
        :return: True if there is element in BinarySearchTree
                 False if there is not element in BinarySearchTree
        """
        if not isinstance(element, int):
            raise ValueError('Element is not integer.')

        if self.root:
            return self.root.find(element)
        return 0

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
