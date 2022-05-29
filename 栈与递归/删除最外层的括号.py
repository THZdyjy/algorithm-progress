def removeOuterParentheses(S: str) -> str:
    stack = []
    result = ''
    for i in S:
        if i == '(':
            stack.append('(')
            if len(stack) > 1:
                result += '('
        else:
            stack.pop()
            if len(stack) != 0:
                result += ')'
    return result
s = "(()())(())"
print(removeOuterParentheses(s))