"""
费曼和简化：
这是partition的变形，题目中只有三种数，012，快排中，将大的放基准值后面，将小的放到基准值前面。这里变具体了，基准就是1，小值为0，大值为2、
所以只需要一次遍历，将2放后面，将0放前面即可。具体来说，就是x的左边为0所在区域，y的右边为1所在的区域。base为1所在的区域。
simplify：排序核心为分区，定义基准是基础，如何遍历数组，得到分区结果是设计的关键。（快排是左大和右小进行交换；本题是将0放在x的左边，将2放在y的右边，选择的是1作为基准）
"""

def three_partition(arr, l, r, z):
    if l >= r: return
    x, y, base = 0, r, l
    while base <= y: # base对数组进行遍历
        if arr[base] == z: base += 1
        elif arr[base] < z:
            arr[x], arr[base] = arr[base], arr[x]
            x += 1
            base += 1  #这里base加1
        elif arr[base] > z:
            arr[y], arr[base] = arr[base], arr[y]
            y -= 1  #这里base不加1

    return

class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0: return
        three_partition(nums, 0, len(nums) - 1, 1)


arr = [2,0,1,2,1,1,0,0,0]
s = Solution()
s.sortColors(arr)
print(arr)