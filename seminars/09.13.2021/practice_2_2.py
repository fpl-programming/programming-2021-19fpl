"""
Practice 2_2
Data Structures: Stack, Task 1
"""


# check sequence of brackets
def check_bracket_sequence(bracket_sequence: str) ->bool:
    """
    Checks bracket sequence is correct or not.
    :param bracket_sequence: string sequence of brackets
    :return: True if sequence is correct, e.g. each open bracket has its closed variant, else False
    """
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']

    stack = []
    for element in bracket_sequence:
        if element in opening_brackets:
            stack.append(element)
        else:
            if opening_brackets.index(stack[-1]) != closing_brackets.index(element):
                return False
            stack.pop(-1)
    if len(stack):
        return False
    return True


if __name__ == '__main__':
    print(check_bracket_sequence('()'))  # True
    print(check_bracket_sequence('([({})])'))  # True
    print(check_bracket_sequence('([({})](){})'))  # True
    print(check_bracket_sequence('([({})][]])'))  # False
    print(check_bracket_sequence('({[})'))  # False
