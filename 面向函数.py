# name = 'Test'
# def f1(n):
#     print(n)
#     print(name)
#
# f1('new')
#
# def f2(name):
#     print(name)
#     print(name)
#
# f2('new')


name = 'tom'
def f3(n):
    global  print
    global name
    print(name)
    print(n)
    name = 'mike'
    print = lambda x: x
    print(n)


f3('new')

# print(dis.dis(f3))


def some_func(f = lambda x: x+1):
    return f

def some_func_out(func, m):
    return lambda m: some_func(func)(m)

aa = some_func_out(lambda x: x**2, 20)(10)
print(aa)