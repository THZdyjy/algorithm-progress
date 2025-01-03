# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        # 递归：将以root为根节点的二叉树拉平；拉平左右子树
        self.flatten(root.left)
        self.flatten(root.right)
        # 记录当前节点的左右子树节点
        left = root.left
        right = root.right
        # 当前节点的左子树为空，将拉平的左子树放过来
        root.left = None
        root.right = left
        # 将拉平的右子树接到左子树末尾, 从root节点走，第27行走到原拉平的左子树末尾，然后连接
        p = root
        while p.right:
            p = p.right
        p.right = right
        return root