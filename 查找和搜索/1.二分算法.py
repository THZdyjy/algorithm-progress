

# ①经典的二分查找
def binary_search(arr, n, x):
    """
    core: 二分查找题目需要注意的是边界条件。
        本题：原始的二分查找，假设元素是不重复的。这个和下面的泛型情况作区分。

    """
    head = 0
    tail = n - 1
    # j1， 必须加‘=’，考虑这个例子[5], target=5, 不加等号的话，初始l=r, 进不去循环。
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
    core: 死记住得了，当数组中存在着重复元素时候。我们面临着两种情况，
    01模型： 例如，找[1,2,3,4,5,5,5,6,7,8]中第一次出现5的位置。可以转换为从左往右，找第一个大于等于5的位置，那么前面的都不满足，为0，后面的满足为1。即0000111111.此时左边界大胆往右移动+1
    10模型： 例如，找[1,2,3,4,5,5,5,6,7,8]中最后一次出现5的位置。可以转换为从右向左找第一个小于等于5的位置，后面的不满足，为0，前面的满足，为1.即1111111000.此时右边界大胆往左移动。-1

    这两种模型，统一使用小区间方法，即下面的两种方法。省的边界条件检查。
    """
    head, tail = 0, len(arr) - 1

    while head < tail:
        mid = head + (tail - head) // 2
        if arr[mid] < x: head = mid + 1
        else: tail = mid

    return head if arr[head] == x else -1 # 边界检查
print(binary_search_01_([1,2,3,4,5,5,5,6,7,8], 5))


# √ ②记忆这种01模型 大范围用二分，小范围用顺序,避免死循环
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



# √ ③ 二分查找的泛型情况代码实现 1111100000, 找到最后一个1，即找到有序数组中第一个<=x的位置。看例子理解
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


# import doctest
# # 大范围用二分，小范围用顺序,避免死循环
#
#
# def binary_search(arr, n, x):
#     """
#
#     >>> binary_search([1,2,3,4,5], 5, 3)
#     2
#     >>> binary_search([1,2,3,4,5], 5, 5)
#     4
#     >>> binary_search([1,2,3,4,5], 5, 1)
#     0
#     """
#     head = 0
#     tail = n - 1
#     while tail - head > 3:
#         mid = head + (tail - head) // 2
#         if arr[mid] == x: return mid
#         elif arr[mid] < x: head = mid + 1
#         else: tail = mid - 1
#     for i in range(head, tail+1):
#         if arr[i] == x: return i
#     return -1
#
#
# doctest.testmod()
# print(binary_search([1,2,3,4,5,6,7,8], 8, 5))
# s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# i = 10
# j = 14
# s[i + 1: j + 1] = s[i + 1: j + 1][::-1]
# print(s)
# print(s[::-1])