"""
core: 不可能存下所有的正整数，所以我们可以用空集代表全部正整数，
调用popSmallest一次，弹出优先队列中的最小元素，并在record中记录。然后如果队列为空了，把下一个待弹出的元素入队
"""
import heapq
class SmallestInfiniteSet:
    def __init__(self):
        # 初始时候top设置为1
        self.hq = [1]
        self.record = set()

    def popSmallest(self) -> int:
        # 弹出最小的
        ret = heapq.heappop(self.hq)
        # 如果为空了，则把下一个加进来。
        if len(self.hq) < 1:
            heapq.heappush(self.hq, ret+1)
        # 如果弹出的是后放入的，将record中的记录给抹去
        self.record.discard(ret)
        return ret

    def addBack(self, num: int) -> None:
        # 比如一直弹弹弹，弹到6，那么你放9的话，9本身就在，直接忽略即可。如果是4，可以放； 这里比较的是max, 比如你弹到6，你先放入个1，你再放入个4，都是和6去比较的
        if num < max(self.hq) and num not in self.record:
            heapq.heappush(self.hq, num)
            # 记录已经放过4了，如果还要放4，可以直接忽略
            self.record.add(num)




# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)