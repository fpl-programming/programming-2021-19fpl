"""
Programming for linguists

Start script for Binary Search Tree
"""

from binary_tree.binary_tree import BinarySearchTree

if __name__ == '__main__':
    tree = BinarySearchTree()

    print("Checking BST for emptiness")
    print(f"Is it empty? --> {tree.empty()}")

    print("Well, let's double check")
    print(f"Is its height 0? --> {tree.height()} --> {bool(tree.height())}")

    print("Gonna add some random int values")

    for element in (10, 42, 330):
        print("Adding", tree.add(element))

    print(f"What if I add them again? --> Well, its wrong so we're getting {tree.add(42)}")

    print("Now let's look at the sorted tree!")
    tree.df_search()

    print("\nWhat about looking for the absent values?")
    print(f"We get {tree.find(1000)}")

    print("And what if we try to remove it?")
    print(f"Well, we get ValueError, look! --> {tree.remove(7)}")
