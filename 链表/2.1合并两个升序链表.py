# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        l1, l2 = list1, list2
        while l1 and l2:
            if l1.val < l2.val:
                # 这是在原链表上面直接进行拼接，没有开辟任何新的节点空间。
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        # 直接拼接到后面即可。
        cur.next = l1 if l1 else l2
        return dummy.next