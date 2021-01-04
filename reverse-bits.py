class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_bit = 0
        power = 31
        while n:
            last_bit = (n & 1)
            reversed_bit |= last_bit << power
            power -= 1
            n >>= 1
        return reversed_bit
