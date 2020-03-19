class Solution:
  def minPathSum(self, grid: List[List[int]]) -> int:
    if len(grid) == 1 and len(grid[0]) == 1:
      return grid[0][0]
    
    # init a matrix
    mat = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))] # O(n)
    mat[0][0] = grid[0][0] #
    # if it is the first col
    for row in range(1, len(grid)): # O(n)
      # then the value of the cell is equal to the sum of current cell
      # and the value of the cell before it
      mat[row][0] = mat[row - 1][0] + grid[row][0]
           
    # if it is the first row
    for col in range(1, len(grid[0])): # O(n) 
      # then the value of the cell is equal to the sum of current cell
      # and the value of the cell above it
      mat[0][col] = mat[0][col - 1] + grid[0][col]
    
    # loop through the grid
    for row in range(1, len(grid)): #O(n) 
      for col in range(1, len(grid[0])): # O(n)
        # calculate value of a cell
        mat[row][col] = min(mat[row - 1][col], mat[row][col - 1]) + grid[row][col]
           
    # return the value of the last cell
    return mat[-1][-1]  
      
    
