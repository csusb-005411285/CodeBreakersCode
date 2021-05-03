class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = []
        visited = set()
        heappush(heap, (grid[0][0], 0, 0))
        visited.add((0, 0))
        time = 0
        while heap:
            elevation, row, col = heappop(heap)
            time = max(time, elevation)
            if row == col == len(grid) - 1:
                return time
            for n_row, n_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if 0 <= n_row < len(grid) and  0 <= n_col < len(grid[0]):
                    if (n_row, n_col) not in visited:
                        visited.add((n_row, n_col))
                        heappush(heap, (grid[n_row][n_col], n_row, n_col))
        return -1
