from pprint import pprint as pp

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        # init vars
        # init matrix
        self.mat = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        # length of rows and cols
        self.m = len(matrix)
        self.n = len(matrix[0])
        # bit
        self.bit = [[0 for _ in range(self.n + 1)] for _ in range(self.m + 1)] # 5
        # initialize prefix sum
        for row in range(self.m): # 3
            for col in range(self.n):
                self.update(row, col, matrix[row][col])

    def update(self, row: int, col: int, val: int) -> None:
        # get the diff
        diff = val - self.mat[row][col] # 4
        # # update the cell with the new value
        self.mat[row][col] = val
        r = row + 1
        # calculate prefix sum using Fenwick tree's algorithm
        # row and col are 1-indexed
        # use + to calculate the prefix sums
        while r <= self.m: # 1
            c = col + 1
            while c <= self.n:
                self.bit[r][c] += diff
                c += (c & -c) # 6
            r += (r & -r)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        #   a. get the cell value from row1 - 1, col2
        top_right = self.get_sum(row1 - 1, col2)
        #   b. get the cell value from row2, col1 - 1
        bottom_left = self.get_sum(row2, col1 - 1)
        #   c. get the value from row1 - 1, col1 - 1
        top_left = self.get_sum(row1 - 1, col1 - 1)
        #   d. get value from row2, col2
        bottom_right = self.get_sum(row2, col2)
        return bottom_right + top_left - top_right - bottom_left 
    
    def get_sum(self, row, col):
        # Use Fenwick tree to get the sum
        # row and col are 1-indexed
        # use - to get the sum
        _sum = 0
        r = row + 1
        while r: # 2
            c = col + 1
            while c:
                _sum += self.bit[r][c]
                c -= (c & -c) # 6
            r -= (r & -r)
        return _sum

'''
1. row and col should iterate until <= len(matrix) as BIT is 1 indexed
2. row and col should iterate until 1 and not until 0 as BIT is 1 indexed
3. calculate the prefix sum for the initial matrix
4. diff should be val - mat[row][col] and not mat[row][col] - val
5. BIT should have an extra row and col
6. It is -c and not ~c
'''
