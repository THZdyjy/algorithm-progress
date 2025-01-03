class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
这道题要注意的点：k的取值范围，k有可能比链表的length大，所以需要做一个取余的操作。还是读题，审题，将题目理解透彻。
"""
class Solution:
    def rotateRight(self, head, k):
        p = head
        num = 1
        while p.next:
            p = p.next
            num += 1
        print(num)
        p.next = head
        k = k % num
        step = num - k - 1
        p = head
        while step > 0:
            P = p.next
            step -= 1
        next_node = p.next
        p.next = None

        return next_node

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