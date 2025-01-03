"""
core: 这道题是找一条路径，且路径的起点就是左上角，终点就是右下角。因此这里可以作为一个corner case判断一下。
然后，它要找到这么一条路径，入口点已经确定了，就是左上角。因此不需要像岛屿数量那样，挨个判断每个点。从入口点进去，对八个方位进行bfs后，如果能够到达左下角，则将路径长度返回。否则需要返回-1.
"""

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        def valid(r, c, grid):
            # j4: 判断边界条件。or的关系
            if r < 0 or r >= len(grid):
                return False
            if c < 0 or c >= len(grid[0]):
                return False
            if grid[r][c] == 0:
                return True
            else:
                return False

        def bfs(r, c, grid, n):
            queue = collections.deque()
            queue.append((r, c, 1))
            grid[r][c] = "#"
            while queue:
                cur_r, cur_c, cur_dist = queue.popleft()
                # j2: 当到达最终点时，结束
                if cur_r == n - 1 and cur_c == n - 1:
                    return cur_dist
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (1, -1), (-1, 1)):
                    r, c = cur_r + dr, cur_c + dc
                    if not valid(r, c, grid): continue
                    # j3:不重不漏，标记状态
                    queue.append((r, c, cur_dist+1))
                    grid[r][c] = "#"
            # 最终遍历完，没有合适的路径的话，到达不了终点，返回-1
            return -1


        # j1:边界判断，题目中要求了这条路径的所有单元格为0， 且从左上角开始，到右下角结束，
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        # 路径是确定性的，就是从左上角开始，不用像岛屿数量那样，遍历所有点。
        return bfs(0, 0, grid, n)
