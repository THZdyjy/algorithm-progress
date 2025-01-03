
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


one = TreeNode(1)
three = TreeNode(3)
two = TreeNode(2.6, one, three)
six = TreeNode(6)
four = TreeNode(4, two, six)

res = []
min_val = float('inf')


def traverse(root):
    global min_val
    if not root:
        return

    traverse(root.left)
    res.append(root.val)
    if len(res) > 1:
        val = res[-1] - res[-2]
        min_val = min(min_val, val)
    traverse(root.right)
    return min_val


def getMinimumDifference(root):
    """
    对二叉搜索树进行中序遍历，遍历的过程中，更新这个最小差值即可。
    """
    min_val = traverse(root)
    return min_val

print(getMinimumDifference(four))

