class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    if not matrix or target is None:
      return False
    # init var to store rows, mid, cols, start and end
    rows = len(matrix)
    col = len(matrix[0])
    start = 0
    end = len(matrix) * len(matrix[0])- 1
    mid = 0
    # loop until start is less than end
    while start <= end:
      # calculate mid
      mid = (start + end)//2
      # calculate the value from the cell in the matrix using the mid
      cell_value = matrix[mid // col][mid%col]
      # if value equals target
      if cell_value == target:  
        # then return True
        return True
      # if value is less than the target
      if cell_value < target:
        # then set start to mid
        start = mid + 1
      # else
      else:
        # then set end to mid
        end = mid - 1
    # return false
    return False
        
