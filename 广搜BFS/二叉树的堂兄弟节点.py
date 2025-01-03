# bfs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 技巧：bfs是一层一层的来遍历，因此可以用for _ in range(len(queue))遍历某一层。并用level来记录层数。
import collections
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # 广度优先遍历
        # 模板，用queue来解决
        # 是不是堂兄弟节点需要用其深度和父节点来比较，所以需要记录这两个状态

        queue = collections.deque()
        queue.append([root, None])
        level = 0
        xd, yd, xf, yf = None, None, None, None
        while queue:
            for _ in range(len(queue)):
                node, father = queue.popleft()
                if node.val == x:
                    xd = level
                    xf = father
                if node.val == y:
                    yd = level
                    yf = father
                if node.left:
                    queue.append([node.left, node])
                if node.right:
                    queue.append([node.right, node])
            level += 1
        return xd == yd and xf != yf


# dfs
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # dfs
        # 深度优先遍历，用递归来解决，设计递归函数的意义
        # 递归函数：从该root节点开始，其左右子树中是否存在x,y,若存在，记录x,y的层级和他们的父节点。因此，我们传入root，其父节点，x和y
        xd, yd, xf, yf = None, None, None, None

        def dfs(node, father, x, y, level):
            nonlocal xd, yd, xf, yf
            # 定义递归出口
            if not node:
                return
                # 进行当前层的一个操作, 记录层级与父节点
            if node.val == x:
                xd = level
                xf = father
            if node.val == y:
                yd = level
                yf = father
            # 进行递归
            dfs(node.left, node, x, y, level + 1)
            dfs(node.right, node, x, y, level + 1)

        dfs(root, None, x, y, 0)
        return xd == yd and xf != yf
