class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head: return head
        dummy = ListNode(0, head)
        p, q = head, dummy
        k = 1
        while p.next:
            p = p.next
            k += 1
        step = k - n
        while step:
            q = q.next
            step -= 1
        q.next = q.next.next
        return dummy.next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        core:  链表这儿一个易混淆的问题：
        从dummy走，while p.next, 走到最后一个节点，走了length步
        从head走，while p，走到None, 走了length步
        本题，latter  former都从dummy走，fommer先走n步，然后再一起走。former走到最后一个节点时候，走了length步。此时former走了length-n步
        正好落到待删除节点的前一个
        """
        dummy = ListNode(-1, head)
        latter = former = dummy
        for i in range(n):
            former = former.next
        while former and former.next:
            former = former.next
            latter = latter.next
        latter.next = latter.next.next
        return dummy.next



if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)


    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None


    solution = Solution()
    head = solution.removeNthFromEnd(node1, 2)
    print('删除第k个节点后，头结点为{}，其值为{}'.format(head, head.val))

    while head != None:
        print(head.val)
        head = head.next