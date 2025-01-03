"""
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        core:  链表这儿一个易混淆的问题：
        从dummy走，while p.next, 走到最后一个节点，走了length步
        从head走，while p，走到None, 走了length步
        本题，latter  former都从dummy走，fommer先走n步，然后再一起走。
        former走到最后一个节点时候，走了length步。此时latter走了length-n步
        正好落到待删除节点的前一个
        """
        dummy = ListNode(-1, head)
        latter = former = dummy
        for i in range(n):
            former = former.next
        while former.next:
            former = former.next
            latter = latter.next
        latter.next = latter.next.next
        return dummy.next