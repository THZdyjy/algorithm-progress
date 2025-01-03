class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]

# 打家劫舍二 连成一个圈
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        def helper(nums_seq):
            n = len(nums_seq)
            if n == 1: return nums_seq[0]
            dp = [0] * len(nums_seq)
            dp[0] = nums_seq[0]
            dp[1] = max(nums_seq[0], nums_seq[1])
            for i in range(2, n):
                dp[i] = max(dp[i-2] + nums_seq[i], dp[i-1])
            return dp[-1]
        return max(helper(nums[1:]), helper(nums[:-1]))