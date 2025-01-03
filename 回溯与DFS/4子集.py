class Solution:
    def __init__(self):
        self.track = []
        self.res = []

    # 递归函数的意义：从位置start处开始，进行子集的收集
    def backtrack(self, nums, start):
        # base case，前序位置添加空集，还有其他的子集。
        self.res.append(self.track[:])

        # 做选择，从start处开始，进行选择
        # start 作用：控制树枝的生长避免产生重复的子集，看下一个位置
        # 5,7,1,2,4
        # 举例子：遍历时，5的索引是0，下一个位置就是7->1
        #        遍历时，1的索引是2，下一个位置就是3->2

        for i in range(start, len(nums)):
            self.track.append(nums[i])
            # 由nums[i]开头的子集，从它的下一个位置起进行选择
            next_position = i + 1
            self.backtrack(nums, next_position)
            self.track.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 从位置0处开始，进行子集的收集
        self.backtrack(nums, 0)
        return self.res

"""
core: 回溯，三个问题
    路径是什么：我们从空集开始，依次选择1,2,3, 在1的基础上再选择2，然后选择3，这样形成的集合[],[1],[1,2][1,2,3]即是一条路径，
        注意这个路径，不一定要全部走完才记录，由于每个节点都是一个子集，因此每个节点都要记录
    选择是什么，如何对选择做约束呢：选择就是1,2,3, 约束就是，只能在当前索引的下一个位置处开始，进行子集的收集，这样不会重复
    base是什么： 本题中由于每个节点都是一个子集，因此不会等到叶子结点才收集子集，而是在每个节点处进行子集的收集

举一反三： 我们可以收集子集个数为1,2，...len(nums)个数的自己，比如77组合这道题目
"""

