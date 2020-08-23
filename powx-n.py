class Solution:
    def __init__(self):
        self.cache = {}

    def myPow(self, x: float, n: int) -> float:
        if x in self.cache:
            return self.cache[x]
        
        if n == 0:
            self.cache[x] = 1
            return self.cache[x] 
        
        if n < 0:
            n = abs(n)
            x = 1/x

        if n % 2 == 0:
            self.cache[x] = self.myPow(x, n/2) * self.myPow(x, n/2)
            return self.cache[x]
        
        self.cache[x] = x * self.myPow(x, n - 1)
        return self.cache[x]
