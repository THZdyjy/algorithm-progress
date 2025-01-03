class Solution:
    """
    此题的核心思想同5
    只不过，进出元素时，分为了三种情况
    """
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        max_res = 0
        for i in range(k):
            if s[i] in 'aeiou':
                res += 1
        max_res = res
        for j in range(k, len(s)):
            in_char = s[j]
            out_char = s[j - k]
            # 进元素是元音，出元素不是，+1
            if in_char in 'aeiou' and out_char not in 'aeiou':
                change = 1
            # 进元素不是元音，出元素是，-1
            elif in_char not in 'aeiou' and out_char in 'aeiou':
                change = -1
            # 进元素是和出元素都是或者不是，不变
            else:
                change = 0
            res += change
            max_res = max(max_res, res)
        return max_res
