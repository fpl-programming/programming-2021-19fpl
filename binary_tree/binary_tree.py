"""
Programming for linguists

Implementation of the data structures "Node" and "Binary Tree"
"""


class Node:
    """Node class."""

    def __init__(self, val):
        self.value = val
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        """Insert data as node's child"""
        if self.value == data:
            return False

        if self.value > data:
            if self.left_child:
                return self.left_child.insert(data)
            self.left_child = Node(data)
            return True

        if self.right_child:
            return self.right_child.insert(data)
        self.right_child = Node(data)
        return True

    def find(self, data):
        """Find data in the node."""
        if self.value == data:
            return True

        if self.value > data:
            if self.left_child:
                return self.left_child.find(data)
            return False
        if self.right_child:
            return self.right_child.find(data)
        return False

    def get_height(self):
        """Get height of the node."""
        if self.left_child and self.right_child:
            return 1 + max(self.left_child.get_height(), self.right_child.get_height())
        if self.left_child:
            return 1 + self.left_child.get_height()
        if self.right_child:
            return 1 + self.right_child.get_height()
        return 1

    def depth_in_order_print(self):
        """Go to depth and print values."""
        if self:
            if self.left_child:
                self.left_child.depth_in_order_print()
            print(str(self.value), end=' ')
            if self.right_child:
                self.right_child.depth_in_order_print()


class BinaryTree:
    """Binary tree class."""

    def __init__(self):
        self.root = None

    def insert(self, data):
        """Insert data to the tree."""
        self._validate_data(data)

        if self.root:
            return self.root.insert(data)
        self.root = Node(data)
        return True

    def find(self, data):
        """Find data in the tree."""
        self._validate_data(data)

        if self.root:
            return self.root.find(data)
        return False

    def get_height(self):
        """Get haight of the tree."""
        if self.root:
            return self.root.get_height()
        return 0

    def remove(self, data):
        """Remove data from the tree."""
        self._validate_data(data)

        # empty tree
        if self.root is None:
            return False

        # data is in root node
        if self.root.value == data:
            self._remove_root()
            return True

        parent = None
        node = self.root

        # find node to remove
        while node and node.value != data:
            parent = node
            if data < node.value:
                node = node.left_child
            elif data > node.value:
                node = node.right_child

        # case 1: data not found
        if node is None or node.value != data:
            return False

        # case 2: remove-node has no children
        if node.left_child is None and node.right_child is None:
            self._remove_node(data, node, parent, mode='no')

        # case 3: remove-node has left child only
        elif node.left_child and node.right_child is None:
            self._remove_node(data, node, parent, mode='left')

        # case 4: remove-node has right child only
        elif node.left_child is None and node.right_child:
            self._remove_node(data, node, parent, mode='right')

        # case 5: remove-node has left and right children
        else:
            self._remove_node_two_children(node)
        return True

    def _remove_root(self):
        """Remove root."""
        if self.root.left_child is None and self.root.right_child is None:
            self.root = None
        elif self.root.left_child and self.root.right_child is None:
            self.root = self.root.left_child
        elif self.root.left_child is None and self.root.right_child:
            self.root = self.root.right_child
        elif self.root.left_child and self.root.right_child:
            del_node_parent = self.root
            del_node = self.root.right_child
            while del_node.left_child:
                del_node_parent = del_node
                del_node = del_node.left_child

            if del_node.right_child:
                if del_node_parent.value > del_node.value:
                    del_node_parent.left_child = del_node.right_child
                elif del_node_parent.value < del_node.value:
                    del_node_parent.right_child = del_node.right_child
            else:
                if del_node.value < del_node_parent.value:
                    del_node_parent.left_child = None
                else:
                    del_node_parent.right_child = None
            self.root.value = del_node.value

    @staticmethod
    def _remove_node(data, node, parent, mode='no'):
        mode_dict = {'no': None, 'left': node.left_child, 'right': node.right_child}
        if data < parent.value:
            parent.left_child = mode_dict[mode]
        else:
            parent.right_child = mode_dict[mode]

    @staticmethod
    def _remove_node_two_children(node):
        """Remove node with two children."""
        del_node_parent = node
        del_node = node.right_child
        while del_node.left_child:
            del_node_parent = del_node
            del_node = del_node.left_child

        node.value = del_node.value
        if del_node.right_child:
            if del_node_parent.value > del_node.value:
                del_node_parent.left_child = del_node.right_child
            elif del_node_parent.value < del_node.value:
                del_node_parent.right_child = del_node.right_child
        else:
            if del_node.value < del_node_parent.value:
                del_node_parent.left_child = None
            else:
                del_node_parent.right_child = None

    def depth_in_order_print(self):
        """Go to depth and print values."""
        if self.root is not None:
            self.root.depth_in_order_print()
        print('', end='\n')

    @staticmethod
    def _validate_data(data):
        """Validate data."""
        if not isinstance(data, int):
            raise ValueError('Data is not integer.')
