class BSTIterator:

    def __init__(self, root: TreeNode):
        # 模拟递归栈
        self.stk = []
        # 左侧树枝一撸到底
        self.push_left_branch(root)

    def next(self) -> int:
        p = self.stk.pop()
        self.push_left_branch(p.right)
        return p.val

    def hasNext(self) -> bool:
        return bool(self.stk)

    def push_left_branch(self, p: TreeNode) -> None:
        # 左侧树枝一撸到底
        while p:
            self.stk.append(p)
            p = p.left
"""
core: 题的本意是，按照中序来遍历二叉搜索树。每调用一次next,从小到大的将二叉树的节点给到。所以核心就是push_left_branch，和栈，用它们来维护性质。
用栈来模拟，然后写一个函数用来维护中序遍历。
初始化时，先将最左边的全都入栈。即入栈73，然后调用next时，便将3出栈，再调用，7出栈，将其right进行处理，push_left_branch.就可以得到结果了，模拟走一遍就理解了
"""
