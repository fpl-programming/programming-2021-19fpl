from binary_tree.main import Node, BSTree

tree = BSTree()
tree.add(8)
tree.add(6)
tree.add(4)
tree.add(5)
tree.remove(5)
print(tree.tree_root.left_node.left_node.right_node) # проверка на удаление
print(tree.find(5)) # проверка на поиск