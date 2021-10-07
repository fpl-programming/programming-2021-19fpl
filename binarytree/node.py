"""
Implementation of the structure "Node" of data structure "Binary Tree"
"""


class Node:
    """
    Node of the Binary Tree Structure (auxiliary)
    """
    def __init__(self, value: int):
        if not isinstance(value, int):
            raise ValueError('Binary tree contains only integers')
        self.value = value
        self.left = None
        self.right = None

    def add_left(self, value_to_add):
        """
        Add left descendant of the node
        :param value_to_add: a value smaller than the value of the node
        """
        if self.left is not None:
            raise IndexError('Left descendant is already added to this node')
        if isinstance(value_to_add, Node):
            if value_to_add.value >= self.value:
                raise ValueError('Left descendant must be smaller than the node value')
            self.left = value_to_add
        elif isinstance(value_to_add, int):
            if value_to_add >= self.value:
                raise ValueError('Left descendant must be smaller than the node value')
            self.left = value_to_add
        else:
            raise TypeError('Binary tree contains only integers and Node instances')

    def add_right(self, value_to_add):
        """
        Add right descendant of the node
        :param value_to_add: a value greater than the value of the node
        """
        if self.right is not None:
            raise IndexError('Right descendant is already added to this node')
        if isinstance(value_to_add, Node):
            if value_to_add.value <= self.value:
                raise ValueError('Right descendant must be greater than the node value')
            self.right = value_to_add
        elif isinstance(value_to_add, int):
            if value_to_add <= self.value:
                raise ValueError('Right descendant must be greater than the node value')
            self.right = value_to_add
        else:
            raise TypeError('Binary tree contains only integers and Node instances')
