
"""
core:核心就是将给定的字符串中能够匹配的括号去掉，剩下的数量，就是需要补充的数量。
所以我们遇见（，在stack中添加(，在遍历的过程中，当碰到stack[-1] + item == ()时，就弹出一对括号。即我们是从中间开始弹出，一直到两边。
如果发现组不成一对括号，我们就把）入栈

为了方便判断是否能组成一对括号，我们全都反过来写，像解法二那样。
"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if s == "":
            return 0
        stack = []
        for item in s:
            if item == '(':
                stack.append('(')

            elif stack and stack[-1] + item == '()':
                stack.pop()
            elif item == ')':
                stack.append(')')

        return len(stack)


"""

"""
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if s == "":
            return 0
        stack = []
        for item in s:
            if item == '(':
                stack.append(')')
            elif stack and stack[-1] == item:
                stack.pop()
            else:
                stack.append('(')
        return len(stack)