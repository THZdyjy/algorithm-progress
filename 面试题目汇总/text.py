# # 贝壳一面凑零钱
# # 定义dp[i]: 凑成i 所需要的张数， dp[i] = dp[i-1] + 1
# import collections
# memo = collections.defaultdict()
# dp = [-1] * 30
# def coins(nums, target):
#     # base
#     if target == 0:
#         return 0
#     if target <= -1:
#         return -1
#     if target in memo.keys():
#         return memo[target]
#
#     res = float('inf')
#     for coin in nums:
#         subproblem = coins(nums, target - coin)
#         if subproblem == -1:
#             continue
#         dp[target] = subproblem + 1
#         res = min(res, dp[target])
#
#     memo[target] = res if res != float('inf') else -1
#     return memo[target]



