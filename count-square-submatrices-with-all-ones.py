class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # init vars
        count = 0
        cache = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        # check for invalid inputs
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return matrix[0][0]
        # process
        # loop rows
        for row in range(len(matrix)):
            # loop cols
            for col in range(len(matrix[0])):
                # if current cell 1
                if matrix[row][col] == 1:
                    # check the neighboring cells
                    # choose the min. value and add 1 to it.
                    cache[row][col] = 1
                    if row - 1 >= 0 and col - 1 >= 0:
                        if cache[row - 1][col] >= 1 and cache[row][col - 1] >= 1 and cache[row - 1][col - 1] >= 1:
                            cache[row][col] = min(cache[row][col - 1], cache[row - 1][col], cache[row - 1][col - 1])  + 1
                    count += cache[row][col]
        return count
