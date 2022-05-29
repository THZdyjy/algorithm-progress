import doctest
# 大范围用二分，小范围用顺序,避免死循环


def binary_search(arr, n, x):
    """

    >>> binary_search([1,2,3,4,5], 5, 3)
    2
    >>> binary_search([1,2,3,4,5], 5, 5)
    4
    >>> binary_search([1,2,3,4,5], 5, 1)
    0
    """
    head = 0
    tail = n - 1
    while tail - head > 3:
        mid = head + (tail - head) // 2
        if arr[mid] == x: return mid
        elif arr[mid] < x: head = mid + 1
        else: tail = mid - 1
    for i in range(head, tail+1):
        if arr[i] == x: return i
    return -1


doctest.testmod()
print(binary_search([1,2,3,4,5,6,7,8], 8, 5))
