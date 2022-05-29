"""
给定一组括号，判断它是否是有效的；
例如()()(())() 有效， （（））（（）））无效
规律：是有效的： ①任意位置左括号数量>=右括号数量
                ②在最后一个位置左括号数量==右括号数量
                ③解决方法：程序中只需要记录左右括号的数量或者差值即可
"""

def is_valid(s):
    cha = 0
    length = len(s)
    for idx in range(length):
        if s[idx] == '(': cha += 1
        elif s[idx] == ')': cha -= 1
        else: return False
        if cha < 0: return False
    return cha == 0
print(is_valid('()()(()))()'))