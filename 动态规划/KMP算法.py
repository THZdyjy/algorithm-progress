"""
core: PMT, 最大公共前后缀
例如 给定a b a b a b c a，其PMT为：
    值为0 0 1 2 3 4 0 0
   右移-1 0 0 1 2 3 4 0
   https://www.zhihu.com/question/21923021/answer/281346746
   https://www.bilibili.com/video/BV1iJ411a7Kb/?p=5&spm_id_from=pageDriver&vd_source=0daad7dbab71655092bed18b041f8556
"""

def get_next(p):

    next = [-1] * len(p)  # next[i]表示：第0位~第i位的最大公共前后缀
    i = 1  # i遍历p串后缀
    j = 0  # j遍历p串前缀，二者错开一个位置
    while i < len(p) - 1:  # 最后位置不必遍历
        if p[i] == p[j]:  # 当i, j 不相等时，j向前移动到最大公共子串的下一个位置
            j += 1
            next[i] = j
            i += 1
        # 当i，j相等时，i，j同时向后移动，最大公共前后缀+1，等于j
        else:
            if j > 0:
                j = next[j-1]
            else:
                i += 1

    return next

# print(get_next("abababca"))

def KMP(t, p):
    next = get_next(p)
    i, j = 0, 0
    while i < len(t):
        if t[i] == p[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j == len(p):
        return i - j
    else:
        return -1

print(KMP("mississippi", "issip"))