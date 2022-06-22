def merge_sort_v0(arr, l, r):
    if l >= r: return [arr[l]]
    mid = (l + r) // 2
    left = merge_sort_v0(arr, l, mid)
    right = merge_sort_v0(arr, mid + 1, r)
    res = []

    while left and right:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    res += left if left else right
    return res

# print(merge_sort_v0([1,5,4,6,8,3,9,0,2], 0, 8))


def merge_sort_v1(arr, l, r):
    if l >= r: return
    mid = (l + r) // 2
    merge_sort_v1(arr, l, mid)
    merge_sort_v1(arr, mid + 1, r)
    res = [None] * (r - l + 1)
    k, p1, p2 = 0, l, mid + 1
    while p1 <= mid or p2 <= r:
        if p2 > r or (p1 <= mid and arr[p1] <= arr[p2]):
            res[k] = arr[p1]
            p1 += 1
            k += 1
        else:
            res[k] = arr[p2]
            p2 += 1
            k += 1
    for i in range(l, r+1):
        arr[i] = res[i-l]
    return


arr = [1, 5, 4, 6, 8, 3, 9, 0, 2]
merge_sort_v1(arr, 0, 8)
print(arr)

