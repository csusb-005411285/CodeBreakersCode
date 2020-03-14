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
  
  # 2nd attempt
  def maxProfit(self, prices: List[int]) -> int:
    # if there are no prices or only one price 
    if len(prices) <= 1:
      # then return 0
      return 0
    
    # init a var to store the profits
    profit = 0
    # loop through the prices
    # start on day 1
    for i in range(1, len(prices)):  
      # if the price on the current day is greater than the previous day
      if prices[i] > prices[i - 1]:
        # then calculate the profit
        # also add the previous days profit
        profit += prices[i] - prices[i - 1]
    
    # return the profit
    return profit
