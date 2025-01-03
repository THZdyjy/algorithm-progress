class Solution:

    def max_depth(self, root, res):
        if not root:
            # 对于为空的节点，返回高度0
            return 0
        # j2：得到当前节点的所在高度
        h = max(self.max_depth(root.left, res), self.max_depth(root.right, res)) + 1
        # j3: 在后序位置将同一高度的节点放到res中, 首先要判断高度为h的存贮列表是否已经新建
        if len(res) < h:
            res.append([])
        res[h - 1].append(root.val)
        return h

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.max_depth(root, res)
        return res
"""
core: 核心思路是得到每个节点的最大深度，例如实例1, 节点4和5和3最大深度都是1，因此将他们放在同一层。1的最大深度是3，因此将它放在一层。如此，遍历每个节点。
该题利用最大深度（参看543二叉树的直径）来解决。其本质是后序遍历。因为我们在前中序的位置先得到当前节点的最大深度。然后在后续位置，利用这个信息来更新res的结果，即将属于同一高度的叶子节点放到结果中

思考：层序遍历的角度来看，3和2是同一层的。
但是如果，从最大深度角度来看，3和节点4,5一样都是叶子节点，他们是同一层的。
题目的要求与相关概念的定义决定了我们看待问题的角度，从而挖掘出深层次的一些性质，然后利用这些性质和已有的一些模板套路来解决个性化的题目。
"""