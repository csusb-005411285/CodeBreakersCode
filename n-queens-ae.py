# tc: o(n2), sc: o(n)
class Solution:

    def solveNQueens(self, n: int) -> [str]:
        positions = {}
        board = []
        self.solve_n_queens_helper(n, 0, positions)
        board = self.format_output(positions, n)
        return board 
    
    def solve_n_queens_helper(self, n, row, positions):
        if row == n:
            return True

        for col in range(n): #n
            if self.is_valid_position(row, col, positions):
                positions[row] = [row, col]
                if self.solve_n_queens_helper(n, row + 1, positions): #n
                    return True

        return False
    
    def is_valid_position(self, row, col, positions):
        for i in range(row): #n
            queen_pos_row, queen_pos_col = positions[i]
            if col == queen_pos_col or row + col == queen_pos_row + queen_pos_col or queen_pos_row - queen_pos_col == row - col:
                return False
        return True

    def format_output(self, positions, n):
        result = [["." for _ in range(n)] for _ in range(n)]
        formatted_res = []
        for position in positions:
            row, col = positions[position] 
            result[row][col] = "Q"

        for row in range(n): 
          col_str = ""
          for col in range(n): 
            col_str += result[row][col]
          formatted_res.append(col_str)
        return formatted_res

"""
[0, 0]  [0, 1] [0, 2]
[1, 0]  [1, 1] [1, 2]
[2, 0]  [2, 1] [2, 2]
"""
