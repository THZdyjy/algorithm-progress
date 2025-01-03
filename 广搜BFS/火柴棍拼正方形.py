class Solution:
    def makesquare(self, matchsticks) -> bool:
        # 定义递归函数：当前木棍能否放到正方形的四个边长中（桶）
        # 递归的是边长的剩余容量，当剩余容量全为0时，则说明能~
            def dfs(ind, edges, matchsticks):
                # 递归出口，当全部木棍都放到木桶中，返回TREU, 说明拼成了
                if ind == len(matchsticks):
                    return True
                # 依次判断每个木桶是否能放下当前木棍，如果不能，则下一个，如果能，则更新木桶容量
                for i in range(4):
                    if matchsticks[ind] > edges[i]:
                        continue
                    if edges[i] == matchsticks[ind] or edges[i] - matchsticks[ind] >= matchsticks[-1]:
                        # 更新容量
                        edges[i] -= matchsticks[ind]

                        # 判断下一根木棍能否放下。当前的木棍能放下，不代表该路径下，后面所有的木棍都能放下，如果返回true，则说明是，
                        # 返回false,说明该路径不行。需要回收木桶的容量
                        if dfs(ind + 1, edges, matchsticks):
                            return True
                        else:
                            edges[i] += matchsticks[ind]
                return False

            if not matchsticks:
                return False
            total = sum(matchsticks)
            if total % 4 != 0:
                return False
            avg = total // 4
            matchsticks.sort(reverse=True)
            edges = [avg] * 4
            return dfs(0, edges, matchsticks)
s = Solution()
res = s.makesquare([12,13,1,15,11,17,16,3,15,11,13,4,2,16,15])
print(res)