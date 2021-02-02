class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        heap = []
        visited = set()
        max_cost = 0
        self.build_adj_list(times, adj_list)
        heappush(heap, (0, k))
        while heap:
            node = heappop(heap)
            cost, vert = node
            if vert in visited:
                continue
            visited.add(vert)
            max_cost = max(max_cost, cost)
            for neighbor in adj_list[vert]:
                vert, cost_vert = neighbor
                if vert not in visited:
                    heappush(heap, (cost + cost_vert, vert))
        return max_cost if max_cost > 0 and len(visited) == n else -1
    
    def build_adj_list(self, edges, adj_list):
        for edge in edges:
            src, dest, cost = edge
            adj_list[src].append((dest, cost))
