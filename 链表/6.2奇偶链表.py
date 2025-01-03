# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        core: 思路同分割链表。拆分成奇偶两个小链表。然后再连起来
        """
        # key: 建立奇偶空节点。奇数的为一组，偶数的为一组。不要将他们与head连接起来，到底连接与否，看题意。
        odd = odd_dummy = ListNode()
        even = even_dummy = ListNode()
        p = head
        flag = 1
        while p:
            if flag % 2:
                odd.next = p
                odd = odd.next
            else:
                even.next = p
                even = even.next
            flag += 1
            tmp = p.next
            p.next = None
            p = tmp
        odd.next = even_dummy.next
        return odd_dummy.next
