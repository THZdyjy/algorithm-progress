"""
编码技巧：①在循环中，被循环的变量，要不断的进行更新，在循环中，这些变量的初始值要尤其注意  ②python，在if else代码块中的变量为局部变量，需要在代码块之外先定义
思维模型：数据结构的实现和维护

"""
from icecream import ic


class Dui(object):
    def __init__(self, n):
        self.data = [None] * n
        self.cnt = 0

    def push(self, val):
        ind = self.cnt
        self.data[ind] = val
        while ind and self.data[(ind - 1) // 2] < self.data[ind]:
            self.data[(ind - 1) // 2], self.data[ind] = self.data[ind],  self.data[(ind - 1) // 2]
            # 不要忘记更新ind为父节点的索引
            ind = (ind - 1) // 2
        self.cnt += 1
        return

    def pop(self):
        # pop 之前先进行判断
        if self.size() == 0: return
        pop_element = self.data[0]
        self.data[0], self.data[self.cnt - 1] = self.data[self.cnt - 1], self.data[0]
        self.cnt -= 1

        ind, n = 0, self.cnt - 1
        while 2 * ind + 1 <= n: # 满足这个条件，肯定有左子树
            # temp维护父节点、左右子树中值最大的索引
            tmp = ind
            if self.data[ind] < self.data[2 * ind + 1]: tmp = 2 * ind + 1
            if 2 * ind + 2 <= n and self.data[tmp] <= self.data[2 * ind + 2]: tmp = 2 * ind + 2
            if tmp == ind: break
            self.data[ind], self.data[tmp] = self.data[tmp], self.data[ind]
            ind = tmp
        print(f'弹出堆的最大元素{pop_element}')
        return

    def top(self):
        return self.data[0]

    def size(self):
        return self.cnt

    def output(self):
        for i in range(self.cnt):
            print(self.data[i], end='\t')
        print()


if __name__ == '__main__':
    dui = Dui(9)
    dui.push(2)
    dui.push(3)
    dui.push(4)
    dui.push(5)
    dui.push(6)
    dui.output()
    dui.pop()
    dui.pop()
    dui.pop()
    dui.output()
