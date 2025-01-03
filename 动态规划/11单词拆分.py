
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        word_set = set(wordDict)
        max_len = float('-inf')
        for word in word_set:
            max_len = max(max_len, len(word))

        # base case
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):  # 从第一个字母开始判断，依次判断dp[1], dp[2].....
            # 判断当前dp[i], 看dp[i-1],dp[i-2], dp[i-j]处能否完美切分，若可以，再判断s[j:i]是否存在于word中，即可
            for j in range(i - 1, -1, -1):
                word = s[j:i]
                if dp[j] and word in word_set:
                    dp[i] = True
        return dp[len(s)]

    """
    core: 单词拆分：在这个单词中切几刀，子单词在word中能够找到
    base: 当单词为""时，为true
    状态转移方程：
        定义状态dp[i] 表示以i为结尾的单词能否被切分
        怎么由子状态来dp[i-1]->dp[i]呢？举例
        a p p l e p e n a p p l e
      0 1 2 3 4 5 6 7 8 9 10 dp[i]
        dp[8]表示，applepen这个单词能否被切分，那么看dp[7],dp[6],dp[5],...dp[4]..dp[l]能否被切分，
        dp[5]正好可以。那么看看pen是否在word中，在的话，dp[8]为true
        并且s[l:i]这个单词存在于word中。
        另外，往前看的步数，不超过word中的最大长度
    因此状态转移方程如下：
        dp[i] = dp[i-l] and s[l:i] in worddict
    """

