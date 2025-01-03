
class Solution:
    max_path_sum = float('-inf')

    def max_depth_weight(self, root):
        if not root:
            # 空节点的高度为0， 权重也为0
            return 0
        # 这里要和0比较下，如果权重为负的，就不加了
        left_max = max(0, self.max_depth_weight(root.left))
        right_max = max(0, self.max_depth_weight(root.right))
        # 在此过程中，更新最大路径和。因为起点和终点没有做限制，所以当前节点的最大路径和
        tmp_path_sum = left_max + right_max + root.val
        self.max_path_sum = max(self.max_path_sum, tmp_path_sum)
        # 返回当前节点的最大单边路径和
        return root.val + max(left_max, right_max)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = float('-inf')
        self.max_depth_weight(root)
        return self.max_path_sum
"""
core：题目中说了，路径不一定经过根节点。所以说起点和终点没有严格的限制。二叉树中的每个节点都可以作为起点和终点
然后本题的核心是和最大深度是一致的。
我们定义递归函数为以root为根节点的树的最大单边路径和。
比较一下，深度中，定义递归函数为以root为根节点的最大深度。
比较一下二者，最大深度，就是左右子树哪个更深，我们选择哪个，然后+1
最大单边路径和，可以理解为在深度上加了权重，我们要乘以这个权重。因此看左右子树哪个单边路径和大，我们选择哪个，然后加上root.val.
为什么是单边路径呢，因为二叉树的性质，它二叉，就跟走路似的，我们必然要选择一条。才符和题目中路径的定义：同一个节点在一条路径中至多出现一次。
同时，这个单边路径的计算，为最大路径和的计算打下基础。我们遍历每一个节点，计算以该节点root的树的最大路径和，是需要用到最大单边路径的，从左子树到右子树的一条路径。在此过程中，我们去更新这个值。
"""


