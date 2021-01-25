class Solution:
    def __init__(self):
        self.possible_partitions = []
        
    def partition(self, s: str) -> List[List[str]]:
        cache = defaultdict(list)
        self._partition(s, 0, cache, [])
        return self.possible_partitions 
    
    def is_palindrome(self, s):
        s_list = list(s)
        return s_list == s_list[::-1]
    
    def _partition(self, s, start_index, cache, curr_combination):
        if not s:
            self.possible_partitions.append(curr_combination)
            return
        for i in range(len(s)):
            if self.is_palindrome(s[:i + 1]):
                self._partition(s[i + 1:], start_index, cache, curr_combination + [s[:i + 1]])
        return
