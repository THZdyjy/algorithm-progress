class Solution:
    def decodeString(self, s: str) -> str:
        res, multi, stack = '', 0, []
        for c in s:
            if c.isdigit():
                multi = 10 * multi + int(c)
            if c.isalpha():
                res += c
            if c == '[':
                stack.append((multi, res))
                multi, res = 0, ''
            if c == ']':
                cur_nulti, last_res = stack.pop()
                res = last_res + cur_nulti * res
        return res
s1 = "xyz3[a2[c]]"
s = Solution()
print(s.decodeString(s1))