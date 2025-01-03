class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        core: 这题和最长连续1的个数，如出一辙。
        转换题意：求最长的且只包含 1 的非空子数组的长度，这个数组中可以包含一个零。-》求最长的连续1的数组，只包含一个零
        """
        left, right = 0, 0
        max_res = 0
        zero_num = 0
        while right < len(nums):
            in_number = nums[right]
            if in_number == 0:
                zero_num += 1
            right += 1

            while zero_num > 1:
                out_number = nums[left]
                if out_number == 0:
                    zero_num -= 1
                left += 1
            # 注意思考这里为什么减一。因为他不管是否含有0，他都要删一个元素
            max_res = max(max_res, right - left - 1)
        return max_res