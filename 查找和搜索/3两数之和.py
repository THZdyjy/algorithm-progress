"""
方法一：哈希表
    建立一个哈希表，存放值与他的下标。遍历数组，如果当前值+ 是否存在值= target. 那么是否存在值如果在哈希表里，就找到了，否则继续遍历。
    题目告诉了，只会存在一个有效答案。因此肯定有，直接返回即可。时空O(n)
方法二：
    先对数组进行排序，然后采用二分法。由于直接对原数组排序，会改变索引，返回时会出错。所以对原数组的索引进行排序。
    排序完成后，遍历整个数组，用二分法去查找是否存在这么个值。
    时间复杂为nlogn, 因为新建了索引数组，空间复杂度为n

两数之和，先进行排序，然后采用二分法进行搜索
[1,3,7,2,4] 9
[0,3,1,4,2]
"""
# 排序+二分
def binary_search(nums, index, head , target):
    tail = len(index) - 1
    while tail >= head:
        mid = head + (tail - head) // 2
        if nums[index[mid]] < target: head = mid + 1
        elif nums[index[mid]] > target: tail = mid - 1
        else: return mid
    return  -1


def two_nums(nums, target):
    # 先对数组进行排序，由于直接对原数组排序，会改变索引，返回时会出错。这里对原数组的索引进行排序
    index = [i for i in range(len(nums))]
    for i in range(len(index)):
        for j in range(i, len(index)):
            if nums[index[i]] > nums[index[j]]: index[i], index[j] = index[j], index[i]
    print(index)
    for i in range(len(index)):
        value = nums[index[i]]
        j = binary_search(nums, index, i + 1, target - value) # 从 i+1开始搜索
        if j == -1: continue
        return [index[i], index[j]]
    return
print(two_nums([1,3,7,2,4] ,9))

# 哈希表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # j1：值作key, 索引作value
        hashmap[nums[0]] = 0
        for i in range(1, len(nums)):
            another = target - nums[i]
            # j2：看看是否存在查找值，这里是O1
            index = hashmap.get(another, -1)
            if index != -1:
                return [i, index]
            else:
                hashmap[nums[i]] = i
        return
