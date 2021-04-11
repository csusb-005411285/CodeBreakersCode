class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        heap = []
        shortest_dist = - 1
        heappush(heap, (0, start))
        visited = set()
        cache = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
        while heap:
            dist, node = heappop(heap)
            row, col = node
            visited.add((row, col))
            cache[row][col] = dist
            if row == destination[0] and col == destination[1]:
                return dist
            for n_row, n_col in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                neigh_row = row
                neigh_col = col
                d = 0
                while 0 <= neigh_row + n_row < len(maze) and 0 <= neigh_col + n_col < len(maze[0]) and maze[neigh_row + n_row][neigh_col + n_col] != 1:
                    neigh_row += n_row
                    neigh_col += n_col
                    d += 1
                if neigh_row < 0 or neigh_row >= len(maze) or neigh_col < 0 or neigh_col >= len(maze[0]):
                    continue
                if (neigh_row, neigh_col) not in visited or cache[neigh_row][neigh_col] > dist + d:
                    cache[neigh_row][neigh_col] = dist + d
                    heappush(heap, (dist + d, (neigh_row, neigh_col)))
        return shortest_dist
        
