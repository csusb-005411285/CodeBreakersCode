class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = int(a,2)
        int_b = int(b, 2)
        _sum = 0
        while int_b:
            _sum = int_a ^ int_b
            carry = (int_a & int_b) << 1
            int_a = _sum
            int_b = carry
        return bin(int_a)[2:]
