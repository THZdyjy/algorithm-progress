"""
for循环在遍历列表的时候，如果列表要发生改变，一定要注意元素有可能
被漏掉，这个时候最后不要用for语句

"""

class RecentCounter:

    def __init__(self):
        self.request = []

    def ping(self, t: int) -> int:
        t_min = max(0, t - 3000)
        self.request.append(t)
        length = len(self.request)
        """
        for _ in range(length):
            if self.request[0] < t_min:
                self.request.pop(0)
        """
        while self.request[0] < t_min:
            self.request.pop(0)
        return len(self.request)
# ["RecentCounter","ping","ping","ping","ping","ping"]
# [[],[642],[1849],[4921],[5936],[5957]]  [null,1,2,1,2,3]

obj = RecentCounter()
param_1 = obj.ping(642)
param_2 = obj.ping(1849)
param_3 = obj.ping(4921)
param_4 = obj.ping(5936)
param_5 = obj.ping(5957)
print(param_1, param_2, param_3, param_4, param_5)

