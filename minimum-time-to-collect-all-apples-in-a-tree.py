class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj_list = defaultdict(list)
        visited = set()
        for i, edge in enumerate(edges):
            src, dest = edge
            adj_list[src].append(dest)
            adj_list[dest].append(src)
        min_time = self._min_time(adj_list, hasApple, visited, 0) - 2
        return max(0, min_time)
    
    def _min_time(self, adj_list, hasApple, visited, vert):
        if vert in visited:
            return 0
        visited.add(vert)
        time = 0
        for neigh in adj_list[vert]:
            time += self._min_time(adj_list, hasApple, visited, neigh)
        if time:
            time += 2
        else:
            time = 2 if hasApple[vert] else 0
        #print(vert, time)
        return time
