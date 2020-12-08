class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_zero = False
        first_col_zero = False
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row == 0 and matrix[0][col] == 0: first_row_zero = True
                if col == 0 and matrix[row][0] == 0: first_col_zero = True
        for row in range(len(matrix)): 
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0
        for row in range(1, len(matrix)):
            if matrix[row][0] == 0:
                for col in range(len(matrix[0])):
                    matrix[row][col] = 0
        for col in range(1, len(matrix[0])):
            if matrix[0][col] == 0:
                for row in range(len(matrix)):
                    matrix[row][col] = 0
        if first_row_zero:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
        if first_col_zero:
            for row in range(len(matrix)):
                matrix[row][0] = 0
        return matrix
