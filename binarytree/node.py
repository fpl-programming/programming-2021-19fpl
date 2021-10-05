"""
Implementation of the structure "Node" for data structure "Binary Tree"
"""


class Node:
    """
    Auxiliary Node Structure
    """
    def __init__(self, value: int):
        self.value = None
        if isinstance(value, int):
            self.value = value
        self.left = None
        self.right = None

    def add_left(self, value: int):
        """
        Add left descendant of the node
        :param value: the value which is smaller than the value of the node
        """
        if isinstance(value, int):
            self.left = value

    def add_right(self, value: int):
        """
        Add right descendant of the node
        :param value: the value which is greater than the value of the node
        """
        if isinstance(value, int):
            self.right = value
    #
    # def return_left(self):
    #     """
    #     Return left descendant of the node
    #     """
    #     return self.left
    #
    # def return_right(self):
    #     """
    #     Return right descendant of the node
    #     """
    #     return self.right
