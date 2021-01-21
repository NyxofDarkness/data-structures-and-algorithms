def multi_bracket_validation(str):
    """[checks brackets to make sure they are paired]

    Args:
        str ([any]): [For each letter in string checks for opening brackets, appends them to stack, checks for closing brackets and pops them off. If stack is empty returns true- all brackets paired. If not empty, returns False, one or more brackets do not have pair]
    """
    stack = []
    pairs = 0
    for letter in str:
        if (letter == '(' or letter == '{' or letter == '['):
            stack.append(letter)

        elif (letter == ')' or letter == '}' or letter == ']'):

                stack.pop()
                pairs += 1
# checks if anything is left in stack, return boolean
    if pairs != 0:
        return True
    else:
         return False
