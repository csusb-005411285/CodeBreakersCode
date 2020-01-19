class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    if len(prices) <= 1:
      return 0
    # intiatize a variable to store the profit
    _max = 0
    # initialize two pointers: start and end
    start, end = 0, 1
    # loop through the prices
    for _ in range(len(prices) - 1):  
      # if end > start, then add to the max var
      if prices[end] > prices[start]:
        _max += prices[end] - prices[start] 
      # increment start and end
      start += 1
      end += 1
      
    # return max
    return _max
