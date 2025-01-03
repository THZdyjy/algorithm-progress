# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    hashmap = {}

    def build(self, postorder, post_s, post_e, inorder, in_s, in_e):

        if post_s > post_e:
            return

        root = TreeNode(postorder[post_e])
        root_index = self.hashmap.get(postorder[post_e])
        left_size = root_index - in_s
        # 核心是将这八个索引确定对了，看图即可
        root.left = self.build(postorder, post_s, post_s + left_size - 1, inorder, in_s, root_index - 1)
        root.right = self.build(postorder, post_s + left_size, post_e - 1, inorder, root_index + 1, in_e)

        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        self.hashmap = {}
        for i in range(len(inorder)):
            if inorder[i] not in self.hashmap.keys():
                self.hashmap[inorder[i]] = i
        return self.build(postorder, 0, len(postorder) - 1, inorder, 0, len(inorder) - 1)
