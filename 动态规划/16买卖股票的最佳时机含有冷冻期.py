class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 空间复杂度优化版本
        n = len(prices)
        dp_i_0, dp_i_1, dp_pre_0 = 0, float('-inf'), 0
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = temp
        return dp_i_0