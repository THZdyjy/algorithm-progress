"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        # 二叉树层序遍历框架
        q = collections.deque()
        q.append(root)
        while q:
            sz = len(q)
            # 遍历一层
            pre = None
            for i in range(sz):
                cur = q.popleft()
                # 链接当前层所有节点的 next 指针
                if pre:
                    pre.next = cur
                pre = cur
                # 将下一层节点装入队列
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return root