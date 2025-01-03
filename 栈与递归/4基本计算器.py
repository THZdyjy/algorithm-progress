class Solution:
    def level(self, op):
        if op == "+" or op == "-":
            return 1
        if op == "*" or op == "/":
            return 2
        if op == '@':
            return 0

    def calc(self, a, b, op):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return a // b

    def calculate(self, s: str) -> int:
        """
        core: 维护一个数据栈，一个操作符栈。
                给加减乘除一个计算等级，等级越高，优先计算。当后入栈的操作符优先级小于栈顶操作符时，先出栈，并计算。
                当运算符从左到右，依次升高时，不会出栈，因此，可以在字符串最后面加一个优先级最低的辅助操作符@
        """
        ops, data = [], []
        # j1: 在原字符串中添加辅助操作符
        s = s + '@'
        # j2: 注意程序中，t变量的处理。
        t = ""
        for i in range(len(s)):
            # j3: 注意空字符要跳过， 否则第34行，会报错。
            if s[i] == ' ': continue
            # j4: 得到数值部分
            if "0" <= s[i] <= "9":
                t += s[i]
                continue
            # j5: 这里不会加上“”的原因是，数值计算中的continue操作
            data.append(int(t))
            t = ""
            # j6：如果操作符栈不为空 且 当前操作符优先级小于栈顶时， 先弹出栈顶操作符并计算结果
            # j7: 注意是<=, 同一级运算的话，从左往右进行计算
            while ops and self.level(s[i]) <= self.level(ops[-1]):
                b = data.pop()
                a = data.pop()
                op = ops.pop()
                res = self.calc(a, b, op)
                data.append(res)
            ops.append(s[i])
        return data[-1]





