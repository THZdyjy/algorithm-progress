"""
给你一个 n x n 矩阵 matrix ，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素
输入：matrix = [[1,5,9],
            [10,11,13],
            [12,13,15]], k = 8
输出：13
"""

"""
core: 此题为二分查找的变形。
二分查找： nums=[1,2,4,5,6,7,9] target=5，通过 l, r 计算mid, 
不断比较nums[mid]与target的值，从而缩小区间范围，最后返回目标索引。
本题：给定matrix，target为第k小元素，其实是依旧是找索引。
看官方题解图，可以发现matrix[0][0]最小为l, matrix[n-1][n-1]最大，为r。 
原始的二分法，target为元素，返回的是索引。而本题，target是索引（数量），返回的是元素。
所以操作反着来，我们通过l,r值计算到mid值，然后去矩阵中得到<=该值的数量。
如果数量num大于等于taget数量k， 则将右值r,改为mid。
否则将左值l改为mid+1。这样查找范围不断缩小，最后返回目标索引对应的元素即可。
时空复杂度：
   """

def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    def get_num(mid):
        # j1：锯齿线的起始点
        i, j = n - 1, 0
        num = 0
        # j2: 走到矩阵的边界
        while i >=0 and j < n:
            # j3：向右走或向上走
            if matrix[i][j] <= mid:
                num += (i+1)
                j += 1
            else:
                i -= 1
        # j4: 》=， 说明，目标在左边范围，此时r移动，命令r = mid
        return num >= k

    n = len(matrix)
    l, r = matrix[0][0], matrix[n-1][n-1]
    # j5：加‘=’陷入死循环
    while l < r:
        mid = l + (r - l)//2
        if get_num(mid):
            r = mid
        else:
            l = mid + 1
    # 最后返回l
    return l