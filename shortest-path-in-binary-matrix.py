class Solution:
    def shortestPathBinaryMatrix(self, grid: [[int]]) -> int:
        queue = deque()
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        queue.append((0, 0, 1))
        while queue:
            x, y, dist = queue.popleft()

            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return dist

            if visited[x][y]:
                continue
            
            visited[x][y] = True

            for r, c in ((x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y - 1), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1)):
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                    if grid[r][c] == 0:
                        queue.append((r, c, dist + 1))    
        
        return -1
