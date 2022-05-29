# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = None

class Solution:
    def reverseList(self, head):
        if head == None:
            return None
        last_node = None
        while head != None:
            next_node = head.next
            head.next = last_node
            last_node = head
            head = next_node
        return last_node
solution = Solution()
head = solution.reverseList(node1)
print(head.val)

head = node6
while head != None:
    print(head.val)
    head = head.next