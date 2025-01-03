class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.val == key:
            # 这两个 if 把情况 1 和 2 都正确处理了
            # 其中，key对应叶子节点的情况，已经包含在里面了。返回的是None,返回到上一层，父节点指向的就是None,这不就相当于把他删除了吗。
            if root.left == None:
                return root.right
            if root.right == None:
                return root.left
            # 处理情况 3
            # 获得右子树最小的节点
            minNode = self.getMin(root.right)
            # 删除右子树最小的节点，不当四品官了
            root.right = self.deleteNode(root.right, minNode.val)
            # 用右子树最小的节点替换 root 节点， 来当二品
            minNode.left = root.left
            minNode.right = root.right
            root = minNode
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root

    def getMin(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        # BST 最左边的就是最小的
        while node.left != None:
            node = node.left
        return node
"""
core: 递归函数：删除以root为根节点的树中，key对应的节点。返回删除节点后的树的根节点。
思路是先找节点，找到之后再将该节点删除。如何删除呢？核心是找到替代它的节点。这里分如下情况讨论：
    A是叶子结点，子节点都为空，直接删掉即可
    A只有一个非空子节点，那么它要让这个孩子接替自己的位置
    A 有两个子节点，为了不破坏 BST 的性质，A 必须找到左子树中最大的那个节点，或者右子树中最小的那个节点来接替自己。两种选一种即可。
"""