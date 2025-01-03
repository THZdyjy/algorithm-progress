
class Solution:
    def __init__(self):
        self.track = []
        self.res = []
    def backtrack(self, nums, start, target):
        if sum(self.track) == target:
            self.res.append(self.track[:])
            return
        # j2：剪枝，防止树无限生长
        if sum(self.track) > target:
            return
        for i in range(start, len(nums)):
            self.track.append(nums[i])
            # j1：当前元素可重复
            next_position = i
            self.backtrack(nums, next_position, target)
            self.track.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.backtrack(candidates, 0, target)
        return self.res
"""
本题是组合的最后一种题型，元素无重复，但是可复选。
先回顾一下之前的两种题型：
组合->元素无重复，不可复选，该题就是在n个数字中，选取k个数字，构成组合。其解决的思路和子集是完全一致的，（子集的题目中，是找出一个nums的所有子集，当然这个nums是没有重复元素的）。类比子集，我们只需要找包含k个子集的答案即可。
组合二->元素重复，不可复选，该题nums中含有重复元素，如果按照‘组合’题目来做，会出现重复的答案。因此需要剪枝，->先对原数组进行排序，这样重复的元素就挨在一起了->然后在做选择的时候，如果当前元素等于前一个元素，则剪枝
下面开始说本题：
本题是元素无重复，可复选。
即当前元素可以复选的。（这儿的理解可以看labuladong的题解，结合图示，很好理解，这里直接给结论）
我们只需要在start控制重复性时，next_position = i 而不是 i+1即可；但是这样的做法，造成了树的无限生长，因此还需要做个剪枝，当sum(track)>target时，return即可。
"""