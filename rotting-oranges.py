class Solution:
    def orangesRotting(self, grid: [[int]]) -> int:
        queue = deque()
        time = 0 
        fresh_oranges = 0
        rotten_oranges = []

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh_oranges += 1

                if grid[r][c] == 2:
                    rotten_oranges.append((r, c))
        
        queue.append(rotten_oranges)

        while queue and fresh_oranges != 0:
            rotten_oranges = queue.popleft()
            time += 1
            neigh_oranges = []

            for i in range(len(rotten_oranges)):
                x, y = rotten_oranges[i]

                for row, col in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]):
                        if grid[row][col] == 1:
                            grid[row][col] = 2
                            neigh_oranges.append((row, col))
                            fresh_oranges -= 1

            if len(neigh_oranges) > 0: 
                queue.append(neigh_oranges)
        
        return time if fresh_oranges <= 0 else -1
