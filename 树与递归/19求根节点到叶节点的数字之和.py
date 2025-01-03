class Solution:
    """
    core: 从根节点开始，遍历每个节点，如果遇到叶子节点，则将叶子节点对应的数字加到数字之和。
    如果当前节点不是叶子节点，则计算其子节点对应的数字，然后对子节点递归遍历。
    在前序位置得到当前节点的值，然后递归遍历左右子树，将得到的值加起来。
    """
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, prevTotal: int) -> int:
            if not root:
                return 0
            total = prevTotal * 10 + root.val
            if not root.left and not root.right:
                return total
            else:
                return dfs(root.left, total) + dfs(root.right, total)

        return dfs(root, 0)

