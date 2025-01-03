"""
core:提炼题目信息，需要用一个合适的数据结构，
    1,维护一些数字中的最小值
    2,需要去掉最小值
    3,需要加入元素 => 最小堆
    特别注意，如果两个队的元素冲得了，直接排序去剩余dek个数
"""
# https://www.bilibili.com/video/BV1Ld4y1r71H/?vd_source=0daad7dbab71655092bed18b041f8556
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ans, n = 0, len(costs)
        if candidates * 2 < n:
            pre = costs[:candidates]
            heapify(pre)
            suf = costs[-candidates:]
            heapify(suf)
            i, j = candidates, n - 1 - candidates
            while k and i <= j:
                if pre[0] <= suf[0]:
                    ans += heapreplace(pre, costs[i])
                    i += 1
                else:
                    ans += heapreplace(suf, costs[j])
                    j -= 1
                k -= 1
            costs = pre + suf
        costs.sort()
        return ans + sum(costs[:k])  # 也可以用快速选择算法求前 k 小