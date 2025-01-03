
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        core: 初始化 window 和 need 两个哈希表，记录窗口中的字符个数和需要凑齐的字符个数，
        valid 变量表示窗口中满足 need 条件的字符个数，如果 valid 和 need.size 的大小相同，则说明窗口已满足条件，已经完全覆盖了串 T。（1，包含所有字符 2，数量要大于等于）
        start和length的设置
        元素进窗口时，先进，后更新数据； 而出窗口时，先更新数据，后出窗口
        """
        need, window = defaultdict(int), defaultdict(int)
        for c in t:
            need[c] += 1
        left, right = 0, 0
        valid = 0
        # 记录最小覆盖子串的起始索引及长度
        start, length = 0, float('inf')
        while right < len(s):
            # c 是将移入窗口的字符
            c = s[right]
            # 扩大窗口
            right += 1
            # 进行窗口内数据的一系列更新
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # 判断左侧窗口是否要收缩
            while valid == len(need):
                # 在这里更新最小覆盖子串
                if right - left < length:
                    # 长度与起始位置的更新
                    start = left
                    length = right - left

                # d 是将移出窗口的字符
                d = s[left]
                # 缩小窗口
                left += 1
                # 进行窗口内数据的一系列更新
                if d in need:
                    # 先看看出窗口的这个字符是否在need中，且其数量相等。这样的话，后面会出去，所以valid减去1.
                    if window[d] == need[d]:
                        valid -= 1
                    # 注意这里是后减
                    window[d] -= 1

        # 返回最小覆盖子串
        return "" if length == float('inf') else s[start:start + length]

"""
core: 本题是在s中找到包含t中所有字母的最小字串。这个最小子串不要求顺序。①包含t全部的字符 ②长度最短 ③不需要顺序

*****************滑动窗口模板*****************
def slidingWindow(s: str):
    # 用合适的数据结构记录窗口中的数据
    window = {}
    left = 0
    right = 0

    while right < len(s):
        # 增大窗口
        in_char = s[right]
        window.add(in_char);
        right += 1
        # 进行窗口内数据的一系列更新...

        # 判断左侧窗口是否要收缩
        while left < right and window needs shrink:
            # 缩小窗口
            out_char = s[left]
            window.remove(out_char);
            left += 1
            # 进行窗口内数据的一系列更新...

*****************滑动窗口模板*****************

细节点：  一. 滑动窗口是在大脑里的一种思维结构，要在大脑中模拟这个过程
        二. 初始化left=right=0, 是左闭右开，即滑动窗口中没有元素（在大脑中想象）；代码中的体现就是，开始遍历时，窗口中加入元素，然后right+=1, 此时[0,1),包含一个元素
        三...处的操作分别是扩大和缩小窗口的更新操作，它们操作是完全对称的。
        四. 元素进窗口时，先进，后更新数据； 而出窗口时，先更新数据，后出窗口

变化点：
        1、什么时候应该移动 right 扩大窗口？窗口加入字符时，应该更新哪些数据？
        2、什么时候窗口应该暂停扩大，开始移动 left 缩小窗口？从窗口移出字符时，应该更新哪些数据？
        3、我们要的结果应该在扩大窗口时还是缩小窗口时进行更新？如何更新？

时间复杂度：
        简单说，指针 left, right 不会回退（它们的值只增不减），所以字符串/数组中的每个元素都只会进入窗口一次，然后被移出窗口一次，不会说有某些元素多次进入和离开窗口，
        所以算法的时间复杂度就和字符串/数组的长度成正比

"""