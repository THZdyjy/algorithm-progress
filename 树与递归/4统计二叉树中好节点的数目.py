
class Solution:
    count = 0

    def traverse(self, root, path_max):
        if not root:
            return
        if root.val >= path_max:
            self.count += 1
            path_max = root.val
        self.traverse(root.left, path_max)
        self.traverse(root.right, path_max)
        return

    def goodNodes(self, root: TreeNode) -> int:
        """
        采取遍历的思路，遍历二叉树中的每一个节点。
        在前序位置判断即可：
            节点的值大于等于最大值时，该节点就是好的。
        然后去遍历左右子树：
            在此过程中，顺便记录下count值-》类变量
        """
        self.traverse(root, root.val)
        return self.count
