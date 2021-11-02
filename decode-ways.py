# Readable solution
class Solution:
    def numDecodings(self, s: str) -> int:
        cache = [0 for _ in range(len(s))]
        if s[0] == '0':
            return 0
        cache[0] = 1
        for i in range(1, len(cache)):
            char = s[i] 
            if char == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    cache[i] = cache[i - 2] if i - 2 >= 0 else 1 # 1.
                else:
                    return 0
            else:
                cache[i] = cache[i - 1]
                num = (int(s[i - 1]) * 10) + int(char)
                if 10 < num < 27:
                    cache[i] += cache[i - 2] if i - 2 >= 0 else 1
        return cache[-1]
'''
1. If you have 210, then the pairs are 2 and 10. And, not 2, 21, and 10. We add the `- 1` to prevent double counting.
'''
    
class Solution:
    def numDecodings(self, s: str) -> int:
        # init a cache
        cache = [0 for i in range(len(s))]
        # if first char is 0
        if s[0] == '0':
            return 0
        else:
            # if not, set the first element of cache to 1
            cache[0] = 1 #man     
        for i in range(1, len(s)): # 3
            one_char = int(s[i]) # 2
            two_char = int(s[i - 1: i + 1]) # 0
            if one_char >= 1:
                cache[i] = cache[i - 1]
            if two_char >= 10 and two_char <= 26:
                # only increment the number of ways when a number having two digits is a valid.
                # 26 => 2|6 is one way to decode it, another way is 26. Hence, there are two ways to decode it. 
                # 28 => 2|8 is one way to decode it, there is no other way to decode it.
                cache[i] += cache[i - 2] if i - 2 >= 0 else 1   
        return cache[-1]
