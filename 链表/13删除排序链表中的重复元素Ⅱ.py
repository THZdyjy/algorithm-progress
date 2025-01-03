# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 不保留重复元素
"""
core: 建立虚拟头节点，从dummy开始，看看后面两个元素是否重复。若是，新建指针，找到非重复节点。p指向它，即跳过了所有重复节点。
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None: return head
        dummy = ListNode(0, head)
        p = dummy
        # j1；从dummy这个头节点开始，看看后面两个节点是否相同，相同的话就是重复的。
        while (p.next and p.next.next):
            if p.next.val == p.next.next.val:
                # j2：如果两个节点重复，从第二个重复节点的下一个节点看，看是否还有重复的
                pre = p.next.next.next
                # j3：跳到不再重复的节点，将p指向它，跳过所有重复的节点。在这里比较和1的区别。
                while (pre and pre.val == p.next.val): pre = pre.next
                p.next = pre
            else:
                p = p.next
        return dummy.next