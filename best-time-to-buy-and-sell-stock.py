# Two pointer technique
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        fast = 1
        slow = 0
        max_profit = 0

        while fast < len(prices):
            if prices[fast] > prices[slow]:
                max_profit = max(max_profit, prices[fast] - prices[slow])
                fast += 1
                continue
            
            slow = fast
            fast += 1

        return max_profit
 
 # One pass technique
 class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            
            if prices[i] > min_price:
                max_profit = max(max_profit, prices[i] - min_price)
            
        return max_profit
