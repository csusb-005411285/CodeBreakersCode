class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        result = [0 for _ in range(len(hits))]
        # for each hit
        # mark down the cells that need to be deleted.
        # we need to differentiate them from cells that will not
        # be deleted.
        for hit in hits:
            row, col = hit
            # set cell to -1 if it is an empty cell
            # set cell to 0 if it is a brick
            grid[row][col] -= 1
        # mark all bricks in the first row as stable     
        # also mark the neigboring bricks(1) as stable(2).
        for col in range(len(grid[0])):
            self.set_cells_to_stable(0, col, grid)
        # loop in reverse. IMPORTANT.    
        for i, hit in enumerate(hits[::-1]):
            row, col = hit
            # if the cell is empty(0), set it to 0. 
            # This is because if an empty cell has to be deleted, it 
            # was set to -1 in the lines above. So, +1 - 1 = 0
            # if the cell has a brick(1), set it to 1. This is because we set it to 0 in the lines above. So, +1 - 0 = 1 
            # we are unsetting the value for the brick to be deleted and resetting it.
            # we are also unsetting the value of the empty cell that is to be deleted and resetting it.
            grid[row][col] += 1
            # if cell is a brick and is stable
            # if the cell is an empty cell that is not to be deleted and the neighbors are stable -- this case will never happen as we are looping through the hits list.
            if grid[row][col] == 1 and self.is_stable(row, col, grid): # 1
                # mark all neighboring cells as stable.
                result[i] = self.get_count_unstable_bricks(row, col, grid) - 1 # 2
        return result[::-1]
    
    def get_count_unstable_bricks(self, row, col, grid):
        # if cell is empty(0) or stable(2)
        # Recall, we mark the cells to be deleted as 0 and -1.
        # in this step, we prevent double counting.
        # we ignore cells that are to be deleted later or is empty or is stable.
        if grid[row][col] != 1:
            return 0
        # mark cell as stable.
        # Why?
        # So that we do not delete the same cell again.
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
    
    # mark all cells that are connected to a stable cell as stable
    def set_cells_to_stable(self, row, col, grid):
        # if cell is an empty space, do nothing
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
