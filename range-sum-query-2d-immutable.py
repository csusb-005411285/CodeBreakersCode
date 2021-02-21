class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_matrix = matrix
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                top_cell = self.prefix_matrix[row - 1][col] if row - 1 >= 0 else 0
                left_cell = self.prefix_matrix[row][col - 1] if col - 1 >= 0 else 0
                diag_cell = self.prefix_matrix[row - 1][col - 1] if row - 1 >= 0 and col - 1 >= 0 else 0
                self.prefix_matrix[row][col] += top_cell + left_cell - diag_cell

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top_cell = self.prefix_matrix[row1 - 1][col2] if row1 - 1 >= 0 else 0
        left_cell = self.prefix_matrix[row2][col1 - 1] if col1 - 1 >= 0 else 0
        diag_cell = self.prefix_matrix[row1 - 1][col1 - 1] if row1 - 1 >= 0 and col1 - 1 >= 0 else 0
        sum_regions = self.prefix_matrix[row2][col2] - top_cell - left_cell + diag_cell 
        return sum_regions
