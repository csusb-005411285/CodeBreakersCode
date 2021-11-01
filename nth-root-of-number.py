def root(x, n):
  left = 1
  right = x
  target = x
  if x == 0:
    return 1
  if n == 1:
    return x
  while left <= right: 
    mid = left + (right - left)/2 
    if pow(mid, n) == target: 
      return mid
    if pow(mid, n) < target:
      left = mid + 0.001
    else:
      right = mid - 0.001 
  return left
