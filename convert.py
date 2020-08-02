class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) < numRows:
            return s

        if numRows == 1:
            return s
        
        mat = [[] for _ in range(numRows)]
        delta = -1
        row = 0
        zigzag_word = ''

        for char in s:
            mat[row].append(char) 

            if row == 0:
                delta = -1
            elif row == numRows - 1:
                delta = 1

            row += -1 * delta
        
        for row in range(len(mat)):
            for col in range(len(mat[row])):
                zigzag_word += mat[row][col]
        
        return zigzag_word
