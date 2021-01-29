# Floyd-Warshall's algorithm
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist_matrix = [[float('inf')]*n for i in range(n)]
        for node1, node2, cost in edges:
            dist_matrix[node1][node2] = dist_matrix[node2][node1] = cost   
        for node in range(n):
            dist_matrix[node][node] = 0 
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist_matrix[i][j] = min(dist_matrix[i][j], dist_matrix[i][k] + dist_matrix[k][j])
        shortest_distance = float('inf')
        final_vert = None
        for row in range(len(dist_matrix)):
            count = 0
            for col in range(len(dist_matrix[0])):
                if dist_matrix[row][col] != float('inf'):
                    if dist_matrix[row][col] <= distanceThreshold:
                        count += 1
            if count <= shortest_distance:
                shortest_distance = count
                final_vert = row
        return final_vert
    

class Solution:
    def findTheCity(self, n: int, edges: [[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        result = {} 

        # build the adjacency list
        for edge in edges:
            src = edge[0]
            dest = edge[1]
            cost = edge[2]

            graph[src].append((dest, cost))
            graph[dest].append((src, cost))

        # get the number of vertices that can be reached starting from vertex i. Also, the vertices
        # that can be reached should have a distance below the threshold.
        for i in range(n): # 0
            num_vertices = self.get_num_vertices_less_than_threshold(graph, i, distanceThreshold) # g, 0, 4
            result[i] = num_vertices

        # Get the max index of the min value in the dict.
        # [0: 10, 1: 5, 2: 7, 3: 10] should return 3

        # get the min value from the map 
        min_vertex_val = min(result.values())
        # Return a list where any value from the dictionary that is not equal to the min_vertex_val 
        # is replaced with -1 and value equal to min_vertex_val is replaced by its index.
        index = list(map(lambda x: -1 if x[1] != min_vertex_val else x[0], result.items()))


        return max(index)
    
    def get_num_vertices_less_than_threshold(self, graph, vertex, thresh): 
        queue = [] 
        queue.append((0, vertex))
        reachable_nodes = []

        while queue:
            dist, node = heapq.heappop(queue)

            if node in reachable_nodes:
                continue
            
            reachable_nodes.append(node)

            for vert in graph[node]:
                neigh_vert = vert[0]
                neigh_cost = vert[1]

                if dist + neigh_cost <= thresh:
                    heapq.heappush(queue, (dist + neigh_cost, neigh_vert))

        return len(reachable_nodes) - 1
