import heapq
class Solution:
    def mergeKLists(self, lists):
        # 采用最小堆+分治法来做
        ret = ListNode()
        p = ret
        heap = []
        for i, node in enumerate(lists):
            if node != None:
                # j1:lists[i]是一个节点，push的是其val,因为要构建小顶堆，要使用这个值去构建
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        while heap:
            val, idx = heapq.heappop(heap)
            # j2:用val值新初始化一个节点，p指向它
            p.next = ListNode(val)
            p = p.next
            # j3: 判断第idx节点是否为None,不是的话，入堆
            if lists[idx] != None:
                heapq.heappush(heap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return ret.next