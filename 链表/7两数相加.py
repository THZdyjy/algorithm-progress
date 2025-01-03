
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.cn/problems/add-two-numbers/solutions/2393210/jie-jian-fan-zhuan-lian-biao-si-lu-di-gu-45x0/
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 反转链表类似的思路
        def get_numbers(head, res):
            if not head.next:
                return str(head.val)
            num = get_numbers(head.next, res)
            res += num
            res += str(head.val)
            return res

        # j1：corner case判断
        if l1.val == 0 and l1.next == None and l2.val == 0 and l2.next == None:
            return ListNode(0)

        res = ""
        dummy = p = ListNode()

        # j2：利用递归，将整数取出
        l1_number = get_numbers(l1, "")
        l2_number = get_numbers(l2, "")
        res_number = int(l1_number) + int(l2_number)

        # j3：将新的整数放入到链表中
        while res_number > 0:
            num = res_number % 10
            res_number = res_number // 10
            tmp = ListNode(num)
            p.next = tmp
            p = p.next 
        return dummy.next

