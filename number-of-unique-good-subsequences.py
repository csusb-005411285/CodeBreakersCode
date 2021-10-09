class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        # init vars
        # 2d cache
        cache = [[0, 0], [0, 0]]
        # mod
        modulus = pow(10, 9) + 7
        # initial checks
        
        # process
        # loop through the string
        for i, char in enumerate(binary):
            # if char is 0
            if char == '0':
                cache[0][0] = 1 # 1.
                # store the result in num of subsequences
                # add the previous result
                # the value of current cache is cache[1][0] + cache[1][1]
                # mod the result
                cache[1][0] = (cache[1][0] + cache[1][1]) % modulus
            # if char is 1
            elif char == '1':
                # store the result in num of subsequences
                # add the previous result
                # the value of current cache is cache[1][1] + cache[1][0] 
                # mod the result
                cache[1][1] = (cache[1][0] + cache[1][1] + 1) % modulus # 3.
        return (cache[0][0] + cache[0][1] + cache[1][0] + cache[1][1]) % modulus # 2. 

'''
1. We force it to be 1 because, the only valid string starting and ending in 0 is '0', '00', '000'. Therefore, the number of distinct subsequences is 1. 
2. We return the sum of all values in the cache. The solution is optimized for space.
3. I don't understand why we add 1. As per the author, Since we append a '1' to every subsequence dp[1][0] and dp[1][1], we are missing the subsequence "1" with length 1; therefore, we add a one to it.
Why don't we use the same approach for string ending in 0?
'''
