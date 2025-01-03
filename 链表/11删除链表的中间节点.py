# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    core: 本题可以分为两种情况讨论
    快慢指针，统一从dummy节点开始走。慢指针走一步，快指针走两步。
    链表长度为奇数：比如7，7/2=3.5取3，删除第四个节点。该情况下：快指针走到倒数第二个节点，就不能走了，此时慢指针正好走到，待删除节点的前一个节点。对应fast.next.next
    为偶数比如6，6/2=3，删除第四个节点。该情况下：快指针走到倒数第一个节点，就不能走了，此时慢指针正好走到，待删除节点的前一个节点。对应fast.next

    """
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = dummy = ListNode(0, head)
        # 对应链表长度为偶数与奇数两种情况
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return dummy.next