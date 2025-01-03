"""
找出数组中最小的k个数
只需要找到最小的k个，且不必对他们进行排序，所以只要能找到partition过程中，索引值为k-1的分割点即可。
因为是最小的，所以分割点选择partition后的y值，当y==k-1的时候，直接返回即可。如果y<k-1,在到右半部分去找这个索引，否则在左半部分寻找即可。
找最大的k个呢？partition的过程，将大的放前面，小的放到后面即可。
如果要求排序返回呢？再进行排序即可。
"""
def quick_sort_v2(arr, l, r, k):
    if l >= r: return
    x, y, pivot = l, r, arr[l]
    while x <= y:
        while x <= y and arr[y] > pivot: y -= 1
        while x <= y and arr[x] < pivot: x += 1
        if x <= y:
            arr[x], arr[y] = arr[y], arr[x]
            x += 1
            y -= 1
    if y == k - 1:
        return
    if y < k - 1:
        quick_sort_v2(arr, x, r, k)
    else:
        quick_sort_v2(arr, l, y, k)


class Solution:
    def smallestK(self, arr, k: int) :
        if k == 0: return []
        quick_sort_v2(arr, 0, len(arr) - 1, k)
        return arr[:k]

arr = [1,3,5,7,2,4,6,8]
s = Solution()
print(s.smallestK(arr, 4))
print(arr)

