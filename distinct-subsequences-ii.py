class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # init vars
        # cache; it should be a list
        cache = []
        char_map = defaultdict(int)
        modulo = pow(10, 9) + 7
        # inital checks
        
        # process
        cache = [1] # 1. 
        # loop through the string
        for i, char in enumerate(s):
            val = cache[-1] * 2
            # if char is cache
            if char in char_map:    
                # get the previous value
                val -= cache[char_map[char]]
            cache.append(val)
            char_map[char] = i # 3.
        # return the value of the last cell
        return (cache[-1] - 1) % modulo # 2. 

'''
1. 1 is for the empty string as a subsequence
2. Remove the empty space added at the start. 
3. This is the most difficult part to understand. Do not store the number of distinct subsequences 
as the value of the cache. Instead store the index of char. We store the index of the char so that we can disregard all the calculations that happened at that index. We do this to prevent double counting.
'''
