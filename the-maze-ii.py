class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        heap = []
        cache = [[float('inf') for _ in range(len(maze[0]))] for _ in range(len(maze))]
        dist = - 1
        visited = set()
        heappush(heap, (0, start))
        while heap:
            dist, node = heappop(heap)
            row, col = node
            cache[row][col] = dist
            if node == destination:
                return dist
            if (row, col) in visited:
                continue
            visited.add((row, col))
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                n_row = row
                n_col = col
                d = dist
                while 0 <= n_row + x < len(maze) and 0 <= n_col + y < len(maze[0]) and maze[n_row + x][n_col + y] != 1: #
                    n_row += x
                    n_col += y
                    d += 1
                if (n_row, n_col) not in visited or cache[n_row][n_col] > d:
                    cache[n_row][n_col] = d
                    heappush(heap, (d, [n_row, n_col]))
        return -1
