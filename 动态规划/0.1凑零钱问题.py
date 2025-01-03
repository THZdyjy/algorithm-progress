"""
说明如何来找状态转移方程：
1，base case: 当amount为0时，显然需要0枚硬币
2，dp函数或数组的定义：
    自顶向下：一般来说函数的参数就是状态转移中的变量，即状态；函数返回值即题目要求的计算量
    定义dp(n): 输入一个金额n,返回凑出目标金额n的最少硬币数量。
状态转移方程：
    dp[n] = 0, n = 0
    dp[n] = -1 n < 0
    dp[n] = min(1 + dp(n-coin)) coin 属于 coins
"""
class Solution:
    memo = dict() # dict
    def coinChange(self, coins, amount):
        def dp(n):
            # 查找备忘录，防止重复计算
            if n in memo: return memo[n]
            # base
            if n == 0: return 0
            if n == -1: return -1
            # 状态转移
            res = float('inf')
            for coin in coins:
                subproblem = self.dp(n - coin)
                # 如果子问题无解，则跳过此种选择
                if subproblem == -1:
                    continue
                # 状态转移
                res = min(res, subproblem + 1)
            memo[n] = res if res != float('inf') else -1
            return memo[n]


class Solution:
    def coinChange(self, coins: List[int], amount: int):
        # 备忘录
        memo = dict()
        def dp(n):
            # 查备忘录，避免重复计算
            if n in memo: return memo[n]
            # base case
            if n == 0: return 0
            # 注意这里是小于0，比如1-5=-4，是无解的。
            if n < 0: return -1
            res = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                if subproblem == -1: continue
                res = min(res, 1 + subproblem)
            # 记入备忘录
            memo[n] = res if res != float('INF') else -1
            return memo[n]

        return dp(amount)
