"""
栈先进后出；
栈反映了一组事件的完成，表示了完全的包含关系，表示了函数套函数，等等。。
栈可以处理完全包含关系的问题。
不断的深入理解概念的泛化性

栈的应用场景一：操作系统中的线程栈
在linux系统中，stack size一般是8M ，能存储200w个整型，当超过这个数之后，就会爆栈。
栈的应用场景二：表达式得求值
"""


# 栈的实现

class Stack():
    def __init__(self, size):
        self.top = -1
        self.cnt = 0
        self.size = size
        self.stack = [None for _ in range(size)]

    def push(self, val):
        if self.is_Full(): return False
        self.top += 1
        self.stack[self.top] = val
        self.cnt += 1
        return

    def pop(self):
        if self.is_Empty(): return  False
        print('出栈元素：{}'.format(( self.stack[self.top])))
        self.stack[self.top] = None
        self.top -= 1
        self.cnt -= 1
        return

    def is_Empty(self):
        return self.top == -1

    def is_Full(self):
        return self.top == self.size - 1

    def output(self):
        print('============')
        for i in range(self.top, -1, -1):
            print(self.stack[i])
        print('============')
        return

s = Stack(5)
s.push(1)
s.push(2)
s.push(3)
s.push(5)
s.pop()
s.push(6)
s.push(9)
s.output()
