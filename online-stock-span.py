class StockSpanner:

    def __init__(self):
        self.stack = []
        self.count = 0

    def next(self, price: int) -> int:
        curr_count = 1
        if self.stack:
            while self.stack and self.stack[-1][0] <= price:
                last_price, index, count = self.stack.pop()
                curr_count += count
        self.stack.append([price, self.count, curr_count])
        self.count += 1
        return self.stack[-1][2]
        
