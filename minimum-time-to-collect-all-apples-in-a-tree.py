class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj_list = defaultdict(list)
        visited = set()
        for i, edge in enumerate(edges):
            src, dest = edge
            adj_list[src].append(dest)
            adj_list[dest].append(src)
        return max(0, self._min_time(adj_list, visited, hasApple, 0) - 2)
    
    def _min_time(self, adj_list, visited, hasApple, vert):
        if vert in visited:
            return 0
        visited.add(vert)
        time = 0
        for neigh in adj_list[vert]:
            time += self._min_time(adj_list, visited, hasApple, neigh)
        if hasApple[vert] or time > 0:
            time += 2
        return time
