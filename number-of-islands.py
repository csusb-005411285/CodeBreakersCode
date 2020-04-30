# tc: o(n), sc: o(n)
class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        visited = [[False for col in range(len(grid[rows]))] for rows in range(len(grid))]
        num_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                '''
                why do we have += here?
                because we need to calculate the total number of islands in the grid.
                '''
                num_islands += self.num_islands_helper(grid, visited, [row, col], 0)
        return num_islands
    
    def num_islands_helper(self, grid, visited, vertex, count = 0):
        x, y = vertex
        if visited[x][y]:
            return count 

        if grid[x][y] == '0':
            return count 

        visited[x][y] = True
        count = 1
        neighbors = self.get_neighbors(vertex, grid)
        for neighbor in neighbors:
            neigh_x, neigh_y = neighbor
            '''
            why don't we have a += here?
            because we are not counting the number of connected islands. Instead we are counting all the connected islands as one.
            '''
            count = self.num_islands_helper(grid, visited, [neigh_x, neigh_y], count)
        return count 
    
    def get_neighbors(self, vertex, grid):
        x, y = vertex
        neighbors = []
        # left
        if x > 0:
            neighbors.append([x - 1, y])
        # top
        if y > 0:
            neighbors.append([x, y - 1]) 
        # right
        if x < len(grid) - 1:
           neighbors.append([x + 1, y]) 
        # down
        if y < len(grid[x]) - 1:
            neighbors.append([x, y + 1])
        return neighbors
