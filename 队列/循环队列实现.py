"""
循环队列的实现
"""
class Deque():
    def __init__(self, size):
        self.head = 0
        self.tail = 0
        self.cnt = 0
        self.size = size
        self.deque = [None] * size

    # 入队
    def push(self, val):
        if self.full():
            print('队列已满，不能再增加元素')
            return
        self.deque[self.tail] = val
        self.cnt += 1
        self.tail += 1
        if self.tail == self.size:
            self.tail = 0
        return

    # 出队
    def pop(self):
        if self.empty():
            print('队列已空，不能再出队')
            return
        self.cnt -= 1
        self.head += 1
        if self.head == self.size:
            self.head = 0
        return    

    # 判空
    def empty(self):
        return self.cnt == 0

    # 判满
    def full(self):
        return self.cnt == self.size

    # 队列中当前的数据量
    def count(self):
        return self.cnt

    def front(self):
        return self.deque[self.head] if not self.empty() else -1

    def rear(self):
        return self.deque[self.tail - 1] if not self.empty() else -1

    # 查看当前队列数据
    def output(self):
        print('当前队列中有{}个元素'.format(self.count()))
        j = self.head
        for i in range(self.cnt):
            print(self.deque[j])
            j += 1
            if j == self.size:
                j = 0
        return
            

queue = Deque(5)
while True:
    op = input('请输入您想执行的操作：')
    if op == 'push':
        val = int(input('请输入入队数据：'))
        queue.push(val)
    elif op == 'pop':
        queue.pop()
    else:
        queue.output()
        print('队首元素：{}'.format(queue.front()))
        print('队尾元素：{}'.format(queue.rear()))
        break


