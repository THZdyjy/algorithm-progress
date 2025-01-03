from collections import deque


class Solution:
    """
    core: 滑动窗口
    因为这里的窗口大小是固定的，为k。
    ①所以，我们可以一上来先计算出一个窗口为k的total值。
    ②然后，滑动这个窗口，出一个元素，进一个元素。只需要把相应的值进行加减即可。
    ③然后更新maxtotal即可
    """

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxtotal = total = sum(nums[:k])

        right = k
        while right < len(nums):
            total = total - nums[right - k] + nums[right]
            maxtotal = max(maxtotal, total)
            right += 1

        return maxtotal / k