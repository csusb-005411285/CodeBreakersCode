class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        indegree = {i: 0 for i in range(numCourses)}
        visited = set()
        queue = deque()
        for start, end in prerequisites:
            adj_list[start].append(end)
            indegree[end] += 1
        for k, v in indegree.items():
            if v == 0: queue.append([k])
        while queue:
            nodes = queue.pop()
            neighbors = []
            for node in nodes:
                visited.add(node)
                for start_vert in adj_list[node]:
                    indegree[start_vert] -= 1
            for k, v in indegree.items():
                if v <= 0 and k not in visited: 
                    neighbors.append(k)
            if neighbors:
                queue.append(neighbors)
        return True if len(visited) == numCourses else False
