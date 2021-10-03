class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # init vars
        num_subseq = 0
        sptr, tptr = 0, 0
        # initial checks

        # process
        # loop through target
        while tptr < len(target):
            # set vars
            sptr = 0
            # set a flag to indicate char found in source
            char_found = False
            # loop through source
            # we are trying to match the target character
            while sptr < len(source) and tptr < len(target):
                # if chars are equal
                if target[tptr] == source[sptr]:
                    # move both the pointers ahead
                    tptr += 1
                    char_found = True
                # if not
                # move the source pointer ahead
                sptr += 1
            # if flag is set return -1
            if not char_found:
                return -1
            # incr count of num_subsequnces
            num_subseq += 1
        # return
        return num_subseq

# DP
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # init vars
        # cache, initalize it to float inf
        cache = [float('inf')] * (len(target) + 1)
        # set the first index to 0
        cache[0] = 0
        # inital checks
        
        # process
        # loop through the cache
        for i in range(1, len(cache)):
            # set vars
            # set the index of source to last char
            sptr = len(source) - 1
            # set the index of target to current index of cache
            tptr = i - 1 # 1. cache has an extra cell
            # loop through source and target
            while sptr >= 0 and tptr >= 0:
                # if chars are equal
                if source[sptr] == target[tptr]:
                    # we choose the max value from the value that already exists in the current cell
                    # vs the value from the previous cell  + 1
                    if cache[tptr] != float('inf'): # 1.
                        cache[i] = min(cache[i], cache[tptr] + 1)
                    # move the target pointer
                    tptr -= 1
                # if the chars are not equal    
                    # move the source pointer
                sptr -= 1
        # return value of last cell of the cache
        return cache[-1] if cache[-1] != float('inf') else -1

'''
1. There is a subsequence ending in target[tptr]. target[tptr] = float('inf') means that there is no subsequence ending in target[tptr]
'''
