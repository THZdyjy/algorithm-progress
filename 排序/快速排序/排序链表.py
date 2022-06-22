# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def output(head):
    if head == None: return
    while head:
        print(head.val,end="\t")
        head = head.next
    return
class Solution:
    def sortList(self, head, n):
        n += 1
        if head == None or head.next == None: return head
        print(head.val)
        min_value, max_value = head.val, head.val
        p = head
        while p:
            min_value = min(min_value, p.val)
            max_value = max(max_value, p.val)
            p = p.next
        if min_value == max_value: return head
        base_val = (min_value + max_value) / 2  # 不加这个就成了死循环了，没有递归出口了
        p = head

        little, big = None, None
        q = None
        while p:
            q = p.next
            if p.val <= base_val:
                p.next = little
                little = p
            else:
                p.next = big
                big = p
            p = q
        output(p)
        output(q)
        print(f'第{n}次递归，笑链表的头结点为{little.val}，大链表头结点的值为{big.val}')
        print('#'*40)
        little = self.sortList(little, n)
        big = self.sortList(big, n)
        p = little
        while p.next: p = p.next
        p.next = big
        return little

l1 = ListNode(4)
l2 = ListNode(19)
l3 = ListNode(14)
l4 = ListNode(5)
l5 = ListNode(-3)
l6 = ListNode(1)
l7 = ListNode(8)
l8 = ListNode(5)
l9 = ListNode(11)
l9 = ListNode(15)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7
l7.next = l8
l8.next = l9

s = Solution()
s.sortList(l1, 0)

# [4,19,14,5,-3,1,8,5,11,15]