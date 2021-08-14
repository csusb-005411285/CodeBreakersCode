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
