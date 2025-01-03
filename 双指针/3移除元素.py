class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        core: 该题是将数组中等于val的值全部移除，最后返回剩下的长度即可。
        如果建立新的数组，不等于val的全部append, 那么直接返回该数组长度即可。但是题目不允许额外开辟空间
        双指针：l初始化为0， r初始化为数组长度。当l小于r时，
        遍历数组，如果当前值不等于val. l+1, 表示数组有效长度加1，也表示遍历下一个元素。
        如果等于val, 将r指针对应的元素赋值过来，r-1, 表示数组的有效长度减1。这样直到l与r重合，此时l的值即数组的有效长度，返回l即可。
        """
        # j2: 这里r是len(nums), 它代表的是数组有效的长度。 l判断一个，去一个，其值减小1.
        left, right = 0, len(nums)
        while left < right:
            if nums[left] != val:
                left += 1
            else:
                # j1：将后面的值赋值过来，即让别的值（无论他是否是val, 是的话，下一循环它也会被取代）来代替它。这样迁移一位，表示有效长度减了一
                nums[left] = nums[right - 1]
                right -= 1

        return left