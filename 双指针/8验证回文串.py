"""
core:字符串中有非字母数字元素，因此也需要对这些东西进行处理，两个函数
s.isalnum() & s.lower(). 然后用头尾双指针即可。
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            # j1: 跳过非字母数字，找到左边和右边的字母数字
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            # j2：找到之后，依旧要先判断l是否小于r
            if l < r:
                if s[l].lower() != s[r].lower():
                    return False
                # 继续遍历
                l = l + 1
                r = r - 1

        return True
