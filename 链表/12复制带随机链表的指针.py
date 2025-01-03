# https://leetcode.cn/problems/copy-list-with-random-pointer/solutions/295083/liang-chong-shi-xian-tu-jie-138-fu-zhi-dai-sui-ji-/?envType=study-plan-v2&envId=top-interview-150

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
"""
本题的核心是复制随机指针。可以采用如下技巧：参看@王尼玛的题解
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return head
        p = head
        # j1：遍历原来链表，并复制每个节点，放到源节点的后面
        while p:
            q = Node(p.val, p.next, p.random)
            p.next = q
            p = p.next.next

        # j2:遍历新复制的节点，对random指针进行处理。
        q = head.next
        while q:
            # j3：如果random指针不为空，进行复制
            if q.random:
                q.random = q.random.next
            # j4: 如果直接写q.next.next 到最后时，q.next == none , 则会报错
            q = q.next
            if q:
                q = q.next
        # j5:断开
        p = head
        q = new_head = head.next

        while p:
            if p.next:
                p.next = p.next.next
            p = p.next
            if q.next:
                q.next = q.next.next
            q = q.next

        return new_head