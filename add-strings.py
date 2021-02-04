class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        carry = 0
        values = []
        while p1 >= 0 or p2 >= 0:
            n1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            n2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            carry, value = divmod((n1 + carry + n2), 10)
            values.append(value)
            p1 -= 1
            p2 -= 1
        if carry != 0:
            values.append(carry)
        return ''.join(list(map(str, values))[::-1])
