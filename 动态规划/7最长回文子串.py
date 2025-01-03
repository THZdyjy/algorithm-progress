def longestPalindrome(self, s: str) -> str:
    length = len(s)
    if length < 2:
        return s
    # 初始化max_len 为1
    max_len = 1
    start = 0
    dp = [[False for _ in range(length)] for _ in range(length)]
    for i in range(length):
        dp[i][i] = True
    for j in range(1, length): # 从第一列遍历
        for i in range(j): # 只遍历上三角
            if s[i] == s[j]:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            if dp[i][j]:
                cur_len = j - i + 1
                if max_len < cur_len:
                    max_len = cur_len
                    start = i
    return s[start:start + max_len]
"""
注意这道题和最长回文子序列进行区分，前者不必是连续的，而本题是子串得是连续的。因此不能直接套用子序列的解法。

core:
定义dp[i][j] 为s[i..j]是否是回文子串。-》dp[i-1][j+1]是否是呢？
最长回文子串。 只有一个字符时，它就是。这就是base情况。因此对角线为True
在子串，子序列这类的问题中，为了方便。我们由dp[i+1][j-1] 来推 dp[i][j], 即从中间向两边推。
状态转移方程：i, j处的两个字符若相同，它是否是回文子串，取决于dp[i + 1][j - 1]
也就是说，只有 s[i+1:j−1] 是回文串，并且 s 的第 i 和 j 个字母相同时，s[i:j] 才会是回文串。 如果不同，那么就不是回文子串。但是我们这里全部初始化为False,
base情况的对角线初始化为True, 因此当两个字符不相等时，不用管；
另外，当满足s[i] = s[j]时，我们判断dp[i + 1][j - 1]是否为true的前提条件是，i+1 <= j-1, 即区间范围是有效的。
i+1 <= j-1 等价于 j - i >= 2, 这里等于2是个临界点，此时s[i]==s[j], i，j之间只有一个字符。
a b a
0 1 2
i   j
因此，j - i <= 2 时的所有情况，我们直接是dp[i][j] = True
综上所述，得到如下状态转移方程：
    if s[i] == s[j]:
        if j - i < 3:
            dp[i][j] = True
        else:
            dp[i][j] = dp[i + 1][j - 1]
然后怎么遍历是由状态转移方程来决定的。
要得到dp[i][j],得知道dp[i + 1][j - 1]，（左下角位置。可以选择从左往右一列一列遍历； 也可以选择从左往右，从下往上，一行一行遍历。但是由于有效区间范围的约束
，使得前者能够得到左下角的值，而后者是不行的。你可以举例子，结合上面所叙述的有效区间，来看一下，因此本题选择一列一列的遍历）

最后在遍历的过程中，记录start和max_len即可。
"""