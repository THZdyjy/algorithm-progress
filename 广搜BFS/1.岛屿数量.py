
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def valid(r, c, grid):
            if r < 0 or r >= len(grid):
                return False
            if c < 0 or c >= len(grid[0]):
                return False
            if grid[r][c] == "1":
                return True
            else:
                return False

        def bfs(r, c, grid, res):
            # j2: 周边点的提取
            queue.append([r, c])
            # j3: 剪枝
            grid[r][c] = "#"
            while queue:
                cur_r, cur_c = queue.popleft()
                # j4：如何定义周边点及其遍历
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    r = cur_r + dr
                    c = cur_c + dc
                    if not valid(r, c, grid):
                        continue
                    # j5：直至遍历完所有点
                    queue.append([r,c])
                    grid[r][c] = "#"

        # j1:注意变量的有效范围，python知识
        res = 0
        queue = collections.deque()
        row, col = len(grid), len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    bfs(r, c, grid, 0)
                    res += 1
        return res

"""
bfs模板：
    数据结构：
        ①用队列collections.deque来解决，入队的内容需要设计
        ②visited用来对访问过的元素进行处理
    算法：
        1.从一个已知点出发，遍历他的周边（注：①什么是已知点，这里是为1的点 ②如何找到周边点）
        2.再从周边依次提取点，遍历周边的周边（注：①判断周边点是否valid,无效continue ②有效，加入队列，并更改状态。用到了queue,来提取周边；用到了visitde来进行剪枝）
        3.直至遍历完所有的周边。

core:
    找联通区域的，明显用bfs来解决。
    从左到右，从上到下，如果是1，可以作为岛屿的入口，从这个入口去遍历他的上下左右。bfs。遍历过的要进行记录，下次就不访问了，否则重复，这是一个剪枝的过程。
    同时需要判断该节点是否是valid, 如果有效，会加入队列，继续bfs.否则我们看下一个点。

"""