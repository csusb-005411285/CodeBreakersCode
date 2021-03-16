class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        cache = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        cache_island_id = defaultdict(int)
        island_id = 2
        for row in range(len(grid)): # 1
            for col in range(len(grid[0])): # 1 
                if grid[row][col] == 1: 
                    cache_island_id[island_id] = self._largest_island(grid, visited, cache, (row, col), island_id)
                    max_area = max(max_area, cache_island_id[island_id])
                    island_id += 1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    area_neighbors = 0
                    neighbors = set()
                    area = 0
                    for n_row, n_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                        if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]):
                            neighbor = grid[n_row][n_col]
                            neighbors.add(neighbor)
                    for neigh in neighbors:
                        area += cache_island_id[neigh]
                    max_area = max(max_area, area + 1)
        return max_area
    
    def _largest_island(self, grid, visited, cache, vert, island_id): # 1, 1
        row, col = vert
        if vert in visited:
            return 0
        grid[row][col] = island_id
        visited.add(vert) # (0, 0) (1, 1)
        area = 1
        for n_row, n_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]: # 1 0
            if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]):
                if grid[n_row][n_col] == 1:
                    area += self._largest_island(grid, visited, cache, (n_row, n_col), island_id)
        visited.remove(vert)
        return area
