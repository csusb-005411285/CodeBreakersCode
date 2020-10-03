class Solution:
    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        adj_list = defaultdict(list)
        vertices_with_no_incoming_edges = []
        stack = deque()
        indegree_graph = defaultdict(int) 

        for i in range(numCourses):
            indegree_graph[i] = 0
        
        for i in range(len(prerequisites)):
            source = prerequisites[i][1]
            dest = prerequisites[i][0]
            adj_list[source].append(dest) 
            indegree_graph[dest] += 1 
        
        for key, val in indegree_graph.items():
            if indegree_graph[key] == 0:
                stack.append(key)
                vertices_with_no_incoming_edges.append(key)

        while stack:
            vert = stack.pop()

            if vert in adj_list:
                for v in adj_list[vert]:
                    indegree_graph[v] -= 1
                
                    if indegree_graph[v] == 0:
                        vertices_with_no_incoming_edges.append(v)
                        stack.append(v)
            
        return len(vertices_with_no_incoming_edges) == numCourses
