class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    # if m is 1 or n is 1
    if m <= 1 or n <= 1:  
      # then return 1
      return 1

    # init a matrix to store unique paths
    # initialize each cell to 0
    unique_paths_mat = [[0 for _ in range(n)] for _ in range(m)]

    # loop through the matrix
    for row in range(m):
      for col in range(n):
        # the top row should have 1s in them
        if row == 0:
          unique_paths_mat[0][col] = 1
        # the left column should have 1s in them
        if col == 0:
          unique_paths_mat[row][col] = 1

    # loop through the matrix
    for row in range(1, m):
      for col in range(1, n):
        # assign values to each cell
        # each cell will have a value equal to the sum of the left cell and the top cell
        unique_paths_mat[row][col] = unique_paths_mat[row - 1][col] + unique_paths_mat[row][col - 1]

    # return the value of the last cell
    return unique_paths_mat[m - 1][n - 1]
