
# 递归->遍历
class Solution:
    """
    core:回溯的思路，遍历一遍二叉树的每个节点, 用一个外部变量记录每个节点所在的深度，取最大值就可以得到最大深度。
    当入节点时候，即前序位置，将深度加1.然后去遍历左右子树。在后续位置，即出节点的时候，depth-1.
    至于对 res 的更新，放到前中后序位置都可以，只要保证在进入节点之后，离开节点之前（即 depth 自增之后，自减之前）就行了
    本解法在前序位置和后续位置都添加了核心代码逻辑。
    """
    def traverse(self, root, res, depth):

        if not root:
            return
        # 前序位置
        depth += 1
        # 到了叶子节点,更新
        if not root.left and not root.right:
            res[0] = max(res[0], depth)

        self.traverse(root.left, res, depth)
        # 中序位置

        self.traverse(root.right, res, depth)
        # 后序位置
        depth -= 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = [0]
        depth = 0
        self.traverse(root, res, depth)
        return res[0]

"""
# ***重要***: 重新理解前中后序位置。 在左右子树中间的位置，就是中序位置。在左子树之前的位置，即前序位置。在右子树之后的位置，即后续位置。根据问题，

#核心代码代码逻辑集可以放在任意一个位置或者多个位置.

# 而一般来说，前序只能利用传入的参数信息。而后续位置能够利用的还有左右子树返回来的信息。

遇到一道二叉树的题目时的通用思考过程是：

1、是否可以通过遍历一遍二叉树得到答案？如果可以，用一个 traverse 函数配合外部变量来实现。

2、是否可以定义一个递归函数，通过子问题（子树）的答案推导出原问题的答案？如果可以，写出这个递归函数的定义，并充分利用这个函数的返回值。

3、无论使用哪一种思维模式，你都要明白二叉树的每一个节点需要做什么，需要在什么时候（前中后序）做。
"""


# 递归->分解子问题

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        core: 分解为子问题的思路
        给递归函数下定义：输入根节点，返回这课二叉树的最大深度.
        可以通过子树的最大深度推导出原树的深度，利用递归函数的定义算出左右子树的最大深度，然后推出原树的最大深度，因此对depth的更新放在后续位置。
        """
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        # 后序位置，
        depth = max(left, right) + 1

        return depth

# 迭代法
def maxDepth(self, root: TreeNode) -> int:
    level = [root] if root else []
    depth = 0
    while level:
        depth += 1
        queue = []
        for item in level:
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
        level = queue
    return depth