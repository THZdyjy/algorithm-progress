"""

因为这道题涉及到元素的插入和删除，不仅仅是在开头，而且还有中间，如果用数组来实现，那么插入的时候，后面的元素全部得移动
所以这个队列的实现采用链表。
"""
class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None


class FrontMiddleBackQueue:

    def __init__(self):
        self.head = self.tail = self.mid = None
        self.sign = False # 队列数目为奇数，偶数为false

    def pushFront(self, val: int) -> None:
        if not self.head:
            self.head = self.mid = self.tail = Node(val)
            self.sign = True
            return

        node = Node(val)
        self.head.pre = node
        node.next = self.head
        self.head = self.head.pre  # 在头部插入节点后，不要忘了将head移动到头结点
        if self.sign:
            self.mid = self.mid.pre
            self.sign = False
        else:
            self.sign = True

    def pushMiddle(self, val: int) -> None:
        if not self.head:
            self.head = self.mid = self.tail = Node(val)
            self.sign = True
            return

        node = Node(val)
        if self.sign:
            self.sign = False
            if not self.mid.pre:
                self.mid.pre = node
                node.next = self.mid
                self.mid = self.head = node

            else:
                self.mid.pre.next = node
                node.pre = self.mid.pre
                self.mid.pre = node
                node.next = self.mid
                self.mid = node

        else:
            self.mid.next.pre = node
            node.next = self.mid.next
            self.mid.next = node
            node.pre = self.mid
            self.mid = node
            self.sign = False

    def pushBack(self, val: int) -> None:
        if not self.head:
            self.head = self.mid = self.tail = Node(val)
            self.sign = True
            return
        
        node = Node(val)
        self.tail.next = node
        node.pre = self.tail
        self.tail = node
        if self.sign:
            self.sign = False
        else:
            self.sign = True
            self.mid = self.mid.next

    def popFront(self) -> int:
        if not self.head:
            return -1
        res = self.head.val
        self.head = self.head.next
        if not self.head:
            self.head = self.mid = self.tail = None
            self.sign = False
            return res
        self.head.pre = None
        if self.sign:
            self.sign = False
        else:
            self.sign = True
            self.mid = self.mid.next
        return res

    def popMiddle(self) -> int:
        if not self.head:
            return -1
        res = self.mid.val
        if not self.mid.next:
            self.mid = self.head = self.tail = None
            self.sign = False
            return res
        if not self.mid.pre:
            self.head = self.mid = self.tail
            self.head.pre = None
            self.sign = True
            return res

        self.mid.pre.next = self.mid.next
        self.mid.next.pre = self.mid.pre
        if self.sign:
            self.sign = False
            self.mid = self.mid.pre
        else:
            self.sign = True
            self.mid = self.mid.next
        return res

    def popBack(self) -> int:
        if not self.head:
            return -1
        res = self.tail.val

        self.tail = self.tail.pre
        if not self.tail:
            self.head = self.mid = self.tail = None
            self.sign = False
            return res
        self.tail.next = None
        if self.sign:
            self.sign = False
            self.mid = self.mid.pre
        else:
            self.sign = True
        return res




# Your FrontMiddleBackQueue object will be instantiated and called as such:
obj = FrontMiddleBackQueue()
obj.pushFront(val)
obj.pushMiddle(val)
obj.pushBack(val)
param_4 = obj.popFront()
param_5 = obj.popMiddle()
param_6 = obj.popBack()