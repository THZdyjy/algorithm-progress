"""
时间复杂度分析。
nlogn：长度为n，partition操作为logn次， 每次partition操作n次

"""
def quick_sort(arr, l, r):
    """
    [5, 7, 1, 4, 2, 8, 6, 3, 10] 双指针，选择基准值pivot，例如5.
    [0, 1, 2, 3 ,4, 5, 6, 7, 8]
    从右边找到第一个小于5的值索引，7,交换arr[x]和arr[y]
    从左边找到第一个大于5的值索引，1,交换arr[x]和arr[y]
    """
    if l >= r: return arr
    x, y = l, r
    base = arr[l]
    while x <= y:
        while x <= y and arr[y] > base: y -= 1
        while x <= y and arr[x] < base: x += 1
        if x <= y:
            arr[x], arr[y] = arr[y], arr[x]
            x += 1
            y -= 1

    arr[x] = base

    quick_sort(arr, l, y)
    quick_sort(arr, x, r)


arr = [5, 7, 1, 4, 2, 8, 6, 3, 10]
quick_sort(arr, 0, len(arr) - 1)

def quick_sort_v2(arr, l, r):
    while l < r:
        x, y, pivot = l, r, arr[l]
        while x < y:
            while x < y and arr[y] > pivot: y -= 1
            if x < y: arr[x] = arr[y]
            while x < y and arr[x] < pivot: x += 1
            if x < y: arr[y] = arr[x]
        arr[x] = pivot
        quick_sort_v2(arr, x + 1, r)
        r = x - 1
quick_sort_v2(arr, 0, len(arr) - 1)
print(arr)