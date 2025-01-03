# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
保留一个重复元素
core: 建立虚拟头节点，从dummy开始，看看后面两个元素是否重复。若是，新建指针，找到最后一个位置。p指向它即可。
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        dummy = ListNode(-1, head)
        p = dummy
        # j1：从dummy这个头节点开始，看看后面两个节点是否相同，相同的话就是重复的。
        while p.next and p.next.next:
            if p.next.val == p.next.next.val:
                # j2：如果两个节点重复，从第二个重复节点看，看后面是否还有重复的
                last = p.next.next
                # j3：一直走，走到最后一个重复节点，将p指向它
                while (last and last.next) and (last.val == last.next.val):
                    last = last.next
                p.next = last
            else:
                p = p.next
        return dummy.next