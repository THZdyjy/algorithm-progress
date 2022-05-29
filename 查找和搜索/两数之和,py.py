"""
两数之和，先进行排序，然后采用二分法进行搜索
[1,3,7,2,4] 9
[0,3,1,4,2]
"""
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
        value =  nums[index[i]]
        j = binary_search(nums, index, i + 1, target - value) # 从 i+1开始搜索
        if j == -1: continue
        return [index[i], index[j]]
    return
print(two_nums([1,3,7,2,4] ,9))