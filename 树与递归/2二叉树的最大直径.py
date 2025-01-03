# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:

    def __init__(self):
        # 记录最大直径的长度
        self.maxDiameter = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxDepth(root)
        return self.maxDiameter

    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        # 后序位置，顺便计算最大直径
        myDiameter = leftMax + rightMax
        self.maxDiameter = max(self.maxDiameter, myDiameter)

        return 1 + max(leftMax, rightMax)
"""
core:二叉树的直径，即左右子树的最大深度和。因此要计算左右子树的最大深度
递归函数定义：当前节点的最大深度
得到左子树的最大深度，得到又子树的最大深度
在后续位置计算当前节点的最大深度
更新最大深度的值
最后将这个值返回即可
比较二叉树的最大深度
"""