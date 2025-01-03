class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head, steps):
        last_node, cur = None, head
        while cur != None and steps:
            next_node = cur.next
            cur.next = last_node
            last_node = cur
            cur = next_node
            steps -= 1
        # 最后last_node停在要反转的最后一个节点上，cur停在下一个节点上
        head.next = cur
        return last_node


    def local(self, head, left, right):
        if head == None or head.next == None:
            return head
        steps = right - left + 1
        # 建立虚拟头结点，指向head
        dummy = ListNode(0, head)
        # 定位左节点的上一个节点
        left_node = dummy
        for _ in range(left - 1):
            left_node = left_node.next

        # 反转从left 到 right 的节点
        left_node.next = self.reverseList(left_node.next, steps)

        return dummy.next


if __name__ == '__main__':
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

    solution = Solution()
    head = solution.local(node1, 1, 2)
    print('反转后的头结点是{}，其值为{}'.format(head, head.val))

    while head != None:
        print(head.val)
        head = head.next