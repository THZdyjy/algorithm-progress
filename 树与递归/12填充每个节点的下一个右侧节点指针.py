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
    """
    core: 采用遍历的思维方式，对每个节点进行处理，next指向右边的节点。
    在递归函数中，将node1和node2的左右子树，跨树分别进行连接。
    """
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def traverse(left, right):
            if not left or not right:
                return
            left.next = right
            traverse(left.left, left.right)
            traverse(right.left, right.right)
            traverse(left.right, right.left)

        if  not root:
            return root
        traverse(root.left, root.right)
        return root
