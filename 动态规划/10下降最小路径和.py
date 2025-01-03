class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        # 初始化memo, 用float('inf')填充，以区别正常答案-10000~10000
        memo = [[float('inf')] * n for _ in range(n)]
        # 求最小和
        res = float('inf')
        # 可能落在最后一行的每一个元素上，因此，我们比较，哪个小，就取哪个
        for j in range(n):
            res = min(res, self.dp(matrix, n-1, j, memo))
        return res

    def dp(self, matrix, i, j, memo):
        # 先检查区间是否有效
        if i < 0 or j < 0 or i > len(matrix) - 1 or j > len(matrix) - 1:
            return float('inf')
        # base, 落在了第一行
        if i == 0: return matrix[0][j]
        # 查看是否已经在备忘录中
        if memo[i][j] != float('inf'):
            return memo[i][j]
        # 状态转移方程
        memo[i][j] = matrix[i][j] + min(
                    self.dp(matrix, i - 1, j, memo),
                    self.dp(matrix, i - 1, j - 1, memo),
                    self.dp(matrix, i - 1, j + 1, memo)
        )
        return memo[i][j]

"""
迭代法
"""
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        # 对应于递归法的 memo & 索引越界的处理
        dp = [[float('inf')] * (n + 2) for _ in range(n)]
        # base case
        for j in range(1, n + 1):
            dp[0][j] = matrix[0][j - 1]
        # 状态转移
        for r in range(1, n):
            for c in range(1, n + 1):
                dp[r][c] = min(dp[r - 1][c - 1], dp[r - 1][c], dp[r - 1][c + 1]) + matrix[r][c - 1]

        # 自底向上 而递归是自顶向下
        res = float('inf')
        for j in range(1, n + 1):
            res = min(res, dp[n - 1][j])
        return res

"""
core: 结合题意，本题的思路是从下往上走，对于最后一行的每个元素，都可以画出一条多叉树，取其中路径和最小的即可
    因此本题的base为：当到达第一行时，即i==0时，返回matrix[i][j]即可。
状态转移方程为：定义dp(matrix, i, j)为从第一行向下落，落到位置matrix[i][j]的最小路径和为dp(matrix, i, j)
    对于当前元素matrix[i][j],只有可能从 matrix[i-1][j], matrix[i-1][j-1], matrix[i-1][j+1]这三个位置转移过来。
    那么，只要知道到达 (i-1, j), (i-1, j-1), (i-1, j+1) 这三个位置的最小路径和，加上 matrix[i][j] 的值，就能够计算出来到达位置 (i, j) 的最小路径和：
    即memo[i][j] = matrix[i][j] + min(
                                    self.dp(matrix, i - 1, j, memo),
                                    self.dp(matrix, i - 1, j - 1, memo),
                                    self.dp(matrix, i - 1, j + 1, memo)
                                    ）
然后本题中初始值的设置很有讲究：
因为：
    1 <= n <= 100
    -100 <= matrix[i][j] <= 100
因此，
    矩阵中元素的路径和的范围在-10000~10000之间
因此，
    在对备忘录进行初始化时我们初始为[10001, inf]，表示matrix[i][j]没有计算过，还没有被记录
另外，
    对于边界的元素，它在进行下一次遍历时，可能会越界，因此，我们需要对索引进行处理，当i或j越界时，我们
给到float('inf)(只要在[10001, inf]之间即可)，这样res永远不会取到，相当于把越界的情况给处理了。
"""