
class Solution:
    """
    core: 分解问题的方法，在后序位置得到左右子树的叶子节点。如果左右子树叶子节点都为空，说明当前节点为叶子节点，将当前的返回即可。否则返回左右子树加起来的。
    """

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # 定义递归函数：返回当前节点的叶子结点。
        def recur(root):
            if not root:
                return []
            left_leaves = recur(root.left)
            right_leaves = recur(root.right)
            if right_leaves or left_leaves:
                cur_leaves = left_leaves + right_leaves
            else:
                cur_leaves = [root.val]
            return cur_leaves

        root1_leaves = recur(root1)
        root2_leaves = recur(root2)
        return True if root1_leaves == root2_leaves else False
