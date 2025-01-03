# 哈希表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # j1：值作key, 索引作value
        hashmap[nums[0]] = 0
        for i in range(1, len(nums)):
            another = target - nums[i]
            # j2：看看是否存在查找值，这里是O1
            index = hashmap.get(another, -1)
            if index != -1:
                return [i, index]
            else:
                hashmap[nums[i]] = i
        return