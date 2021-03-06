class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        cache[0][0] = True
        for j in range(2, len(cache[0])):
            if p[j - 1] == '*':
                cache[0][j] = cache[0][j - 2]
        for i in range(1, len(cache)):
            for j in range(1, len(cache[0])):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    cache[i][j] = cache[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if p[j - 2] != s[i - 1] and p[j - 2] != '.':
                        cache[i][j] = cache[i][j - 2]
                    else:
                        cache[i][j] = cache[i - 1][j] | cache[i][j - 1] | cache[i][j - 2]
        return cache[-1][-1]
