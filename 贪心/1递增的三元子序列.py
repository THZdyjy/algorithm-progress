"""
core: 贪心算法，first 和 second 尽可能选择最小的
赋初始值的时候，已经满足second > first了，现在找第三个数third
(1) 如果third比second大，那就是找到了，直接返回true
(2) 如果third比second小，但是比first大，那就把second指向third，然后继续遍历找third
(3) 如果third比first还小，那就把first指向third，然后继续遍历找third（这样的话first会跑到second的后边，但是不要紧，因为在second的前边，老first还是满足的）
"""


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first = second = 0
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                first = nums[i - 1]
                second = nums[i]
                break
        else:
            return False
        # first = nums[0]
        # second = float('inf')这种骚操作想象不来，故可以替换成以上代码，来找first second
        for num in nums[i - 1:]:
            if num > second:
                return True
            elif first < num < second:
                second = num
            elif num < first:
                first = num
        return False