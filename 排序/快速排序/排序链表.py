class Solution:
    def sortList(self, head, n):
        n += 1
        if head == None or head.next == None: return head
        print(head.val)
        min_value, max_value = head.val, head.val
        p = head
        while p:
            min_value = min(min_value, p.val)
            max_value = max(max_value, p.val)
            p = p.next
        if min_value == max_value: return head
        base_val = (min_value + max_value) / 2  # 不加这个就成了死循环了，没有递归出口了
        p = head

        little, big = None, None
        q = None
        while p:
            q = p.next
            if p.val <= base_val:
                p.next = little
                little = p
            else:
                p.next = big
                big = p
            p = q
        little = self.sortList(little, n)
        big = self.sortList(big, n)
        p = little
        while p.next: p = p.next
        p.next = big
        return little
