"""
时间复杂度分析。
nlogn：长度为n，partition操作为logn次， 每次partition操作n次

"""
def quick_sort(arr, l, r):
    """
    选择基准、小的放左，大的放右；
    """
    if l >= r: return arr
    x, y, base = l, r, arr[l+(r-l)//2]
    while x <= y:
        while x <= y and arr[y] > base: y -= 1
        while x <= y and arr[x] < base: x += 1
        if x <= y:
            arr[x], arr[y] = arr[y], arr[x]
            x += 1
            y -= 1
    quick_sort(arr, l, y)
    quick_sort(arr, x, r)
arr = [5, 7, 1, 4, 2, 8, 6, 3, 10]
quick_sort(arr, 0, len(arr) - 1)
print(arr)

def quick_sort_v2(arr, l, r):
    # 单边递归法
    while l < r:
        x, y, pivot = l, r, arr[l]
        while x <= y:
            while x <= y and arr[y] > pivot: y -= 1
            while x <= y and arr[x] < pivot: x += 1
            if x <= y:
                arr[x], arr[y] = arr[y], arr[x]
                x += 1
                y -= 1
        quick_sort_v2(arr, x, r)
        r = y
# quick_sort_v2([6,2,1,3,2,3,4,5,3], 0, len(arr) - 1)
# print(arr)



threshold = 16


# 三点取中法
def median(a, b, c):
    if a > b: a, b = b, a
    if a > c: a, c = c, a
    if b > c: b, c = c, b
    return b

# 无监督写法+插入排序
def final_insert_sort(arr, l, r):
    ind = l
    for i in range(l + 1, r + 1):
        if arr[i] < arr[ind]: ind = i
    while ind > l:
        arr[ind], arr[ind - 1] = arr[ind - 1], arr[ind]
        ind -= 1
    for i in range(l+2, r + 1):
        j = i
        while arr[j] < arr[j -1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

def __quick_sort_v3(arr, l, r):
    while r - l > threshold:
        x, y, base = l, r, median(arr[l], arr[r], arr[(l + r) // 2])  # 三点取中法
        while x <= y:
            while x <= y and arr[r] > base: y -= 1
            while x <= y and arr[l] < base: x += 1
            if x <= y:
                arr[x], arr[y] = arr[y], arr[x]
                x += 1
                y -= 1
        __quick_sort_v3(arr, x, r)
        r = y  # 单边递归法
    return

def quick_sort_v3(arr, l, r):
    __quick_sort_v3(arr, l, r)
    final_insert_sort(arr, l, r)

#
# quick_sort_v3(arr, 0, len(arr) - 1)
# print(arr)