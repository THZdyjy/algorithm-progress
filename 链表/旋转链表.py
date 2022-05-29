class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
这道题要注意的点：k的取值范围，k有可能比链表的length大，所以需要做一个取余的操作。还是读题，审题，将题目理解透彻。
"""
class Solution:
    def rotateRight(self, head, k):
        cur = head
        length = 1
        while cur.next:
            cur = cur.next
            length += 1
        cur.next = head
        k = k % length
        steps = length - k
        cur = head
        for _ in range(steps - 1):
            cur = cur.next
        rotate_head = cur.next
        cur.next = None
        return rotate_head

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
    head = solution.rotateRight(node1, 2)
    print('旋转后的头结点是{}，其值为{}'.format(head, head.val))

    while head != None:
        print(head.val)
        head = head.next