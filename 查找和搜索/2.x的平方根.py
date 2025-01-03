"""
转化为10模型，找到最后一个1
"""
def mysqrt(x):
    head, tail = 0, x
    while tail - head > 3:
        mid = head + (tail - head) // 2
        if mid * mid > x: tail = mid -1
        else: head = mid
    for i in range(head, tail + 1)[::-1]:
        if i * i <= x:return i
    return -1