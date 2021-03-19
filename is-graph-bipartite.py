class Solution:
    def __init__(self):
        self.found_verts_with_same_color = False
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        adj_list = defaultdict(set)
        vert_list = [0] * len(graph)
        self.build_adj_list(graph, adj_list)
        for vert in adj_list.keys():
            if not self._is_bipartite(adj_list, vert_list, vert):
                return False
        return True
    
    def build_adj_list(self, graph, adj_list):
        for source, destinations in enumerate(graph):
            for dest in destinations:
                adj_list[source].add(dest)
                adj_list[dest].add(source)
    
    def _is_bipartite(self, adj_list, vert_list, vert):
        if self.found_verts_with_same_color:
            return False
        if vert_list[vert] == 0:
            vert_list[vert] = 1
        for neighbor in adj_list[vert]:
            if vert_list[vert] == vert_list[neighbor]:
                self.found_verts_with_same_color = True
                return False
            if vert_list[neighbor] == 0:
                vert_list[neighbor] = -vert_list[vert]
                self._is_bipartite(adj_list, vert_list, neighbor)
        return True
