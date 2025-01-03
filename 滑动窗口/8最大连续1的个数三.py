class Solution:
    """
    core:
    题意转换。把「最多可以把 K 个 0 变成 1，求仅包含 1 的最长子数组的长度」转换为 「找出一个最长的子数组，该子数组内最多允许有 K 个 0 」。
    """
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        max_res = 0
        zero_num = 0
        while right < len(nums):
            in_number = nums[right]
            if in_number == 0:
                zero_num += 1
            right += 1

            while zero_num > k:
                out_number = nums[left]
                if out_number == 0:
                    zero_num -= 1
                left += 1
            max_res = max(max_res, right - left)
        return max_res