class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 边界条件判断
        if numCourses == 1:
            return True
        if len(prerequisites) == 0:
            return True

        # 建立拓扑关系图&计算每个节点的入度
        course_neighbor_graph = collections.defaultdict(set)
        indegrees = [0] * numCourses
        for course_pair in prerequisites:
            post, pre = course_pair
            course_neighbor_graph[pre].add(post)
            indegrees[post] += 1

        # 遍历入度列表，将入度为0的节点入队
        queue = collections.deque([])
        res = list()
        for node_id, num in enumerate(indegrees):
            if num == 0:
                queue.append(node_id)
                res.append(node_id)

        # bfs，遍历图，依次将入度为0的节点入队，出队
        while queue:
            cur_course = queue.popleft()
            neighbors = course_neighbor_graph[cur_course]
            for neighbor in neighbors:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    res.append(neighbor)
                    queue.append(neighbor)
        return len(res) == numCourses
