from binary_search_tree import BinarySearchTree

bs_tree = BinarySearchTree(10)
print(bs_tree.root.value)

bs_tree.add(8)
print(bs_tree.root.left.value)
print(bs_tree.root.left.parent.value)  # 10 expected
bs_tree.add(7)
print(bs_tree.root.left.left.value)
print(bs_tree.root.left.left.parent.value)  # 8 expected
bs_tree.add(9)
print(bs_tree.root.left.right.value)

bs_tree.add(12)
print(bs_tree.root.right.value)
bs_tree.add(11)
print(bs_tree.root.right.left.value)
bs_tree.add(13)
print(bs_tree.root.right.right.value)

print(bs_tree.find(13))
print(bs_tree.find(14))

# no children
bs_tree.remove(13)
print(bs_tree.root.right.right)  # None expected

# two children
bs_tree.remove(8)
print(bs_tree.root.left.value)  # 9 expected
print(bs_tree.root.left.left.value)  # 7 expected
print(bs_tree.root.left.right)  # None expected

# one child
bs_tree.remove(12)
print(bs_tree.root.right.value)  # 11 expected
print(bs_tree.root.right.left)  # None expected
print(bs_tree.root.right.right)  # None expected

bs_tree.remove(10)
print(bs_tree.root.value)  # 11 expected
print(bs_tree.root.right)  # None expected
