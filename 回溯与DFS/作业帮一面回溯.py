
res = 0
def traverse(matrix, i, j):
    m, n = len(matrix), len(matrix[0])
    global res
    if i > m - 1 or j > n - 1:
        return False
    if matrix[i][j] == 1:
        return False
    if i == m - 1 and j == n - 1:
        res += 1
    if not traverse(matrix, i + 1, j):
        i -= 1
    if not traverse(matrix, i, j + 1):
        i -= 1
# 给定这个matrix, 1代表障碍。问从[0][0]位置走到[n-1][n-1]位置一共有多少条路径。
matrix = [[0,1,0,0], [0,0,0,0],[1,0,0,0],[0,0,0,0]]
traverse(matrix, 0, 0)
print(res)


"""
抛硬币：
1枚 字 花
2枚 都是字
2枚 都是花
问，抛一枚硬币，正面是花，反面也是花的概率 0.8
答案：
4/5
"""