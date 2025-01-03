class Solution:
    """
    core: 首先套用滑动窗口的框架。
    需要注意的是，在哪里更新结果 res 呢？我们要的是最长无重复子串，哪一个阶段可以保证窗口中的字符串是没有重复的呢？
这里和之前不一样，要在收缩窗口完成后更新 res，因为窗口收缩的 while 条件是存在重复元素，换句话说收缩完成后一定保证窗口中没有重复嘛
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        length = 0
        window = {}
        while right < len(s):
            in_char = s[right]
            right += 1
            window[in_char] =  window.get(in_char, 0) + 1

            while window[in_char] > 1:
                out_char = s[left]
                left += 1
                window[out_char] -= 1
            # 注意点。这里去更新长度时，思考如何更新，去往窗口上靠，滑动窗口 滑动窗口，不往上面靠，你干嘛吗。其长度就是right - left嘛
            length = max(length, right - left)

        return length