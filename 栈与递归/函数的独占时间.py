"""
题目的意思是给定log信息，求出每个函数运行的时间.例如：
输入：n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
输出：[3,4]
采用栈来解决；
这道题我有疑问的一点是，如果存在（（（）））这样的递归调用的话是怎么处理的。√ 已明白
"""
def exclusiveTime(n, logs):
    result = [0] * n
    stack = []
    log_info = [log.split(':') for log in logs]
    print(log_info)
    run_time = 0
    for log in log_info:
        if log[1] == 'start':
            stack.append(log)
        else:
            run_time = int(log[2]) - int(stack.pop()[2]) + 1
            result[int(log[0])] += run_time
            if stack:
                result[int(stack[-1][0])] -= run_time # 出栈的时候，如果栈不为空，减去被调用函数的执行时间
    return result
logs = ["0:start:0","1:start:2","2:start:3","2:end:4","1:end:5","0:end:6"]

logs2 = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
res = exclusiveTime(3, logs)
print(res)