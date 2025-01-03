"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        # Implementing the technique of using two pointers for linked lists
    # 施展链表双指针技巧
        a, b = p, q
        while a != b:
            # If a reaches root, it changes direction to q
            # a 走一步，如果走到根节点，转到 q 节点
            if not a:
                a = q
            else:
                a = a.parent
            # If b reaches root, it changes direction to p
            # b 走一步，如果走到根节点，转到 p 节点
            if not b:
                b = p
            else:
                b = b.parent
        return a

