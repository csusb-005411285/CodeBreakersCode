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

    # binary search solution. Exponential by squaring method.
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
            
        res = 1

        while n > 0:
            if n % 2 == 1:
                res = res * x
                n = n - 1

            x = x * x
            n = n//2

        return res
