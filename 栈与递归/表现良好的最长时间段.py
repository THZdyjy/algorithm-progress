"""
本题就是求原数组某一区间，和大于0，即区间和大于0的问题
转化为前缀和，就是求前缀和数组中，后一个值减去前一个值大于0且相隔最远的问题
很自然的想法就是双指针，一个在最左，一个最右边，固定一个，另一个往下走，时间复杂度为n方
在此过程中发现，只需要维护一个单调递减的栈可以节省比较的次数，所以转化为一个单调递减栈求最大宽度坡的问题。
从最右边进行遍历，由于本题的特殊性，前缀和数组是连续的，所以当n《 res的时候，就退出遍历循环
每一个n遍历时，从单调栈的栈首元素进行比较，如果满足条件则更新res，并出栈（当前n是最大长度的，后续的n不必再比较了）
编码技巧：前缀和第一个元素为0 ②栈不为空不是 not stack， ③记录的是索引值相减，而不是前缀和的元素相减 ④循环遍历栈，而不是if

"""
class Solution:
    def longestWPI(self, hours) -> int:

        for i in range(len(hours)):
            if hours[i] > 8:
                hours[i] = 1
            else:
                hours[i] = -1

        pre_sum = [0] * (len(hours) + 1)
        for i in range(1, len(hours)+1):
            pre_sum[i] = pre_sum[i-1] + hours[i-1]
        # print(pre_sum)
        stack = []
        for i, item in enumerate(pre_sum):
            if i == 0: stack.append(i)
            if item < pre_sum[stack[-1]]:
                stack.append(i)
        # print(stack)
        n = len(pre_sum) - 1
        res = 0
        while n > res: # 只在前缀和数组是连续的情况下
            while stack and pre_sum[n] > pre_sum[stack[-1]]:
                res = max(res, n - stack[-1])
                stack.pop()
            n -= 1
        return res
solution = Solution()
print(solution.longestWPI([9,9,6,0,6,6,9]))