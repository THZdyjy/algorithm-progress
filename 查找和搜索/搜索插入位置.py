"""
转化为01模型，找到第一个1
"""
def search_insert(nums, target):
    head, tail = 0, len(nums) - 1
    while tail - head > 3:
        mid = head + (tail - head) // 2
        if nums[mid] < target: head = mid + 1
        else: tail = mid
    for i in range(head, tail + 1):
        if nums[i] >= target: return i
    return len(nums)
print(search_insert([1,2,3,4,6], 5))