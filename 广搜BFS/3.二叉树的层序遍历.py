"""
广度优先搜索。
逐层遍历，这里用for循环来体现层次
"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)
        final = []
        while queue:
            res = []
            for _ in range(len(queue)):
                node = queue.popleft()
                res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            final.append(res)
        return final