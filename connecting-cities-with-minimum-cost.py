class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for a,b,cost in connections:
            graph[a].append((b,cost))
            graph[b].append((a,cost))
        cost = 0
        minHeap = [(0, 1)]
        visited = set()
        while minHeap:
            minCost,city = heapq.heappop(minHeap)
            if city in visited:
                continue
            visited.add(city)
            cost += minCost
            for nxt,c in graph[city]:
                heapq.heappush(minHeap,(c, nxt))
        return -1 if len(visited) < n else cost
