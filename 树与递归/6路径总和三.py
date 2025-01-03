from collections import defaultdict
class Solution:
    def __init__(self):
        self.res = 0
        self.path_sum = 0
        self.prefix_sum = defaultdict(int)

    def traverse(self, root, targetSum):
        if not root:
            return

        # 计算路径和
        #  self.path_sum - targetSum 因为前缀和是累加而成，当前的path_sum减去targetSum后得到的值
        # 如果存在前缀和字典中，说明从那个值到当前值的这条路径上，能够满足加起来等于target。
        # 在前缀和字典中看看是存在这个值，不存在的话结果加0
        self.path_sum += root.val

        self.res += self.prefix_sum.get(self.path_sum - targetSum, 0)
        self.prefix_sum[self.path_sum] = self.prefix_sum.get(self.path_sum, 0) + 1
        # 遍历左右子树
        self.traverse(root.left, targetSum)
        self.traverse(root.right, targetSum)
        # 回溯
        self.prefix_sum[self.path_sum] = self.prefix_sum.get(self.path_sum) - 1
        self.path_sum -= root.val

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.prefix_sum = defaultdict(int)
        self.traverse(root, targetSum)
        return self.res

"""
core: 核心是维护一个前缀和字典，该字典记录二叉树路径的前缀和。例如10，5，3，3即为[10:1, 15:1, 18:1, 21:1]
记录当前前缀和的值path_sum，例如为18时，判断18-8=10是否在字典中，O（1）在，说明在该路径上，（10，18]对应的原节点值5，3可以组成一条路径。
然后将该值更新到前缀和字典中，继续往下判断，当回溯时，需要从前缀和字典中移除path_sum, 并减去root.val
"""