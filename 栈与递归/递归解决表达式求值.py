"""
递归用的是系统栈；
"""

def calc(s, left, right):
    """
    ①先找到优先级最低的运算符的位置；
    ②再进行递归，分治运算

    总结反思：
    ①遍历得到最低优先级时，cur的赋值得比pre大，否则，在没有加减乘除操作时，如果遇到（）依然会赋值，导致操作为（），后面会发生 错误
    ②在给op赋值时，其位置应该加上传入的参数left，才是最低优先级操作在原字符串中的真正位置
    ③在op==-1时，需要将字符串转为数字，如‘((234’. 字符转ascii码
    """
    # 当前优先级最低的运算符索引，如果不是运算符，索引为-1，表示是数字
    op = -1
    # 前一优先级
    pre = 10000 - 1
    # 当前优先级
    cur = 10000
    # 表示在遇到括号时，优先级增加的数值
    temp = 0

    # 遍历，找到优先级最低的位置，然后进行分治递归计算

    for idx, character in enumerate(s[left:right]):
        if character == '+' or character == '-':
            cur = 1 + temp
        elif character == '*' or character == '/':
            cur = 2 + temp
        elif character == '(':
            temp += 100 # 遇到括号后，为了增加后面的优先级，但此步骤cur不变
        elif character == ')':
            temp -= 100
        else:
            continue

        if cur < pre:
            pre = cur
            op = idx + left
    if op != -1:
        print('当前最低优先级的操作为：{}'.format(s[op]))
    else:
        num = 0
        for number in s[left: right]:
            if ord(number) < ord('0') or ord(number) > ord('9'): continue
            num = num * 10 + (ord(number) - ord('0'))
        return num
    a, b = calc(s, left, op), calc(s, op+1, right)
    if s[op] == '+':
        return a + b
    elif s[op] == '-':
        return a - b
    elif s[op] == '*':
        return a * b
    elif s[op] == '/':
        return a / b


if __name__ == '__main__':
    s = '2*(2+5)+10+2*5'
    res = calc(s, 0, len(s))
    print('表达式{}的计算结果为：{}'.format(s, res))