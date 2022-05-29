class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
删除排序链表中的重复元素，使每个元素只出现一次 。返回已排序的链表 。
如何将重复的元素全部删除，一次都不剩下
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None: return head
        p = head
        while p and p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head

"""
删除链表中的重复元素2
①pre指向哑结点， cur指向head节点，cur作为探索指针，去探索重复元素
②从head开始探索，如果存在重复的元素，我们找到重复元素的最后一个节点，将这一段重复元素全部跳过
③这里用到一个技巧，如果pre.next == cur 说明，是同一个节点，中间无重复元素，pre走一步，否则走到cur的下一个节点
④不断向下走
"""
class Solution2:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0, head)
        pre, cur = dummy, head
        while cur:
            # 找到重复元素的最后一个节点
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            # 用来判断有无重复元素，若相同，说明pre和cur挨着，没有重复，pre向前走一步
            if pre.next == cur:
                pre = pre.next
            # 有重复元素，pre.next指向cur.next, 但是pre没有向前走，因为cur.next有可能还是重复元素
            else:
                pre.next = cur.next

            cur = cur.next

        return dummy.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node5 = ListNode(5)
    node6 = ListNode(5)
    node7 = ListNode(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = None


    solution2 = Solution2()
    head = solution2.deleteDuplicates(node1)
    print('删除第k个节点后，头结点为{}，其值为{}'.format(head, head.val))

    while head != None:
        print(head.val)
        head = head.next