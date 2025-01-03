"""
core: 这道题里面出现了重复元素，所以我们需要剪枝
为了保证剪枝的顺利进行，我们可以先对原数组进行排序，这样，在遍历数字的过程中，如果当前数字和上一个数字相同，跳过即可。
"""
class Solution:

    def __init__(self):
        self.track = []
        self.res = []

    def backtrack(self, nums, start):
        self.res.append(self.track[:])
        for i in range(start, len(nums)):
            # 从start处开始剪枝
            if i > start and nums[i] == nums[i - 1]:
                continue
            self.track.append(nums[i])
            next_position = i + 1
            self.backtrack(nums, next_position)
            self.track.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 从位置0处开始，进行子集的收集
        # 先排序
        nums.sort()
        self.backtrack(nums, 0)
        return self.res