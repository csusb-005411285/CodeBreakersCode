class Solution: 

    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]: 

        if not matrix or not matrix[0]: 

            return [] 

        neighbors = [[0,1],[0,-1],[1,0],[-1,0]] 

        pacific = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))] 

        atlantic = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))] 

         

        def dfs(i, j, ocean): 

            ocean[i][j] = 1 

            for x, y in neighbors: 

                x += i 

                y += j 

                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[i][j] <= matrix[x][y] and ocean[x][y] == 0: 

                    dfs(x, y, ocean) 

                     

        for i in range(len(matrix)): 

            dfs(i, 0, pacific) 

            dfs(i, len(matrix[0]) - 1, atlantic) 

        for j in range(len(matrix[0])): 

            dfs(0, j, pacific) 

            dfs(len(matrix) - 1, j, atlantic) 

         

        ans = [] 

        for i in range(len(matrix)): 

            for j in range(len(matrix[0])): 

                if pacific[i][j] and atlantic[i][j]: 

                    ans.append([i,j]) 

                     

        return ans 

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        cells_pacific_ocean = []
        cells_atlantic_ocean = []
        self.get_cells_that_touch_pacific_ocean(matrix, cells_pacific_ocean)
        self.get_cells_that_touch_atlantic_ocean(matrix, cells_atlantic_ocean)
        cells_reach_pacific_ocean = set()
        cells_reach_atlantic_ocean = set()
        for vert in cells_pacific_ocean:
            self._dfs(matrix, cells_reach_both_oceans, vert, set(), cells_reach_pacific_ocean)
        for vert in cells_atlantic_ocean:
            self._dfs(matrix, cells_reach_both_oceans, vert, set(), cells_reach_atlantic_ocean)
        return self.get_cells_reach_both_oceans(cells_reach_pacific_ocean, cells_reach_atlantic_ocean)
    
    def get_cells_that_touch_pacific_ocean(self, matrix, cells_pacific_ocean):
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if col == 0 or row == 0:
                    cells_pacific_ocean.append([row, col])
    
    def get_cells_that_touch_atlantic_ocean(self, matrix, cells_atlantic_ocean):
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if col == len(matrix[0]) - 1 or row == len(matrix) - 1:
                    cells_atlantic_ocean.append([row, col])
    
    def _dfs(self, matrix, cells_reach_both_oceans, vert, visited, can_reach_ocean):
        row, col = vert
        if (row, col) in visited:
            return
        visited.add((row, col))
        can_reach_ocean.add((row, col))
        for neighbor_row, neighbor_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if 0 <= neighbor_row < len(matrix) and 0 <= neighbor_col < len(matrix[0]):
                if matrix[neighbor_row][neighbor_col] >= matrix[row][col]:
                    self._dfs(matrix, cells_reach_both_oceans, [neighbor_row, neighbor_col], visited, can_reach_ocean)     
        
    
    def get_cells_reach_both_oceans(self, cells_reach_pacific_ocean, cells_reach_atlantic_ocean):
        return list(set(cells_reach_pacific_ocean) & set(cells_reach_atlantic_ocean))
      
class Solution:
  # https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/90739/Python-DFS-bests-85.-Tips-for-all-DFS-in-matrix-question.  
  def get_neighboring_cells(self, matrix, i, j):
    rows = len(matrix)
    cols = len(matrix[0])
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    neighbors = []
    
    for x, y in directions:
      if 0 <= i + x < rows and 0 <= j + y < cols:
        # Check that water can actually flow downstream.
        if matrix[i][j] <= matrix[i + x][j + y]:
          neighbors.append((i + x, j + y))
    return neighbors 
  
  
  def can_reach_ocean(self, matrix, is_pacific):
    cells_that_can_reach_ocean = set();
    queue = collections.deque([])
    
    if is_pacific:
      for j in range(len(matrix[0])):
        queue.append((0, j))
      
      for i in range(len(matrix)):
        queue.append((i, 0))
    else:
      for j in range(len(matrix[0])):
        queue.append((len(matrix) - 1, j))
      
      # Initialize Queue to have all cells in the left column.
      for i in range(len(matrix)):
        queue.append((i, len(matrix[0]) - 1)) 
    
    while queue:
      x, y = queue.popleft()
      if (x, y) in cells_that_can_reach_ocean:
        continue
      
      cells_that_can_reach_ocean.add((x, y))
      
      for neighbor in self.get_neighboring_cells(matrix, x, y):
        queue.append(neighbor)
    
    return cells_that_can_reach_ocean
      
    
  def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
    if len(matrix) == 0:
      return []
    can_visit_matrix = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    pacific_atlantic_cells = set();
    
    pacific_cells = self.can_reach_ocean(matrix, True)
    atlantic_cells = self.can_reach_ocean(matrix, False)
      
    for cell in pacific_cells:
      if cell in atlantic_cells:
        pacific_atlantic_cells.add(cell)
    
    return pacific_atlantic_cells
