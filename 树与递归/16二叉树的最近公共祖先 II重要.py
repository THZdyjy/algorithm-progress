class Solution:
    found_p = False
    found_q = False
    """
    如果p或q之一不存在于该二叉树中，返回null p和q不一定都存在，因此标准中的第二种情况不再适用。
    """

    def find(self, root, p, q):
        if not root:
            return

        left = self.find(root.left, p, q)
        right = self.find(root.right, p, q)
        # 如果左右子树中都找到了，说明当前节点是他们的祖先
        if left and right:
            return root
        # 后序位置，判断当前节点是不是目标值
        if root == p or root == q:
            # 找到了，记录一下
            if root == p:
                self.found_p = True
            if root == q:
                self.found_q = True
            return root

        return left if left else right

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = self.find(root, p, q)
        if self.found_p and self.found_q:
            return res
        else:
            return None

"""

对下面具体说明一下：
当左右子树不同时存在时，剩下的情况还有两种：
只有其中一个树有：root也有，那么root就是lca，那么返回root即可(必须得记录)；root没有，返回left or right
都没有：看看root有没，有的话记录下是哪个，没有的话，返回None

elif left or right:
    if root == p or root == q:
        if root == p:
            self.found_p = True
        if root == q:
            self.found_q = True
        return root
    else:
        return left if left else right
else:
    if root == p or root == q:
        # 找到了，记录一下
        if root == p:
            self.found_p = True
        if root == q:
            self.found_q = True
        return root
    else:
        return None
@labuladong的题解中，将这两种情况合并了。
"""