class Solution:
    """
    这题有两个思路：
    1、用 BFS 层序遍历算法，每一层的最后一个节点就是二叉树的右侧视图。我们可以把 BFS 反过来，从右往左遍历每一行，进一步提升效率。
    2、用 DFS 递归遍历算法，同样需要反过来，先递归 root.right 再递归 root.left，同时用 res 记录每一层的最右侧节点作为右侧视图。
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)

        res = []
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                if i == length - 1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res



class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def traverse(root: TreeNode):
            nonlocal depth
            if not root:
                return
            # 前序遍历位置
            depth += 1
            if len(res) < depth:
                # 这一层还没有记录值
                # 说明 root 就是右侧视图的第一个节点
                res.append(root.val)
            # 注意，这里反过来，先遍历右子树再遍历左子树
            # 这样首先遍历的一定是右侧节点
            traverse(root.right)
            traverse(root.left)
            # 后序遍历位置
            depth -= 1

        res = []
        # 记录递归的层数
        depth = 0
        traverse(root)
        return res