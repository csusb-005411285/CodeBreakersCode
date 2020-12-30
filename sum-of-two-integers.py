class Solution:
    def getSum(self, a: int, b: int) -> int:
        if abs(a)<abs(b):
            a, b = b, a
        x, y = abs(a), abs(b)
        sign = 1 if a>=0 else -1
        if a*b >= 0:
          #sum
          while y!=0:
            x, y = x^y, ((x&y)<<1)
        else:
          #diff
          while y!=0:
            x, y = x^y, (((~x)&y)<<1)
        return x*sign
