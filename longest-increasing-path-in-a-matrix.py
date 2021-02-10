class Solution:
    def __init__(self):
        self.longest_increasing_path = 1
        
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        visited = set()
        cache = [[1 for col in range(len(matrix[0]))] for row in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                self._longest_increasing_path(matrix, (row, col), visited, cache)
        return self.longest_increasing_path
    
    def _longest_increasing_path(self, matrix, vert, visited, cache):
        row, col = vert
        if cache[row][col] != 1:
            return cache[row][col]
        if vert in visited:
            return cache[row][col]
        visited.add(vert)
        for neighbor in [(row - 1, col), (row + 1, col), (row, col + 1), (row, col - 1)]:
            n_row, n_col = neighbor
            if 0 <= n_row < len(matrix) and 0 <= n_col < len(matrix[0]):
                if (n_row, n_col) not in visited and matrix[n_row][n_col] < matrix[row][col]:
                    cache[row][col] = max(cache[row][col], self._longest_increasing_path(matrix, (n_row, n_col), visited, cache) + 1)
                    if cache[row][col] > self.longest_increasing_path:
                        self.longest_increasing_path = cache[row][col]
        visited.remove(vert)
        return cache[row][col]
