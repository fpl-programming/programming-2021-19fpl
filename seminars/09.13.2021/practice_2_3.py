"""
Practice 2_3
Data Structures: Stack, Task 2
"""


def sort_stack(stack_object: list) -> list:
    """
    Sorts stack.
    :param stack_object: stack object, iterable object
    :return: sorted stack, iterable object
    """
    tmp_stack = []

    while stack_object:
        # complexity check
        print(f'stack 1')
        element = stack_object.pop(-1)
        while tmp_stack and tmp_stack[-1] > element:
            stack_object.append(tmp_stack.pop())
        tmp_stack.append(element)
    return tmp_stack


if __name__ == '__main__':
    # + check complexity O(n^2)
    print(sort_stack([5, 7, 2]))  # 2, 5, 7
    print(sort_stack([2, 5, 7]))  # 2, 5, 7
    print(sort_stack([7, 5, 2]))  # 2, 5, 7
