"""
leetcode 树的子结构
特殊情况判断，如果一开始B为空，则返回False，这是题目中规定的；
如果，A也为空，那么B肯定不是A的子结构，同样返回False；

树的问题一般都要进行递归，递归左子树和右子树。本题就是先判断以当前根节点为根节点的树A是否是否包含了B，如果不包含，递归的去判断他的左子树和右子树。

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def match(self, A, B):
        """
        ①首先是判断当前节点值是否相等，如果不相等直接返回False
        ②以节点A为根节点的A中的子树，必须根节点相同，然后判断他的左右子树也必须相同，除非B为空了，那么
        是子结构，否则B不为空，A先为空了，就不是子结构了。返回False
        ③当前节点相同时，去递归遍历左子树和右子树，为且的关系

        """
        if not B: return True
        if not A or A.val != B.val: return False
        return self.match(A.left, B.left) and self.match(A.right, B.right)

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:

        if not A or not B: return False
        return self.match(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    