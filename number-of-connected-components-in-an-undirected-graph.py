class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        node_map = defaultdict(int)
        adj_list = defaultdict(list)
        visited = set()
        for i, edge in enumerate(edges):
            src, dest = edge
            adj_list[src].append(dest)
            adj_list[dest].append(src)
        _id = 1
        for node in range(n):
            if node not in visited:
                node_map[_id] = self._count_components(adj_list, visited, node)
                _id += 1
        return len(node_map)
    
    def _count_components(self, graph, visited, vert):
        if vert in visited:
            return 0
        visited.add(vert)
        path = 1
        for neigh in graph[vert]:
            path += self._count_components(graph, visited, neigh)
        return path
                
