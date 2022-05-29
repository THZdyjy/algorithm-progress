# 链表的实现方式1
# 学算法学的是思维方式，算法思想
class node():
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = node(1)
node2 = node(2)
node3 = node(3)
node1.next = node2
node2.next = node3
node3.next = None

p = node1
while p != None:
    print(p.data)
    print(id(p))
    p = p.next
print(p)

# 实现方式2
# data = [None 3    2 0 None 1]
# next = [None None 1 5 None 2]
data, next = [None] * 10, [None] * 10

# 在ind号节点的后面添加p号节点，值为v
def add(ind, p, v):
    next[ind] = p
    data[p] = v

data[3] = 0
add(3, 5, 1)
add(5, 2, 2)
add(2, 1, 3)
add(1, 0, 4)
add(0, 4, 5)

p = 3
while p != None:
    print(data[p])
    p = next[p]

