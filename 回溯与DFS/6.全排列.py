class Solution:
    def __init__(self):
        self.res = []
    # 主函数，输入一组不重复的数字，返回它们的全排列
    def permute(self, nums):
        # 记录「路径」
        track = []
        # 「路径」中的元素会被标记为 true，避免重复使用
        used = [False] * len(nums)
        self.backtrack(nums, track, used)
        return self.res

    # 路径：记录在 track 中
    # 选择列表：nums 中不存在于 track 的那些元素（used[i] 为 false）
    # 结束条件：nums 中的元素全都在 track 中出现
    def backtrack(self, nums: List[int], track: List[int], used: List[bool]):
        # 触发结束条件
        if len(track) == len(nums):
            self.res.append(track.copy())
            return

        for i in range(len(nums)):
            # 排除不合法的选择
            if used[i]:
                # nums[i] 已经在 track 中，跳过
                continue
            # 做选择
            track.append(nums[i])
            used[i] = True
            # 进入下一层决策树
            self.backtrack(nums, track, used)
            # 取消选择
            track.pop()
            used[i] = False

# 先回忆这个，然后，细节点，再看上面。
# 切片和deepcopy都是深度拷贝， copy是浅拷贝  https://blog.csdn.net/u011559236/article/details/78399216
class Solution:
    def __init__(self):
        self.track = []
        self.res = []
    def dfs(self, nums, used):
        # base
        if len(self.track) == len(nums): # 收集如果题目不让你算全排列，而是让你算元素个数为 k 的排列，怎么算？也很简单，改下 backtrack 函数的 base case，仅收集第 k 层的节点值即可
            self.res.append(self.track[:])
        # 遍历, 我们的选择是什么，nums & 没有使用过的
        for i in range(len(nums)):
            if used[i]: continue
            self.track.append(nums[i])
            used[i] = True
            self.dfs(nums, used)
            # 出节点，回溯时，需要从路径中pop, 并改为未使用
            self.track.pop()
            used[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        self.dfs(nums, used)
        return self.res

"""

1、路径：也就是已经做出的选择。->track,记录选择的节点，构成的路径。
2、选择列表：也就是你当前可以做的选择。
3、结束条件：也就是到达决策树底层，无法再做选择的条件

框架：
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        # 做选择
        将该选择从选择列表移除->used->false
        路径.add(选择)->track
        backtrack(路径, 选择列表)
        # 撤销选择
        路径.remove(选择)
        将该选择再加入选择列表

"""