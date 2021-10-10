"""
Programming for linguists

Implementation of the data structure "Binary tree"
"""


class TreeNode:
    """
    The Tree Node
    """

    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def has_left(self):
        """
        Return the left child
        """
        return self.left

    def has_right(self):
        """
        Return the right child
        """
        return self.right

    def is_root(self):
        """
        :return: True if child hasn't got a parent
                 False if child has a parent
        """
        return not self.parent

    def is_leaf(self):
        """
        Return the right or the left leaf
        """
        return not (self.right or self.left)

    def is_left(self):
        """
        :return: True if a child is left
                False if a child child is right
        """
        return self.parent and self.parent.left == self

    def is_right(self):
        """
        :return: True if a child is right
                 False if a child is left
        """
        return self.parent and self.parent.right == self

    def has_any_children(self):
        """
        :return: True if there is at least one child
                 False if there is no children
        """
        return self.right or self.left

    def has_both_children(self):
        """
        :return: True if there are both children
                 False if there are no children
        """
        return self.right and self.left

    def replace_node(self, val, left, right):
        """
        Replace an element and saves its position and parents
        """
        self.val = val
        self.left = left
        self.right = right
        if self.has_left():
            self.left.parent = self
        if self.has_right():
            self.right.parent = self

    def find_min(self):
        """
        :return: minimum element (left element)
        """
        current_node = self
        while current_node.has_left():
            current_node = current_node.left
        return current_node

    def find_successor(self):
        """
        Find successor
        :return: successor
        """
        successor = None
        if self.has_right():
            successor = self.right.find_min()
        else:
            if self.parent:
                if self.is_left():
                    successor = self.parent
                else:
                    self.parent.right = None
                    successor = self.parent.find_successor()
                    self.parent.right = self
        return successor

    def splice(self):
        """
        Finds a part of the tree that is suitable for replacing (in case you delete some child)
        """
        if self.is_leaf():
            if self.is_left():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.has_any_children():
            if self.has_left():
                if self.is_left():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.is_left():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, val):
        """
        Create root element if there is no root
        Call private method
        """
        if self.root:
            self._put(val, self.root)
        else:
            self.root = TreeNode(val)
        self.size = self.size + 1

    def _put(self, val, current_node):
        """
        Put a new element
        """
        if val < current_node.val:
            if current_node.has_left():
                self._put(val, current_node.left)
            else:
                current_node.left = TreeNode(val, parent=current_node)
        else:
            if current_node.has_right():
                self._put(val, current_node.right)
            else:
                current_node.right = TreeNode(val, parent=current_node)

    def get(self, val):
        """
        Get an element
        :return: Noun if there is no such element or root
                 An element if it exists
        """
        if self.root:
            res = self._get(val, self.root)
            if res:
                return res.val
            else:
                return None
        else:
            return None

    def _get(self, val, current_node):
        """
        Return an element
        """
        if not current_node:
            return None
        elif current_node.val == val:
            return current_node
        elif val < current_node.val:
            return self._get(val, current_node.left)
        else:
            return self._get(val, current_node.right)

    def print_tree(self):
        """
        Print values of nodes
        If there is no root, print None
        """
        if self.root:
            self._print_tree(self.root)
        else:
            print('root is None')
        print("root val:", self.root.val)

    def _print_tree(self, current_node):
        """
        Prints values of nodes
        """
        if current_node.has_left():
            self._print_tree(current_node.left)
        print(current_node.val)
        if current_node.has_right():
            self._print_tree(current_node.right)

    def delete(self, val):
        """
        Delete an element
        If there is one element, delete root
        Delete with remove method
        """
        if self.size > 1:
            node_to_delete = self._get(val, self.root)
            if node_to_delete:
                self.removee(node_to_delete)
                self.size = self.size - 1
            else:
                raise KeyError('Error, value not in tree')
        elif (self.size == 1 and self.root.val == val):
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, value not in tree')

    def removee(self, current_node):
        """
        Consider 3 cases:
                        an element we want to remove doesn't have parents
                        an element we want to remove has a parent and they can take place of this element
                        an element we want to remove has a parent but cannot take its place
        """
        if current_node.is_leaf():
            if current_node == current_node.parent.left:
                current_node.parent.left = None
            else:
                current_node.parent.right = None
        elif current_node.has_both_children():
            succ = current_node.find_successor()
            succ.splice()
            current_node.val = succ.val
        else:
            if current_node.has_left():
                if current_node.is_left():
                    current_node.left.parent = current_node.parent
                    current_node.parent.left = current_node.left
                elif current_node.is_right():
                    current_node.left.parent = current_node.parent
                    current_node.parent.right = current_node.left
                else:
                    current_node.replaceNode(current_node.left.payload, current_node.left.left, current_node.left.right)
            else:
                if current_node.is_left():
                    current_node.right.parent = current_node.parent
                    current_node.parent.left = current_node.right
                elif current_node.is_right():
                    current_node.right.parent = current_node.parent
                    current_node.parent.right = current_node.right
                else:
                    current_node.replaceNode(current_node.right.payload, current_node.right.left, current_node.right.right)

    def contains(self, key):
        """
        Check if the element is in the tree
        :return: True if the tree has this element
                 False if the tree doesn't have this element
        """
        if self._get(key, self.root):
            return True
        else:
            return False

    def height(self):
        """
        Find height of the tree
        """
        if self.root:
            return self._height(self.root)
        else:
            return 0

    def _height(self, current_node):
        if not current_node:
            return 0
        if current_node.has_left():
            l_height = self._height(current_node.left)
        else:
            l_height = 0

        if current_node.has_right():
            r_height = self._height(current_node.right)
        else:
            r_height = 0

        return max(l_height, r_height) + 1
