import math
"""
core: str1是t的倍数， mt， str2是t的倍数, nt。所以 str1 + str2 = str2 + str1.
这样，如果可以找到t的话，必然是满足以上性质的。然后返回长度为最大公约数的子串即可
"""
def gcdOfStrings(str1: str, str2: str) -> str:
    candidate_len = math.gcd(len(str1), len(str2))
    candidate = str1[: candidate_len]
    if str1 + str2 == str2 + str1:
        return candidate
    return ''

print(gcdOfStrings('ABcABcABc', 'aABc'))