# 递归的方法，广度优先搜索
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        def dfs(root, level):
            if not root:
                return
                # 在前序位置， 将节点值放到相应的sum[i], 其对应的count[i] + 1
            if level >= len(totals):  # 新的层，进行新建
                totals.append(root.val)
                counts.append(1)
            else:
                totals[level] += root.val
                counts[level] += 1
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        totals = list()
        counts = list()
        dfs(root, 0)
        return [total / count for total, count in zip(totals, counts)]

"""
core: 利用level这个核心变量。来维护层次。
然后使用totals，counts两个列表，记录每一层的节点值总和与数量总和。在前序位置进行更新。
这样，递归的时候，每一层都有level这个变量的指引，就可以正确的将节点进行归类了。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 迭代法
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            layer_sum = 0
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                layer_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(layer_sum / size)
        return res