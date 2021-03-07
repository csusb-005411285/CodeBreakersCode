class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        cache = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        area = 0
        for row in range(1, len(cache)):
            for col in range(1, len(cache[0])):
                if matrix[row - 1][col - 1] == '1':
                    cache[row][col] = min(cache[row - 1][col], cache[row][col - 1], cache[row - 1][col - 1]) + 1
                    area = max(area, cache[row][col])
        return area ** 2
