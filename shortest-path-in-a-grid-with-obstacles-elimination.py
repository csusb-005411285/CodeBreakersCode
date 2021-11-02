# Dijkastra's algorithm
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # init vars
        heap= []
        visited = set()
        cache = defaultdict(int)
        min_cost = float('inf')
        # process
        # add a tuple to heap. Tuple should contain ((row, col), cost, k value)
        heappush(heap, (0, (0, 0), k)) 
        # add source to visited
        visited.add((0, 0, k)) 
        cache[(0, 0, 0)] = 0
        # set the default value of cache to  float inf
        while heap:
            # pop from heap
            cost, vert, new_k = heappop(heap) 
            row, col = vert 
            # if value of k is less than 0
            if new_k < 0:
                continue
            # if we are at the destination
            if row == len(grid) - 1 and col == len(grid[0]) - 1: 
                return cost
            # get neighbors
            for n_row, n_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                updated_k = new_k
                new_cost = cost
                if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]): 
                    # if neighbring cell is 1, add 1 to cost and decrement k by 1
                    if grid[n_row][n_col] == 1:
                        updated_k -= 1 
                    # calculate the cost
                    new_cost += 1
                    # if neighbor is not visited or cost of visting neighbor is smaller than the current value
                    if (n_row, n_col, updated_k) not in visited or ((n_row, n_col, updated_k) in cache and  cache[(n_row, n_col, updated_k)] > new_cost):
                        # add to heap
                        heappush(heap, (new_cost, (n_row, n_col), updated_k))
                        # add to visited
                        visited.add((n_row, n_col, updated_k))
                        # add to cache
                        cache[(n_row, n_col, updated_k)] = new_cost
        # return
        return -1

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # init vars
        queue = deque()
        visited = set()
        _min = float('inf')
        # check edge cases
        if k == 0:
            return len(grid) - 1 + len(grid[0]) - 1
        queue.append((0, 0, 0, 0))
        # bfs
        while queue:
            row, col, k_so_far, edges = queue.popleft()
            # check if the number of edges exceed k
            if k_so_far > k:
                continue
            # check if the vert is visited
            if (row, col, k_so_far) in visited:
                continue
            visited.add((row, col, k_so_far))
            
            # check dest
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                _min = min(_min, edges)
            # get neighbors
            for n_row, n_col in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]):
                    neigh_k = k_so_far + 1 if grid[n_row][n_col] == 1 else k_so_far
                    queue.append((n_row, n_col, neigh_k, edges + 1))
        return _min if _min != float('inf') else -1

    
# Alternate
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # init vars
        queue = deque()
        visited = set()
        cache = defaultdict(int)
        _min = float('inf')
        # check for invalid inputs
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0
        # BFS
        # add first node
        queue.append((0, 0, 0, 0))
        visited.add((0, 0))
        # keep looping until we encounter all nodes
        while queue:
            # pop
            row, col, obst, path = queue.popleft()
            # check for k
            if obst > k:
                continue
            # check for dest
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                # store max path
                _min = min(_min, path)
            # store in cache
            cache[(row, col)] = obst
            # get neighbors
            for n_row, n_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                new_obst = obst
                if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]):
                    if grid[n_row][n_col] == 1:
                        new_obst = obst + 1
                    # check for visited or current count for obstacles is less than in cache.
                    if (n_row, n_col) not in visited or ((n_row, n_col) in cache and new_obst < cache[(n_row, n_col)]):
                        # add neighbors to queue
                        queue.append((n_row, n_col, new_obst, path + 1))
                        # add to visited
                        visited.add((n_row, n_col))
                        cache[(n_row, n_col)] = new_obst
        # return min path
        return _min if _min != float('inf') else -1
