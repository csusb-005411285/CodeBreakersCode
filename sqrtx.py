class Solution:
  def mySqrt(self, x: int) -> int:
    if x <= 1:
      return x
    
    # init a var to store the result
    sqrt = x # O(1)
    
    # loop until the square of x is greater than original x
    while sqrt*sqrt > x: # O(log n) 
      # calculate the new x as per Newton's formula
      sqrt = (sqrt + x/sqrt) // 2
    
    return int(sqrt)
