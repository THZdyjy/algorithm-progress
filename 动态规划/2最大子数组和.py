# 状态压缩写法
"""
base情况dp[i] = nums[i]
dp[i] = max(nums[i], dp[i-1]+nums[i])
观察状态转移方程，dp[i]与当前数字nums[i]有关，然后与dp[i-1]有关。因此只存一个dp[i-1]即可，可以将O(n）的复杂度压缩到1
因此可以初始化 dp_0 = nums[0], dp_1 = nums[1]
然后计算dp1 = max(nums[i], nums[i] + dp0) 更新dp0 = dp1; 顺便更新res
"""
def maxSubArray(nums) -> int:
    n = len(nums)
    if n == 0:
        return 0

    # base ①人生之始 ②人生目的 ③大道至简-》最后才优化的
    dp0 = nums[0]
    dp1 = 0
    res = dp0
    # ④人生状态与当下选择
    for i in range(1, n):
        # ⑤ 不断取得最大的成就
        dp1 = max(nums[i], nums[i] + dp0) # 状态
        res = max(res, dp1)
        dp0 = dp1
    return res

"""
core: 定义dp[i]为：以nums[i]这个数字结尾的子数组和。
确定base为，数组长度为1，即第一个数字时，dp[0] = nums[0], 以他为结尾的最大子数组和就是nums[0]
确定状态转移方程： 由dp[i-1] -> 得到dp[i] ，如果dp[i-1]是大于0 的 dp[i] = dp[i-1] + nums[i]
                                                   小于0，  dp[i] = nums[i], 不加前面了，就是我本身
因此状态转移方程为 dp[i] = max(nums[i], dp[i-1]+nums[i])
最后再遍历dp, 更新res的值。

"""

def maxSubArray(nums) -> int:
    n = len(nums)
    if n == 0:
        return 0

    dp = [0] * n
    # base
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = max(nums[i], nums[i] + dp[i - 1]) # 状态

    res = float('-inf')
    for i in range(n):
        res = max(res, dp[i])

    return res

