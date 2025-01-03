class StockSpanner:

    def __init__(self):
        # 初始化时，先入栈inf, 否则对于一直递增的股票， 1,2,3,4,5,8,9 每一天都找不到最大的，栈为空，导致出错
        self.stack = [(float('inf'), -1)]
        self.idx = -1


    def next(self, price: int) -> int:
        self.idx += 1

        # 维护一个单调递减栈
        while self.stack and price >= self.stack[-1][0]:
            self.stack.pop()
        res = self.idx - self.stack[-1][1] if self.stack else 1
        self.stack.append((price, self.idx))
        return res
"""
core: 将问题转化为前面的历史天数中，高于当天股价的那一天。然后计算二者的索引差值即可
维护一个单点递减的栈，当天价格price大于栈顶元素时，就出栈，知道遇到比他大的那一天，计算跨度即可。
simplify：为什么维护单调递减的栈呢，没得干时好好想想，同那个单调栈模板比较比较，结合问题的场景。
对于模板来说，在后面找到一个比他大的元素，我们从后往前走，维护单减栈。然后用cur与栈顶元素比较，不断去出栈，直到遇到比他大的。得到结果
对于本题来说，在前面找到一个比他大的元素，我们从前往后走，维护单减栈。然后用cur与栈顶元素比较，不断去出栈，直到遇到比他大的。得到跨度。
可以说，两道题目的完全思想一致，所以关键在于对题目进行转化。转化成我们熟知的问题，或者更为本质的问题。
"""