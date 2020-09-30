class Solution:
    def updateMatrix(self, matrix: [[int]]) -> [[int]]:
        if not matrix: return []
        queue = deque()
        res = [[0 for col in range(len(matrix[0]))] for row in range(len(matrix))]
        visited = [[False for col in range(len(matrix[0]))] for row in range(len(matrix))]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    queue.append((row, col))

        while queue:
            x, y = queue.popleft() # (1, 1)

            for row, col in ((x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)): # 1, 1 
                if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
                    if matrix[row][col] == 1 and not visited[row][col]:
                        res[row][col] = res[x][y] + 1
                        visited[row][col] = True
                        queue.append((row, col)) # (1, 1)
        
        return res
