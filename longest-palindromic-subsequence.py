class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self._longest_palindromic_subsequence(s, 0, len(s) - 1)
    
    def _longest_palindromic_subsequence(self, s, start, end):
        if start > end:
            return 0
        if start == end:
            return 1
        if s[start] == s[end]:
            return 2 + self._longest_palindromic_subsequence(s, cache, start + 1, end - 1)
        return max(self._longest_palindromic_subsequence(s, cache, start + 1, end), self._longest_palindromic_subsequence(s, cache, start, end - 1))

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = defaultdict(str)
        return self._longest_palindromic_subsequence(s, cache, 0, len(s) - 1)
    
    def _longest_palindromic_subsequence(self, s, cache, start, end):
        if (start, end) in cache:
            return cache[(start, end)]
        if start > end:
            return 0
        if start == end:
            return 1
        if s[start] == s[end]:
            str_len = 2 + self._longest_palindromic_subsequence(s, cache, start + 1, end - 1)
            cache[(start, end)] = str_len  
            return str_len
        str_len = max(self._longest_palindromic_subsequence(s, cache, start + 1, end), self._longest_palindromic_subsequence(s, cache, start, end - 1))
        cache[(start, end)] = str_len
        return str_len

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rev_s = s[::-1]
        cache = [[0 for _ in range(len(s) + 1)] for _ in range(len(rev_s) + 1)]
        for row in range(1, len(cache)):
            for col in range(1, len(cache[0])):
                if s[row - 1] == rev_s[col - 1]:
                    cache[row][col] = 1 + cache[row - 1][col - 1]
                else:
                    cache[row][col] = max(cache[row - 1][col], cache[row][col - 1])
        return cache[-1][-1]
