class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            diff = val - self.min
            if diff < 0:
                self.min = val
            self.stack.append(diff)

    def pop(self) -> None:
        diff = self.stack.pop()
        if diff < 0:
            self.min = self.min - diff

    def top(self) -> int:
        diff = self.stack[-1]
        if diff < 0:
            return self.min
        else:
            return self.min + diff


    def getMin(self) -> int:

        return self.min

"""
core simplify: 画图：三列值 实际，diff，min。
            一个核心公式diff = cur_val - orgin_min
            当diff < 0时，三值合一 val=min=top
维护一个差值diff, 当stack为空的时候， 初始化diff=0, 最小值为入栈的第一个值。
后面继续入栈时，将val与最小值比较，相减得到差值，如果差值小于0，则更新最小值为val。此时当前实际值=最小值=top值
push函数，一是初始化，二是计算差值，并维护差值，更新最小值
pop函数，将栈顶元素弹出，即将栈中的diff弹出，注意当diff小于0时，说明三值合一，这个diff对应的实际值就是最小值，因此需要更新最小值，为原先的orgin_min
    根据计算公式diff=val-orgin_min. 所以orgin_min = val(min) - diff ,这样就得到了原来的origin_min
top 函数，获得栈顶的元素， 如果diff是小于0的，说明 min 就是实际值； 否则返回，self.min + diff 即可

"""


minStack =  MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()
minStack.pop()
minStack.top()
minStack.getMin()