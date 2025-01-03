"""
思考过程：
1.刚开始进出滑动窗口的元素数量是k，这样滑动窗口的大小为k， 每次三步三步走。
    但是"ling mindraboofooowingdingbarrwingmonkeypoundcake" ["fooo","barr","wing","ding","wing"]这个例子过不去。
2，于是，刚开始先一步一步走，即先找到foood的位置，然后再k步走，
    但是"aaaaaaaaaaaaaa" ["aa","aa"] 无法通过，少了；原因是我们k步走，丢失了结果。看来还得一步走
3.于是我们一步走，每次都重置valid, window, right的值，这次通过了，但造成了极大的时间开销。原因就是，每次right再走过word_num * word_length，判断完毕后。
    都要进行重置为left，之前的努力都白费了。怎么进行优化呢？
4.看了@画图小匠的题解，有了启发。比如 "bbbarfoothefoobarman" ["foo","bar"].我们对s进行切分
    "bbb arf oot hef oob arm an" 初始化left=right=0
    "b bba rfo oth efo oba rma n" 初始化left=right=1
    "bb bar foo the foo bar man" 初始化left=right=2
    "bbb arf oot hef oob arm an" 初始化left=right=3 可以发现到初始化3时，这种切分方式与初始化0时是相同的。因此，上面三种切分方式已经把所有的能够出现的额单词全包括了
    因此，我们依然三步走，只不过，按照三种切分方式，循环三次。这样时间复杂度是O（3n）。而思考3中，如果word_num * word_length非常长，接近s的长度。其时间复杂度接近n方。
core: 切分规律的把握 + 滑动窗口模板。
"""


from collections import defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) < len(words) * len(words[0]):
            return []

        need = defaultdict(int)
        res = []
        s_len = len(s)
        word_num = len(words)
        word_length = len(words[0])

        for word in words:
            need[word] += 1

        # j1：这里是与前面几道题目的不同之处， 按照切分方式走k个循环
        for split_position in range(word_length):
            # j2：要在每一轮循环的起始重置valid 和 window
            valid = 0
            window = defaultdict(int)
            left = right = split_position
            # j3：滑动窗口模板
            while right < s_len:
                cur_word = s[right: right + word_length]
                right += word_length
                # right += 1
                if cur_word in need:
                    window[cur_word] += 1
                    if window[cur_word] == need[cur_word]:
                        valid += 1

                while right - left == word_num * word_length:
                    if valid == len(need):
                        res.append(left)
                    out_word = s[left: left + word_length]
                    if out_word in need:
                        if window[out_word] == need[out_word]:
                            valid -= 1
                        window[out_word] -= 1
                    left += word_length

        return res



