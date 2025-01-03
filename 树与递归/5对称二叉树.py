
class Solution:
    """
    core: 是否是镜像对称
    只需要遍历两个子树，使得左子树的左子树等于右子树的右子树； 左子树的右子树等于右子树的左子树
    """
    def dfs(self, left, right):
        # 递归的终止条件是两个节点都为空
		# 或者两个节点中有一个为空
		# 或者两个节点的值不相等
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.dfs(left.left, right.right) and self.dfs(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        # 调用递归函数，比较左节点，右节点
        return self.dfs(root.left, root.right)