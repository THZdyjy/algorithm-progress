class Solution:
    def trap(self, height: List[int]) -> int:
        """
        core: 双指针，在左右指针移动的过程中，维护左边最大高度leftmax，右边最大高度rightmax。
        此时联想图片（官方题解）。如果左边的高的柱子>右边最高的柱子。则接雨水量取决于右边柱子最大高度（木桶效应）此时从右往左遍历与计算。
        在此过程中，更新为何左右柱子的最大高度即可。
        时间复杂度，O（n），因为不使用额外空间，故空间复杂度为O(1)
        """
        # 边界条件判断
        if len(height) <= 2:
            return 0

        left, right = 0, len(height) - 1
        leftmax, rightmax = height[left], height[right]
        ans = 0
        while left < right:
            if leftmax < rightmax:
                ans += (leftmax - height[left])
                left += 1
            else:
                ans += (rightmax - height[right])
                right -= 1

            leftmax = max(leftmax, height[left])
            rightmax = max(rightmax, height[right])
        return ans 

