class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        result = []
        remainder_map = {}
        sign = '-' if numerator * denominator < 0 else ''
        quotient, remainder = divmod(abs(numerator), abs(denominator))
        result = [sign + str(quotient), '.']
        while remainder > 0 and remainder not in remainder_map:
            remainder_map[remainder] = len(result)
            q, remainder = divmod(remainder * 10, abs(denominator))
            result.append(str(q))
        if remainder in remainder_map:
            index = remainder_map[remainder]
            result.insert(index, '(')
            result.append(')')
        return ''.join(result).rstrip('.')
