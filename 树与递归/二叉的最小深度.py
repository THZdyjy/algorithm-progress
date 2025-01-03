# 递归写法
class Solution:
    def minDepth(self, root):
        def dfs(root):
            # 定义递归函数为以当前节点为root的树，其最小深度。当该节点为一个叶子节点时，直接返回1即可。如果其有左右子树，得到其左右子树的最小深度。然后比较左右子树的深度，返回最小的+1即可。
            if root.left == None and root.right == None:
                return 1
            depth = float("+inf")  # 该值设置的必要性
            if root.left:
                depth = min(depth, dfs(root.left))
            if root.right:
                depth = min(depth, dfs(root.right))
            return depth + 1

        if not root:
            return 0
        return dfs(root)

# 非递归写法