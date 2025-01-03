# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find(self, root, nodes):
        if not root:
            return
        # nodes中的节点本身是祖先，情况2
        if root in nodes:
            return root
        left = self.find(root.left, nodes)
        right = self.find(root.right,nodes)
        if left and right:
            # 左右子树中都找到了，说明当前节点是他们的祖先，情况1
            return root
        else:
            # 否则将找到的值返回即可
            return left if left else right
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        return self.find(root, nodes)