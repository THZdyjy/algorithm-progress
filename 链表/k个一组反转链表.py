# Definition for singly-linked list.
"""
①定义虚头dummy，指向head，每次向前走k步，若所在的节点不为None，则进行反转
②进行反转
③链接
④重复进行

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 用递归来解决，待思考
class Solution2:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur = head
        count = 0
        while cur and count!= k:
            cur = cur.next
            count += 1
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                count -= 1
            head = cur
        return head

class Solution:
    def reverseList(self, head, steps):
        last_node, cur = None, head
        while cur != None and steps:
            next_node = cur.next
            cur.next = last_node
            last_node = cur
            cur = next_node
            steps -= 1
        head.next = cur
        return last_node


    def reverseKGroup(self, head, k):
        if head == None or head.next == None:
            return head
        dummy = ListNode(0, head) # 虚拟头节点
        p = dummy
        has_two_nodes = p  # 用来探索接下来的k的节点是否为空，为空就停止反转
        # 当需要执行这样一个问题：遍历一个数据结构，当满足某种条件时，停下来，进行某种操作，之后，继续遍历。可以使用while True
        while True:
            for _ in range(k):
                has_two_nodes = has_two_nodes.next
                if has_two_nodes == None : return dummy.next
            p.next = self.reverseList(p.next, k)
            for _ in range(k):
                p = p.next
        return dummy.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = None

    solution = Solution2()
    head = solution.reverseKGroup(node1, 2)
    print('反转后的头结点是{}，其值为{}'.format(head, head.val))

    while head != None:
        print(head.val)
        head = head.next