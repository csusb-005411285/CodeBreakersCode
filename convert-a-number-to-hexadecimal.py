class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        res = ''
        hex_map = '0123456789abcdef'
        while num and len(res) < 8:
            index = num & 15
            res = hex_map[index] + res
            num = num >> 4
        return res or '0'
