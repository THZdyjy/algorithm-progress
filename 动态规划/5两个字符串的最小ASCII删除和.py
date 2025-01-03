class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        row, col = len(s1), len(s2)
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        for c in range(1, col + 1):
            dp[0][c] = ord(s2[c - 1]) + dp[0][c - 1]

        for r in range(1, row + 1):
            dp[r][0] = ord(s1[r - 1]) + dp[r - 1][0]

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # 不用删除
                else:
                    # 当s1[i-1] != s2[j-1]时， 考虑 -》 使得s1[:i-1] 与 s2[:j]相同的最小删除和，再加上删掉s1[i-1]的ascii值
                    #                         考虑 -》 使得s1[:i] 与 s2[:j-1]相同的最小删除和，再加上删掉s2[j-1]的ascii值
                    #                         二者中求最小的
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1])) # 关键
        return dp[row][col]


