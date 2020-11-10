class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        vertex_colors = [0 for i in range(len(graph))]
        is_bipartite = True
        for k, v in enumerate(graph):
            is_bipartite = self.is_bipartite_helper(graph, k, vertex_colors)
            if not is_bipartite:
                return False
        return is_bipartite
    
    def is_bipartite_helper(self, graph, vert, vertex_colors):
        if vertex_colors[vert] == 0:
            vertex_colors[vert] = 1
        for neigh in graph[vert]:
            if vertex_colors[neigh] == vertex_colors[vert]:
                return False
            if vertex_colors[neigh] == -vertex_colors[vert]:
                continue
            vertex_colors[neigh] = -vertex_colors[vert]
            self.is_bipartite_helper(graph, neigh, vertex_colors)
        return True
