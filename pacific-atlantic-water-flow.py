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
