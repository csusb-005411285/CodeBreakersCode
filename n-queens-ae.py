class Solution:
    def __init__(self):
        self.queens = []
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        self._solve_n_queens(n, 0, [])
        boards = self.construct_boards(n)
        return boards
    
    def _solve_n_queens(self, n, row, queens):
        if n == row:
            self.queens.append(queens)
            return
        for col in range(n):
            if self.can_place(row, col, queens):
                self._solve_n_queens(n, row + 1, queens + [col])
        return
    
    def can_place(self, row, col, queens):
        for r, c in enumerate(queens):
            if col == c or row - r == abs(col - c):
                return False
        return True
    
    def construct_boards(self, n):
        boards = []
        for row in self.queens:
            board = []
            for r, c in enumerate(row):
                row = []
                for i in range(n):
                    if i == c:
                        row.append('Q')
                    else:
                        row.append('.')
                board.append(''.join(row))
            boards.append(board)
        return boards
