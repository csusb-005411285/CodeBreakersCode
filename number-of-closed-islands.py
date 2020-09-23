class Solution:
    def closedIsland(self, grid: [[int]]) -> int:
        if len(grid[0]) == 0:
            return 0

        num_islands = 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if (i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1):
                    self.closed_island_helper(grid, [i, j])
                    
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[i]) - 1):
                if grid[i][j] == 1:
                    continue

                num_islands += 1
                self.closed_island_helper(grid, [i, j])
        
        return num_islands
    
    def closed_island_helper(self, grid, coord):
        x, y = coord
        
        if x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid[0]) - 1:
            return

        if x == 0 or y == 0 or x == len(grid) - 1 or y == len(grid[0]) - 1:
            if grid[x][y] == 1:
                return

        if grid[x][y] == 1:
            return

        grid[x][y] = 1

        self.closed_island_helper(grid, [x - 1, y])
        self.closed_island_helper(grid, [x + 1, y])
        self.closed_island_helper(grid, [x, y - 1])
        self.closed_island_helper(grid, [x, y + 1])

        return
