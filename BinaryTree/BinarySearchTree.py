class Node:
    def __init__(self, root, left_node=None, right_node=None):
        self.root = root
        self.left_node = left_node
        self.right_node = right_node


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return True if self.root is None else False

    def _add_node_recursive(self, element, node):
        if element == node.root:
            print(f'{element} is already in the tree')
            return

        if element < node.root:
            if node.left_node is None:
                node.left_node = Node(element)
            else:
                return self._add_node_recursive(element, node.left_node)
        else:
            if node.right_node is None:
                node.right_node = Node(element)
            else:
                return self._add_node_recursive(element, node.right_node)

    def add(self, element):
        if not isinstance(element, (int, float)):
            raise ValueError

        if self.is_empty():
            self.root = Node(element)
            return

        self._add_node_recursive(element, self.root)

    def _find_element_in_root_recursive(self, element, node):
        if node is None:
            return

        if node.root == element:
            return node

        if element < node.root:
            return self._find_element_in_root_recursive(element, node.left_node)

        return self._find_element_in_root_recursive(element, node.right_node)

    def find(self, element):
        if not isinstance(element, (int, float)):
            raise ValueError

        if self.is_empty():
            print('The tree is empty')
            return
        node = self._find_element_in_root_recursive(element, self.root)
        if node is None:
            print('Not found')
        else:
            return node

    def _find_element_in_left_right_nodes_recursive(self, element, node):
        if element < node.root:
            if node.left_node is None:
                return
            if node.left_node.root == element:
                return node
            return self._find_element_in_left_right_nodes_recursive(element, node.left_node)

        elif element > node.root:
            if node.right_node is None:
                return
            if node.right_node.root == element:
                return node
            return self._find_element_in_left_right_nodes_recursive(element, node.right_node)

    def remove(self, element):
        if not isinstance(element, (int, float)):
            raise ValueError
        if self.is_empty():
            print('The tree is empty')
            return

        if element == self.root.root:
            self.root = None
            return

        node = self._find_element_in_left_right_nodes_recursive(element, self.root)

        if node is None:
            print(f'{element} is not in the tree')
        elif node.left_node is not None and node.left_node.root == element:
            node.left_node = None
        else:
            node.right_node = None

    def _get_max_height_recursive(self, node):
        return 1 + max(self._get_max_height_recursive(node.left_node) if node.left_node is not None else 0,
                       self._get_max_height_recursive(node.right_node) if node.right_node is not None else 0)

    def get_max_height(self):
        if self.is_empty():
            print('The tree is empty')
            return 0

        return self._get_max_height_recursive(self.root)

    def _dfs_recursive(self, node):
        if node:
            print(node.root, end=' ')
            self._dfs_recursive(node.left_node)
            self._dfs_recursive(node.right_node)

    def look_dfs(self):
        if self.is_empty():
            print('The tree is empty')
            return
        self._dfs_recursive(self.root)
        print('')
