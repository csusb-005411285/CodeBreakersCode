class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        row = 0
        col = cols - 1
        while 0 <= row < rows and 0 <= col < cols:
            element = binaryMatrix.get(row, col)
            if element == 0: row += 1
            if element == 1: col -= 1
        return col + 1 if row != -1 and col != cols - 1 else -1

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
