class Solution:
  def eventualSafeNodes(self, graph: [[int]]) -> [int]:
        adj_list = defaultdict(list)
        outdegree = defaultdict(int)
        nodes = []
        stack = []
        for i in range(len(graph)):
            outdegree[i] = 0
        # build adj list and outdegree list
        for src, vertices in enumerate(graph):
            for i, dest in enumerate(vertices):
                adj_list[dest].append(src)
                outdegree[src] += 1
        # get all the nodes that have no outgoing edges
        for key, value in outdegree.items():
            if value == 0:
                stack.append(key)
        # perform topological sort
        while stack:
            node = stack.pop()
            nodes.append(node)
            for neigh in adj_list[node]:
                outdegree[neigh] -= 1
                if outdegree[neigh] == 0:
                    stack.append(neigh)
        # reverse the result and return
        return sorted(nodes)
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
