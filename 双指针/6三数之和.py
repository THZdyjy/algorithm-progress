"""
#两数之和最优解哈希表，O(n)
#两数之和2最优解双指针+剪枝O(n)
本题是三数之和，因为a+b+c=0->a+b = -c-> 因此可以转化为两数之和
解题思路是：先排序+双指针。-c作为target,遍历数组，l,r作为左右指针再遍历一遍。因此时间为n方。
本题的难点在于重复性，因此要进行各种剪枝：
    ①边界条件的剪枝
    ②外层for循环，即对target重复元素的剪枝
    ③内层循环，即双指针移动的过程中，对左右指针重复值的剪枝
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3 and sum(nums) != 0:
            return []

        nums.sort()
        length = len(nums)
        res = []
        for i in range(length):
            # j2: 剪枝2，target重复度排除
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = 0 - nums[i]
            l = i + 1
            r = length - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    # j3：剪枝，排除左右指针的重复元素
                    while l < r and nums[l + 1] == nums[l]: l += 1
                    while l < r and nums[r - 1] == nums[r]: r -= 1
                    l += 1
                    r -= 1

                elif nums[l] + nums[r] < target:
                    l += 1

                else:
                    r -= 1
        return res 