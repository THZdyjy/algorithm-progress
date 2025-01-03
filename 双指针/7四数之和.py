"""
core: 多加一层循环，转化为三数之和。O(n三次方)
本题的剪枝策略注意 与 三数之和进行区分。
三数之后的target为0 ，所以排序后，第一个值如果大于零，和值肯定大于零，直接返回即可。
而本题，target为任意数，如果target为负数，第一个值即使大于target, 但他是个负数，后面通过负数的累加，还能加回来。 负数加负数越加越小，正数加正数，越加越大。
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4 or (len(nums) == 4 and sum(nums) != target):
            return []

        nums.sort()
        length = len(nums)
        res = []
        for i in range(length):
            # j1: 剪枝1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, length):
                # j2：剪枝2
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                goal = target - nums[i] - nums[j]
                l = j + 1
                r = length - 1
                while l < r:
                    if nums[l] + nums[r] == goal:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        # j3：剪枝3
                        while l < r and nums[l+1] == nums[l]: l += 1
                        while l < r and nums[r-1] == nums[r]: r -= 1
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] < goal:
                        l += 1
                    else:
                        r -= 1
        return res