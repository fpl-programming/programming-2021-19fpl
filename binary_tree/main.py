"""
Programming for linguists

Implementation of the data structure "Binary Searching Tree"
"""


class Node:
    """
    Node Structure
    """

    def __init__(self, root: int):
        if not isinstance(root, int) or isinstance(root, bool):
            raise TypeError
        self.root = root
        self.left_node = None
        self.right_node = None
        self.value = None

    def first_public_method(self):
        """
        Solves lint problem
        """
        return 1

    def second_public_method(self):
        """
        Solves lint problem
        """
        return 1


class BSTree:
    """
    Binary Searching Tree Structure
    """

    def __init__(self, tree_root=None):
        if isinstance(tree_root, int):
            self.tree_root = Node(tree_root)
        elif tree_root is None:
            self.tree_root = None
        else:
            raise TypeError

    def add(self, new_node: int):
        """
        Adds a node in Tree
        """
        if not isinstance(new_node, int):
            raise TypeError

        new_node = Node(new_node)

        if self.tree_root is None:
            self.tree_root = new_node

        base_node = self.tree_root  # значение, с которым будем сравнивать новое

        while True:
            if new_node.root < base_node.root:
                if base_node.left_node is None:  # если меньшего значения нет, добавляем
                    base_node.left_node = new_node
                    break
                # если уже есть меньшее значение, то будем сравнивать с меньшим
                base_node = base_node.left_node
            elif new_node.root > base_node.root:
                if base_node.right_node is None:  # если большего значения нет, добавляем
                    base_node.right_node = new_node
                    break
                # если уже есть большее значение, то будем сравнивать с большим
                base_node = base_node.right_node
            else:
                break

    def remove(self, bad_node: int):
        """
        Removes a node from Tree
        """
        if not isinstance(bad_node, int) or isinstance(bad_node, bool):
            raise TypeError

        if self.find(bad_node) is False:
            raise ValueError

        bad_node = Node(bad_node)

        if self.tree_root.root == bad_node.root:  # если узел, который надо удалить, равен корню
            self.tree_root = None
        else:

            base_node = self.tree_root  # узел, с которым сравниваем тот, что подали на вход

            while True:
                # если узел, который надо удалить меньшего сравниваемого
                if bad_node.root < base_node.root:
                    # если это его ближайший левый узел - удаляем
                    if bad_node.root == base_node.left_node.root:
                        base_node.left_node = None
                        break
                    # если не ближайший левый узел - смотрим дальше
                    base_node = base_node.left_node
                    # если узел, который надо удалить больше сравниваемого
                elif bad_node.root > base_node.root:
                    # если это его ближайший правый узел - удаляем
                    if bad_node.root == base_node.right_node.root:
                        base_node.right_node = None
                        break
                    # если не ближайший правый узел - смотрим дальше
                    base_node = base_node.right_node

    def find(self, number):
        """
        Finds a node in Tree
        :return: the node that was found in Tree
        """
        if not isinstance(number, int) or isinstance(number, bool):
            raise TypeError

        if self.tree_root is None:
            return False

        base_node = self.tree_root  # сравниваемое значение

        while True:
            if number == base_node.root:
                return Node(number)
            if number < base_node.root:  # если искомое число меньше,
                if base_node.left_node is None:  # а меньшего значения нет, то
                    return False  # в дереве нет такого значения
                # если есть меньшее значение
                # будем сравнивать с числом, которое меньше рассматриваемого
                base_node = base_node.left_node
            elif number > base_node.root:  # если искомое число больше,
                if base_node.right_node is None:  # а большего значения нет, то
                    return False  # в дереве нет такого значения
                # если есть большее значение
                # будем сравнивать с числом, которое больше рассматриваемого
                base_node = base_node.right_node

    def depth(self, node):
        """
        Finds the depth of Tree
        :return: a number of Tree levels
        """
        if isinstance(node, int):
            node = Node(node)
        elif node is None:
            return 0
        elif not isinstance(node, Node):
            raise TypeError

        if self.find(node.root) is False:  # если нет дерева с таким корнем
            raise ValueError

        if node.root == self.tree_root.root:  # начинаем с корня дерева
            node = self.tree_root

        tree_depth = 1 + max(self.depth(node.left_node), self.depth(node.right_node))
        return tree_depth

    def print_tree(self):
        """
        Represents the depth of Tree
        """
        def recurse(node, level):
            tree_structure = ""
            if node is not None:
                tree_structure += recurse(node.right_node, level + 1)
                tree_structure += "| " * level
                tree_structure += str(node.root) + "\n"
                tree_structure += recurse(node.left_node, level + 1)
            return tree_structure
        return recurse(self.tree_root, 0)
