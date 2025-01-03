"""
core: 定义dp[i]： 以nums[i]这个数字结尾的最长递增子数列的长度。
数学归纳法：
base: dp[0] = 1
然后我们知道了dp[i-1] -》推导 dp[i]。举个例子：
1,4,3,4,2,3 数组
1,2,2,3,2,? dp数组
对于位置5的元素3来说，dp[5]??? 因为是递增子序列，所以，我们要找到比他小的元素，有位置0的1，位置4的2，很明显，为了最长，我们接在2的后面，所以是3
这样便得到状态转移方程了：
for j in range(i): 从头开始比较到i-1这个位置
    if nums[j] < nums[i] 满足递增的要求
        dp[i] = max(dp[i], dp[j] + 1)
然后求每个dp[i即可

"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        1，base case
        2，选择与状态-》最优子结构，状态转移
        3，dp定义与备忘录
        """
        # 定义dp数组的含义为：以当前字符结尾的子序列，其最长递增子序列的长度为dp[i]->目标
        length = len(nums)
        dp = [1] * length # 反思，备忘录
        for i in range(1, length): # 选择，改变的动力
            for j in range(i): # 回看人生走过的每一步路
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i]) # 人生状态的改变
        res = 0
        for i in range(len(dp)):
            res = max(res, dp[i])
        return res


class Solution:
    """
    core: 核心思路参看玩纸牌https://labuladong.github.io/algo/di-er-zhan-a01c6/zi-xu-lie--6bc09/dong-tai-g-6ea57/
    1，纸牌建堆：如果当前牌点数较大没有可以放置的堆，则新建一个堆，
    2，否则的话，将纸牌放到相应的堆（点数小的牌压到点数比它大的牌上）
    3，如果当前牌有多个堆可供选择，则选择最左边的那一堆放置。-> 保证了牌有序
    4，牌的堆数就是最长递增子序列的长度
    """
    # 01模型
    def binary_search(self, dp, target):
        l, r = 0, len(dp) - 1
        while r - l > 3:
            mid = l + (r - l) // 2
            if target > dp[mid]:
                l = mid + 1
            else:
                r = mid
        for i in range(l, r + 1):
            if dp[i] >= target:
                return i
        return -1

    def lengthOfLIS(self, nums: List[int]) -> int:

        size = len(nums)
        if size < 2:
            return size
        # base, 第一张牌肯定是一个堆
        dp = [nums[0]]
        for i in range(1, size):
            # 这里在建立堆后，只保留下面那个最小的数字-> 因为是有序地，因此和dp[-1]比较即可
            if nums[i] > dp[-1]:
                dp.append(nums[i])
                continue
            # 利用二分查找，将牌放入相应的堆， 01模型. 在l, r中一定能够找到。因为如果nums[i] > dp[-1], 就新建堆了，相当于吧找不到的情况排除了。
            target = nums[i]
            pile = self.binary_search(dp, target) # 更新索引处的牌的值
            dp[pile] = nums[i]

        return len(dp)