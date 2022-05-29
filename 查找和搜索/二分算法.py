import doctest

# ①经典的二分查找
def binary_search(arr, n, x):
    head = 0
    tail = n - 1
    while head <= tail:
        mid = head + (tail - head) // 2
        if arr[mid] == x: return mid
        elif arr[mid] < x: head = mid + 1
        else: tail = mid - 1
    return -1
# print(binary_search([1,2,3,4,5,6,7,8], 8, 5))


# 二分查找的泛型情况代码实现 0000011111, 找到有序数组中第一个>=x的位置
def binary_search_01_(arr, x):
    """
    备注：如果没有大于等于x的位置，即全为0,000000，最后返回的是最后一个0，即最后一个<x的位置
    """
    head, tail = 0, len(arr) - 1

    while head < tail:
        mid = head + (tail - head) // 2
        if arr[mid] < x: head = mid + 1
        else: tail = mid

    return head if arr[head] == x else -1 # 边界检查
# print(binary_search_01_([1,2,3,4,5,5,5,6,7,8], 9))


# ②记忆这种01模型 大范围用二分，小范围用顺序,避免死循环
def binary_search_01(arr, x):
    head, tail = 0, len(arr) - 1
    while tail - head > 3:
        mid = head + (tail - head) // 2
        if arr[mid] < x: head = mid + 1
        else: tail = mid
    for i in range(head, tail+1):
        if arr[i] >= x: return i # 这里写为>= 而不是==，是为了提高泛化性 。当数组不是连续的时候，即x不存在于数组中时
    return -1
# print(binary_search_01([1,2,3,4,6,6,6,7,8], 5))



# ③ 二分查找的泛型情况代码实现 1111100000, 找到最后一个1，即找到有序数组中第一个<=x的位置
def binary_search_10(arr, x):

    head, tail = 0, len(arr) - 1
    while tail - head > 3:
        mid = head + (tail - head) // 2
        if arr[mid] > x: tail = mid - 1
        else: head = mid
    for i in range(head, tail+1)[::-1]:
        if arr[i] <= x: return i
    return -1
# print(binary_search_10([1,2,3,4,6,6,6,7,8], 5)) # 找到最后一个<=6的元素位置 11111 11100.
doctest.testmod()


# 备注：以下解法会陷入死循环。原因：10模型，满足head情况时，head=mid，满足tail情况时，tail=mid-1; 然后当两个head与tail相邻时，此时计算mid=head，然而循环中head
# 更新后仍然等于mid，所以陷入死循环。已经修改
def binary_search_10_error(arr, x):
    head, tail = 0, len(arr) - 1
    while tail >= head:
        mid = head + (tail - head) // 2
        if arr[mid] > x:
            tail = mid - 1
        else:
            head = mid + 1
    return head - 1
print(binary_search_10_error([1,2,3,4,5,6,6,6,7,8], 5))

"""
升华：
123456789
000011111 大于等于 找第一个1
111110000 小于等于 找最后一个1
这两种情况互为对偶，最终答案是一样的，针对具体问题选择01模型还是10模型，但是当列表中有重复元素时，答案是不同的
"""
