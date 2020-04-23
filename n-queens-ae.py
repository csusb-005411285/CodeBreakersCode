class Solution:

    def solveNQueens(self, n: int) -> [str]:
        # init a list to store the positions of the queens
        positions = {}
        self.solve_n_queens_helper(n, 0, positions)
        result = self.format_output(positions, n)
        return result
    
    def solve_n_queens_helper(self, n, row, positions):
        # n is not 0-based and row is 0-based
        if n == row:
            return True

        col = 0
        for col in range(n):
            if self.is_cell_safe(positions, row, col):
                positions[row] = Position(row, col)              
                if self.solve_n_queens_helper(n, row + 1, positions):
                    return True

        return False
    
    def is_cell_safe(self, positions, row, col):
        """
        [0, 1]          [0, 3]
                [1, 2]
        [2, 1]          [2, 3]

        [0, 1] [1, 2] [2, 3] = (0 - 1) == (1 - 2) == (2 - 3) = -1
        [0, 3] [1, 2] [2, 1] = (0 + 3) == (1 + 2) == (2 + 1) = 3
        """
        for i in range(row):
            if positions[i].col == col or \
              positions[i].row - positions[i].col == row - col or \
              positions[i].row + positions[i].col == row + col:
                return False
        return True

    def format_output(self, positions, n):
        result = [["." for _ in range(n)] for _ in range(n)]
        formatted_res = []
        for position in positions:
          curr_pos = positions[position]
          result[curr_pos.row][curr_pos.col] = "Q"

        for row in range(n): 
          col_str = ""
          for col in range(n): 
            col_str += result[row][col]
          formatted_res.append(col_str)

        return formatted_res

class Position:
  def __init__(self, row, col):
    self.row = row
    self.col = col
    pass
