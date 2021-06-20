# top-down
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        cache = defaultdict(str)
        return self._find_scs_length(str1, str2, 0, 0, cache)

    def _find_scs_length(self, s1, s2, i, j, cache):
        if (i, j) in cache:
            return cache[(i, j)]
        if i == len(s1):
            cache[(i, j)] = s2[j:] 
            return s2[j:]
        if j == len(s2):
            cache[(i, j)] = s1[i:]
            return s1[i:]
        if s1[i] == s2[j]:
            cache[(i, j)] = s1[i] + self._find_scs_length(s1, s2, i + 1, j + 1, cache)
            return cache[(i, j)]
        include_s1 = s1[i] + self._find_scs_length(s1, s2, i + 1, j, cache)
        include_s2 = s2[j] + self._find_scs_length(s1, s2, i, j + 1, cache)
        cache[(i, j)] = include_s1 if len(include_s1) < len(include_s2) else include_s2
        return cache[(i, j)]

# bottom-up
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        s1 = str1
        s2 = str2
        s = ''
        cache = [[float('inf') for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        for row in range(len(cache)):
            cache[row][0] = row
        for col in range(len(cache[0])):
            cache[0][col] = col
        for row in range(1, len(cache)):
            for col in range(1, len(cache[0])):
                if s1[row - 1] == s2[col - 1]:
                    cache[row][col] = 1 + cache[row - 1][col - 1]
                else:
                    cache[row][col] = 1 + min(cache[row - 1][col], cache[row][col - 1])
        row = len(cache) - 1
        col = len(cache[0]) - 1
        while 0 < row < len(cache) and 0 < col < len(cache[0]):
            if s1[row - 1] == s2[col - 1]:
                s += s1[row - 1]
                row -= 1
                col -= 1
            else:
                if cache[row - 1][col] < cache[row][col - 1]:
                    s += s1[row - 1]
                    row -= 1
                else:
                    s += s2[col - 1]
                    col -= 1
        while row > 0:
            s += s1[row - 1]
            row -= 1
        while col > 0:
            s += s2[col - 1]
            col -= 1
        return s[::-1]
