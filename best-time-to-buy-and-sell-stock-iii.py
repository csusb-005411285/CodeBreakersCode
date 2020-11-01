class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # init a cache
        cache = [[0 for _ in range(len(prices))] for i in range(3)] 
        # loop through the transactions, start at 1
        for trans in range(1, 3):
            # loop through the prices
            max_profit_before_selling_at_price_i = float('-inf')
            for i in range(1, len(prices)):
                # calculate max profit so far
                max_profit_before_selling_at_price_i = max(max_profit_before_selling_at_price_i, cache[trans - 1][i - 1] - prices[i - 1]) 
                # calculate max profit for the day 
                cache[trans][i] = max(cache[trans][i - 1], max_profit_before_selling_at_price_i + prices[i])
        return cache[-1][-1]
