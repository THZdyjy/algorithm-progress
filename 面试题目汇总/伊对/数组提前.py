# 伊对
"""
把一个数组里等于某个值的元素往前提，要求不改变其他元素的位置且不开新的内存。比如[1，6，5，1]，value=1，就输出为[1，1，6，5]
"""
def front(nums, target):
    n = len(nums)
    l = 0
    for i in range(1, n):
        while i > 0 and nums[i] == target and nums[i] != nums[i-1]:
            nums[i - 1], nums[i] = nums[i], nums[i-1]
            i -= 1
    return nums
# print(front([1,6,3,3,4,1,2,1,1,5,1], 1))

def bubble(nums, target):
    n = len(nums)
    i = j = n - 1
    while i >= 0:
        if nums[i] != target:
            if nums[j] == target:
                nums[i], nums[j] = nums[j], nums[i]
            j -= 1
        i -= 1
    return nums
print(bubble([1,6,3,3,4,1,2,1,1,5,1], 1))
