"""
算法：①用栈来解决这道题目
首先遇到左括号的时候，其对应的右括号入栈，如果遇到右括号，先判断是否与栈顶元素相匹配，如若不匹配直接返回
false，否则进行出栈。到最后如果栈中的元素不为空，则返回false，否则为true
算法漏洞： 以上思维方式忽略了一开始是])}的情况，如果这样，就不会入栈，栈一直是空，所以在false中加入栈为空的判断
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '[':
                stack.append(']')
            elif item == '{':
                stack.append('}')
            elif not stack or item != stack[-1]:# 注意栈为空的判断，对应'](){}'
                return False
            else:
                stack.pop()

        return len(stack) == 0
solution = Solution()
print(solution.isValid('](){}'))