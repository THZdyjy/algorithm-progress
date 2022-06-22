def merge_sort(nums, l, r):
    if l >= r: return 0
    mid = (l + r) // 2
    reverse_pair = 0
    reverse_pair += merge_sort(nums, l, mid)
    reverse_pair += merge_sort(nums, mid + 1, r)
    pl, pr, k = l, mid + 1, 0
    temp = [None] * (r - l + 1)
    while pl <= mid or pr <= r:
        if pr > r or (pl <= mid and nums[pl] <= nums[pr]):
            temp[k] = nums[pl]
            pl, k = pl + 1, k + 1
        else:
            temp[k] = nums[pr]
            reverse_pair += (mid - pl + 1)
            pr, k = pr + 1, k + 1

    for i in range(l, r+1):
        nums[i] = temp[i - l]
    return reverse_pair

class Solution:
    def reversePairs(self, nums) -> int:
       return merge_sort(nums, 0, len(nums) - 1)

s = Solution()
print(s.reversePairs([7,5,6,4]))