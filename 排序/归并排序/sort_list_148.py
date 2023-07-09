# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def merge_sort(head, n):
    if not head or not head.next: return head
    # 划分左右两半部分，拆分链表，然后递归排序
    l = n // 2
    r = n - l
    pl, pr_tmp, tmp = head, head, l
    ret = ListNode(0, None)
    p = ret
    while tmp - 1:
        pr_tmp = pr_tmp.next
        tmp -= 1
    pr = pr_tmp.next
    pr_tmp.next = None
    watch1, watch2 = pl.val, pr.val
    pl = merge_sort(pl, l)
    pr = merge_sort(pr, r)
    while pl or pr:
        if pr == None or (pl != None and pl.val < pr.val):
            p.next = pl
            pl = pl.next
            p = p.next
        else:
            p.next = pr
            pr = pr.next
            p = p.next
    return ret.next


class Solution:
    def sortList(self, head):
        # 采用归并排序，需要分而治之，即将链表分为左右两部分，因为链表是相连的
        # 且不能通过索引来定位，故在进行归并排序的时候，根据其长度，拆分为左右两半部分
        # 然后在进行递归合并
        p = head
        n = 0
        while p:
            p = p.next
            n += 1
        return merge_sort(head, n)

a = ListNode(4)
b = ListNode(2)
c = ListNode(3)
d = ListNode(1)
a.next = b
b.next = c
c.next = d
d.next = None

s = Solution()
s.sortList(a)
