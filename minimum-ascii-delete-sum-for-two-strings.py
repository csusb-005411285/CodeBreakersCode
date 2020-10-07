class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        cache = [[float('inf') for i in range(len(s2) + 1)] for i in range(len(s1) + 1)]

        for r in range(len(s1) + 1):
            for c in range(len(s2) + 1):
                if r == 0 and c == 0:
                    cache[0][0] = 0
                elif r == 0:
                    cache[0][c] = cache[0][c - 1] + ord(s2[c - 1])
                elif c == 0:
                    cache[r][0] = cache[r - 1][0] + ord(s1[r - 1])
                else:
                    if s1[r - 1] == s2[c - 1]:
                        cache[r][c] = min(cache[r][c], cache[r - 1][c - 1])
                    else:
                        cache[r][c] = min(cache[r - 1][c] + ord(s1[r - 1]), cache[r][c - 1] + ord(s2[c - 1]))

        return cache[-1][-1] 
