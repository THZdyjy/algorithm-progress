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


# 递归法
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def recur(head):
            """
            core:
            # 这里的递归出口是当前节点的下一个节点为None时，直接返回当前节点。
            # 当前节点作为反转后链表的头节点。
            :return: 反转后链表的头节点
            时间复杂度：O(n))，其中 n 是链表的长度。需要对链表的每个节点进行反转操作。
            空间复杂度：O(n)，其中 n 是链表的长度。空间复杂度主要取决于递归调用的栈空间，最多为 n 层
            """

            if not head.next:
                return head
            # j1,递归函数返回的是反转后链表的头节点
            node = recur(head.next)
            # j2, 当前层的反转与断开操作
            head.next.next = head
            head.next = None
            return node
        if not head:
            return head
        return recur(head)