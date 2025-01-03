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

print(merge_sort_v0([1,5,4,6,8,3,9,0,2], 0, 8))



