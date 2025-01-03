class Solution:
    """
    core: 逆波兰表达式求值。后缀表达式，将运算符放到数字的后边。
        用栈来解，遇到数字则入栈，遇到运算符，出栈两个数字并计算，将计算值入栈
    时空：O(n)
    """
    def evalRPN(self, tokens: List[str]) -> int:

        def evaluate(num1, num2, token):
            if token == "+":
                return num1 + num2
            if token == "-":
                return num1 - num2
            if token == "*":
                return num1 * num2
            # j2：向零取整
            if token == "/":
                return int(float(num1) / num2)

        stack = []
        for token in tokens:
            if token in "+-*/":
                num2 = stack.pop()
                num1 = stack.pop()
                new_num = evaluate(num1, num2, token)
                stack.append(new_num)
            else:
                # j1:入栈数字
                stack.append(int(token))
        return stack[-1]
