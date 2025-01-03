class Solution:
    hashmap = {}

    def build(self, preorder, pre_s, pre_e, inorder, in_s, in_e):

        if pre_s > pre_e:
            return

        root = TreeNode(preorder[pre_s])
        root_index = self.hashmap.get(preorder[pre_s])
        left_size = root_index - in_s
        # 核心是将这八个索引确定对了，看图即可
        root.left = self.build(preorder, pre_s + 1, pre_s + left_size, inorder, in_s, root_index - 1)
        root.right = self.build(preorder, pre_s + left_size + 1, pre_e, inorder, root_index + 1, in_e)

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]):
        self.hashmap = {}
        for i in range(len(inorder)):
            if inorder[i] not in self.hashmap.keys():
                self.hashmap[inorder[i]] = i
        # 这里直接传preorder和其对应的范围，这样利用的信息也多了。我们只需管理索引即可，不要对对数组进行切片操作。大大减少内存占用。
        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
"""
preorder中确定根节点的位置 -> 找到根节点在inorder中的索引 -> 在inorder中划分左右子树 ->
->在preorder中再次去寻找左右子树根节点的位置 ->递归左右子树

二叉树的构造问题一般都是使用「分解问题」的思路：
        构造整棵树 = 根节点 + 构造左子树 + 构造右子树。先找出根节点，然后根据根节点的值找到左右子树的元素，进而递归构建出左右子树。
"""