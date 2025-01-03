class Solution:
    # 在 BST 中寻找 val1 和 val2 的最近公共祖先节点
    def find(self, root: TreeNode, val1: int, val2: int) -> TreeNode:
        if not root:
            return None
        if root.val > val2:
            # 当前节点太大，去左子树找
            return self.find(root.left, val1, val2)
        elif root.val < val1:
            # 当前节点太小，去右子树找
            return self.find(root.right, val1, val2)

        # min_val <= root.val < max_val
        # min_val < root.val <= max_val
        else:
            # val1 <= root.val <= val2
            # 则当前节点就是最近公共祖先
            return root

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        # 保证 val1 较小，val2 较大
        val1 = min(p.val, q.val)
        val2 = max(p.val, q.val)
        return self.find(root, val1, val2)

"""
core: 找到最近公共祖先，由于是二叉搜索树，所有要充分利用其左小，右大的性质
对于p和q,其中一个是小值，一个是大值。那么我们比较当前节点值，与他们的大小。
如果pq中的小值还大于root.val， 说明pq都在右子树中，去右子树寻找
反之pq中的大值还小于root.val， 说明pq都在左子树中，去右子树寻找
"""

"""
但对于 BST 来说，根本不需要老老实实去遍历子树，由于 BST 左小右大的性质，将当前节点的值与 val1 和 val2 作对比即可判断当前节点是不是 LCA：
假设 val1 < val2，那么 val1 <= root.val <= val2 则说明当前节点就是 LCA；若 root.val 比 val1 还小，则需要去值更大的右子树寻找 LCA；若 root.val 比 val2 还大，则需要去值更小的左子树寻找 LCA。
"""