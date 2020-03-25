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
