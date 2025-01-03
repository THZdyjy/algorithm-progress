"""
core: 使用辅助栈的方法相对来说简单，只需要用一个minStack来始终维护最小值即可。
    这里较难的方法是不使用辅助栈的做法。
    具体来说。入栈的是一个差值。diff = cur_val - min.
    每次新元素入栈时，计算这个差值，如果小于0，则说明cur_val为最小值，则更新最小值为当前值。然后将diff入栈
    当每次出栈时，判断diff是否小于0.是：min==top; 弹出top相当于弹出min,所以min值要更新。diff = val(min)-origin_min.故origin_min=min - diff
    得到top:diff<0? 是：min==top, 返回min. 否：计算top = min + diff。
时空复杂度均为O（1）
死记硬背吧，多做几遍。

core simplify: 画图：三列值 实际，diff，min。
            一个核心公式diff = cur_val - orgin_min
            当diff < 0时，三值合一 val=min=top
"""

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # 刚开始为空的时候，将0入栈。最小值为当前值
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            # 计算当前值与最小值的差值
            diff = val - self.min
            # 如果这个差值小于0，说明当前值小于之前的最小值，更新最小值。将这个差值入栈
            self.stack.append(diff)
            self.min = val if diff < 0 else self.min

    def pop(self) -> None:
        # 获取差值并pop出去
        diff = self.stack.pop()
        # 当前差值如果小于0，说明对应的最后入栈的值小于最小值，即min==最后入栈的那个，弹出的时候相当于把那个谈走了，这样我们就需要变化最小值。变成上一层的最小值。
        if diff < 0:
            self.min = self.min - diff

    def top(self) -> int:
        # 如果stack[-1]小于0，说明最后入栈的那个值小于之前的最小值，它被更新为最小值；即当前最小值==就是那个最后入栈的，就是那个top
        if self.stack[-1] < 0:
            return self.min
        else:
            # 否则的话，重新寻找计算top。因为stack[-1] 大于0，所以最后入栈的那个值（top）比之前的最小值小，二这个stack[-1]怎么得到的呢，他是top-min 得到的。所有top = min + stack[-1]
            return self.stack[-1] + self.min

    def getMin(self) -> int:
        if self.stack:
            return self.min
        else:
            return -1

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()