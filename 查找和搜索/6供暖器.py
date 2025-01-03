class Solution:
    def binary_search(self, heaters, target):
        head, tail = 0, len(heaters) - 1
        while head < tail:
            mid = head + (tail - head) // 2
            if heaters[mid] >= target: tail = mid
            else: head = mid + 1
        return head

    def findRadius(self, houses, heaters) -> int:
        ans = 0
        heaters = sorted(heaters) # 换成快速排序
        for target in houses:
            #0000的情况，找到的是最后一个小于等于的位置正好与本题相符合
            j = self.binary_search(heaters, target)
            a = abs(heaters[j] - target)
            b = abs(target - heaters[j-1]) if j else a + 1
            ans = max(ans, min(a, b))
        return ans
"""
将房子数组的每一个元素视为target，为其选择最近的供暖期
在供暖器数组中搜索房子所在的位置，即确定房子在哪两个供暖器之间，从而确定最小半径
最后取最小半径的最大值
问题转换为01模型或者10模型，用二分法进行查找
"""
houses = [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
heaters = [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]
index =   [0,         1,        2,        3,       4,       5,        6,         7,        8,       9]
s = Solution()
print(s.findRadius(houses, heaters))