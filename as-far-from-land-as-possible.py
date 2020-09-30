class Solution:
    def maxDistance(self, grid: [[int]]) -> int:
        ma = -1
        matrix = grid

        if not matrix: return []
        queue = deque()
        res = [[0 for col in range(len(matrix[0]))] for row in range(len(matrix))]
        visited = [[False for col in range(len(matrix[0]))] for row in range(len(matrix))]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 1:
                    queue.append((row, col))

        while queue:
            x, y = queue.popleft()

            for row, col in ((x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)): # 1, 1 
                if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
                    if matrix[row][col] == 0 and not visited[row][col]:
                        res[row][col] = res[x][y] + 1
                        ma = max(ma, res[row][col])
                        visited[row][col] = True
                        queue.append((row, col))

        return ma
