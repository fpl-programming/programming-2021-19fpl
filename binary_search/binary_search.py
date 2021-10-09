"""
Programming for linguists

Implementation of the data structure "BinarySearchTree"
"""


class BinarySearchTree:
    """
    BinarySearchTree Structure
    """

    def __init__(self, name: str = None, root: int = None):
        self.name = name
        self._root = Node(root)

    def add(self, element: int):
        """
        Add the element ‘element’ at the correct place of the tree
        :param element: element to add to the tree
        """
        if not self._root.root:
            self._root = Node(element)
            return
        if self.find(element).root:
            raise ValueError('Element Already In The Tree')
        self._add_node(self._root, element)

    def _add_node(self, root: 'Node', element: int):
        """
        Auxiliary recursive function to find the right place for the element in the tree
        :param root: current node to search a free place in
        :param element: element to add to the tree
        """
        if element < root.root and root.left_node:
            self._add_node(root.left_node, element)
        elif element > root.root and root.right_node:
            self._add_node(root.right_node, element)
        else:
            new_node = Node(element)
            if element < root.root:
                root.left_node = new_node
            elif element > root.root:
                root.right_node = new_node
            return

    def find(self, element: int):
        """
        Find and return the required node
        :param element: element to find in the tree
        """
        current_node = self._root
        while current_node.root != element and current_node.root:
            if element < current_node.root and current_node.left_node:
                current_node = current_node.left_node
            elif element > current_node.root and current_node.right_node:
                current_node = current_node.right_node
            else:
                return Node(None)
        return current_node

    def remove(self, element: int):
        """
        Remove the required node from the tree
        :param element: element to remove from the tree
        """
        if self.find(element).root is None:
            raise ValueError('No node found to remove')
        if element == self._root.root:
            self._root = Node(None)
            return
        self._remove_side_node(self._root, element)

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
        if element < root.root:
            self._remove_side_node(root.left_node, element)
        elif element > root.root:
            self._remove_side_node(root.right_node, element)

    def get_root(self):
        """
        Return the current root of the tree
        """
        return self._root.root

    def go_width_traversal(self):
        if not self._root.root:
            raise ValueError('Impossible to go around tree, no elements in the tree')
        all_nodes = [self._root]
        current_level = [self._root]
        nodes_of_level = [self._root]
        while nodes_of_level:
            nodes_of_level = [node.left_node for node in current_level if node.left_node] + \
                             [node.right_node for node in current_level if node.right_node]
            all_nodes.extend(nodes_of_level)
            current_level = nodes_of_level
        return all_nodes

    def __str__(self):
        all_nodes = ['\n', str(self._root.root), '\n']
        current_level = [self._root]
        nodes_of_level = [self._root]
        while nodes_of_level:
            nodes_of_level = [node.left_node for node in current_level if node.left_node] + \
                             [node.right_node for node in current_level if node.right_node]
            list_to_add = [str(node.root) for node in nodes_of_level] + ['\n']
            all_nodes.extend(list_to_add)
            current_level = nodes_of_level
        return ' '.join(all_nodes)


# pylint: disable=too-few-public-methods
class Node:
    """
    Node Data Structure
    """

    def __init__(self, root: int or None, left_node: 'Node' = None, right_node: 'Node' = None):
        self.root = root
        self.left_node = left_node
        self.right_node = right_node
