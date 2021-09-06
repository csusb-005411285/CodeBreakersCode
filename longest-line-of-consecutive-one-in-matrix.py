class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        # init vars
        # 3d matrix
        cache = [[[0 for _ in range(4)] for _ in range(len(mat[0]))] for _ in range(len(mat))]
        # max    
        _max = 0
        # initial checks
        # if 1 row and 1 col
        if len(mat[0]) == 1 and len(mat) == 1:
            return mat[0][0]
        # process
        # loop through rows
        for row in range(len(mat)):
            # loop through cols
            for col in range(len(mat[0])):
                # if cell has a value of 1
                if mat[row][col] == 1:
                    for i in range(4): # 1
                        cache[row][col][i] = 1 
                    # check the top row               
                    if row - 1 >= 0:
                        cache[row][col][0] += cache[row - 1][col][0] 
                    # check the left column
                    if col - 1 >= 0:
                        cache[row][col][1] += cache[row][col - 1][1] 
                    # check the digaonal cell
                    if col - 1 >= 0 and row - 1 >= 0:
                        cache[row][col][2] += cache[row - 1][col - 1][2]
                    # check the cell in the next col and previous row
                    if row - 1 >= 0 and col + 1 < len(mat[0]):
                        cache[row][col][3] += cache[row - 1][col + 1][3]
                    # calculate the max value
                    _max = max(_max, max(cache[row][col]))
        # return
        return _max

'''
1. If a cell has 1 in it, then it forms a line of length 1 along the horizontal, vertical, diagonal, and anti-diagonal line. 
'''
