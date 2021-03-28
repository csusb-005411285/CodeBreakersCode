class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        cell_map = defaultdict(list)
        buildings = 0
        building_count = defaultdict(int)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    buildings += 1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                visited = set()
                if grid[row][col] == 1:
                    self._shortest_distance(grid, visited, cell_map, building_count, (row, col))
        min_dist = float('inf')
        for key, value in cell_map.items():
            dist, count_buildings = value
            if count_buildings == buildings:
                min_dist = min(min_dist, dist)
        return min_dist if min_dist != float('inf') else -1
    
    def _shortest_distance(self, grid, visited, cell_map, building_count, vert):
        queue = deque()
        queue.append((vert, 0))
        while queue:
            node, dist = queue.popleft()
            row, col = node
            if node in visited:
                continue
            visited.add(node)
            if grid[row][col] == 0:
                key = self.get_key(row, col)
                if key in cell_map:
                    cell_map[key] = [cell_map[key][0]+dist, cell_map[key][1]+1] 
                else:
                    cell_map[key] = [dist, 1]
            for n_row, n_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:   
                if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]):
                    if grid[n_row][n_col] == 0:
                        queue.append(((n_row, n_col), dist + 1))
                    
    def get_key(self, row, col):
        return str(row) + ',' + str(col)
        
