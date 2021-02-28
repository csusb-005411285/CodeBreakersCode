class Solution:
    def __init__(self):
        self.merge_cells = False

    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        self._candy_crush(board)
        return board

    def _candy_crush(self, board):
        self.merge_cells = False
        # check adjacent cells in cols
        for row in range(len(board)):
            for col in range(len(board[0]) - 2):
                if abs(board[row][col]) == abs(board[row][col + 1]) == abs(board[row][col + 2]) != 0:
                    board[row][col] = board[row][col + 1] = board[row][col + 2] = -abs(board[row][col])
                    self.merge_cells = True
        
        # check adjacent cells in rows
        for row in range(len(board) - 2):
            for col in range(len(board[0])):
                if abs(board[row][col]) == abs(board[row + 1][col]) == abs(board[row + 2][col]) != 0:
                    board[row][col] = board[row + 1][col] = board[row + 2][col] = -abs(board[row][col])
                    self.merge_cells = True     

        # merge cells using the technique used in move zeroes problem
        for col in range(len(board[0])):
            back = len(board) - 1
            for top in range(len(board) - 1, -1, -1):
                if board[top][col] > 0:
                    board[back][col] = board[top][col]
                    back -= 1
            for b in range(back, -1, -1):
                board[b][col] = 0
        return self.candyCrush(board) if self.merge_cells else board
        #return board
