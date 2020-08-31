class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix[0]) == 0:
            return False

        row = 0 
        col = len(matrix[0]) - 1 # 1

        while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]): # 0 1
            if target == matrix[row][col]: # 3 == m[0][1]
                return True
            elif target < matrix[row][col]: # 
                col -= 1
            else:
                row += 1 # 1
        
        return False
