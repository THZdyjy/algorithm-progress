class Solution:
    """
    core: 从左往右算一遍前缀和
    从右往左算一遍前缀和，中间碰到相同的数字返回即可；
    举例：对于[1,7,3,6,5,6]
    从左往右：[1,  8,  11, 17, 22, 28]
    从右往左：[28, 27, 20, 17, 11, 6]
    """
    def pivotIndex(self, nums: List[int]) -> int:
        pre = [0] * len(nums)
        fix = [0] * len(nums)
        res = []
        for i in range(len(nums)):
            if i == 0:
                pre[i] = nums[i]
            else:
                pre[i] = pre[i-1] + nums[i]
        for j in range(len(nums)-1, -1, -1):
            if j == len(nums)-1:
                fix[j] = nums[j]
            else:
                fix[j] = fix[j+1] + nums[j]
            if fix[j] == pre[j]:
                res.append(j) # 从满足条件的下标中取出最左边的那个
        print(pre, fix, res)
        return min(res) if res else -1
