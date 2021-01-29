class Solution:
    def find_all_gate_cells(self, rooms):
        n_rows, n_cols = len(rooms), len(rooms[0])
        cells = []
        for r in range(n_rows):
            for c in range(n_cols):
                if not rooms[r][c]: cells.append((r, c))
        return cells
    
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = deque()
        gate_cells = self.find_all_gate_cells(rooms)
        queue.append([cells for cells in gate_cells])
        while queue:
            nodes = queue.popleft()
            for node in nodes:
                x, y = node
                neighbors = []
                for n_x, n_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= n_x < len(rooms) and 0 <= n_y < len(rooms[0]):
                        if rooms[n_x][n_y] == 2147483647:
                            rooms[n_x][n_y] = rooms[x][y] + 1
                            neighbors.append((n_x, n_y))
                if neighbors:
                    queue.append(neighbors)
        
