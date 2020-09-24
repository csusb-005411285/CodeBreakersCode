class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if len(grid) == 1 and len(grid[0]) == 1 and grid[0] == 1:
            return 4

        perimeter = 0

        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                val = grid[i][j] 

                if val == 0:
                    continue

                perimeter += 4 

                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    perimeter -= 1 
                    
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    perimeter -= 1 
                    
                if i + 1 < len(grid) and grid[i + 1][j] == 1:
                    perimeter -= 1 
                    
                if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                    perimeter -= 1 
        
        return perimeter
