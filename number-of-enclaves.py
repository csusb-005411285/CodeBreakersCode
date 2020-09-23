class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        grid = A

        if len(grid[0]) == 1:
            return 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if (i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1):
                    self.num_enclaves_helper(grid, [i, j])
                    
        return sum(sum(row) for row in grid) 
    
    def num_enclaves_helper(self, grid, coord):
        x, y = coord
        
        if x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid[0]) - 1:
            return

        if x == 0 or y == 0 or x == len(grid) - 1 or y == len(grid[0]) - 1:
            if grid[x][y] == 0:
                return

        if grid[x][y] == 0:
            return

        grid[x][y] = 0

        self.num_enclaves_helper(grid, [x - 1, y])
        self.num_enclaves_helper(grid, [x + 1, y])
        self.num_enclaves_helper(grid, [x, y - 1])
        self.num_enclaves_helper(grid, [x, y + 1])

        return
