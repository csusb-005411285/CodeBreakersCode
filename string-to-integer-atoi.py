# tc: o(n), sc: o(n)
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        is_negative = True if s[0] == '-' else False
        is_positive = True if s[0] == '+' else False

        if len(s) == 1:
            return 0 if is_negative or (ord(s[0]) > ord('9')) or (ord(s[0]) < ord('0')) else ord(s[0]) - ord('0')

        integer = ord(s[1]) - ord('0') if is_negative or is_positive else ord(s[0]) - ord('0')

        if integer > 9 or integer < 0:
            return 0
        
        start_from = 2 if is_negative or is_positive else 1

        for i in range(start_from, len(s)):
            char = s[i]

            if ord(char) > ord('9') or ord(char) < ord('0'):
                break 

            int_relative_to_zero = ord(char) - ord('0') 
            integer = (integer * 10) + int_relative_to_zero
        
        if abs(integer) >= 2147483648:
            return -2147483648 if is_negative else 2147483647  
        
        return -1 * integer if is_negative else integer
