class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        采用双指针的解法，结合@nettee的图解，一次能够排除一行或者一列。
        最后时间复杂度为n
        """
        l, r = 0, len(numbers) - 1
        # j1：不能使用重复元素，故没有=号
        while l < r:
            two_sum = numbers[l] + numbers[r]
            if two_sum == target:
                return [l+1, r+1]
            elif two_sum < target:
                l += 1
            else:
                r -= 1
        return

