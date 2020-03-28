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
  
  # 2nd attempt. binary search
  def mySqrt(self, x: int) -> int:
    # init a var to store the mid
    mid = 0 # O(1)
    # init left to 1
    left = 1 # O(1)
    # init right to x
    right = x # O(1)
    
    # while left < right
    while left <= right:
      # find mid
      mid = left + (right - left)//2 # O(log n)
      # if mid == x/mid
      if mid == x/mid:
        # return mid
        return mid
      
      # if mid > x / mid
      if mid > x/mid:
        # the answer is in the left
        right = mid - 1
      # else
      else:
        # the answer is in the right
        left = mid + 1
        
    # return right
    return right

