class Solution:
  def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    # init a matrix to store the unique paths
    unique_paths = [[-1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))] #O(n)
    
    # loop through the obstaclegrid to populate the first row and column of unique paths
    for row in range(len(obstacleGrid)): #O(n)
      for col in range(len(obstacleGrid[0])):
        if row == 0 and col == 0:
          unique_paths[0][0] = 1
        # if the cell to the left of it has an obstacle or the cell to the left of it has 0 ways to reach it 
        if row == 0:
          if obstacleGrid[0][col] == 1 or unique_paths[0][col - 1] == 0:
            # then enter 0 in the cell
            unique_paths[0][col] = 0
          else:
            unique_paths[0][col] = 1
        
        # if the cell above it has an obstalce or the cell above it has 0 wasy to reach it
        if col == 0:
          if obstacleGrid[row][0] == 1 or unique_paths[row - 1][0] == 0:
            # then enter 0 in the cell
            unique_paths[row][0] = 0
          else:
            unique_paths[row][0] = 1

    # loop through other cells of the obstacle grid
    # start from the 1 row and col
    for row in range(1, len(obstacleGrid)): 
      for col in range(1, len(obstacleGrid[0])):
        # if the cell has an obstacle
        if obstacleGrid[row][col] == 1:
          # then the number of ways to reach it is 0
          unique_paths[row][col] = 0
        # else
        else:      
          # the number of ways to reach a cell is sum of
          # number of ways to reach the cell to the left of it and
          # the number of ways to reach the cell to the top of it
          unique_paths[row][col] = unique_paths[row - 1][col] + unique_paths[row][col - 1]
        
    # return the value of the last cell
    return unique_paths[-1][-1]
