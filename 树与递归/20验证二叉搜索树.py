class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, lower, upper):
            if not root:
                return True
            if lower and root.val <= lower.val:
                return False
            if upper and root.val >= upper.val:
                return False
            # 核心，根节点，给左子树规定了上界（不能比我挣得多）；给右子树规定了下界（不能比我干活少）
            return helper(root.left, lower, root) and helper(root.right, root, upper)

        return helper(root, None, None)

"""
core: 二叉搜索树，其左子树所有节点的值都要小于根节点；右子树所有节点的值都要大于根节点。
因此这道题，给节点设置一个上下界。这个节点要处于这个范围内。否则就是False.
如何设置呢：将父节点root作为左子树的上界给到左子树，作为下界给到右子树。这样就可以了
本质：root节点作为上界给到左子树，那么子树中的所有节点都不会比他大。例如左图（力扣官方题解））中的例子，对与节点7，4给他传过来时，是作为下界给到他的。7的上界依然是5.
继续探究：可以将二叉搜索树看为等级森严的封建制度。 根节点5对左子树说了，你们的收入不能超过我。我是5，你们不能超过5，我始终作为这条界限卡着你们。对于左边的，肯定是5>4>1, 但是到7这里，它要比4大。于是4和他说，你一定是比我大的，但是你也不能大过咱们得头儿5呀，现在你比他大了，你等着被枪毙吧。
"""