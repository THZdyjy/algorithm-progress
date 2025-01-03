class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        core：双指针。
        指针j刚开始指向开头，它去探索0所在的位置
        指针i遍历数组，当前值不等于零时，与零进行交换，否则往前走，去找不为零的元素。
        i找到不为零的元素，进行交换。j 维护的是0所在位置
        """

        # j永远记录下一个非零元素该存放的位置
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                # 更新j元素的位置
                # j = i 错误，这样吧中间的0给跳过了
                j += 1
            # 走到0所在位置，就不走了
            else:
                j += 0
        return nums
