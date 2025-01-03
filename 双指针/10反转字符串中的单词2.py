# class Solution:
#     def reverseWords(self, s: List[str]) -> None:
#         """
#         core: 在1的基础上，直接对单词进行反转。然后对整个列表反转。但是这种的空间复杂度还是O(n),不满足题意。
#         """
#         left, right = len(s) - 1, len(s) - 1
#         while left >= 0:
#             while left >= 0 and s[left] != " ": left -= 1
#             s[left+1: right+1] = s[left+1: right+1][::-1]
#             while left >= 0 and s[left] == " ": left -= 1
#             right = left
#         return s.reverse()

class Solution:
    def reverseWords(self, s: [str]) -> None:
        """
        依次反转每个单词，最后再反转整个列表，注意不能用切片，用切片的话就开辟额外空间了，这里自己写的反转函数。
        因为是数组，我们可以自己写反转函数（赋值），字符串就不行。
        """
        i = 0
        # j1: j去探索第一个空格，即单词之间的分界线
        for j in range(len(s)):
            if s[j] != ' ': continue
            self.reverse(s, i, j - 1)  # j2：aT bT ，到了该行，j所处位置是空格，即找到了分界。反转单词
            i = j + 1
        self.reverse(s, i, len(s) - 1)  # j3：cT
        self.reverse(s, 0, len(s) - 1)  # j4：反转整个列表c b a

        return s

    def reverse(self, s, i, j):
        l, r = i, j
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1