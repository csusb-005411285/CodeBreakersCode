class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        curr_row, curr_col = 0, cols-1
        while curr_row < rows and curr_col >= 0:
            if not binaryMatrix.get(curr_row, curr_col):
                curr_row += 1
            else:
                curr_col -= 1
        return curr_col + 1 if (curr_col != cols-1) else -1
