def multiBracketValidation(str):
    stack = []
    pairs = 0
    for letter in str:
        if (letter == '(' or letter == '{' or letter == '['):
            stack.append(letter)

        elif (letter == ')' or letter == '}' or letter == ']'):
            if len(stack) == 0:
                pass
            else:
                stack.pop()
                pairs += 1
      return pairs

# if __name__ == '__main__':
#     new_search = multi_bracket_validation()

#     print(new_search)

#     new_search.insert('{}')