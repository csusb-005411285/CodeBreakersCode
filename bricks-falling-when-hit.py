class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        result = [0 for _ in range(len(hits))]
        for hit in hits:
            row, col = hit
            grid[row][col] -= 1
        for col in range(len(grid[0])):
            self.set_cells_to_stable(0, col, grid)
        for i, hit in enumerate(hits[::-1]):
            row, col = hit
            grid[row][col] += 1
            if grid[row][col] == 1 and self.is_stable(row, col, grid): # 1
                result[i] = self.get_count_unstable_bricks(row, col, grid) - 1 # 2
        return result[::-1]
    
    def get_count_unstable_bricks(self, row, col, grid):
        if grid[row][col] != 1:
            return 0
        grid[row][col] = 2
        count = 1
        for n_row, n_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]):
                count += self.get_count_unstable_bricks(n_row, n_col, grid)
        return count
    
    def is_stable(self, row, col, grid):
        if row == 0:
            return True
        for n_row, n_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]):
                if grid[n_row][n_col] == 2:
                    return True
        return False
    
    def set_cells_to_stable(self, row, col, grid):
        if grid[row][col] != 1:
            return
        grid[row][col] = 2
        for n_row, n_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]):
                self.set_cells_to_stable(n_row, n_col, grid)
        
'''
1. If the cell had a brick and is stable, then get a count of all of its neighbors that are bricks and are not stable.
2. -1 is because we do not count the initial coordinate in the hits list. 
'''
