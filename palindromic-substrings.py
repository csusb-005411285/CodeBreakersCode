class Solution:
    def __init__(self):
        self.count = 0
    
    def countSubstrings(self, s: str) -> int:
        for left, char in enumerate(s):
            self._count_substrings(left, left, s)
            self._count_substrings(left, left + 1, s) 
        return self.count
    
    def _count_substrings(self, left, right, s):
        while left >= 0 and right < len(s): 
            if s[left] != s[right]:
                break
            self.count += 1
            left -= 1
            right += 1 
