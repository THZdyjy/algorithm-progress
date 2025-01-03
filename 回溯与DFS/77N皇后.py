"""
core: 回溯，思考清楚三个问题即可
    路径是什么：下棋的时候，从左往右下，从上往下走；然后每一行，我们肯定只放一个皇后，然后放下一行，当放到最后一行的时候，说明所有的皇后的位置都不会造成冲突。
        这时候，我们就形成了一条路径，把这个路径放到res即可。所以路径就是，放完N皇后之后，棋盘的格局。
    选择是什么，如何对选择做约束：在往每一行防止皇后的时候，有N列供选择。但是是有题目中的约束条件的，因此需要检查这个位置是否可以放。
    base是什么：当我们把N行都放完之后，说明是一个合法的解决办法，因此将棋盘格局放入到res中，这就是base.
"""
class Solution:
    def valid(self, track, row, col):
        # 检查列
        for i in range(len(track)):
            if track[i][col] == 'Q':
                return False

        # 检查左上角
        r, c = row - 1, col - 1
        # 注意不要写成col了，浪费了我一个番茄钟
        while r >= 0 and c >= 0:
            if track[r][c] == 'Q':
                return False
            r = r - 1
            c = c - 1

        # 检查右上角
        r, c = row - 1, col + 1
        while r >= 0 and c <= len(track) - 1:
            if track[r][c] == 'Q':
                return False
            r = r - 1
            c = c + 1
        # 哥们记得给返回True
        return True

    def backtrack(self, row, track, res):
        # base case
        if row == len(track):
            res.append(["".join(row) for row in track])
            # 注意点：这里要返回return，否则索引会越界
            return
        n = len(track[row])
        for col in range(n):
            if not self.valid(track, row, col): continue
            track[row][col] = 'Q'
            self.backtrack(row + 1, track, res)
            track[row][col] = '.'
        return


    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        track = [['.'] * n for _ in range(n)]
        self.backtrack(0, track, res)
        return res