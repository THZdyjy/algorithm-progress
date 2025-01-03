class Solution:
    def __init__(self):
        self.track = []
        self.res = []

    def backtrack(self, nums, start, k):
        # 在子集的基础上，值收集子集数量为k的即可。
        if len(self.track) == k:
            self.res.append(self.track[:])
            return

        for i in range(start, len(nums)):
            self.track.append(nums[i])
            next_position = i + 1
            self.backtrack(nums, next_position, k)
            self.track.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n + 1))
        self.backtrack(nums, 0, k)
        return self.res