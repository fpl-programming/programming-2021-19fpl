from node import Node


class BinarySearchTree:
    def __init__(self, root: int):
        self.root = Node(root)

    def add(self, element: int, current_node: Node = None, in_tree_check: bool = True):
        if in_tree_check and self.find(element, current_node):
            raise AlreadyInTree
        current_node = current_node if current_node else self.root
        if element < current_node.value and not current_node.left:
            current_node.left = Node(element)
            current_node.left.parent = current_node
        elif element > current_node.value and not current_node.right:
            current_node.right = Node(element)
            current_node.right.parent = current_node
        else:
            current_node = current_node.left if element < current_node.value else current_node.right
            return self.add(element, current_node, False)

    def remove(self, element: int, current_node: Node = None):
        current_node = current_node if current_node else self.root
        if element == current_node.value:
            while current_node.right or current_node.left:
                current_node.value = (current_node.right.value if current_node.right
                                      else current_node.left.value)
                current_node = current_node.right if current_node.right else current_node.left
            if current_node.parent and current_node.value == current_node.parent.left.value:
                current_node.parent.left = None
            elif current_node.parent and current_node.value == current_node.parent.right.value:
                current_node.parent.right = None
            return
        if not current_node.right and not current_node.left:
            raise ValueError
        current_node = current_node.left if element < current_node.value else current_node.right
        return self.remove(element, current_node)

    def find(self, element: int, current_node: Node = None):
        current_node = current_node if current_node else self.root
        if element == current_node.value:
            return True
        if (element < current_node.value and not current_node.left) or (element > current_node.value and
                                                                        not current_node.right):
            return False
        current_node = current_node.left if element < current_node.value else current_node.right
        return self.find(element, current_node)

    def get_height(self):
        pass


class AlreadyInTree(Exception):
    """
    Raised when trying to add an element that is already in the tree
    """
