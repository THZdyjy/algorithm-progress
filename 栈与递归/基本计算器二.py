"""
输入：s = " 3+5 / 2 "
输出：5
利用栈，遍历，入栈和弹栈操作
"""
class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        stack = []
        num = 0
        pre = '+'
        for i in range(n):
            if s[i].isdigit():
                num = num * 10 + int(ord(s[i]) - ord('0'))
            if i == n - 1 or s[i] in '+-*/':
                if pre == '+':
                    stack.append(num)
                elif pre == '-':
                    stack.append(-num)
                elif pre == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop / num))
                num = 0
                pre = s[i]
        return sum(stack)
s = Solution()
print(s.calculate("3+2*2"))


