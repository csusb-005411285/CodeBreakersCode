class Solution:
    def networkDelayTime(self, times: [[int]], N: int, K: int) -> int:
        graph = defaultdict(list)
        queue = [] 
        visited = []
        result = [float('-inf') for i in range(N + 1)]

        if N == 1:
            return 0

        for time in times:
            src = time[0]
            dest = time[1]
            cost = time[2]

            graph[src].append((dest, cost))

        if K in graph: 
            queue.append((0, K)) 
        else:
            return -1

        
        while queue:
            # pop the vertex with the smallest distance from source
            dist, node = heapq.heappop(queue)

            if node in visited:
                continue
            
            result[node] = dist
            visited.append(node)

            for vert in graph[node]:
                neigh_vert = vert[0]
                neigh_cost = vert[1]

                heapq.heappush(queue, (dist + neigh_cost, neigh_vert))

        if float('-inf') in set(result[1:]):
            return -1 

        return max(result) if max(result) != 0 else -1
