class Solution:
    def __init__(self):
        self.track = []
        self.res = []
    def dfs(self, nums, used):
        # base
        if len(self.track) == len(nums):
            self.res.append(self.track[:])
            return
        # 遍历, 我们的选择是什么，nums & 没有使用过的
        for i in range(len(nums)):
            if used[i]:
                continue
            # 额外的剪枝操作
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            self.track.append(nums[i])
            used[i] = True
            self.dfs(nums, used)
            # 出节点，回溯时，需要从路径中pop, 并改为未使用
            self.track.pop()
            used[i] = False

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 排序
        nums.sort()
        used = [False] * len(nums)
        self.dfs(nums, used)
        return self.res