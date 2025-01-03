class Solution:
    """
    core: 核心就是实现加减乘除括号的运算
    首先对于一个字符串，将其转为数字： num = num * 10 + (ord(c) - ord('0'))
    可以将字符串看成是一对一对儿的，例如"2-1+2"看成是+2， -1， +2， 将每对数字依次入栈，最后计算总和就可以
    """

    def calculate(self, s: str) -> int:

        def helper(s):
            stack = []
            sign = '+'  # j1: 初始化符号为+
            num = 0

            while len(s) > 0:
                c = s.popleft()
                # if c == ' ': continue # j4: c为空格的时候，在这里判断的话，最后一个数字无法入栈
                if c.isdigit():  # str.isdigit() 可以判断正数，但是无法判断负数。
                    num = num * 10 + (ord(c) - ord('0'))
                if c == '(':
                    num = helper(s) # j5:递归计算括号里面的内容

                if not c.isdigit() and c != ' ' or len(s) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                        # pre = stack.pop()
                        # stack.append(pre * num)
                    elif sign == '/':
                        stack[-1] = int(stack[-1] / float(num))
                        # pre = stack.pop()
                        # stack.append(int(pre / float(num)))  # j3：向0取整。 注意//是向0取整，例如-3//2 = -2 。int是向0取整，这里先计算浮点数，然后用int
                    # j2: 更新num值为0， sign符号
                    num = 0
                    sign = c

                if c == ')':  # j6:出递归的时候,在这里.如果放到前面，）前面的数字无法入栈
                    break
            return sum(stack)

        s = collections.deque(s)
        return helper(s)