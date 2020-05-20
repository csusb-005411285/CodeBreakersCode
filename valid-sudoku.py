class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        if not self.are_rows_valid(board):
            return False
        
        if not self.are_cols_valid(board):
            return False
        
        if not self.are_grids_valid(board):
            return False
        
        return True
        
    def are_grids_valid(self, board):
        for i in (0, 3, 6):
            squares = []
            for j in (0, 3, 6):
                squares = [board[row][col] for col in range(j, j + 3) for row in range(i, i + 3)]

                unique_elements = []
                for square in squares:
                    if square != '.':
                        unique_elements.append(square)
    
    
                if len(set(unique_elements)) != len(unique_elements):
                    return False

        return True
    
    def are_cols_valid(self, board):
        cols = list(zip(*board))

        for i in range(len(cols)):
            unique_elements = []
            for j in range(len(cols[i])):
                if cols[i][j] != '.':
                    unique_elements.append(cols[i][j])

            if len(set(unique_elements)) != len(unique_elements):
                return False
        
        return True
    
    def are_rows_valid(self, board):
        for row in range(len(board)):
            cols = []
            for col in range(len(board[row])):
                if board[row][col] != '.':
                    cols.append(board[row][col]) 
            

            if len(set(cols)) != len(cols):
                return False
        
        return True 
