class Solution:
    def __init__(self):
        self.longest_path = 1
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = [[1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        visited = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                self._longest_increasing_path(matrix, cache, (row, col))
        return self.longest_path
    
    def _longest_increasing_path(self, matrix, cache, vert):
        row, col = vert
        if cache[row][col] != 1:
            return cache[row][col]
        for n_row, n_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if 0 <= n_row < len(matrix) and 0 <= n_col < len(matrix[0]):
                if matrix[n_row][n_col] < matrix[row][col]:
                    path = self._longest_increasing_path(matrix, cache, (n_row, n_col))
                    cache[row][col]  = max(cache[row][col], path + 1)
                    if cache[row][col] > self.longest_path:
                        self.longest_path = cache[row][col]
        return cache[row][col]
        
