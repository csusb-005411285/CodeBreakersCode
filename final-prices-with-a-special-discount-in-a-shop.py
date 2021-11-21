class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        prices_with_discount = prices[:] 
        for i, price in enumerate(prices): 
            while stack and price <= stack[-1][1]: 
                indx, last_price = stack.pop() 
                prices_with_discount[indx] -= price 
            stack.append((i, price))
        return prices_with_discount
