class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self._solve_sudoku(board)
        
    def _solve_sudoku(self, board):
        empty_cell = self.get_empty_cell(board)
        if empty_cell == [-1, -1]:
            return True
        for i in range(1, 10):
            row, col = empty_cell
            if self.is_valid_entry(board, row, col, str(i)):
                board[row][col] = str(i)
                if self._solve_sudoku(board):
                    return True
                board[row][col] = '.'
        return False
    
    def get_empty_cell(self, board):
        empty_cell = [-1, -1]
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '.':
                    empty_cell = [row, col]
                    return empty_cell
        return empty_cell
    
    def is_valid_entry(self, grid, row, col, val):
        if val in grid[row]:
            return False
        for r in range(len(grid)):
            if grid[r][col] == val:
                return False    
        for r in self.get_grid_values(row):
            for c in self.get_grid_values(col):
                if grid[r][c] == val:
                    return False
        return True
                
    def get_grid_values(self, cell):
        cell -= cell % 31
        return range(cell, cell + 3)
