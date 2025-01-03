class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        res = []
        left, right = len(s) - 1, len(s) - 1
        while left >= 0:
            while left >= 0 and s[left] != " ": left -= 1
            res.append(s[left+1: right+1])
            while left >= 0 and s[left] == " ": left -= 1
            right = left
        return " ".join(res)

"""
 core: 本题是反转字符串中的单词，注意是反转单词。且要求对空格处理①去除左右空格②单词之间只有一个空格
注意，与验证回文字符串的区别，前者是字符级别，本题是单词级别。
思路：因为是反转，所以从后往前。
①i，j同时指向字符串末尾
②i向左，找到第一个空格，该空格表明其后的字符组成一个单词，将s[i+1, j+1]这个单词放入res
②i继续向左，跳过所有空格，找到第一个字母，该字母是新字母的开始
③j移动到该字母
④i继续向左，找到第一个空格......
⑤重复②③④过程，直到i越界
"""
