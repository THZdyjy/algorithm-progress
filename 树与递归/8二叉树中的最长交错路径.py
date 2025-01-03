
class Solution:
    res = 0
    def dfs(self, root):
        # 递归出口，None节点为0，减去1得-1.这里返回两个值，代表该none节点的左右交错路径分别为-1
        if not root:
            return [-1, -1]
        # 计算左右子树的交错路径
        left = self.dfs(root.left)
        # 这里的right子树，是个列表。right[0]代表该树的左交错路径， 1代表右交错路径。
        right = self.dfs(root.right)
        # 在后续位置更新当前节点的交错路径
        left_cross = left[1] + 1
        # 右交错路径 = 右子树的左交错路径 + 节点，其中左交错路径为right[0],
        right_cross = right[0] + 1
        # 更新
        self.res = max(self.res, max(left_cross, right_cross))
        return [left_cross, right_cross]

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        return self.res
"""
core:采用分解子问题的方式，计算当前节点的左右交错路径，哪个长，就取哪个，再加一。遍历所有节点，在此过程中，更新res的值。
这里面的核心是：左右交错路径该如何定义
左交错路径 = 左子树的右交错路径 + 节点
右交错路径 = 右子树的左交错路径 + 节点
举例：拿实例1来说，对于root1， 其左交错路径为0. 右交错路径为2，看图右左。3-1=2，因此该节点的交错路径长度即为2.然后遍历每一个节点，发现第二个节点1的交错路径最长。为3.
"""