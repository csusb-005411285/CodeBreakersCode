class Solution:
    def __init__(self):
        self.surrounded_vertex = []
        
    def colorBorder(self, grid: [[int]], r0: int, c0: int, color: int) -> [[int]]:
        if not grid:
            return [[]]

        if len(grid) == 1 and len(grid[0]) == 0:
            return [[]]

        # call dfs on the initial position
        og_color = grid[r0][c0]
        self.color_border_helper(grid, r0, c0, og_color, color)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] < 0:
                    grid[row][col] = color

        return grid 

    def color_border_helper(self, grid, x, y, oc, nc):
        if grid[x][y] != oc:
            return grid
        
        grid[x][y] = -oc

        for i in ((x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)):
            row, col = i

            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]):
                self.color_border_helper(grid, row, col, oc, nc)

        if x - 1 >= 0 and y - 1 >= 0 and x + 1 <= len(grid) - 1 and y + 1 <= len(grid[0]) - 1:
            if abs(grid[x - 1][y]) == oc and abs(grid[x][y - 1]) == oc and abs(grid[x + 1][y]) == oc and abs(grid[x][y + 1]) == oc:
                grid[x][y] = oc
                
        return grid
