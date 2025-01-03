class Solution:
    def __init__(self):
        self.track = []
        self.res = []

    def backtrack(self, nums, start, k):
        # j3：base 记得return，结束遍历
        # 在子集的基础上，值收集子集数量为k的即可。
        if sum(self.track) == k:
            self.res.append(self.track[:])
            return
        # j4：这里也是关键点,不一定恰好就等于k, 因此,大于k的也要返回
        if sum(self.track) > k:
            return

        for i in range(start, len(nums)):
            # j2：剪枝
            # 这里是i>start, 而不是i>0,如果不明白为什么，debug一下。（从start的下一个位置计算重复）
            if i > start and nums[i] == nums[i - 1]: continue
            self.track.append(nums[i])
            next_position = i + 1
            self.backtrack(nums, next_position, k)
            self.track.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # j1：排序
        candidates.sort()
        self.backtrack(candidates, 0, target)
        return self.res


