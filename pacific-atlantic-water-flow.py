class Solution:
  # https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/90739/Python-DFS-bests-85.-Tips-for-all-DFS-in-matrix-question.
  def __init__(self):
    self.rows = 0
    self.cols = 0
    self.matrix = [[]]
    # init a list to store the list of directions 
    self.directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
  
  def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
    self.matrix = matrix
    # init a var to store the length of rows
    self.rows = len(matrix)
    # init a var to store the length of cols
    self.col = len(matrix[0])
    
    # init a boolean matrix to store value if a cell can move water to Pacific ocean
    can_move_to_pac_ocean = [[False for _ in range(self.cols)] for _ in range(self.rows)]
    # init a boolean matrix to store value if a cell can move water to Atlantic ocean
    can_move_to_atl_ocean = [[False for _ in range(self.cols)] for _ in range(self.rows)]
    
    # init a list of grid coordinates
    grid_coordinates = []
    
    # perform DFS from the left edge; check if water can move from Pacific ocean to Atlantic ocean
    # mark cells in the can_move_to_pac_ocean to 1 if the water can flow into it
    for i in range(self.col): # O(n)
      self.dfs(i, 0, can_move_to_atl_ocean)
    
    # perform DFS from the top edge; check if water can move from Pacific ocean to Atlantic ocean
    for i in range(self.col):
      self.dfs(0, i, can_move_to_atl_ocean)
    
    # perform DFS from the right edge
    for i in range(self.rows):
      self.dfs(i, self.cols - 1, can_move_to_pac_ocean)
    
    # perform DFS from the bottom edge
    for i in range(self.rows):
      self.dfs(self.rows - 1, i, can_move_to_atl_ocean)
    
    # loop through both the matrix to check if the cells match
    return []
    
    
  # dfs method
  def dfs(self, x, y, can_move_to_ocean):
      print(x)
      print(y)
      print(can_move_to_ocean)
      print(can_move_to_ocean[0])
      # init a list to store the visited nodes
      can_move_to_ocean[x][y] = True
      # for the x and y value of the cell indices
      for direction in self.directions:
        neighbor_x, neighbor_y = x + direction[0], y + direction[1]
        # check if it can accept value from the four neighbors
        if x < 0 or x > self.rows or y < 0 or y > self.cols or can_move_to_ocean[x][y] or can_move_to_ocean[x][y] < can_move_to_ocean[neighbor_x][neighbor_y]:
          continue
        # recurse itself
        self.dfs(x, y, can_move_to_ocean)
      
    
        
