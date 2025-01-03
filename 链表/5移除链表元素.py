# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
core:思路，因为要删除链表元素，从前往后删的话，当前节点上一个节点你不清楚，没法删。所以想到从最后一个删。那么就需要用到递归。
定义递归函数：删除当前节点的下一个节点（满足条件时）。递归出口：None。 当前层逻辑处理，如果下一个节点需要删除（有），则删除下一个节点。然后判断当前节点是否需要删除，是，将当前节点返回，否，返回None.
"""
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        def recur(node, value):

            if not node:
                return
            delete_node = recur(node.next, value)
            if delete_node:
                node.next = delete_node.next
            if node.val == value:
                return node
            return


        dummy = ListNode()
        dummy.next = head
        recur(dummy, val)
        return dummy.next
# 非递归
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(-1, head)
        p = dummy
        # 注意p.next 的前提是p不为None
        while p and p.next:
            # 当p.next为删除元素时，将它删除，直到下一个元素不再是待删除元素
            while p.next and p.next.val == val:
                p.next = p.next.next
            p = p.next
        return dummy.next