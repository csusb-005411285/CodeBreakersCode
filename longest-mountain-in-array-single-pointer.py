class Solution:
  def longestMountain(self, A: List[int]) -> int:
    # initialize two pointers up and down, they have 0 as value
    up, down = 0, 0
    # initialzie a max variable
    _max = 0
    # loop from the beginning
    for i in range(1, len(A)): 
      # for each element, check:
      # if we encounter a break: break occurs when we switch from down to up, or we enter a "flat area"  
      # then reset up and down
      # is it going up from down?
      if down > 0 and A[i - 1] < A[i] or A[i - 1] == A[i]:
        up = 0
        down = 0
      # if the prev element is less than the current, then increment up
      if A[i - 1] < A[i]:
        up += 1
      # if the prev element is greater than the current, then increment down
      if A[i - 1] > A[i]:
        down += 1
      # if up and down are greater than 0, then set the max, max = up + down + 1
      if up > 0 and down > 0:
        _max = max(_max, up + down + 1)
    # return max
    return _max
      
