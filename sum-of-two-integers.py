class Solution:
    def getSum(self, a: int, b: int) -> int:
        if abs(a) < abs(b):
            a, b = b, a
        sign = False if a >= 0 else True
        x = abs(a)
        y = abs(b)
        if a * b > 0:
            while y:
                sum_without_carry = x ^ y
                carry = (x & y) << 1
                y = carry
                x = sum_without_carry
        else:
            while y:
                sum_without_carry = x ^ y
                carry = (~x & y) << 1
                y = carry
                x = sum_without_carry
        return -x if sign else x
