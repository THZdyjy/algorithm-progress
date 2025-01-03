# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        core: 将链表分为一个大的， 一个小的。 最后将二者连接起来。
        技巧就是，建立两个虚拟头节点，和两个指针。分别代表大的和小的。

        """
        little_dummy = ListNode()
        big_dummy = ListNode()
        l = little_dummy
        b = big_dummy
        p = head
        # j1：遍历链表，并且比较当前val和x的大小，小的放在l的后边
        while p:
            if p.val < x:
                l.next = p
                l = l.next
            else:
                b.next = p
                b = b.next
            # j2：这里要断开原链表的指针，先将后面的保存起来，tmp，再断开
            tmp = p.next
            p.next = None
            p = tmp
        # j3：将小链表的尾巴与大链表的脑袋连接起来
        l.next = big_dummy.next
        return little_dummy.next