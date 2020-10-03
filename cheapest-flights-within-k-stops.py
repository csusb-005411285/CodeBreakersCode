class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        adj_list = defaultdict(list)
        queue = [] 
        visited = []
        vertices_visited = K
        edges = 0

        # build a adjacency list from the list of edges
        for flight in flights:
            source = flight[0] 
            dest = flight[1] 
            cost = flight[2] 

            adj_list[source].append((dest, cost)) 

        # if source is in the graph
        if src in adj_list: 
            queue.append((0, src, edges)) 
        else:
            return -1

        while queue: 
            dist, node, edges = heapq.heappop(queue) 
                
            if edges > vertices_visited + 1:
                continue
            
            if node == dst:
                return dist 
            
            for vert in adj_list[node]:
                neigh_vert = vert[0] 
                neigh_cost = vert[1] 
                heapq.heappush(queue, (dist + neigh_cost, neigh_vert, edges + 1))

        return -1 
