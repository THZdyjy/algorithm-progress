class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        core: 利用双指针进行数组的反转。
        但是，其核心是用到了如下技巧：观察如下事实：向右轮转k个位置，则末尾的k（先取余数k=k%n）个元素跑到了开头。
        然后剩下的n-k个元素向后移动了k位。因此我们可以这样做：
        1，2，3，4，  5，6，7  k=3
        7，6，5，  4，3，2，1
        5，6，7，  1，2，3，4
        反转三次即可
        """

        def reverse(nums, l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        length = len(nums)
        k = k % length
        reverse(nums, 0, length-1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, length-1)
        return nums