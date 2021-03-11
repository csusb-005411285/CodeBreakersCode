class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        cache[0][0] = True
        for col in range(2, len(cache[0])):
            if p[col - 1] == '*':
                cache[0][col] = cache[0][col - 2] 
        for row in range(1, len(cache)):
            for col in range(1, len(cache[0])):
                if s[row - 1] == p[col - 1]:
                    cache[row][col] = cache[row - 1][col - 1]
                else:
                    if p[col - 1] == '.':
                        cache[row][col] = cache[row - 1][col - 1]
                    elif p[col - 1] == '*':
                        cache[row][col] = cache[row][col - 2]
                        if s[row - 1] == p[col - 2] or p[col - 2] == '.':
                            cache[row][col] |= cache[row - 1][col]
        return cache[-1][-1]
