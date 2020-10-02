class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: [[int]], blue_edges: [[int]]) -> [int]:
        graph = defaultdict(list)
        visited = set()
        path = defaultdict(int) 
        queue = deque()
        RED = 1
        BLUE = 0
        result = [-1 for i in range(n)]

        for i in range(len(red_edges)):
            graph[red_edges[i][0]].append((red_edges[i][1], RED))
            
        for j in range(len(blue_edges)):
            graph[blue_edges[j][0]].append((blue_edges[j][1], BLUE))
        
        queue.append((0, 0, -1))
        path[0] = 0
        visited.add((0, 0))

        while queue:
            node, dist, edge_color = queue.popleft() 

            for neigh_node in graph[node]:
                if neigh_node not in visited:
                    neigh_val = neigh_node[0]
                    neigh_col = neigh_node[1]

                    if edge_color != neigh_col:
                        # for cases where the same node is being processed but with a different
                        # edge color
                        # 0 ->(r) 1 and 3 ->(b) 1
                        # store 1 when it is encountered for the first time
                        if neigh_val not in path:
                            path[neigh_val] = dist + 1

                        visited.add(neigh_node)
                        color = BLUE if neigh_col == RED else RED 
                        queue.append((neigh_val, dist + 1, neigh_col))

        for key in path.keys():
            val = path[key]
            if val != float('inf'):
                result[key] = val
        
        return result
