class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        时空复杂度为O(n)
        core:用分治法+小顶堆来实现
        """
        ret = ListNode(0, None)
        p = ret
        heap = []

        # j1：将链表数组中的链表的头结点放入小顶堆，并记录该头结点属于哪个链表
        # j1:lists[i]是一个节点，push的是其val,因为要构建小顶堆，要使用这个值去构建
        for idx, link_list in enumerate(lists):
            if link_list:
                heapq.heappush(heap, (link_list.val, idx))
                # j2:写出如下这样，会重新复制出一个链表，不是原链表了，会报错
                # link_list = link_list.next
                lists[idx] = lists[idx].next

        while len(heap) != 0:
            val, idx = heapq.heappop(heap)
            # j3：更新p节点
            p.next = ListNode(val)
            p = p.next
            # j4：如果节点还有值，则压入到小顶堆中，并更新
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return ret.next

