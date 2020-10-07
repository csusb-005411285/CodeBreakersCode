class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = [[0 for i in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # abcde ace
        for r in range(len(text1) + 1): 
            for c in range(len(text2) + 1): 
                if r == 0 or c == 0:
                    cache[r][c] = 0
                else:
                    if text1[r - 1] == text2[c - 1]: 
                        cache[r][c] = cache[r - 1][c - 1] + 1 
                    else:
                        cache[r][c] = max(cache[r - 1][c], cache[r][c - 1], cache[r - 1][c - 1])
        
        return cache[-1][-1]
