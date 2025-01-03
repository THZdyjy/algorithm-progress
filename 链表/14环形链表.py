"""
环形链表，判断链表中是否有环，如果有环，返回入环节点。

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 判断是否是环形链表，快慢指针
class Solution:
    def hascycle(self, head):
        if head == None or head.next == None:
            return False
        p, q = head, head
        while q.next and q.next.next:
            p = p.next
            q = q.next.next
            if p == q: return True
        return False

# 若有环，返回链表的入环节点
# p走k q走 2k， 当他们相遇时，q比p多走了一个环L, 则 2k - k = k = L ；若总长为 s=L+M .此时p再走M步即走到入环节点，
# 将q放到head走M步，他俩相遇，返回即可
class Solution2:
    def detectCycle(self, head):
        if head == None or head.next == None:
            return None
        p, q = head, head
        while p != q:
            if q == None or q.next == None: return None
            p = p.next
            q = q.next.next
        q = head
        while p != q:
            p = p.next
            q = q.next
        return p
"""
1.数据观察，从例子中得到规律，并且进行数学证明
2.数学建模，转换为链表有无环的问题
3.代码实现与细节处理
"""


def isHappy(n):
    def get(n):
        quotient = n
        sum = 0
        while quotient != 0:
            quotient, remaindern = quotient // 10, quotient % 10
            sum += remaindern ** 2
        return sum

    p, q = n, n
    while True:
        p = get(p)
        q = get(get(q))
        print(p, q)
        if p == q or q == 1: break
    return q == 1





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

    n = 15
    res = isHappy(n)
    print('{}是快乐数吗：{}'.format(n, res))


    solution = Solution()
    print('链表是否有环？{}'.format(solution.hascycle(node1)))

    solution2 = Solution2()
    print('链表的入环节点是？{}，其值为{}'.format(solution2.detectCycle(node1), solution2.detectCycle(node1).val))
