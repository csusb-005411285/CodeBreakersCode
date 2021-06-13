class Solution:
    def minInsertions(self, s: str) -> int:
        length_of_palindromic_substring = self.get_len_palindromic_substring(s, 0, len(s) - 1)
        return len(s) - length_of_palindromic_substring
    
    def get_len_palindromic_substring(self, s, start, end):
        if start > end:
            return 0
        if start == end: # make a note of this
            return 1
        if s[start] == s[end]:
            return 2 + self.get_len_palindromic_substring(s, start + 1, end - 1)
        return max(self.get_len_palindromic_substring(s, start + 1, end), self.get_len_palindromic_substring(s, start, end - 1))
      
class Solution:
    def minInsertions(self, s: str) -> int:
        cache = defaultdict(int)
        length_of_palindromic_substring = self.get_len_palindromic_substring(s, 0, len(s) - 1, cache)
        return len(s) - length_of_palindromic_substring
    
    def get_len_palindromic_substring(self, s, start, end, cache):
        if (start, end) in cache:
            return cache[(start, end)]
        if start > end:
            return 0
        if start == end: # make a note of this
            cache[(start, end)] = 1
            return 1
        if s[start] == s[end]:
            count = 2 + self.get_len_palindromic_substring(s, start + 1, end - 1, cache)
            cache[(start, end)] = count
            return count
        count = max(self.get_len_palindromic_substring(s, start + 1, end, cache), self.get_len_palindromic_substring(s, start, end - 1, cache))
        cache[(start, end)] = count
        return count
      
  class Solution:
    def minInsertions(self, s: str) -> int:
        cache = [[0 for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]
        rev_s = s[::-1]
        for row in range(1, len(cache)):
            for col in range(1, len(cache[0])):
                if s[row - 1] == rev_s[col - 1]:
                    cache[row][col] = 1 + cache[row - 1][col - 1]
                else:
                    cache[row][col] = max(cache[row - 1][col], cache[row][col - 1]) 
        return len(s) - cache[-1][-1]
