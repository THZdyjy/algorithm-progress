from collections import Counter
class Solution:
    def findWords(self, board, words):
        # 如果word存在于网格中，返回true。其实就是是否有这么一条路径
        # 使用dfs, 定义状态: 给定abord和word,给定当前待搜寻下一个字母，如果在当前字母的前后左右搜索到了，则返回True, 如果没有，则返回FALSE
        def dfs(board, word, i, r, c, visited):
            # 定义递归出口，如果遍历到完了word, 则说明找到了这条路径。
            if i == len(word):
                return True
            if r < 0 or r >= len(board):
                return False
            if c < 0 or c >= len(board[0]):
                return False
            if board[r][c] != word[i]:
                return False
            if (r, c) in visited:
                return False
            visited.add((r, c))

            # 看看在当前字母的上下左右是否存在word的下一个字母
            if dfs(board, word, i + 1, r - 1, c, visited) or \
                    dfs(board, word, i + 1, r + 1, c, visited) or \
                    dfs(board, word, i + 1, r, c + 1, visited) or \
                    dfs(board, word, i + 1, r, c - 1, visited):
                return True
            visited.remove((r, c))
            return False

        res = set()
        # 找到入口
        row = len(board)
        col = len(board[0])
        cnts = Counter()
        for i in range(row):
            for j in range(col):
                cnts[board[i][j]] += 1

        for ii, word in enumerate(words):
            cur = Counter(word)
            canexist = True
            for c in cur:
                if cnts[c] < cur[c]:
                    canexist = False
                    break
            if not canexist:
                continue

            find = False
            for r in range(row):
                for c in range(col):
                    # 找到了递归的入口
                    if board[r][c] == word[0]:
                        if dfs(board, word, 0, r, c, set()):
                            res.add(words[ii])
                            find = True
                            break
                if find:
                    break

        return list(res)


board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]

words = ["oath","pea","eat","rain"]
s = Solution()
res = s.findWords(board, words)
print(res)