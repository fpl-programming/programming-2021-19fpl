"""
Programming for linguists

Implementation of the data structure "Binary Searching Tree"
"""


class Node:

    def __init__(self, root: int):  # число
        self.root = root
        self.left_node = None
        self.right_node = None
        self.value = None


class BSTree:

    def __init__(self, tree_root=None):  # число
        if isinstance(tree_root, int):
            self.tree_root = Node(tree_root)
        else:
            self.tree_root = None

    def add(self, new_node: int):  # число
        new_node = Node(new_node)

        if self.tree_root is None:
            self.tree_root = new_node

        base_node = self.tree_root  # значение, с которым будем сравнивать новое

        while True:
            if new_node.root < base_node.root:
                if base_node.left_node is None:  # если меньшего значения нет, добавляем
                    base_node.left_node = new_node
                    break
                else:  # если уже есть меньшее значение, то будем сравнивать с меньшим
                    base_node = base_node.left_node
            elif new_node.root > base_node.root:
                if base_node.right_node is None:  # если большего значения нет, добавляем
                    base_node.right_node = new_node
                    break
                else:  # если уже есть большее значение, то будем сравнивать с большим
                    base_node = base_node.right_node
            else:
                break

    def remove(self, bad_node: int):  # число
        bad_node = Node(bad_node)

        if self.tree_root.root == bad_node.root:  # если узел, который надо удалить, равен корню
            self.tree_root = None
        else:

            base_node = self.tree_root  # узел, с которым сравниваем тот, что подали на вход

            while True:
                if bad_node.root < base_node.root:  # если узел, который надо удалить меньшего сравниваемого
                    if bad_node.root == base_node.left_node.root:  # если это его ближайший левый узел - удаляем
                        base_node.left_node = None
                        break
                    else:
                        base_node = base_node.left_node  # если не ближайший левый узел - смотрим дальше
                elif bad_node.root > base_node.root:  # если узел, который надо удалить больше сравниваемого
                    if bad_node.root == base_node.right_node.root:  # если это его ближайший правый узел - удаляем
                        base_node.right_node = None
                        break
                    else:
                        base_node = base_node.right_node  # если не ближайший правый узел - смотрим дальше

    def find(self, number):   # число

        base_node = self.tree_root  # сравниваемое значение

        while True:
            if number == base_node.root:
                return Node(number)
            elif number < base_node.root:  # если искомое число меньше,
                if base_node.left_node is None:  # а меньшего значения нет, то
                    return False  # в дереве нет такого значения
                else:  # если есть меньшее значение
                    base_node = base_node.left_node  # будем сравнивать с числом, которое меньше рассматриваемого
            elif number > base_node.root:  # если искомое число больше,
                if base_node.right_node is None:  # а большего значения нет, то
                    return False  # в дереве нет такого значения
                else:  # если есть большее значение
                    base_node = base_node.right_node  # будем сравнивать с числом, которое больше рассматриваемого

    def depth(self, node):
        if isinstance(node, int):
            node = Node(node)

        if node is None:
            return 0

        if node.root == self.tree_root.root:  # начинаем с корня дерева
            node = self.tree_root

        tree_depth = 1 + max(self.depth(node.left_node), self.depth(node.right_node))
        return tree_depth

    def print(self):
        pass