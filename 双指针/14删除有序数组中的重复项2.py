class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 2, 2
        while j < len(nums):
            if nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i += 1
                j += 1
            else:
                j += 1
        return i