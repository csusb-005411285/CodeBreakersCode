class Solution:
    def sortString(self, s: str) -> str:
        res = ''
        min_char = {}
        i = 0

        while i < len(s):
            char = s[i]

            ascii_val = ord(char) - ord('a') 
            if ascii_val in min_char:
                min_char[ascii_val] += 1
            else:
                min_char[ascii_val] = 1
            
            i += 1

        while len(res) != len(s):
            for key in sorted(min_char.keys()):
                if min_char[key] != 0:
                    char = chr(97 + key)
                    res += char
                    min_char[key] -= 1
    
            for key in sorted(min_char.keys(), key=None, reverse=True):
                if min_char[key] != 0:
                    char = chr(97 + key)
                    res += char
                    min_char[key] -= 1
                    
        return res
