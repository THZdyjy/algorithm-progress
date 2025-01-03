class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        """
        core:其子问题是：柱状图中的最大矩形（维护单调递增的辅助栈）
        然后 用prefix来记录每一层的矩形高度。
        时间复杂度O(mn)；空间复杂度O(n)
        """

        def get_row_rectangle(heights):
            heights = heights + [0]
            stack, max_area = [], 0
            for r, height in enumerate(heights):
                while stack and height < heights[stack[-1]]:
                    idx = stack.pop()
                    l = stack[-1] if stack else -1
                    max_area = max(max_area, heights[idx] * (r - l - 1))
                stack.append(r)
            return max_area

        final_area = 0
        rows, cols = len(matrix), len(matrix[0])
        prefix = [0] * cols
        for i in range(rows):
            for j in range(cols):
                # j1:prefix 记录每一层矩形的高度
                prefix[j] = prefix[j] + 1 if matrix[i][j] == "1" else 0

            cur_max = get_row_rectangle(prefix)
            final_area = max(cur_max, final_area)
        return final_area



