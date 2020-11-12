# Recursive DFS
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        len_grid = len(grid) * 3
        big_grid = [['' for _ in range(len_grid)] for _ in range(len_grid)]
        visited = set()
        num_regions = 0
        self.build_graph(big_grid, grid) 
        for i, big_string in enumerate(big_grid): # 
            for j, char in enumerate(big_string):
                num_regions += self.regions_by_slashes_helper(big_grid, visited, (i, j))
        return num_regions
    
    def build_graph(self, big_grid, grid):
        # the column corresponds to the position of the character in the string
        # \/ and / are considered two separate strings
        # grid is a list and not a matrix
        for i, string in enumerate(grid): # 
            for j, char in enumerate(string):
                if char == '/':
                    # start from first row and last col
                    # keep traversing diagonally
                    # until the last row and first col 
                    big_grid[3 * i][(3 * j) + 2] = '/'
                    big_grid[(3 * i) + 1][(3 * j) + 1] = '/'
                    big_grid[(3 * i) + 2][3 * j] = '/'
                elif char == '\\':
                    # start from first row and first col
                    # keep traversing diagonally
                    # until the last row and last col 
                    big_grid[3 * i][3 * j] = '\\'
                    big_grid[(3 * i) + 1][(3 * j) + 1] = '\\'
                    big_grid[(3 * i) + 2][(3 * j) + 2] = '\\'

    def regions_by_slashes_helper(self, matrix, visited, vert):
        x, y = vert
        # Pay attention to this step
        if matrix[x][y] != '':
            return 0
        if vert in visited:
            return 0
        visited.add(vert)
        num_regions = 1
        for n_x, n_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= n_x < len(matrix) and 0 <= n_y < len(matrix[0]):
                self.regions_by_slashes_helper(matrix, visited, (n_x, n_y))
        return num_regions 

# Iterative DFS
class Solution:
    # the variable names are deceptive, grid is not a grid, but a list
    def regionsBySlashes(self, grid: [str]) -> int:
        len_grid = len(grid) * 3
        big_grid = [['' for _ in range(len_grid)] for _ in range(len_grid)]
        visited = set()
        num_regions = 0
        stack = deque()
        # [\/, /]
        # when building a grid * 3
        # the row corresponds to index of the list
        # the column corresponds to the position of the character in the string
        # \/ and / are considered two separate strings
        # grid is a list and not a matrix
        for i, string in enumerate(grid): # 
            for j, char in enumerate(string):
                if char == '/':
                    # start from first row and last col
                    # keep traversing diagonally
                    # until the last row and first col 
                    big_grid[3 * i][(3 * j) + 2] = '/'
                    big_grid[(3 * i) + 1][(3 * j) + 1] = '/'
                    big_grid[(3 * i) + 2][3 * j] = '/'
                elif char == '\\':
                    # start from first row and first col
                    # keep traversing diagonally
                    # until the last row and last col 
                    big_grid[3 * i][3 * j] = '\\'
                    big_grid[(3 * i) + 1][(3 * j) + 1] = '\\'
                    big_grid[(3 * i) + 2][(3 * j) + 2] = '\\'
        
        for i, big_string in enumerate(big_grid): # 
            for j, char in enumerate(big_string):
                if char == '' and (i, j) not in visited:
                    num_regions += 1
                    stack.append((i, j))
                    while stack:
                        x, y = stack.pop()
                        if (x, y) in visited:
                            continue
                        visited.add((x, y))
                        for n_x, n_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                            if 0 <= n_x < len_grid and 0 <= n_y < len_grid:
                                if big_grid[n_x][n_y] == '':
                                    stack.append((n_x, n_y))
        return num_regions
