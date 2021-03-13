class Solution:
    def findNthDigit(self, n: int) -> int:
        digits = 1
        start = 1
        count = 9
        while n > count * digits:
            n -= count * digits
            start = start * 10
            digits += 1
            count *= 10
        offset_from_start, digit_in_num = divmod((n - 1), digits)
        start += offset_from_start
        return int(str(start)[digit_in_num])
