class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_matrix = matrix
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                row_val = 0
                col_val = 0
                diag_val = 0
                if 0 <= row - 1 < len(matrix):
                    row_val = self.prefix_matrix[row - 1][col]
                if 0 <= col - 1 < len(matrix[0]):
                    col_val = self.prefix_matrix[row][col - 1]
                if 0 <= row - 1 < len(matrix) and 0 <= col - 1 < len(matrix[0]):
                    diag_val = self.prefix_matrix[row - 1][col - 1]
                self.prefix_matrix[row][col] += row_val + col_val - diag_val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_up_to_first_cell = self.prefix_matrix[row1 - 1][col1 - 1] if 0 <= row1 - 1 < len(self.prefix_matrix) and 0 <= col1 - 1 < len(self.prefix_matrix[0]) else 0
        sum_up_to_first_row = self.prefix_matrix[row1 - 1][col2] if 0 <= row1 - 1 < len(self.prefix_matrix) else 0
        sum_up_to_first_col = self.prefix_matrix[row2][col1 - 1] if 0 <= col1 - 1 < len(self.prefix_matrix[0]) else 0
        result = self.prefix_matrix[row2][col2] + sum_up_to_first_cell - sum_up_to_first_col - sum_up_to_first_row 
        return result
