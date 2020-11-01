class Solution:
    def __init__(self):
        # use a var to store the number of paths
        self.path = 0
        self.num_of_empty_squares = 0

    def uniquePathsIII(self, grid: [[int]]) -> int:
        start = (0, 0)
        visited = set()
        curr_coord = [(0, 0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    self.num_of_empty_squares += 1
                if grid[i][j] == 1:
                    start = (i, j)
        # call a helper method
        self.unique_paths_helper(grid, visited, start, curr_coord)
        # retunr the number of paths
        return self.path

    def unique_paths_helper(self, grid, visited, coord, curr_coord):
        x, y = coord
        if grid[x][y] == -1:
            return
        # check if vertex is the dest
        if grid[x][y] == 2:
            if len(curr_coord) == self.num_of_empty_squares + 2: #man
                self.path += 1
            return # man
        # check if the vertex is already visited
        if (x, y) in visited:
            return
        # mark the vertex as visited
        visited.add((x, y))
        # get the neighbors
        for n_x, n_y in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            # loop through the neighbors
            if 0 <= n_x < len(grid) and 0 <= n_y < len(grid[0]):
                # call the recursive method
                self.unique_paths_helper(grid, visited, (n_x, n_y), curr_coord + [(n_x, n_y)])
        # remove the vertex from the visited list
        visited.remove((x, y))
        return
