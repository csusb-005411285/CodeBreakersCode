class Solution:
    def solve(self, n, edges):
        if n <= 0:
            return 0

        adj = [[] for _ in range(n+1)]
        times = [float("inf") for _ in range(n+1)]
        heap = []
        seen = set()

        for start, end, time in edges:
            adj[start].append((end, time))
            adj[end].append((start, time))

        heap.append((0, 0)) 

        while heap:
            time_node, node = heapq.heappop(heap) 
            times[node] = min(times[node], time_node) 

            if node in seen:
                continue

            seen.add(node) 

            for neighbors in adj[node]: 
                heapq.heappush(heap, (neighbors[1] + times[node], neighbors[0]))

        return max(times)
