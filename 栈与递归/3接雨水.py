class Solution:
    def trap(self, height: List[int]) -> int:
        """
        core:维护一个单调递减的栈， 当前柱子高度大于目标柱子高度时，便出栈，计算盛的雨水。
        时空复杂度均为O(n)
        """
        length = len(height)
        stack, ans = [], 0
        # 遍历右边界
        for r, r_height in enumerate(height):
            # j1：维护单调递减栈
            while stack and r_height > height[stack[-1]]:
                target_index = stack.pop()
                if not stack:
                    break
                # j2：左边界为targe左边的柱子，即栈顶索引对应的
                l = stack[-1]
                # j3：高度的计算，不要忘记减掉targer柱子的高度
                h = min(r_height, height[l]) - height[target_index]
                # j4：注意target柱子能够盛的水是怎么计算的
                ans += (r - stack[-1] - 1) * h
            stack.append(r)
        return ans
