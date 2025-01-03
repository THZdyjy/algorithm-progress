# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    hashmap = {}

    def build(self, preorder, pre_s, pre_e, postorder, post_s, post_e):
        if pre_s > pre_e:
            return
        if pre_s == pre_e:
            return TreeNode(preorder[pre_s])

        root_value = preorder[pre_s]
        left_root_val = preorder[pre_s + 1]
        left_root_index = self.hashmap[left_root_val]
        # 因为index对饮的值也是左子树的，所以要+1
        left_size = left_root_index - post_s + 1

        root = TreeNode(root_value)
        # 不是1，left_root_index-1，left_root_index 是左子树
        root.left = self.build(preorder, pre_s + 1, pre_s + left_size, postorder, post_s, left_root_index)
        # 这里是post_e-1，最后一个是根节点
        root.right = self.build(preorder, pre_s + left_size + 1, pre_e, postorder, left_root_index + 1, post_e - 1)

        return root

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.hashmap = {}
        for i in range(len(postorder)):
            if postorder[i] not in self.hashmap.keys():
                self.hashmap[postorder[i]] = i
        return self.build(preorder, 0, len(preorder) - 1, postorder, 0, len(postorder) - 1)