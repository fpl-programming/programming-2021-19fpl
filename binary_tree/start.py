"""
Programming for linguists

Realization of the data structure "Binary Searching Tree"
"""
from binary_tree.main import BSTree

tree = BSTree()
# Добавляем значения в дерево
tree.add(8)
tree.add(6)
tree.add(3)
tree.add(9)
tree.add(7)
# Удаляем значение из дерева
tree.remove(7)
# Ищем значение в дереве --> False
print(tree.find(7))
# Находим глубину дерева
print(tree.depth(8))  # поиск глубины --> 3
# Выводим дерево
print(tree.print_tree())
