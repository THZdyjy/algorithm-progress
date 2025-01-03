def maxProfit(self, k: int, prices: List[int]) -> int:
    n = len(prices)
    if n <= 0:
        return 0
    max_k = k

    # base case：
    # dp[-1][...][0] = dp[...][0][0] = 0
    # dp[-1][...][1] = dp[...][0][1] = -infinity
    dp = [[[0] * 2 for _ in range(max_k + 1)] for _ in range(n)]
    # k = 0 时的 base case
    for i in range(n):
        dp[i][0][1] = -float("inf")
        dp[i][0][0] = 0

    for i in range(n):
        for k in range(max_k, 0, -1):
            if i - 1 == -1:
                # 处理 i = -1 时的 base case
                dp[i][k][0] = 0
                dp[i][k][1] = -prices[i]
                continue
            dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
            dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
    return dp[n - 1][max_k][0]
