"""
斐波那契数列：
形象的说明了备忘录与状态压缩
"""
class Solution:
    # 备忘录, 避免重复计算
    dp = collections.defaultdict()
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n <= 2: return 1
        if self.dp.get(n, 0): return self.dp[n]
        self.dp[n] = self.fib(n-1) + self.fib(n-2)
        return self.dp[n]

class Solution:

    # 状态压缩，当前状态只与前两个状态有关，将dp table由O(N) 降低到O(1) ，即状态压缩。
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n <= 2: return 1
        dp_0 = 1
        dp_1 = 1
        for i in range(3, n + 1):
            tmp = dp_0 + dp_1
            dp_0 = dp_1
            dp_1 = tmp
        return dp_1

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        f1, f2 = 1, 2
        for i in range(3, n+1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3