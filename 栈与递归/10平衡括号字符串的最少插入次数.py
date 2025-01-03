class Solution:
    def minInsertions(self, s: str) -> int:
        res, need = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                need += 2
                # 当遇到左括号时，若对右括号的需求量为奇数，需要插入1个右括号，来匹配之前缺一个右括号的左括号
                if need % 2 == 1:
                    res += 1
                    need -= 1
            elif s[i] == ')':
                need -= 1
                if need == -1:
                    res += 1
                    need = 1
        return res + need
"""
确实，res表示的是当前遍历过程中为了配平当前的状态，所需要插入左括号或是右括号的总次数，need表示的是遍历结束后仍需要的右括号数量
res的定义是插入操作 need的定义是 需要的右括号数量
need 是需要的右括号的数量，当遇见左括号使，need 自然而然需要2个，故+2
当碰见右括号时，need自然而然减去1，需求量减1，但是如果need==-1,说明）太多了，这时候需要给补个（， 补了一个（，自然需要两个））对应，已经有了一个，因此还需要一个，need=1
当碰到（，且need数量为奇数时（它是大于1的），需要先给补一个右括号，使得右括号的需求量减去1，变为偶数。这点其实不太理解。先记住。
最后返回res+need

"""