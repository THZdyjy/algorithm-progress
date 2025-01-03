class Solution:
    """
    core: 排序 + 双指针
    """
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == k:
                ans += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                r -= 1
        return ans