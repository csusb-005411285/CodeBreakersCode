# recursion
class Solution:
    def solve(self, s0, s1):
        return self._find_lcs(s0, s1, 0, 0, 0)
    
    def _find_lcs(self, s1, s2, i, j, count):
        if i == len(s1) or j == len(s2):
            return count
        max_len = 0
        if s1[i] == s2[j]:
            max_len = self._find_lcs(s1, s2, i + 1, j + 1, count + 1)
        include = self._find_lcs(s1, s2, i + 1, j, 0)
        exclude = self._find_lcs(s1, s2, i, j + 1, 0)
        return max(max_len, max(include, exclude), count)


# top-down with caching
class Solution:
    def solve(self, s0, s1):
        cache = {}
        return self._find_lcs(s0, s1, 0, 0, 0, cache)
    
    def _find_lcs(self, s1, s2, i, j, count, cache):
        if (i, j, count) in cache:
            return cache[(i, j, count)]
        if i == len(s1) or j == len(s2):
            return count
        max_len = 0
        if s1[i] == s2[j]:
            max_len = self._find_lcs(s1, s2, i + 1, j + 1, count + 1, cache)
            cache[(i, j, count)] = max_len
        include = self._find_lcs(s1, s2, i + 1, j, 0, cache)
        exclude = self._find_lcs(s1, s2, i, j + 1, 0, cache)
        res = max(max_len, max(include, exclude), count)
        cache[(i, j, count)] = res
        return res

class Solution:
    def solve(self, s0, s1):
        max_len = 0
        cache = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s0) + 1)]
        for row in range(1, len(cache)):
            for col in range(1, len(cache[0])):
                if s0[row - 1] == s1[col - 1]:
                    cache[row][col] = cache[row - 1][col - 1] + 1
                    max_len = max(max_len, cache[row][col])
        return max_len
