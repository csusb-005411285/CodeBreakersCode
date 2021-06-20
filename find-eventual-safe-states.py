class Solution:
  def eventualSafeNodes(self, graph: [[int]]) -> [int]:
        adj_list = defaultdict(list)
        vertices_with_no_outgoing_edges = []
        stack = deque()
        outdegree_graph = defaultdict(int) 
        no_of_vertices = len(graph)

        for i in range(no_of_vertices):
            outdegree_graph[i] = 0

        for source in range(no_of_vertices):
            for dest in graph[source]:
                adj_list[dest].append(source) 
                outdegree_graph[source] += 1

        for key, val in outdegree_graph.items():
            if outdegree_graph[key] == 0:
                stack.append(key)
                vertices_with_no_outgoing_edges.append(key)

        while stack:
            vert = stack.pop()

            if vert in adj_list:
                for v in adj_list[vert]:
                    outdegree_graph[v] -= 1
                
                    if outdegree_graph[v] == 0:
                        vertices_with_no_outgoing_edges.append(v)
                        stack.append(v)

        return sorted(vertices_with_no_outgoing_edges) 

# DFS
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]: 
        visited = [False] * len(graph)
        in_process =[False] * len(graph)
        safe_nodes = []
        for i in range(len(graph)):
            if not dfsUtils(i, graph, visited, in_process):
              safe_nodes.append(i)
        return safe_nodes
    
    def dfsUtils(self, node, g, visited, in_process):
        if in_process[node]:
            return True
        if visited[node]:
          return False
        in_process[node] = True
        visited[node] = True
        for adj_node in g[node]:
          if self.dfsUtils(adj_node, g, visited, in_process):
            return True
        in_process[node] = False
        return False
