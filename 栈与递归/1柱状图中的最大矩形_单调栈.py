class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0: return 0
        max_area, stack = 0, []  # 辅助栈存储数组下标
        # j1:右边界r遍历数组下标。遍历到数组后一位，目的是处理完辅助栈剩下的下标, 并将该处高度定义为0
        heights = heights + [0]
        for r, cur_height in enumerate(heights):

            # j2:如果栈不为空且 当前高度小于栈顶索引对应的高度，说明找到了右边界，开始计算面积.heights[stack[-1]]为target_height
            while stack and cur_height < heights[stack[-1]]:
                idx = stack.pop()
                # j4：栈为空了，左边界为-1
                l = stack[-1] if stack else -1
                # j5：面积的计算
                max_area = max(max_area, heights[idx] * (r - l - 1))
            stack.append(r)
        return max_area

"""
core: heights数组给定了高度。遍历这个数组，计算每个高度对应的左右边界即可。
    具体来说,遍历数组，其下标r作为右边界。考察该当前右边界对应的当前高度与栈顶索引对应的高度，如果小于，则说明右边界找到了。
    然后找左边界：因为栈维护的是一个单调递增栈，（入栈过程中，后一高度小于前一高度就把前面的出栈了），所以目标索引（栈顶元素）的左边一位即是左边界。
    计算面积即可。
    trick: 辅助栈为单调递增栈，维护的是依次增高的高度。我们遍历一遍数组，就能找到所有柱子对应的左右边界，所以时间复杂度为O(n)。具体的就是当前高度小于前面的时候，就不断出栈，这样就能把所有的柱子对应的面积算出来了。
    simplify: 维护单调递增栈，遇见小的出栈计算，遇见大的就入栈遍历。
"""