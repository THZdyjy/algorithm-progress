class Solution:
    """
    core: 双指针
    """
    def maxArea(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        area = 0
        while l <= r:
            cur_height = height[l] if height[l] < height[r] else height[r]
            cur_area = (r - l) * cur_height
            area = max(area, cur_area)
            # j1: 计算完面积后再更新指针位置
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area

