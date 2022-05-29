class Solution:
    def binary_search(self, nums, target):
        head, tail = 0, len(nums) - 1
        while tail >= head:
            mid = head + (tail - head) // 2
            if nums[mid] < target:
                head = mid + 1
            elif nums[mid] == target:
                return mid
            else:
                tail = mid - 1
        return -1

    def minOperations(self, nums, x) -> int:
        """
        。和：前缀和
        。顺序：二分法
        。从左边或右边删值，采用前缀和来解决。
        。构建左边的前缀和 [0, 1, 2, 6, 8, 11]
        。构建右边的前缀和 [0, 3, 5, 9, 10, 11]
        。遍历左边的前缀和，然后到右边前缀中采用二分法查找（target - val）
        。返回i + j 的值，代表左边和右边的操作数
        。如果 i + j > len(nums) 表明，选择的元素超过nums的元素数量，返回-1
        。ans 来存储 i + j 的值，不断更新，最后返回ans
        """
        length = len(nums)
        sum_l, sum_r = [0] * (length + 1), [0] * (length + 1)
        for i in range(length):
            sum_l[i + 1] = nums[i] + sum_l[i]

        for i in range(length):
            sum_r[i + 1] = nums[length - i - 1] + sum_r[i]

        ans = -1
        for i in range(length + 1):
            val = x - sum_l[i]
            j = self.binary_search(sum_r, val)
            if i + j > len(nums) or j == -1: continue
            if ans == -1 or i + j < ans: ans = i + j
        return ans

s = Solution()
print(s.minOperations([5,6,7,8,9], 4))