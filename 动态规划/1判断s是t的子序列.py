class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        core:动态规划
        s是否是t的子序列？？？
        初始化一个len(t)+1 行，26列的dp矩阵；
        dp[i][j]表示，字符串t中，从当前位置t[i]往后，后面所有字符在字符串中第一次出现的位置（举个例子，看官方题解：当前位置3，字母为t[3]b, 后面的字符为bdz, 那么b第一次出现的位置就是3，d是4，z是5，其他的都是6，表示不可能其他的字母在字符串中不再出现了）
        解决思路是，从后往前，动态方程如下：
        dp[i][j] = i           if t[i] = j
        dp[i][j] = dp[i+1][j]  if t[i]!=j

        如何匹配呢？
        abz, 从a开始，从第0行开始，a在字符串t中的0位置->sp和tp指针加1->b在字符串t中的3位置->sp+1, st->3+1即更新到b后一位->z在5位置->sp走完了，st走到z，还小于6.故√
        zdz, 2位置-》4位置-》5位置 √
        adb, 0位置-》4位置-》6位置，超出×

        为什么有奇效：
        原来复杂是O（n），但空间复杂度为O（1）,n是s和t中较长的。
        现在空间复杂度为O(n)，但是在输入大量的s，t不变的情况下，时间复杂度降低了：
        每个s直接在dp矩阵中得到一个位置序列即可。变为了O(n)，n为s的长度，即s和t较短的那个，子串嘛。这样大量的匹配时，这种预处理就会有奇效。
        """
        s_len, t_len = len(s), len(t)
        # j1：dp矩阵的初始化
        dp = [[0] * 26 for _ in range(t_len)]
        dp.append([t_len] * 26)

        # alpha = ['a', 'b', 'c'......]
        # j2：倒着建立dp矩阵
        for i in range(t_len - 1, -1, -1):
            for j in range(26):
                # ord(t[i]) 字符t[i]的ASCII码；ord('a') + j 依次为abcd...的ASCII码
                # j3：b ?= c -> ord(b) ?= ord('a') + 3, 依次更新每行的的26个字母
                dp[i][j] = i if ord(t[i]) == ord('a') + j else dp[i+1][j]

        # j4：搜索位置初始化
        search_position = 0
        for i in range(s_len):
            col = ord(s[i]) - ord('a')
            # 超出len(t)了，在t中找不到当前字符了
            if dp[search_position][col] == t_len:
                return False
            # 更新搜寻的起始位置
            search_position = dp[search_position][col] + 1
        return True


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 定义d[i][j]: 以s[i]结尾的是否是 以t[j]结尾的 子序列
        m, n = len(s), len(t)
        # base case, s为空，或者t为空的情况下，如何初始化
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        print(dp)
        for j in range(n + 1):
            dp[0][j] = 1
        for i in range(1, m + 1):
            dp[i][0] = 0
        # 画出状态转移过程，就能得到状态转移方程。状态与选择
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 注意这里的细节，不要越界
                if s[i - 1] == t[j - 1] and dp[i - 1][j - 1]:
                    dp[i][j] = 1
                else:
                    if dp[i][j - 1]:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
        return True if dp[-1][-1] else False