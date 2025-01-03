"""
core: 核心就是，计算当前值前一部分的乘积，和后一部分的乘积，将两者相乘，便得到当前位置的结果。
前一部分的乘积计算如下：初始化索引0位置的前一部分的乘积为1*1（只有它本身嘛）。然后索引2部分的乘积等于本身值1*前一部分的乘积，那就是ans[0]*nums[0].举个例子
[2,3,-2,4] -> 初始化ans=[1,1,1,1]
对于0位置，其结果为ans[0] = 前一部分乘积（没有数，故为1）* 本身的1 = 1
对于1位置，ans[1] = 上个数前一部分乘积1*nums[0]*1=2
对于2位置，ans[2] = 上个数前一部分乘积*nums[i-1]*1=2*3*1 = 6
对于3位置，ans[3] = 上个数前一部分乘积*nums[i-1]*1=6*-2*1 = -12
同理计算后一部分的乘积得到 [-24,-8,4,1]
最终结果为【-24，-16， 24， -12】

可以归类到前缀和。
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix, ans = [1] * n, [1] * n, [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for j in range(n-2, -1, -1):
            suffix[j] = suffix[j+1] * nums[j+1]
        print(prefix, suffix)
        for i in range(n):
            ans[i] = prefix[i] * suffix[i]
        return ans

# 化简一下
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        temp = 1
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]
        print(ans)
        for j in range(n-2, -1, -1):
            temp = temp * nums[j+1]
            ans[j] = ans[j] * temp
        return ans
