# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
core: 快慢指针+反转链表（反转后半部分）
"""


class Solution:
    # 递归
    def reverse(self, head):
        if not head.next:
            return head
        node = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return node

    # 非递归
    def reverse2(self, head):
        last_node = None
        while head != None:
            next_node = head.next
            head.next = last_node
            last_node = head
            head = next_node
        return last_node

    def pairSum(self, head: Optional[ListNode]) -> int:
        # j1:快慢指针找到待反转的后半部分的头节点
        dummy = ListNode(-1, head)
        fast = slow = dummy
        while fast.next:
            slow = slow.next
            fast = fast.next.next
        # j2：对后半部分进行反转
        slow.next = self.reverse2(slow.next)

        # j3：计算孪生和
        pair_head = slow.next
        p = head
        max_pair_sum = 0
        while pair_head:
            pair_sum = pair_head.val + p.val
            max_pair_sum = max(max_pair_sum, pair_sum)
            pair_head = pair_head.next
            p = p.next
        return max_pair_sum
