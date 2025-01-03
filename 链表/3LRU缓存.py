"""
lru概念：LRU是Least Recently Used的缩写，即最近最少使用，是一种常用的页面置换算法，选择最近最久未使用的页面予以淘汰。
        该算法赋予每个页面一个访问字段，用来记录一个页面自上次被访问以来所经历的时间 t，当须淘汰一个页面时，选择现有页面中其 t 值最大的，即最近最少使用的页面予以淘汰。
core:LRU的性质：①取和放的操作都是O(1) ② 取和放元素时，这次操作是最近的，所以需要将该节点放到最头起。③当元素超出capacity时，淘汰节点
    core: 用双向链表和词典来维护以上的三个性质；get和put操作，都会涉及对节点最近状态的更新。
时空复杂度：get()和put()是O(1), 因为新建了个词典，空间为O(n),这里是n个节点。
标签：双向链表，哈希表，设计
"""
import collections

# 定义双端队列的节点(节点的key和val, next, pre)
class DoubleLinkedNode:
    def __init__(self, key=0, val=0, next=None, pre=None):
        self.key = key
        self.val = val
        self.next = next
        self.pre = pre


class LRUCache:
    # 初始化
    def __init__(self, capacity):
        self.capacity = capacity  # 总容量
        self.cur_capacity = 0  # 当前容量
        # j1：建立虚拟的头尾节点, 并连接（必须连起来，这样初始化的才是一个双端的队列，并且后面在移动节点位置时是需要的）
        self.head = DoubleLinkedNode()
        self.tail = DoubleLinkedNode()
        self.head.next = self.tail
        self.tail.pre = self.head
        # j2：建立词典，用来存放节点,key为key,node为value。这样在取和放时需要查找，时间复杂度都为O(1)
        self.key_node_dict = collections.defaultdict(DoubleLinkedNode)


    def put(self, key, value):
        # 如果key已经存在，对它重新赋值
        if key in self.key_node_dict:
            node = self.key_node_dict[key]  # O(1)
            node.val = value
            # j3：移动节点的位置
            self.removeNode(node)
            self.putHeadNext(node)
        else:
            self.cur_capacity += 1
            # 新建节点并放在head之后，（对页面操作了，更新它的时间）
            new_node = DoubleLinkedNode(key=key, val=value)
            self.putHeadNext(new_node)
            # 更新词典
            self.key_node_dict[key] = new_node

            # j5: 超出容量的话，淘汰最后一个节点, 没有等于号。是超出！！！
            if self.cur_capacity > self.capacity:
                self.removeLastNode()


    # 取元素
    def get(self, key):
        # 元素不存在
        if key not in self.key_node_dict:
            return -1
        # 得到当前节点值
        node = self.key_node_dict[key]
        val = node.val
        # 当前操作为最近操作，移动节点

        # 首先将当前节点从原双端队列中“摘”下来（画图）
        self.removeNode(node)
        # 放到head之后
        self.putHeadNext(node)
        return val


    # 将节点摘下来
    def removeNode(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        node.next, node.pre = None, None


    # 将节点放回去
    def putHeadNext(self, node):
        # j4：注意这里的顺序，先对head后的节点进行操作，否则节点丢失
        node.next = self.head.next
        self.head.next = node
        node.next.pre = node
        node.pre = self.head


    def removeLastNode(self):
        last_node = self.tail.pre
        last_key = last_node.key
        # 把节点从缓存和词典中同时删掉
        del self.key_node_dict[last_key]
        # 将节点摘下去即可
        self.removeNode(last_node)