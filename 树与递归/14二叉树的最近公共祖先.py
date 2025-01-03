# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    core:
    """

    def find(self, root, p, q):
        if not root:
            return
        if root == p or root == q:
            return root
        left = self.find(root.left, p, q)
        right = self.find(root.right, p, q)
        if left and right:
            return root
        else:
            return left if left else right

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.find(root, p, q)
