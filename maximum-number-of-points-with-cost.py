class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # init vars
        # length of rows and cols
        m = len(points)
        n = len(points[0])
        # cache
        cache = [0] * n
        # cache to store max left and right values
        left = [points[0][0]] + [0] * (n - 1)
        right = [0] * (n - 1) + [points[0][n - 1]] 
        prev = points[0]
        # initial checks
        
        # process
        # loop through the rows
        for row in range(1, m):
            left = [-1] + [0] * n
            right = [0] * n + [-1]
            for col in range(n):
                left[col] = max(prev[col], left[col - 1] - 1)
            for col in range(n - 1, -1, -1): 
                right[col] = max(prev[col], right[col + 1] - 1)
            for col in range(n):
                cache[col] = points[row][col] + max(left[col], right[col])
            prev = cache[:]
        # return the max value of the last row of cache
        return max(prev)
