class Solution:
  def minimumTotal(self, triangle: List[List[int]]) -> int:
    if len(triangle) == 0:
      return 0
    
    if len(triangle) == 1:
      return triangle[0][0]
    
    # init a matrix to store the results
    min_sum = [[0 for _ in range(len(triangle))] for _ in range(len(triangle))] # O(n)
    min_sum[0][0] = triangle[0][0]
    
    for row in range(1, len(triangle)): # O(n)
      for col in range(row + 1): # O(n)
        if row - 1 >= 0 and col == 0:
            min_sum[row][col] = min_sum[row - 1][col] + triangle[row][col]
        elif row - 1 >= 0 and col == row:
            min_sum[row][col] = min_sum[row - 1][col - 1] + triangle[row][col]
        else:
          min_sum[row][col] = min(min_sum[row - 1][col], min_sum[row - 1][col - 1]) + triangle[row][col]
    
    min_total = float("inf")
    row = len(min_sum) - 1
    for col in range(len(min_sum)): # O(n)
      if min_total > min_sum[row][col]:
        min_total = min_sum[row][col]

    return min_total
  
  # 2nd attempt
  def minimumTotal(self, triangle: List[List[int]]) -> int:
    # if triangle has length 0
    if len(triangle) == 0:
      # then return 0
      return 0
      
    # if triangle has column of length of 1
    if len(triangle) == 1:
      # then return the value of the cell
      return triangle[0][0]
    
    # define a list to store the results
    min_path_sum = [[0 for _ in range(len(triangle))] for _ in range(len(triangle))] # O(n)
    
    # the first col has the same value as the first col of the original list
    min_path_sum[0][0] = triangle[0][0]
    
    # loop through the triangle
    # loop through rows
    for row in range(1, len(triangle)): # O(n)
      # loop through columns
      for col in range(row + 1):  # O(n)
        # if the col is the first col
        if col == 0:
          # then the value of path sum would be the sum of the cell from the above row and the value of the cell in the original list
          min_path_sum[row][0] = min_path_sum[row - 1][0] + triangle[row][0]
        # if the col is the last col
        elif col == row:
          # then the value is the value of the above cell and the sum of the cell in the original list
          min_path_sum[row][col] = min_path_sum[row - 1][col - 1] + triangle[row][col]
        # else
        else:
          # the value of the cell is the minimum of the two adjacent cells in the previous row and the sum of the value of the cell in the original list
          min_path_sum[row][col] = min(min_path_sum[row - 1][col - 1], min_path_sum[row - 1][col]) + triangle[row][col]
      
    result = float("inf")
    # return the min value from the last row
    for i in range(len(triangle)): # O(n)
      result = min(result, min_path_sum[len(triangle) - 1][i])

    return result
