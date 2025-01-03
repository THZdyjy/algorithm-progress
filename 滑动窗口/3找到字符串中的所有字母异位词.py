from collections import defaultdict
class Solution:
    """
    core: 与2题比较，其唯一的不同点就是返回值的不同，前者返回一种情况，true即可。本题将所有满足的都返回。
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need, window = defaultdict(int), defaultdict(int)
        left, right = 0, 0
        valid = 0
        res = []
        # 有哪个字符，其数量是多少
        for c in p:
            need[c] += 1
        while right < len(s):
            in_char = s[right]
            right += 1
            if in_char in need:
                window[in_char] += 1
                if window[in_char] == need[in_char]:
                    valid += 1
            # 左闭右开区间，right-left即为窗口大小
            while right - left == len(p):
                if valid == len(need):
                    res.append(left)
                out_char = s[left]
                left += 1
                if out_char in need:
                    # 先看看出窗口的这个字符是否在need中，且其数量相等。这样的话，后面会出去，所以valid减去1.
                    if window[out_char] == need[out_char]:
                        valid -= 1
                    window[out_char] -= 1
        return res