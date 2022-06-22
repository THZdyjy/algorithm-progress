# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq
class Solution:
    def mergeKLists(self, lists):
        heap = []
        ret = ListNode(0, None)
        p = ret
        # for i in range(len(lists)):
        #     if lists[i]:
        #         heapq.heappush(heap, (lists[i].val, i))
        #         print((lists[i].val, i))
        #         lists[i] = lists[i].next
        #         print(lists[i].val)
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i))
                print((node.val, i))
                node = node.next
                print(node.val)
        while len(heap) != 0:
            val, idx = heapq.heappop(heap)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                temp = lists[idx]
                temp_val = temp.val
                heapq.heappush(heap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return ret.next

a = ListNode(1)
b = ListNode(4)
c = ListNode(5)
a.next = b
b.next = c
c.next = None

d = ListNode(1)
e = ListNode(3)
f = ListNode(4)
d.next = e
e.next = f
f.next = None

g = ListNode(2)
h = ListNode(6)
g.next = h
h.next = None

s = Solution()
s.mergeKLists([a, d, g])