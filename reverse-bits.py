class Solution:
    def reverseBits(self, n: int) -> int:
        reverse_bits = 0
        power = 31
        while n:
            reverse_bits += (n & 1) << power
            n = n >> 1
            power = power - 1
        return reverse_bits
