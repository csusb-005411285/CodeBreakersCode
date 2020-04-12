class Solution:
  def __init__(self):
    self.mat = [] #n
  
  def getMoneyAmount(self, n: int) -> int:
    if n == 0 or n == 1:
      return 0

    # init a matrix to store the sum of values
    self.mat = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
    self.min_max(1, n) #n
    return self.mat[1][n]
    
  def min_max(self, start, end):
    if start >= end:
      return 0
    
    if self.mat[start][end] != float('inf'):
      return self.mat[start][end]
    
    for i in range(start, end + 1):
      # It takes me some time to understand the simple question "why it's using max(dp[i][x-1], dp[x+1][j])",
      # so I want to share my understanding here to help people like me.
      # dp[i][j] is the minimal cost to guess from range(i...j).
      # When you choose an x where i <= x <= j, you may find the target number from left i...x-1,
      # or you may find the target number from the x+1...j,
      # because you don't know which way should go, so to guarantee you have enough money to find the target,
      # you need to prepare the more, which is max(dp[i][x-1], dp[x+1][j]).
      self.mat[start][end] = min(self.mat[start][end], max(self.min_max(start, i - 1), self.min_max(i + 1, end)) + i) #n
      
    return self.mat[start][end]
