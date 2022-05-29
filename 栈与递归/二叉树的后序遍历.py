"""
递归是最简单的做法
不用递归的话，用栈来实现
"""

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack = [root]
        stack2 = []
        res = []
        while stack:
            root = stack.pop()
            stack2.append(root)
            if root and root.left: stack.append(root.left)
            if root and root.right: stack.append(root.right)
        while stack2:
            res.append(stack2.pop().val)
        return res
