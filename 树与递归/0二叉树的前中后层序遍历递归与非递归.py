import collections
# 前序遍历
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    def dfs(root):
        if not root:
            return
        res.append(root.val)
        dfs(root.left)
        dfs(root.right)
        return
    res = []
    dfs(root)
    return res


# 非递归写法
def preorderTraversal(self, root):
    if not root:
        return []
    # 为了保持后续代码的统一性，定义一个双端队列来模拟栈。或者直接用列表即可。
    stack = collections.deque()
    stack.append(root)
    res = []
    while stack:
        # 栈的性质：先入后出，因此我们在入栈时，先入右子树
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)
    return res



# 中序遍历
def inorderTraversal(self, root):
    def dfs(root):
        if not root:
            return
        dfs(root.left)
        res.append(root.val)
        dfs(root.right)
    res = []
    dfs(root)
    return res


# 非递归写法
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = collections.deque()
        pos = root
        res = []
        while pos or stack:
            # 中序遍历，左根右，所以将左节点不断入栈，直至左节点为null
            while pos:
                stack.append(pos)
                pos = pos.left

            # 当前节点的左子树为空，所以不必添加。即左子树访问完了，因此需要在当前位置，添加处理逻辑
            node = stack.pop()
            res.append(node.val)
            pos = node.right # 去迭代右子树
        return res



# 后序遍历
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        # 维护栈2，进栈顺序为跟右左，则出栈顺序为左右跟，即为后序遍历
        # stack 先按跟左右append，再弹出并添加到stack2,这时为跟右左，最后弹出Stack2，即为左右跟，后续遍历。
        """
        if not root:
            return list()

        stack = [root]
        stack2 = []
        res = []
        while stack:
            node = stack.pop()
            # stack2依次入栈，根节点，右子树，左子树
            stack2.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        while stack2:
            node = stack2.pop()
            res.append(node.val)

        return res



# 层序遍历 bfs，前三者都是dfs 完全二叉树的节点个数
    def _countNodes(self, root):
        queue = collections.deque()
        queue.append(root)
        sum = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                sum += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return sum

    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        return self._countNodes(root)
