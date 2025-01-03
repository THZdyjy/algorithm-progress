from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        core: 本题与最小覆盖子串如出一辙，只不过前者这个子串可以是不连续的。而本题，子串必须连续。换句话说，前者，窗口大小是不断变化的。而本题窗口大小就是子串的长度
        """
        need, window = defaultdict(int), defaultdict(int)
        for c in s1:
            need[c] += 1
        left, right = 0, 0
        # start, length = 0, float('inf')
        valid = 0
        while right < len(s2):
            in_char = s2[right]
            right += 1
            if in_char in need:
                window[in_char] += 1
                if window[in_char] == need[in_char]:
                    valid += 1
            # 窗口何时进行收缩，满足什么条件时进行收缩，比较1和2
            while right - left == len(s1):
                # 结果怎么更新及返回
                if valid == len(need):
                    return True

                out_char = s2[left]
                left += 1
                if out_char in need:
                    if window[out_char] == need[out_char]:
                        valid -= 1
                    window[out_char] -= 1
        return False