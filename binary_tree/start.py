"""
Binary Tree starter
"""


from binary_tree.binary_tree import BinaryTree

if __name__ == '__main__':
    list_of_elements = [8, 10, 3, 1, 6, 14, 4, 7, 13]
    binary_tree = BinaryTree()
    for element in list_of_elements:
        binary_tree.add(element)


    print('\nНайден элемент: {}'.format(binary_tree.find(14)))
    print('Высота бинарного дерева поиска: {}'.format(binary_tree.get_height()))
    binary_tree.remove(6)
    print('Удален элемент: 6')
    binary_tree.remove(10)
    print('Удален элемент: 10')
    print('Высота бинарного дерева поиска: {}'.format(binary_tree.get_height()))

    RESULT = binary_tree.get_height()
    expected = 3
    assert RESULT == expected, 'BinaryTree not working'
