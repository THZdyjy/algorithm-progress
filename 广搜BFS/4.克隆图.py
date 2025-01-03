class Solution:
    def bfs(self, node):
        # 利用bfs进行遍历
        # 先建一个队列
        queue = collections.deque([node])
        # 新建容器用来盛放这个节点, 使用set,这样盛放节点时，不会造成重复
        visited = {node}
        # 遍历该节点的所有邻居
        while queue:
            node = queue.popleft()
            for node in node.neighbors:
                if node in visited:
                    continue
                queue.append(node)
                visited.add(node)
        return list(visited)

    def copy_value(self, nodes):
        node_map = dict()
        for node in nodes:
            # 建立容器来盛放新的节点值,这里选择字典
            node_map[node] = Node(node.val) # 利用老节点的value来对新节点进行初始化
        return node_map

    def copy_neighbor(self, nodes, node_mapping):
        # 我们刚刚copy了旧节点的value,现在需要copy旧节点的neigbor
        # 遍历旧节点
        for node in nodes:
            new_node = node_mapping[node]
            # 遍历旧节点的neigbors
            for neighbor in node.neighbors:
                # 取出对应的新节点
                new_neighbor = node_mapping[neighbor]
                # 添加到新节点的neighbors中
                new_node.neighbors.append(new_neighbor)
        return

    def cloneGraph(self, node: 'Node') -> 'Node':
        # 首先进行corner case判断
        if not node:
            return node
        # 1.遍历所有的节点，将所有的节点取出来bfs
        nodes = self.bfs(node)
        # 依据旧节点,建立新节点，比如这里有四个，我们就建立四个，依次copy旧节点的两个属性，值和邻居到新节点中
        # 2.copy值
        node_mapping = self.copy_value(nodes)
        # 3.copy邻居
        self.copy_neighbor(nodes, node_mapping)
        return node_mapping[node]