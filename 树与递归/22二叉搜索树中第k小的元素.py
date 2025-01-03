class Solution:
    def find(self, root, find_value):
        if not root:
            return
        if root.val == find_value:
            return find_value
        if find_value < root.val:
            return self.find(root.left, find_value)
        elif find_value > root.val:
            return self.find(root.right, find_value)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 先找到最小的值，看看是从哪个值开始的。
        node = root
        while node.left:
            node = node.left
        min_val = node.val
        # 将要查询的第k个最小值计算出来, 比如第二个最小值，就是比最小值大一的那个。所以第k个最小是，就是比min_val 大k=1的那个。
        find_value = k - 1 + min_val
        return self.find(root, find_value)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = []
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        core: 二叉搜索树的中序遍历为递增序列
        因此本题转化为：求中序遍历的第k个节点
        """
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.res.append(root.val)
            dfs(root.right)
        self.res = []
        dfs(root)
        print(self.res)
        return self.res[k-1]
