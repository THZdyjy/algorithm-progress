class Solution:
    """
    core: 注意本题与两数之和的区别。前者只有唯一解。 而本题拥有多个解，因此在使用哈希表时，需要记录数值的数目而不是index。
    """
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        hashmap = {}
        ans = 0
        for num in nums:
            find = k - num
            if find in hashmap:
                ans += 1
                # j1：如果数值只有一个了，直接删掉，而不是减1，否则。dict = {num: 0}。该值会重复被利用，只有删掉，说明用光了，后面有了的话，再初始化。
                if hashmap.get(find) == 1:
                    del hashmap[find]
                else:
                    hashmap[find] -= 1 # j2：大于1的话，直接减即可。
            else:
                hashmap[num] = hashmap.get(num, 0) + 1  # j3: 初始化
        return ans
