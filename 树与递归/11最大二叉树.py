class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """
        core: 完全按照题意来就行。
        遍历的解法： 树=根+左子树+右子树
        给定nums,先选出最大值，去构建根节点。以max_idx为界，左边的去构建左子树。右边的去构建右子树。
        """
        if not nums:
            return None

        # 找到数组中的最大值及其索引
        max_num = max(nums)
        max_idx = nums.index(max_num)

        # 以最大值构造根节点
        root = TreeNode(max_num)

        # 递归调用构造左右子树
        root.left = self.constructMaximumBinaryTree(nums[:max_idx])
        root.right = self.constructMaximumBinaryTree(nums[max_idx+1:])

        return root
