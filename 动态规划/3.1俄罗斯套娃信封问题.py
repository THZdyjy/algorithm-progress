"""
core: 核心是利用最长递增子数列。
题目说了，要能够套进去的话，宽度和高度都得比前一个大。
这样我们先将信封按照w从小到大排序，保证在宽度上是能够套进去的
其次，两个 w 相同的信封不能相互包含，所以对于宽度 w 相同的信封，对高度 h 进行降序排序。
为什么降序呢，比如w 5,5,6
                h 2,4,7
这样，我们对h应用最长递增子序列中的算法，那么这三个都能套了。
如果降序排列则为h 4,2,7 这样，只能套俩
"""


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        res = 0
        for i in range(len(dp)):
            res = max(res, dp[i])
        return res

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # 对x[0]进行排序，当其相等时，对-x[1]进行排序，为什么是-号，自己举个例子
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        print(envelopes)
        height = [envelope[1] for envelope in envelopes]
        return self.lengthOfLIS(height)