class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return 0
        
        if not word1:
            return len(word2)
        
        if not word2:
            return len(word1)
        cache = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        for r in range(len(word1) + 1):
            for c in range(len(word2) + 1):
                if r == 0 and c == 0:
                    cache[0][0] = 0
                elif r == 0:
                    cache[0][c] = c
                elif c == 0:
                    cache[r][0] = r
                else:
                    if word1[r - 1] == word2[c - 1]:
                        cache[r][c] = cache[r - 1][c - 1]
                    else:
                        cache[r][c] = 1 + min(cache[r - 1][c], cache[r][c - 1])
                        
        return cache[-1][-1]
