class Solution:
  # https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/90739/Python-DFS-bests-85.-Tips-for-all-DFS-in-matrix-question.
  def __init__(self):
    self.rows = 0
    self.cols = 0
    self.matrix = [[]]
    # init a list to store the list of directions 
    self.directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    self.neighbors = []
    
  def can_reach_ocean(matrix, is_pacific = False):
    cells_that_can_reach_ocean = set();
    queue = collections.dequeue([])
    
    if is_pacific:
      for j in range(len(matrix[0])):
        queue.append((0, j))
      
      for i in range(len(matrix)):
        queue.append((i, 0))
    else:
      for j in range(len(matrix[0])):
        queue.append((len(matrix)-1,j))
      
      # Initialize Queue to have all cells in the left column.
      for i in range(len(matrix)):
        queue.append((i,len(matrix)-1)) 

      
  
  def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
    can_visit_matrix = [[False for _ in range len(matrix[0])] for _ in range(len(matrix))]
    pacific_atlantic_cells = set();
    
    pacific_cells = can_reach_ocean(matrix, is_pacific=True)
    atlantic_cells = can_reach_ocean(matrix, is_atlantic=True)
      
    for cell in pacific_cells:
      if cell in atlantic_cells:
        pacific_atlantic_cells.add(cell)
    
    return pacific_atlantic_cells
