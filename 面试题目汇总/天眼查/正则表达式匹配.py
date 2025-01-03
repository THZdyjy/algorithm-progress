"""
若 dp(s, i, p, j) = true，则表示 s[i..] 可以匹配 p[j..]；
若 dp(s, i, p, j) = false，则表示 s[i..] 无法匹配 p[j..]
"""

def dp(s, i, p, j) -> bool:
    # 如果索引都指向了末尾
    if j == len(p):
        return i == len(s)
    if i == len(s):
        return j + 1 < len(p) and p[j + 1] == '*' and dp(s, i, p, j + 2)

    if p[j] == s[i] or p[j] == '.':  # pattern at j matches the string at i
        if j + 1 < len(p) and p[j + 1] == '*':
            # Two options: Either ignore the pattern-j* pair or ignore the string-i match and check rest of the pattern
            return dp(s, i, p, j + 2) or dp(s, i + 1, p, j)
        else:
            # pattern at j matches the string at i, move to next character in both
            return dp(s, i + 1, p, j + 1)
    else:
        # pattern at j does not match with string i. If pattern-j* is there then we need to skip current pattern/j or
        # skip current string/i
        return j + 1 < len(p) and p[j + 1] == '*' and dp(s, i, p, j + 2)
dp(s, 0, p, 0)