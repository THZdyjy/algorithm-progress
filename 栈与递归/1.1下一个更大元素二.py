
from typing import List
"""
core: 在模板的基础上进行一些略微的改动。
首先题目要求的是环形链表。那我们将数组长度翻倍，尾巴和脑袋不就连起来了吗，这里你主要用元素3去思考问题。
翻倍数组之后呢，我们从后往前走，维护单调递减栈，那么到达3时（从后往前数第二个），栈中的最高值是4，这样，存储在结果中的值就为4了，而不是-1.
其他的入栈，出栈，保存结果等，都取余数运算，保存在实际的位置。
"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        res = [0] * n
        # 数组长度加倍模拟环形数组
        for i in range(2*n-1, -1, -1):
            # 这里与2*n-1相互配合，虚拟的将数组翻倍，就是为了多遍历一遍数组，满足环形性质。
            i = i % n
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            res[i] = stack[-1] if stack else -1
            stack.append(nums[i])
        return res