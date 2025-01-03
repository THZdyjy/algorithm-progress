class Solution:
    # 这里要用01模型
    def binary_search(self, p, left, right, target):
        while right - left > 3:
            mid = left + (right - left) // 2
            if p[mid] < target:
                left = mid + 1
            else:
                right = mid
        for i in range(left, right + 1):
            if p[i] >= target:
                return i
        return -1

    def longestOnes(self, nums: List[int], k: int) -> int:

        p = [0]
        ans = 0
        for num in nums:
            p.append(p[-1] + (1 - num))
        for right in range(len(p) - 1, -1, -1):
            find = p[right] - k
            left = self.binary_search(p, 0, right, find)
            ans = max(ans, right - left)

        return ans
    """
    时间复杂度：O(nlogn) 空间复杂度O(n) 
    首先构造前缀和，表示当前位置的前面有几个0.所以前缀和数组长度为len(nums)+1
    其次，我们从右边开始寻找。right所在的p的当前位置上的数字表示前面有几个零。因为只能反转k个0，所以【left, right）这个左闭右开的区间里，只允许存在k个0。因此我们要找到左边一个位置，该位置前面有find=p[right] - k个零。找到这个find所在的位置。
    则【left, right）这个区间里，包含了k个零。
    left前有p[right] - k个零。 【left, right）这个区间有k个零， 加起来不就是所有零的个数嘛。
    不懂的话，去看官方题解。二分法
    """

