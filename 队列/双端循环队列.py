class MyCircularDeque:
    """
    tail维护队尾指针的下一位
    head维护队首指针
    凡是get方法，head和tail指针不要动

    """

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.head = 0
        self.tail = 0
        self.size = k
        self.deque = [None for _ in range(k)]
        self.cnt = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull(): return False
        self.head = (self.head - 1 + self.size) % self.size
        self.deque[self.head] = value
        self.cnt += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull(): return False
        self.deque[self.tail] = value
        self.cnt += 1
        self.tail = (self.tail + 1) % self.size
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty(): return False
        self.deque[self.head] = None
        self.cnt -= 1
        self.head = (self.head + 1) % self.size
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty(): return False
        self.tail = (self.tail - 1 + self.size) % self.size
        self.deque[self.tail] = None
        self.cnt -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.deque[self.head] if not self.isEmpty() else -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        pos = (self.tail - 1 + self.size) % self.size
        return self.deque[pos] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.cnt == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.cnt == self.size

queue = MyCircularDeque(5)
print(queue.insertFront(7))
print(queue.insertLast(0))
print(queue.getFront())
print(queue.insertLast(3))
print(queue.getFront())
print(queue.insertFront(9))
print(queue.getRear())
print(queue.getFront())
print(queue.getFront())
print(queue.deleteLast())
print(queue.getRear())


"""
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
"""
