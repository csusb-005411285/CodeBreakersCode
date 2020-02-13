class Solution:
  def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
    # preflight
    if not matrix: 
      return []
    # set the directions matrix
    self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
    # init rows and columns
    rows = len(matrix)
    cols = len(matrix[0])
    # init two boolean matrixes where each index indicates whether a 
    # the ocean can be reached from that index or not
    p_visited = [[False for _ in range(cols)] for _ in range(rows)]
    a_visited = [[False for _ in range(cols)] for _ in range(rows)]
    # init a var to store results
    result = []
        
    for i in range(rows):
      # p_visited[i][0] = True
      # a_visited[i][n-1] = True
      # check if the water can flow from left edge to the right or bottom edge
      self.dfs(matrix, i, 0, p_visited, rows, cols)
      # check if the water can flow from the right edge to the left or top edge
      self.dfs(matrix, i, cols-1, a_visited, rows, cols)
    
    for j in range(cols):
      # p_visited[0][j] = True
      # a_visited[m-1][j] = True
      # check if the water can flow from the top edge to the right or bottom edge
      self.dfs(matrix, 0, j, p_visited, rows, cols)
      # check if the water can flow from the bottom edge to the top edge or left edge
      self.dfs(matrix, rows-1, j, a_visited, rows, cols)

    for i in range(rows):
      for j in range(cols):
        # indicates the water can reach this index from Pacific ocean as well as Atlantic ocean
        if p_visited[i][j] and a_visited[i][j]:
          result.append([i,j])
    return result
                
  def dfs(self, matrix, i, j, visited, rows, cols):
    # when dfs called, meaning its caller already verified this point 
    visited[i][j] = True
    for dir in self.directions:
      x, y = i + dir[0], j + dir[1]
      # check whether the cell can "receive" the water; not "send" the water
      if x < 0 or x >= rows or y < 0 or y >= cols or visited[x][y] or matrix[x][y] < matrix[i][j]:
        continue
      self.dfs(matrix, x, y, visited, rows, cols)
        
